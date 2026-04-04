import tkinter as tk
from tkinter import ttk
from datetime import datetime


# Back Function
def go_back(frame):
    frame.destroy()


def create_bill_screen(root):
    frame_1 = tk.Frame(root, bg = "#fafafa")
    frame_1.place(x=0, y=0, relwidth=1 , relheight=1)

    frame_2 = tk.LabelFrame(frame_1 , text="Current Bill" , bg="#fafafa" ,
                          highlightbackground="black",
                          font=("Arial", 12),)
    frame_2.place(x=10, y=10, relwidth=0.5, relheight=0.9)
    



    frame_3 = tk.LabelFrame(frame_1, text="Product Management", bg="#fafafa",
                        highlightbackground="black",
                        font=("Arial", 12))
    frame_3.place(relx=0.55, y=10, relwidth=0.35, height=250)

    frame_4 = tk.Frame(frame_1, bg="#fafafa", highlightbackground="black" , highlightthickness=1)
    frame_4.place(relx=0.55, y=270, relwidth=0.35, height=50)

#     # Frame 3 (right side)

#     frame_3 = tk.LabelFrame(frame_1 , text="Cart" , bg="#fafafa" ,
#                          highlightbackground="black",
#                          font=("Arial", 12),)
    
#     frame_3.place(x=380, y=10, width=350, height=250)




# # Working in Product Managment 

    input_1 = tk.Label(frame_3 , text="Description :" , font=("Arial", 14) , bg="#fafafa" )
    input_1.place(x=20 , y=20)
    description_entry = tk.Entry(frame_3 , highlightthickness=1 , highlightbackground="black")
    description_entry.place(x=250 , y=25)

    input_2 = tk.Label(frame_3 , text="Rate :" , font=("Arial", 14) , bg="#fafafa"  )
    input_2.place(x=20 , y=60)
    rate_entry = tk.Entry(frame_3 , highlightthickness=1 , highlightbackground="black")
    rate_entry.place(x=250 , y=65)
    
    input_3 = tk.Label(frame_3 , text="Quantity:" , font=("Arial", 14) , bg="#fafafa"  )
    input_3.place(x=20 , y=100)
    quantity_entry = tk.Entry(frame_3 , highlightthickness=1 , highlightbackground="black")
    quantity_entry.place(x=250 , y=105)

    add_btn = tk.Button(
    frame_3,
    text="Add to Cart",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",   # nice green button
    fg="white",
    padx=10,
    pady=5
)
    
    add_btn.place(relx=0.5, rely=1, anchor="s", y=-20)


    input_4 = tk.Label(frame_4, text="Discount:", font=("Arial", 14), bg="#fafafa")
    input_4.place(x=20, y=10)

    discount_entry = tk.Entry(frame_4, highlightthickness=1, highlightbackground="black", width=20)
    discount_entry.place(x=250, y=15) 

#     # input_4 = tk.Label(frame_2 , text="Discount:" , font=("Arial", 14) , bg="#fafafa"  )
#     # input_4.place(x=20 , y=140)
#     # quantity_entry = tk.Entry(frame_2 , highlightthickness=1 , highlightbackground="black")
#     # quantity_entry.place(x=200 , y=145)

#     # input_5 = tk.Label(frame_2 , text="Discount:" , font=("Arial", 14) , bg="#fafafa"  )
#     # input_5.place(x=20 , y=180)
#     # quantity_entry = tk.Entry(frame_2 , highlightthickness=1 , highlightbackground="black")
#     # quantity_entry.place(x=200 , y=185)




root = tk.Tk()
root.title("Medical Store System")
root.state("zoomed")
create_bill_screen(root)
root.mainloop()







