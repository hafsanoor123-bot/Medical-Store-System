import tkinter as tk
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox


# Back Function
def go_back(frame):
    frame.destroy()


item_no = 1  # cart me items count

description_entry = None
rate_entry = None
quantity_entry = None
discount_entry = None

tree = None  # table

# <-- Important: Tkinter StringVar init
amount_var = None
amount_after_discount_var = None

def add_to_cart(description_entry, rate_entry, quantity_entry, tree):
    
    global item_no, discount_entry, amount_var, amount_after_discount_var

    desc = description_entry.get()
    rate = rate_entry.get()
    qty = quantity_entry.get()

    if desc == "" or rate == "" or qty == "":
        return

    try:
        rate = float(rate)
        qty = int(qty)
    except:
        return

    amount = round(rate * qty, 2)
    tree.insert("", "end",
            values=(item_no, desc, rate, qty, amount),
            tags=("border",))
    item_no += 1

    # Clear entries
    description_entry.delete(0, tk.END)
    rate_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)    



def apply_discount(tree, discount_entry):

    global amount_var, amount_after_discount_var  # access global variables
    
    # Total Amount Calculate
    total = 0
    for child in tree.get_children():
        total += float(tree.item(child)["values"][4])  # Amount column
    
    amount_var.set(round(total, 2))  # Total Amount Show

    # Discount
    discount = discount_entry.get()
    try:
        discount = float(discount)
    except:
        discount = 0

    after_discount = total - discount
    if after_discount < 0:
        after_discount = 0

    amount_after_discount_var.set(round(after_discount, 2))


def check_data():
    des = description_entry.get()
    rate = rate_entry.get()
    quan = quantity_entry.get()

    if des == "" or rate == "" or quan == "" :
        messagebox.showwarning("Warning", "Please enter the data!")
        return False
    
    return True

def handle_submit():
    if check_data():   # agar data sahi hai
        add_to_cart(description_entry, rate_entry, quantity_entry, tree)


def create_bill_screen(root):

    global description_entry, rate_entry, quantity_entry , discount_entry , tree
    global amount_var, amount_after_discount_var
   
    amount_var = tk.StringVar(root)
    amount_after_discount_var = tk.StringVar(root)

    frame_1 = tk.Frame(root, bg = "#fafafa")
    frame_1.place(x=0, y=0, relwidth=1 , relheight=1)

    frame_2 = tk.LabelFrame(frame_1 , text="Current Bill" , bg="#fafafa" ,
                          highlightbackground="black",
                          font=("Arial", 12),)
    frame_2.place(x=10, y=10, relwidth=0.56, relheight=0.9)

    columns = ("No", "Description", "Rate", "Quantity", "Amount")

# Style pehle define karo
    style = ttk.Style()
    style.theme_use("clam")   # important

    style.configure(
        "Custom.Treeview",
        background="white",
        fieldbackground="white",
        foreground="black",
        rowheight=30,
        font=("Arial", 12),
        borderwidth=1,
        relief="solid"
    )

    style.configure(
        "Custom.Treeview.Heading",
        font=("Arial", 13, "bold"),
        borderwidth=1,
        relief="solid"
    )

# Treeview create karo style ke saath
    tree = ttk.Treeview(frame_2, columns=columns, show="headings", style="Custom.Treeview")

# Headings set karo
    for col in columns:
        tree.heading(col, text=col)

# Columns width & alignment set karo
    tree.column("No", width=20, anchor="center")           
    tree.column("Description", width=220, anchor="w")      
    tree.column("Rate", width=80, anchor="center")        
    tree.column("Quantity", width=80, anchor="center")   
    tree.column("Amount", width=100, anchor="center")   

