import tkinter as tk
from tkinter import ttk
from datetime import datetime


# Back Function
def go_back(frame):
    frame.destroy()


# def create_bill(root):
#     frame = tk.Frame(root, bg="white")
#     frame.place(x=0, y=0, relwidth=1 , relheight=1)

#     # BACK BUTTON
#     tk.Button(frame, text="Back", bg="#27762A" , fg="white", font= ("Verdana", 10, "bold") ,
#                     command=lambda: go_back(frame)).place(x=0, y=0)
    



# def create_bill_screen(root):
#     frame = tk.Frame(root, bg="white")
#     frame.place(x=0, y=0, relwidth=1, relheight=1)

#     # Title
#     tk.Label(frame, text="INVOICE", font=("Arial", 20, "bold"), bg="white").pack(pady=10)

#     # Customer + Date
#     top_frame = tk.Frame(frame, bg="white")
#     top_frame.pack(pady=5)


#     tk.Label(top_frame, text="Date:", bg="white").grid(row=0, column=2)
#     tk.Label(top_frame, text=datetime.now().strftime("%d-%m-%Y"), bg="white").grid(row=0, column=3)

#     # Product Inputs
#     input_frame = tk.Frame(frame, bg="white")
#     input_frame.pack(pady=10)

#     tk.Label(input_frame, text="Product").grid(row=0, column=0)
#     tk.Label(input_frame, text="Price").grid(row=0, column=1)
#     tk.Label(input_frame, text="Qty").grid(row=0, column=2)

#     entry_product = tk.Entry(input_frame)
#     entry_product.grid(row=1, column=0)

#     entry_price = tk.Entry(input_frame)
#     entry_price.grid(row=1, column=1)

#     entry_qty = tk.Entry(input_frame)
#     entry_qty.grid(row=1, column=2)

#     # Table
#     tree = ttk.Treeview(frame, columns=("P", "Pr", "Q", "T"), show="headings")
#     tree.pack(pady=10)

#     tree.heading("P", text="Product")
#     tree.heading("Pr", text="Price")
#     tree.heading("Q", text="Qty")
#     tree.heading("T", text="Total")

#     def add_item():
#         p = entry_product.get()
#         pr = float(entry_price.get())
#         q = int(entry_qty.get())
#         t = pr * q

#         items.append(t)
#         tree.insert("", "end", values=(p, pr, q, t))

#     tk.Button(frame, text="Add Item", command=add_item).pack()

#     # Total
#     total_label = tk.Label(frame, text="Grand Total: 0", font=("Arial", 12, "bold"), bg="white")
#     total_label.pack(pady=10)

#     def generate_bill():
#         total = sum(items)
#         total_label.config(text=f"Grand Total: {total}")

#     tk.Button(frame, text="Generate Bill", command=generate_bill).pack(pady=5)

#     tk.Button(frame, text="Back", command=lambda: frame.destroy()).pack()





def create_bill_screen(root):
    frame_1 = tk.Frame(root, bg="white")
    frame_1.place(x=0, y=0, relwidth=1 , relheight=1)

    frame_2 = tk.Frame(frame_1, bg="lightgreen")
    frame_2.place(x=0 , y=0 , relwidth=1 , height=50)
    tk.Label(frame_2, text="Rehman Medical Store", font=("Verdana", 15), bg="white").pack(pady=10)
    # tk.Label(frame_2, text="100Feet Road, Society Sukkur", font=("Verdana", 15), bg="white").pack(pady=10)


    frame_3 = tk.LabelFrame(frame_1 , text="Product Management" , bg="white" ,
                         highlightthickness=1 , highlightbackground="black",
                         font=("Arial", 12, "bold"),)
    frame_3.place(x=0 , y=70, relwidth=0.5 , height=300)




root = tk.Tk()
root.title("Medical Store System")
root.state("zoomed")
create_bill_screen(root)
root.mainloop()

def manage_stock(root):
    frame = tk.Frame(root, bg="white")
    frame.place(x=0, y=0, relwidth=1 , relheight=1)

    # BACK BUTTON
    tk.Button(frame, text="Back", bg="#27762A" , fg="white", font= ("Verdana", 10, "bold") ,
                    command=lambda: go_back(frame)).place(x=10, y=10)
    

def sales_report(root):
    frame = tk.Frame(root, bg="white")
    frame.place(x=0, y=0, relwidth=1 , relheight=1)

    # BACK BUTTON
    tk.Button(frame, text="Back", bg="#27762A" , fg="white", font= ("Verdana", 10, "bold") ,
                    command=lambda: go_back(frame)).place(x=10, y=10)





