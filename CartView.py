from tkinter import *
from tkinter import ttk
from Utils import Utils
import os

class CartView():
    def __init__(self, window, cart, shop_view):
        self.window = window
        self.cart = cart
        self.window.wm_iconphoto(False, Utils.Icon(os.path.dirname(__file__) + "../image/cart_icon.png"))
        self.shop_view = shop_view
        self.cart_tree = None
        self.treeFrame = None

        self.header()

        self.body()
        
        self.footer()
    
    def header(self):
        Utils.Image(self.window, os.path.dirname(__file__) + "../image/cart.png").pack()

    def body(self):
        Utils.Separator(self.window).pack(expand=True, fill=X, pady=(10, 15))
        bodyFrameUpper = Utils.Frame(self.window)
        Utils.Label(self.window, "Your Cart").pack(fill=X)
        Utils.Separator(self.window).pack(expand=True, fill=X, pady=(15, 15))
        bodyFrameUpper.pack(expand=True, fill=X)

        #Add Tree View of Orders
        self.treeFrame = Utils.Frame(self.window)
        self.setup_treeview()
        self.treeFrame.pack(expand=True, fill=X)


    def footer(self):
        footerFrame = Utils.Frame(self.window)
        self.shop_button = Utils.Button(footerFrame, "Remove", lambda:self.remove_order())
        self.shop_button.config(state=DISABLED)
        self.shop_button.pack(expand=True, fill=X, side='left')
        Utils.Button(footerFrame, "Close", lambda:self.window.destroy()).pack(expand=True, fill=X, side='left')
        footerFrame.pack(expand=True, fill=X)

    

    def setup_treeview(self):
        self.cart_tree = ttk.Treeview(self.treeFrame, columns=('Name', 'Quantity'), show='headings', selectmode='browse')

        self.cart_tree.bind("<<TreeviewSelect>>", self.remove_button_enabler)

        for col in self.cart_tree['columns']:
            self.cart_tree.column(col, anchor=CENTER, stretch=YES)

        self.cart_tree.heading('Name', text='Name')
        self.cart_tree.heading('Quantity', text='Quantity')

        for order in self.cart.orders:
            self.cart_tree.insert('', END, values=[order.product.name, order.quantity])

        self.cart_tree.pack(expand=True, fill=X)

    def remove_order(self):
        removed_prod = None
        selected_item_name = self.get_selection()[0]
        for order in self.cart.orders:
            if order.product.name == selected_item_name:
                removed_prod = order.product.name
                self.cart.remove_order(order)
        self.shop_button.config(state=DISABLED)
        self.update_treeview()
        # Add product back to ShopView products for purchase list
        for prod in self.cart.catalogue:
            if prod.name == removed_prod:
                self.shop_view.products_for_purchase.append(prod)

        # Call update tree_view() on ShopView
        self.shop_view.update_treeview()
        
    
    def update_treeview(self):
        self.cart_tree.pack_forget()
        self.setup_treeview()
    
    def get_selection(self):
        return self.cart_tree.item(self.cart_tree.selection()[0], option='values')

    def remove_button_enabler(self, *args):
        if(self.get_selection() == None):
            self.shop_button.config(state=DISABLED)
        else:
            self.shop_button.config(state=NORMAL)