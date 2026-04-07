import tkinter as tk
import create_bill 
import manage_stock

#main window 
root = tk.Tk()
root.title("Medical Store System")
root.configure(bg="lightgreen")  

# title = tk.Label(root, text="Medical Store System", font=("Verdana", 24, "bold"), bg="#e6f2ff", fg="#333")
# title.pack(pady=20)


# Zommed mode
root.state("zoomed")

frame = tk.Frame(root, bg="lightgreen" , width=1000 , height=800)
frame.place(relx=0.5, rely=0.5, anchor="center")


# Buttons Style
button_options = {
    "width": 12 ,  # button ka width
    "height": 3 ,   # button ka height
    "font": ("Verdana", 20, "bold"),  # text style
    "bg": "white",    # green background
    "fg": "#27762A",      # text color
  
    "relief": "raised", # 3D effect
    "cursor": "hand2" ,  # mouse pointer change

    "highlightthickness": 2,        # border thickness
    "highlightbackground": "#4CAF50", # border color
}



# Buttons
btn1 = tk.Button(frame, text="Create Bill", **button_options , command=lambda: create_bill.create_bill_screen(root))
btn1.pack(side=tk.LEFT, padx=10)  # 10 px gap

btn2 = tk.Button(frame, text="Manage Stock", **button_options , command=lambda:manage_stock.open_stock_window(root))
btn2.pack(side=tk.LEFT, padx=10)

btn3 = tk.Button(frame, text="Sales Report", **button_options , command=lambda:create_bill.sales_report(root))
btn3.pack(side=tk.LEFT, padx=10)

root.mainloop()

