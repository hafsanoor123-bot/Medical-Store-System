import tkinter as tk
from tkinter import messagebox
from datetime import datetime

from database import (
    get_connection,
    create_database_and_table,
    fetch_all_stock,
    insert_empty_row,
    update_stock_row,
)

ROWS = 15
HEADERS = ["No.", "Qty", "Description", "Stock", "Rate", "Expiry Date"]


class StockManager:
    def __init__(self, win, back_cmd=None):
        self.win = win
        self.back_cmd = back_cmd
        self.conn = get_connection()
        create_database_and_table(self.conn)

        self.page = 0
        self.entries = []
        self.saved_pages_data = {}

        self._build_ui()
        self._load_page()

    # ───── UI
    def _build_ui(self):
        self.win.configure(bg="#f0f4f8")

        # ── TABLE with border ──
        self.table_frame = tk.Frame(self.win, bg="black", bd=1, relief="solid" , height=500)
        self.table_frame.pack(fill="both", padx=10, pady=(10, 10) )

        self.table = tk.Frame(self.table_frame, bg="white")
        self.table.pack(fill="both", expand=True, padx=1, pady=1)

        widths = [5, 8, 40, 12, 12, 15]

        for c in range(len(HEADERS)):
            self.table.columnconfigure(c, weight=1)

        for c, h in enumerate(HEADERS):
            tk.Label(self.table, text=h,
                     bg="#d9e1f2",
                     font=("Segoe UI", 15, "bold"),
                     width=widths[c],
                     relief="solid",
                     bd=1).grid(row=0, column=c, sticky="nsew")

        # ── BUTTONS ──
        bottom = tk.Frame(self.win, bg="#f0f4f8")
        bottom.pack(fill="x", padx=10, pady=(0, 10))

        if self.back_cmd:
            tk.Button(bottom, text="🏠 Back to Home",
                      bg="#7f8c8d", fg="white",
                      font=("Segoe UI", 13, "bold"),
                      relief="solid", bd=2, cursor="hand2",
                      command=self.back_cmd).pack(side="left", padx=(0, 10))

        tk.Button(bottom, text="💾 Save All",
                  bg="#2e7d32", fg="white",
                  font=("Segoe UI", 13, "bold"),
                  relief="solid", bd=2, cursor="hand2",
                  command=self._save_all).pack(side="left")

        tk.Button(bottom, text="Next ▶",
                  bg="#f0f4f8", fg="black",
                  font=("Segoe UI", 13, "bold"),
                  relief="solid", bd=2, cursor="hand2",
                  command=self._next).pack(side="right", padx=(5, 10))

        tk.Button(bottom, text="◀ Prev",
                  bg="#f0f4f8", fg="black",
                  font=("Segoe UI", 13, "bold"),
                  relief="solid", bd=2, cursor="hand2",
                  command=self._prev).pack(side="right")

    # ───── BIND ARROW KEYS
    def _bind_arrow_keys(self):
        for r in range(ROWS):
            for c in range(1, len(HEADERS)):
                entry = self.entries[r][c]
                entry.bind("<Up>",        lambda e, row=r, col=c: self._move_up(row, col))
                entry.bind("<Down>",      lambda e, row=r, col=c: self._move_down(row, col))
                entry.bind("<Left>",      lambda e, row=r, col=c: self._move_left_key(row, col, e))
                entry.bind("<Right>",     lambda e, row=r, col=c: self._move_right_key(row, col, e))
                entry.bind("<Tab>",       lambda e, row=r, col=c: self._move_right(row, col))
                entry.bind("<Shift-Tab>", lambda e, row=r, col=c: self._move_left(row, col))

    # ───── MOVE FUNCTIONS
    def _move_up(self, row, col):
        if row > 0:
            self.entries[row-1][col].focus_set()
            self.entries[row-1][col].icursor(tk.END)
        return "break"

    def _move_down(self, row, col):
        if row < ROWS - 1:
            self.entries[row+1][col].focus_set()
            self.entries[row+1][col].icursor(tk.END)
        return "break"

    def _move_left(self, row, col):
        if col > 1:
            self.entries[row][col-1].focus_set()
            self.entries[row][col-1].icursor(tk.END)
        return "break"

    def _move_right(self, row, col):
        if col < len(HEADERS) - 1:
            self.entries[row][col+1].focus_set()
            self.entries[row][col+1].icursor(tk.END)
        return "break"

    def _move_left_key(self, row, col, event):
        """Left arrow: agar cursor text ke start pe hai to prev cell jao, warna text me move karo"""
        widget = event.widget
        if widget.index(tk.INSERT) == 0:
            return self._move_left(row, col)
        return None  # default cursor movement

    def _move_right_key(self, row, col, event):
        """Right arrow: agar cursor text ke end pe hai to next cell jao, warna text me move karo"""
        widget = event.widget
        if widget.index(tk.INSERT) == len(widget.get()):
            return self._move_right(row, col)
        return None  # default cursor movement

    # ───── GET CURRENT PAGE DATA
    def _get_current_page_data(self):
        page_data = []
        for r in range(ROWS):
            row_data = []
            for c in range(1, len(HEADERS)):
                value = self.entries[r][c].get().strip()
                row_data.append(value)
            page_data.append(row_data)
        return page_data

    # ───── LOAD DATA TO CURRENT PAGE
    def _load_data_to_page(self, page_data):
        if not page_data:
            return
        for r in range(ROWS):
            if r < len(page_data):
                for c in range(1, len(HEADERS)):
                    value = page_data[r][c-1]
                    if value:
                        self.entries[r][c].delete(0, tk.END)
                        self.entries[r][c].insert(0, value)

    # ───── LOAD PAGE
    def _load_page(self):
        for row in self.entries:
            for e in row:
                e.destroy()
        self.entries.clear()

        start = self.page * ROWS

        for r in range(ROWS):
            row_entries = []

            for c in range(len(HEADERS)):
                e = tk.Entry(self.table, font=("Segoe UI", 13), bd=1, relief="solid")
                e.grid(row=r + 1, column=c, sticky="nsew", ipady=6, padx=0, pady=0)

                if c == 0:
                    e.insert(0, start + r + 1)
                    e.config(state="readonly", readonlybackground="#ecf0f1")

                row_entries.append(e)

            self.entries.append(row_entries)

        self._bind_arrow_keys()

        if self.page in self.saved_pages_data:
            self._load_data_to_page(self.saved_pages_data[self.page])

    # ───── SAVE ALL TO DB
    def _save_all(self):
        current_data = self._get_current_page_data()
        self.saved_pages_data[self.page] = current_data
        
        confirm = messagebox.askyesno("Confirm Save", "Kya aap sure ho ke data save karna hai?")
        if not confirm:
            return

        now = datetime.now()
        date = now.strftime("%Y-%m-%d")
        time = now.strftime("%H:%M:%S")
        
        saved_count = 0

        for page_num, page_rows in self.saved_pages_data.items():
            for row_data in page_rows:
                qty = row_data[0]
                desc = row_data[1]
                stock = row_data[2]
                rate = row_data[3]
                expiry = row_data[4]
                
                if not desc:
                    continue

                stock_val = int(stock) if stock else 0
                rate_val = float(rate) if rate else 0

                insert_empty_row(self.conn)
                data = fetch_all_stock(self.conn)
                last_id = data[-1]["id"]

                update_stock_row(self.conn, last_id, desc, stock_val, rate_val, date, time)
                saved_count += 1

        if saved_count > 0:
            messagebox.showinfo("Saved", f"{saved_count} records successfully saved!")
            self.saved_pages_data.clear()
            self.page = 0
            self._load_page()
        else:
            messagebox.showwarning("Warning", "Koi data save nahi kiya gaya!")

    # ───── PAGINATION
    def _next(self):
        current_data = self._get_current_page_data()
        self.saved_pages_data[self.page] = current_data
        self.page += 1
        self._load_page()

    def _prev(self):
        if self.page > 0:
            current_data = self._get_current_page_data()
            self.saved_pages_data[self.page] = current_data
            self.page -= 1
            self._load_page()


def build_stock_ui(parent_frame, back_cmd=None):
    StockManager(parent_frame, back_cmd=back_cmd)