import tkinter as tk
from tkinter import ttk, font
from datetime import datetime

import create__bill
import manage_stock
import view_stock   # ✅ NEW IMPORT


def create_main_screen():
    root = tk.Tk()
    root.title("Medical Store Management System")
    root.state("zoomed")
    root.configure(bg="#f0f4f8")

    window_width  = 1200
    window_height = 700
    screen_width  = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width  - window_width)  // 2
    y = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    container = tk.Frame(root, bg="#f0f4f8")
    container.pack(expand=True, fill="both")

    def show_frame(frame):
        frame.lift()

    # ═════════════════════════════════════════════
    #  HOME FRAME
    # ═════════════════════════════════════════════
    home_frame = tk.Frame(container, bg="#f0f4f8")
    home_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    home_header = tk.Frame(home_frame, bg="#2c3e50", height=120)
    home_header.pack(fill="x")
    home_header.pack_propagate(False)

    tk.Label(home_header, text="🏥", font=("Segoe UI", 40),
             bg="#2c3e50", fg="white").pack(side="left", padx=(30, 10), pady=20)

    tk.Label(home_header, text="MEDICAL STORE",
             font=("Segoe UI", 28, "bold"),
             bg="#2c3e50", fg="white").pack(side="left", padx=10)

    tk.Label(home_header, text="Management System",
             font=("Segoe UI", 14),
             bg="#2c3e50", fg="#bdc3c7").pack(side="left", padx=5)

    tk.Label(home_header,
             text=datetime.now().strftime("%A, %B %d, %Y"),
             font=("Segoe UI", 11),
             bg="#2c3e50", fg="#bdc3c7").pack(side="right", padx=30)

    main_frame = tk.Frame(home_frame, bg="#f0f4f8")
    main_frame.pack(expand=True, fill="both", padx=40, pady=40)

    tk.Label(main_frame,
             text="Welcome! Please select an option to continue",
             font=("Segoe UI", 16),
             bg="#f0f4f8", fg="#34495e"
             ).grid(row=0, column=0, columnspan=4, pady=(0, 40))

    button_style = {
        "width": 15, "height": 2,
        "font": ("Segoe UI", 14, "bold"),
        "relief": "flat", "cursor": "hand2", "borderwidth": 0
    }

    buttons_frame = tk.Frame(main_frame, bg="#f0f4f8")
    buttons_frame.grid(row=1, column=0, columnspan=4, pady=20)

    # ── Buttons ──
    bill_btn = tk.Button(buttons_frame, text="💰 Create Bill",
                         bg="#27ae60", fg="white",
                         activebackground="#2ecc71",
                         activeforeground="white",
                         command=lambda: show_frame(bill_frame),
                         **button_style)
    bill_btn.pack(side="left", padx=15, pady=10)

    stock_btn = tk.Button(buttons_frame, text="📦 Manage Stock",
                          bg="#2980b9", fg="white",
                          activebackground="#3498db",
                          activeforeground="white",
                          command=lambda: show_frame(stock_frame),
                          **button_style)
    stock_btn.pack(side="left", padx=15, pady=10)

    view_stock_btn = tk.Button(buttons_frame, text="📋 View Stock",
                               bg="#c55a11", fg="white",
                               activebackground="#e07030",
                               activeforeground="white",
                               command=lambda: show_frame(view_stock_frame),
                               **button_style)
    view_stock_btn.pack(side="left", padx=15, pady=10)

    report_btn = tk.Button(buttons_frame, text="📊 Sales Report",
                           bg="#e67e22", fg="white",
                           activebackground="#f39c12",
                           activeforeground="white",
                           command=lambda: show_frame(report_frame),
                           **button_style)
    report_btn.pack(side="left", padx=15, pady=10)

    # Stats cards
    stats_frame = tk.Frame(main_frame, bg="#f0f4f8")
    stats_frame.grid(row=2, column=0, columnspan=4, pady=(50, 0))

    card_style = {"bg": "white", "relief": "ridge", "bd": 1, "padx": 20, "pady": 15}

    for title, val, color in [
        ("Today's Sales",   "Rs. 0", "#27ae60"),
        ("Low Stock Items", "0",     "#e74c3c"),
        ("Total Medicines", "0",     "#3498db"),
    ]:
        card = tk.Frame(stats_frame, **card_style)
        card.pack(side="left", padx=10)
        tk.Label(card, text=title, font=("Segoe UI", 11),
                 bg="white", fg="#7f8c8d").pack()
        tk.Label(card, text=val, font=("Segoe UI", 20, "bold"),
                 bg="white", fg=color).pack()

    home_footer = tk.Frame(home_frame, bg="#34495e", height=40)
    home_footer.pack(fill="x", side="bottom")
    home_footer.pack_propagate(False)
    tk.Label(home_footer,
             text="© 2024 Medical Store Management System | Developed with ❤️",
             font=("Segoe UI", 9),
             bg="#34495e", fg="#ecf0f1").pack(pady=10)

    # ═════════════════════════════════════════════
    #  BILL FRAME
    # ═════════════════════════════════════════════
    bill_frame = tk.Frame(container, bg="#f0f4f8")
    bill_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
    create__bill.build_billing_ui(
        bill_frame,
        back_cmd=lambda: show_frame(home_frame)
    )

    # ═════════════════════════════════════════════
    #  STOCK FRAME
    # ═════════════════════════════════════════════
    stock_frame = tk.Frame(container, bg="#f0f4f8")
    stock_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
    manage_stock.build_stock_ui(
        stock_frame,
        back_cmd=lambda: show_frame(home_frame)
    )

    # ═════════════════════════════════════════════
    #  VIEW STOCK FRAME (external file)
    # ═════════════════════════════════════════════
    view_stock_frame = tk.Frame(container, bg="#f0f4f8")
    view_stock_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    view_stock.build_view_stock_ui(
        view_stock_frame,
        back_cmd=lambda: show_frame(home_frame)
    )

    # ═════════════════════════════════════════════
    #  REPORT FRAME
    # ═════════════════════════════════════════════
    report_frame = tk.Frame(container, bg="#f0f4f8")
    report_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    tk.Label(report_frame,
             text="📊  Sales Report\n\nComing Soon!",
             font=("Segoe UI", 20, "bold"),
             bg="#f0f4f8", fg="#34495e",
             justify="center").pack(expand=True)

    show_frame(home_frame)
    return root


if __name__ == "__main__":
    root = create_main_screen()
    root.mainloop()

