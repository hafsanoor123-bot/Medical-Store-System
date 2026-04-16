import tkinter as tk
from tkinter import ttk


# ═════════════════════════════════════════════
#  MAIN UI FUNCTION
# ═════════════════════════════════════════════
def build_view_stock_ui(parent, back_cmd=None):
    from database import get_connection, create_database_and_table, fetch_all_stock

    parent.configure(bg="#f0f4f8")

    # ───────── TOP BAR ─────────
    top_frame = tk.Frame(parent, bg="#f0f4f8")
    top_frame.pack(fill="x", padx=10, pady=10)

    # Back Button
    if back_cmd:
        tk.Button(top_frame, text="🏠 Back",
                  bg="#7f8c8d", fg="white",
                  font=("Segoe UI", 11, "bold"),
                  relief="flat", cursor="hand2",
                  command=back_cmd).pack(side="left", padx=(0, 10))

    # Refresh Button
    def refresh_data():
        populate_table(tree)

    tk.Button(top_frame, text="🔄 Refresh",
              bg="#2980b9", fg="white",
              font=("Segoe UI", 11, "bold"),
              relief="flat", cursor="hand2",
              command=refresh_data).pack(side="left")

    # Title
    tk.Label(parent,
             text="📋 Stock Records",
             font=("Segoe UI", 18, "bold"),
             bg="#f0f4f8", fg="#2c3e50").pack(pady=(5, 10))

    # ───────── TABLE ─────────
    table_frame = tk.Frame(parent)
    table_frame.pack(fill="both", expand=True, padx=10, pady=10)

    columns = ("No", "Description", "Stock", "Rate", "Date", "Time")

    tree = ttk.Treeview(table_frame, columns=columns, show="headings")

    widths = [50, 300, 100, 100, 120, 100]

    for col, w in zip(columns, widths):
        tree.heading(col, text=col)
        tree.column(col, width=w, anchor="center")

    # Scrollbar
    scrollbar = tk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)

    tree.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Initial Load
    populate_table(tree)


# ═════════════════════════════════════════════
#  POPULATE TABLE
# ═════════════════════════════════════════════
def populate_table(tree):
    from database import get_connection, create_database_and_table, fetch_all_stock

    conn = get_connection()
    create_database_and_table(conn)
    data = fetch_all_stock(conn)

    # Clear old data
    tree.delete(*tree.get_children())

    # Insert new data
    for i, row in enumerate(data, start=1):
        tree.insert("", "end", values=(
            i,
            row.get("description", ""),
            row.get("stock", ""),
            row.get("rate", ""),
            row.get("created_date", ""),
            row.get("created_time", ""),
        ))