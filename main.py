import tkinter as tk

# window create karna
root = tk.Tk()

# window ka title
root.title("My First Window")

# window ka size
root.geometry("400x300")

# ek label (text)
label = tk.Label(root, text="Hello Hafsa 👋", font=("Arial", 14))
label.pack(pady=20)

# button
button = tk.Button(root, text="Click Me", command=lambda: print("hafsa Noor!"))
button.pack()

# window run karna
root.mainloop()