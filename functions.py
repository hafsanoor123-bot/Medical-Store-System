import tkinter as tk


# Back Function
def go_back(frame):
    frame.destroy()


def create_bill(root):
    frame = tk.Frame(root, bg="white")
    frame.place(x=0, y=0, relwidth=1 , relheight=1)

    # BACK BUTTON
    tk.Button(frame, text="Back", bg="#27762A" , fg="white", font= ("Verdana", 10, "bold") ,
                    command=lambda: go_back(frame)).place(x=10, y=10)
    

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





