import tkinter as tk
from tkinter import messagebox
import json

DATA_FILE = "stock_data.json"
ROWS_PER_PAGE = 15

def open_stock_window(root):
    

    win = tk.Frame(root)
    win.pack(fill=tk.BOTH, expand=True)

    headers = ["No", "Description", "Stock"]
    column_widths = [5, 40, 10]
    all_data = []
    current_page = [0]

    grid_frame = tk.Frame(win)
    grid_frame.pack(fill=tk.BOTH, expand=True)

    entries = []

    # Headers
    for c in range(len(headers)):
        label = tk.Label(grid_frame, text=headers[c], bd=1, relief="solid",
                         width=column_widths[c], bg="#d9d9d9")
        label.grid(row=0, column=c, sticky="nsew")

    for i in range(len(headers)):
        grid_frame.grid_columnconfigure(i, weight=1)

    for i in range(ROWS_PER_PAGE + 1):
        grid_frame.grid_rowconfigure(i, weight=1)

    def load_page(page_index):
        entries.clear()
        for widget in grid_frame.winfo_children():
            if int(widget.grid_info()["row"]) > 0:
                widget.destroy()

        start = page_index * ROWS_PER_PAGE
        page_rows = all_data[start:start + ROWS_PER_PAGE]

        for r in range(ROWS_PER_PAGE):
            row_entries = []
            for c in range(len(headers)):
                e = tk.Entry(grid_frame, bd=1, relief="solid", justify="center")
                e.grid(row=r + 1, column=c, sticky="nsew")

                if c == 0:
                    e.insert(0, str(start + r + 1))
                    e.config(state="readonly")
                elif r < len(page_rows):
                    if c == 1:
                        e.insert(0, page_rows[r].get("Description", ""))
                    elif c == 2:
                        e.insert(0, page_rows[r].get("Stock", ""))

                row_entries.append(e)
            entries.append(row_entries)

    def add_row():
        all_data.append({"Description": "", "Stock": ""})
        load_page(current_page[0])

    def save_data():
        for r, row in enumerate(entries):
            index = current_page[0] * ROWS_PER_PAGE + r
            if index >= len(all_data):
                all_data.append({})
            all_data[index]["Description"] = row[1].get()
            all_data[index]["Stock"] = row[2].get()

        try:
            with open(DATA_FILE, "w") as f:
                json.dump(all_data, f, indent=2)
            messagebox.showinfo("Saved", "Stock saved!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def next_page():
        if (current_page[0] + 1) * ROWS_PER_PAGE >= len(all_data):
            for _ in range(ROWS_PER_PAGE):
                all_data.append({"Description": "", "Stock": ""})
        current_page[0] += 1
        load_page(current_page[0])

    def prev_page():
        if current_page[0] > 0:
            current_page[0] -= 1
            load_page(current_page[0])

    def back():
        win.destroy()
           # 👈 wapas menu

    # Buttons
    button_frame = tk.Frame(win)
    button_frame.pack(fill=tk.X)

    tk.Button(button_frame, text="Save", command=save_data).pack(side=tk.LEFT, padx=5, pady=5)
    tk.Button(button_frame, text="Back", command=back).pack(side=tk.LEFT, padx=5, pady=5)
    tk.Button(button_frame, text="Previous", command=prev_page).pack(side=tk.RIGHT, padx=5, pady=5)
    tk.Button(button_frame, text="Next", command=next_page).pack(side=tk.RIGHT, padx=5, pady=5)

    try:
        with open(DATA_FILE, "r") as f:
            all_data.extend(json.load(f))
    except:
        pass

    load_page(0)