# Place tree
    tree.place(relwidth=1, relheight=1)
    tree.tag_configure("border", background="white")


    frame_3 = tk.LabelFrame(frame_1, text="Add Cart", bg="#fafafa" , highlightthickness=1,
                        highlightbackground="black",
                        font=("Arial", 12))
    frame_3.place(relx=0.6, y=30, relwidth=0.35, height=250)

    frame_4 = tk.Frame(frame_1, bg="#fafafa", highlightbackground="black" , highlightthickness=1)
    frame_4.place(relx=0.6, y=300, relwidth=0.35, height=120)

    frame_5 = tk.Frame(frame_1, bg="#fafafa", highlightbackground="black", highlightthickness=1)
    frame_5.place(relx=0.6, y=440, relwidth=0.35, height=100)

    frame_6 = tk.Frame(frame_1, bg="#fafafa", highlightbackground="black", highlightthickness=1)
    frame_6.place(relx=0.6, y=580, relwidth=0.35, height=60)


# # Working of frames  

    input_1 = tk.Label(frame_3 , text="Description :" , font=("Arial", 14) , bg="#fafafa" )
    input_1.place(x=20 , y=20)
    description_entry = tk.Entry(frame_3 , font=("Arial", 12), highlightthickness=1 , highlightbackground="black")
    description_entry.place(x=250 , y=25)

    input_2 = tk.Label(frame_3 , text="Rate :" , font=("Arial", 14) , bg="#fafafa"  )
    input_2.place(x=20 , y=60)
    rate_entry = tk.Entry(frame_3 , font=("Arial", 12), highlightthickness= 1 , highlightbackground="black")
    rate_entry.place(x=250 , y=65)
    
    input_3 = tk.Label(frame_3 , text="Quantity:" , font=("Arial", 14) , bg="#fafafa"  )
    input_3.place(x=20 , y=100)
    quantity_entry = tk.Entry(frame_3 , font=("Arial", 12), highlightthickness=1 , highlightbackground="black")
    quantity_entry.place(x=250 , y=105)

    add_btn = tk.Button(
    frame_3,
    text="Add to Cart",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",   
    fg="white",
    padx=10,
    pady=5,
    command=lambda: handle_submit
)
    
    add_btn.place(relx=0.5, rely=1, anchor="s", y=-20)
    
    

    input_4 = tk.Label(frame_4, text="Discount:", font=("Arial", 14), bg="#fafafa")
    input_4.place(x=20, y=10)

    discount_entry = tk.Entry(frame_4, font=("Arial", 12), highlightthickness=1, highlightbackground="black", width=20)
    discount_entry.place(x=250, y=15)

# ---------------- Apply Discount Button ----------------
    apply_btn = tk.Button(
    frame_4,
    text="Apply Discount",
    font=("Arial", 12, "bold"),
    bg="#2196F3",
    fg="white",
    padx=10,
    pady=5,
    width=12,
    command=lambda: apply_discount(tree, discount_entry)
)

# Center bottom
    apply_btn.place(relx=0.5, rely=1, anchor="s", y=-10)


    tk.Label(frame_5, text="Total Amount:", font=("Arial", 14), bg="#fafafa").place(x=20, y=10)
    tk.Entry(frame_5, font=("Arial", 12), textvariable=amount_var, readonlybackground="white",
             highlightthickness=1, highlightbackground="black",
             state="readonly", width=20).place(x=250, y=10)

    tk.Label(frame_5, text="Amount After Discount:", font=("Arial", 14), bg="#fafafa").place(x=20, y=45)
    tk.Entry(frame_5, font=("Arial", 12), textvariable=amount_after_discount_var, readonlybackground="white",
             highlightthickness=1, highlightbackground="black",
             state="readonly", width=20).place(x=250, y=45)
    

        # Back Button - left side
    back_btn = tk.Button(frame_6, text="Back", font=("Arial", 12, "bold"),
                     bg="#f44336", fg="white", padx=20, pady=5,
                     command=lambda: go_back(root))
    back_btn.place(relx=0, rely=0.5, anchor="w", x=10)  # left side, vertically centered

# Print Button - right side
    print_btn = tk.Button(frame_6, text="Print", font=("Arial", 12, "bold"),
                      bg="#4CAF50", fg="white", padx=20, pady=5,
                      command=lambda: print("Printing Bill..."))
    print_btn.place(relx=1, rely=0.5, anchor="e", x=-10)  # right side, vertically centered




root = tk.Tk()
root.title("Medical Store System")
root.state("zoomed")
create_bill_screen(root)
root.mainloop()









