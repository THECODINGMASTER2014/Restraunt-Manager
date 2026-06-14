import tkinter as tk
from tkinter import tkk, messagebox

class RestrauntOrderManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Order Management System")


        self.menu_items = {
            "Fries": 2,
            "Lunch": 2,
            "Burger": 3,
            "Pizza": 4, 
            "Cheese Burger": 2.5,
            "Drinks": 1,
        }

        self.exchange_rate = 95.11        
        self.setup_background(root)  
        frame = tkk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)   

        tkk.Label(frame, text="Restaurant Order Management System", font=("Arial", 20, "bold")).grid(row=0,columnspan=3, padx=10, pady=10)
        self.menu.labels = {}
        self.menu.qauntities = {}

        for i, (item, price) in enumerate(self.menu_items.items()):
            label = tkk.Label(frame, text=f"{item} ${price:.2f}", font=("Arial", 12))
            label.grid(row=i, column=0, padx=10, pady=5)
            self.menu.labels[item] = label

            qauntity_entry = tkk.Entry(frame, width=5)
            qauntity_entry.grid(row=i, column=1, padx=10, pady=5)
            self.menu.qauntities[item] = qauntity_entry

        self.currency_var = tk.StringVar()
        ttk.label(frame, text="Currency:", font=("Arial", 12)).grid(row=len(self.menu_items) + 1, column=0, padx=10, pady=5)

        currency_dropdown = ttk.Combobox(frame, textvariable = self.currency_var, state = "readonly", width = 18, values = ("USD", "INR"))
        currency_dropdown.grid(row = len(self.menu_items)+1, column=1, padx=10, pady=5)
        currency_dropdown.current(0)
        self.currency_var.trace("w", self.update_menu_prices)
        order_button = ttk.button(frame, text="Place Order", command=self.place_order)
        order_button.grid(row=len(self.menu_items) + 2, columnspan = 3,padx = 10, pady = 10)

