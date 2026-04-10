# create__bill.py
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# ─────────────────────────────────────────────
#  Color Palette & Fonts
# ─────────────────────────────────────────────
BG        = "#f0f4f8"
PANEL     = "#ffffff"
HEADER_BG = "#1a3c5e"
HEADER_FG = "#ffffff"
ACCENT    = "#2ecc71"
ACCENT2   = "#3498db"
DANGER    = "#e74c3c"
TEXT      = "#2c3e50"
BORDER    = "#bdc3c7"
ROW_ALT   = "#eaf4fb"
ROW_EVEN  = "#ffffff"
GOLD      = "#f39c12"

FONT_HEAD  = ("Segoe UI", 10, "bold")
FONT_BODY  = ("Segoe UI", 10)
FONT_LABEL = ("Segoe UI", 10, "bold")
FONT_SMALL = ("Segoe UI", 9)
FONT_BTN   = ("Segoe UI", 10, "bold")
FONT_STAT  = ("Segoe UI", 14, "bold")


def build_billing_ui(parent, back_cmd=None):
    BillingWindow(parent, back_cmd=back_cmd)

def sales_report(root):
    messagebox.showinfo("Sales Report", "Sales Report coming soon!")


class BillingWindow:
    def __init__(self, win, back_cmd=None):
        self.win      = win
        self.back_cmd = back_cmd
        self.cart     = []
        self.discount_pct = 0.0

        self.ent_desc     = None
        self.ent_rate     = None
        self.ent_qty      = None
        self.ent_discount = None

        self._build_ui()

    def _build_ui(self):
        # ── Top Header Bar ──────────────────────────
        header = tk.Frame(self.win, bg=HEADER_BG, pady=12)
        header.pack(fill="x")
        tk.Label(header, text="🏥  Medical Store Billing System",
                 font=("Segoe UI", 18, "bold"), bg=HEADER_BG, fg=HEADER_FG
                 ).pack(side="left", padx=24)
        self.lbl_time = tk.Label(header, text="", font=FONT_SMALL,
                                 bg=HEADER_BG, fg="#aed6f1")
        self.lbl_time.pack(side="right", padx=24)
        self._tick()

        # ── Main Body ───────────────────────────
        body = tk.Frame(self.win, bg=BG)
        body.pack(fill="both", expand=True, padx=18, pady=14)

        left = tk.Frame(body, bg=BG)
        left.pack(side="left", fill="y", padx=(0, 12))

        right = tk.Frame(body, bg=BG)
        right.pack(side="left", fill="both", expand=True)

        self._build_add_cart(left)
        self._build_discount(left)
        self._build_summary(left)
        self._build_table(right)
        self._build_action_bar(right)

    # ── Add Cart Panel
    def _build_add_cart(self, parent):
        pnl = self._panel(parent, "🛒  Add Item to Cart")
        pnl.pack(fill="x", pady=(0, 10))

        inner = tk.Frame(pnl, bg=PANEL)
        inner.pack(fill="x", padx=14, pady=10)

        self.var_desc = tk.StringVar()
        self.var_rate = tk.StringVar()
        self.var_qty  = tk.StringVar()

        self._field_row(inner, "Description :", self.var_desc, 0)
        self._field_row(inner, "Rate (Rs.)  :", self.var_rate, 1)
        self._field_row(inner, "Quantity    :", self.var_qty,  2)

        tk.Button(inner, text="➕  Add to Cart",
                  font=FONT_BTN, bg=ACCENT, fg="white",
                  activebackground="#27ae60", activeforeground="white",
                  relief="flat", cursor="hand2", bd=0,
                  padx=20, pady=8,
                  command=self._add_to_cart
                  ).grid(row=3, column=0, columnspan=2, pady=(12, 4), sticky="ew")

        inner.columnconfigure(1, weight=1)

        if self.ent_desc: self.ent_desc.bind("<Return>", self._add_to_cart)
        if self.ent_rate: self.ent_rate.bind("<Return>", self._add_to_cart)
        if self.ent_qty:  self.ent_qty.bind("<Return>",  self._add_to_cart)

    def _field_row(self, parent, label, var, row):
        tk.Label(parent, text=label, font=FONT_LABEL,
                 bg=PANEL, fg=TEXT, anchor="w"
                 ).grid(row=row, column=0, sticky="w", pady=(8, 0), padx=(0, 10))

        ent = tk.Entry(parent, textvariable=var,
                       font=FONT_BODY, relief="solid", bd=1,
                       highlightthickness=2,
                       highlightcolor=ACCENT2,
                       highlightbackground=BORDER,
                       width=22)
        ent.grid(row=row, column=1, sticky="ew", pady=(8, 0))

        if "desc" in label.lower():
            self.ent_desc = ent
        elif "rate" in label.lower():
            self.ent_rate = ent
        elif "qty" in label.lower() or "quan" in label.lower():
            self.ent_qty = ent

    # ── Discount Panel
    def _build_discount(self, parent):
        pnl = self._panel(parent, "🏷️  Discount")
        pnl.pack(fill="x", pady=(0, 10))

        inner = tk.Frame(pnl, bg=PANEL)
        inner.pack(fill="x", padx=14, pady=10)

        tk.Label(inner, text="Discount % :", font=FONT_LABEL,
                 bg=PANEL, fg=TEXT, anchor="w"
                 ).grid(row=0, column=0, sticky="w", padx=(0, 10))

        self.var_disc = tk.StringVar()
        ent = tk.Entry(inner, textvariable=self.var_disc,
                       font=FONT_BODY, relief="solid", bd=1,
                       highlightthickness=2,
                       highlightcolor=ACCENT2,
                       highlightbackground=BORDER,
                       width=22)
        ent.grid(row=0, column=1, sticky="ew")
        inner.columnconfigure(1, weight=1)

        self.ent_discount = ent
        self.ent_discount.bind("<Return>", lambda e: self._apply_discount())

        tk.Button(inner, text="✅  Apply Discount",
                  font=FONT_BTN, bg=ACCENT2, fg="white",
                  activebackground="#2980b9", activeforeground="white",
                  relief="flat", cursor="hand2", bd=0,
                  padx=20, pady=8,
                  command=self._apply_discount
                  ).grid(row=1, column=0, columnspan=2,
                         pady=(12, 4), sticky="ew")

    # ── Summary Panel
    def _build_summary(self, parent):
        pnl = self._panel(parent, "📊  Bill Summary")
        pnl.pack(fill="x", pady=(0, 10))

        inner = tk.Frame(pnl, bg=PANEL)
        inner.pack(fill="x", padx=14, pady=14)

        def stat_box(col, icon, title, var_name, color):
            box = tk.Frame(inner, bg=color, bd=0, relief="flat")
            box.grid(row=0, column=col, padx=6, pady=4, sticky="nsew")
            inner.columnconfigure(col, weight=1)
            tk.Label(box, text=icon, font=("Segoe UI", 18),
                     bg=color, fg="white").pack(pady=(10, 0))
            tk.Label(box, text=title, font=FONT_SMALL,
                     bg=color, fg="white").pack()
            lbl = tk.Label(box, text="0", font=FONT_STAT,
                           bg=color, fg="white")
            lbl.pack(pady=(4, 10))
            setattr(self, var_name, lbl)

        stat_box(0, "🧾", "Total Items",  "lbl_items",      "#2980b9")
        stat_box(1, "💰", "Total (Rs.)",  "lbl_total",      "#27ae60")
        stat_box(2, "🏷️", "After Disc.", "lbl_after_disc", "#e67e22")

    # ── Table
    def _build_table(self, parent):
        frame = self._panel(parent, "📋  Current Bill")
        frame.pack(fill="both", expand=True, pady=(0, 10))

        cols = ("Qty", "Description", "Rate (Rs.)", "Amount (Rs.)")
        self.tree = ttk.Treeview(frame, columns=cols, show="headings",
                                 selectmode="browse")

        widths = [55, 200, 95, 100]
        for col, w in zip(cols, widths):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=w, anchor="center", minwidth=w)

        vsb = ttk.Scrollbar(frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)
        self.tree.pack(side="left", fill="both", expand=True, padx=(10, 0), pady=10)
        vsb.pack(side="left", fill="y", pady=10, padx=(0, 10))

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",
                        background=ROW_EVEN, foreground=TEXT,
                        rowheight=32, fieldbackground=ROW_EVEN,
                        font=FONT_BODY, borderwidth=1, relief="solid")
        style.configure("Treeview.Heading",
                        background=HEADER_BG, foreground=HEADER_FG,
                        font=FONT_HEAD, relief="flat", padding=6)
        style.map("Treeview",
                  background=[("selected", "#d6eaf8")],
                  foreground=[("selected", TEXT)])

        self.tree.tag_configure("even", background=ROW_EVEN)
        self.tree.tag_configure("odd",  background=ROW_ALT)
        self.tree.bind("<Delete>", self._remove_selected)

    # ── Action Bar — Remove | Clear All  ........  Print Bill | Back
    def _build_action_bar(self, parent):
        bar = tk.Frame(parent, bg=BG)
        bar.pack(fill="x", pady=(0, 6))

        # Left side buttons
        tk.Button(bar, text="🗑️  Remove Selected",
                  font=FONT_BTN, bg=DANGER, fg="white",
                  activebackground="#c0392b", activeforeground="white",
                  relief="flat", cursor="hand2", bd=0, padx=16, pady=8,
                  command=self._remove_selected
                  ).pack(side="left", padx=(0, 8))

        tk.Button(bar, text="🔄  Clear All",
                  font=FONT_BTN, bg="#95a5a6", fg="white",
                  activebackground="#7f8c8d", activeforeground="white",
                  relief="flat", cursor="hand2", bd=0, padx=16, pady=8,
                  command=self._clear_all
                  ).pack(side="left", padx=(0, 8))

        # Right side — Back button pehle pack karo (taake Print se left mein rahe)
        if self.back_cmd:
            tk.Button(bar, text="⬅  Back",
                      font=FONT_BTN, bg=DANGER, fg="white",
                      activebackground="#c0392b", activeforeground="white",
                      relief="flat", cursor="hand2", bd=0, padx=16, pady=8,
                      command=self.back_cmd
                      ).pack(side="right", padx=(8, 0))

        tk.Button(bar, text="🖨️  Print Bill",
                  font=FONT_BTN, bg=GOLD, fg="white",
                  activebackground="#d68910", activeforeground="white",
                  relief="flat", cursor="hand2", bd=0, padx=16, pady=8,
                  command=self._print_bill
                  ).pack(side="right")

    # ── Panel helper
    def _panel(self, parent, title):
        outer = tk.Frame(parent, bg=PANEL,
                         highlightthickness=1,
                         highlightbackground=BORDER)
        title_bar = tk.Frame(outer, bg=HEADER_BG, pady=6)
        title_bar.pack(fill="x")
        tk.Label(title_bar, text=title, font=FONT_HEAD,
                 bg=HEADER_BG, fg=HEADER_FG, padx=12
                 ).pack(side="left")
        return outer

    # ══════════════════════════════════════════
    #  Logic
    # ══════════════════════════════════════════
    def _add_to_cart(self, event=None):
        desc   = self.var_desc.get().strip()
        rate_s = self.var_rate.get().strip()
        qty_s  = self.var_qty.get().strip()

        if not desc:
            messagebox.showwarning("Input Error", "Description khali hai!")
            if self.ent_desc: self.ent_desc.focus()
            return
        try:
            rate = float(rate_s)
            if rate < 0: raise ValueError
        except ValueError:
            messagebox.showwarning("Input Error", "Rate sahi number hona chahiye!")
            if self.ent_rate: self.ent_rate.focus()
            return
        try:
            qty = int(qty_s)
            if qty <= 0: raise ValueError
        except ValueError:
            messagebox.showwarning("Input Error", "Quantity sahi number hona chahiye!")
            if self.ent_qty: self.ent_qty.focus()
            return

        self.cart.append({"desc": desc, "rate": rate,
                          "qty": qty, "amount": rate * qty})
        self._refresh_table()
        self._refresh_summary()
        self.var_desc.set("")
        self.var_rate.set("")
        self.var_qty.set("")
        if self.ent_desc: self.ent_desc.focus()

    def _apply_discount(self):
        try:
            pct = float(self.var_disc.get().strip())
            if not (0 <= pct <= 100): raise ValueError
        except ValueError:
            messagebox.showwarning("Input Error", "Discount 0–100 k beech hona chahiye!")
            return
        self.discount_pct = pct
        self._refresh_summary()

    def _remove_selected(self, event=None):
        sel = self.tree.selection()
        if not sel: return
        vals = self.tree.item(sel[0], "values")
        qty_v, desc_v = int(vals[0]), vals[1]
        for i, item in enumerate(self.cart):
            if item["desc"] == desc_v and item["qty"] == qty_v:
                self.cart.pop(i)
                break
        self._refresh_table()
        self._refresh_summary()

    def _clear_all(self):
        if not self.cart: return
        if messagebox.askyesno("Confirm", "Kya saara cart khali kar dein?"):
            self.cart.clear()
            self.discount_pct = 0.0
            self.var_disc.set("")
            self._refresh_table()
            self._refresh_summary()

    def _refresh_table(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for i, item in enumerate(self.cart, 1):
            tag = "even" if i % 2 == 0 else "odd"
            self.tree.insert("", "end", values=(
                item["qty"], item["desc"],
                f"Rs. {item['rate']:.2f}",
                f"Rs. {item['amount']:.2f}"
            ), tags=(tag,))

    def _refresh_summary(self):
        total      = sum(i["amount"] for i in self.cart)
        total_qty  = sum(i["qty"]    for i in self.cart)
        disc_amt   = total * self.discount_pct / 100
        after_disc = total - disc_amt
        self.lbl_items.config(text=str(total_qty))
        self.lbl_total.config(text=f"{total:.2f}")
        self.lbl_after_disc.config(text=f"{after_disc:.2f}")

    def _print_bill(self):
        if not self.cart:
            messagebox.showinfo("Empty", "Cart khali hai, kuch add karein pehle!")
            return

        win = tk.Toplevel(self.win)
        win.title("Bill Preview")
        win.configure(bg=PANEL)
        win.geometry("520x620")
        win.resizable(False, False)

        txt = tk.Text(win, font=("Courier New", 10), bg=PANEL, fg=TEXT,
                      relief="flat", bd=0, padx=20, pady=20)
        txt.pack(fill="both", expand=True)

        total     = sum(i["amount"] for i in self.cart)
        disc_amt  = total * self.discount_pct / 100
        after_d   = total - disc_amt
        total_qty = sum(i["qty"] for i in self.cart)

        lines = [
            "=" * 50,
            "         🏥  MEDICAL STORE RECEIPT",
            f"    Date: {datetime.now().strftime('%d-%b-%Y  %I:%M %p')}",
            "=" * 50,
            f"{'Qty':>4} {'Description':<20} {'Rate':>7} {'Amt':>9}",
            "-" * 50,
        ]
        for it in self.cart:
            lines.append(f"{it['qty']:>4} {it['desc']:<20} "
                         f"{it['rate']:>7.2f} {it['amount']:>9.2f}")
        lines += [
            "-" * 50,
            f"{'Total Items:':<30} {total_qty:>10}",
            f"{'Sub-Total (Rs.):':<30} {total:>10.2f}",
            f"{'Discount (' + str(self.discount_pct) + '%):':<30} {disc_amt:>10.2f}",
            f"{'After Discount (Rs.):':<30} {after_d:>10.2f}",
            "=" * 50,
            "       Thank you for your visit! 😊",
            "=" * 50,
        ]
        txt.insert("1.0", "\n".join(lines))
        txt.config(state="disabled")

        tk.Button(win, text="Close", font=FONT_BTN, bg=DANGER, fg="white",
                  relief="flat", cursor="hand2", padx=20, pady=6,
                  command=win.destroy).pack(pady=10)

    # ── Clock Function ────────────────────────────
    def _tick(self):
        now = datetime.now().strftime("%A, %d %B %Y   %I:%M:%S %p")
        self.lbl_time.config(text=now)
        self.win.after(1000, self._tick)