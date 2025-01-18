import os
from tkinter import *
from tkinter import ttk
from Utils import Utils
from Cart import Cart
from Order import Order
from Product import Product
from InvalidQuantityException import InvalidQuantityException
from InvalidQuantityErrorWindow import InvalidQuantityErrorWindow

class AddOrderView:

    def __init__(self, window, cart, product):
        self.window = window
        self.cart = cart
        self.product = product
        self.quantity_entry = None
        
        self.window.wm_iconphoto(False, Utils.Icon(os.path.dirname(__file__)  + "../image/cart_icon.png"))

        self.header()
        self.body()
        self.footer()

    def header(self):
        headerFrame = Utils.Frame(self.window)
        Utils.Image(self.window, os.path.dirname(__file__)  + "../image/cart.png").pack()
        headerFrame.pack(expand=True, fill=X)

    def body(self):
        bodyFrameUpper = Utils.Frame(self.window)
        Utils.Separator(bodyFrameUpper).pack(expand=True, fill=X, pady=(10,10))
        Utils.Label(bodyFrameUpper, "Adding " + self.product.name).pack()
        Utils.Separator(bodyFrameUpper).pack(expand=True, fill=X, pady=(10,10))
        bodyFrameUpper.pack(expand=True, fill=X)

        bodyFrameLower = Utils.Frame(self.window)
        Utils.Label(bodyFrameLower, "Stock:").pack(side=LEFT)
        self.quantity_entry = Entry(bodyFrameLower)
        self.quantity_entry.insert(0, '0')
        self.quantity_entry.pack(side=LEFT)
        bodyFrameLower.pack(expand=True)
    
    def footer(self):
        footerFrame = Utils.Frame(self.window)
        Utils.Button(footerFrame, "Add", lambda:self.try_add()).pack(side=LEFT, expand=True, fill=X)
        footerFrame.pack(expand=True, fill=X, pady=(10,0))
    
    def try_add(self):
        try:
            if not self.quantity_entry.get().isdigit():
                raise InvalidQuantityException()
            quantity = int(self.quantity_entry.get())
            self.cart.add_order(Order(self.product, quantity, self.cart))
            self.window.destroy()
        except InvalidQuantityException as err:
            InvalidQuantityErrorWindow(err)

    def restrict_input(self, *args):
        if self.entry_var.get().isdigit():
            return
        else:
            self.entry_var.set("")

    def add_product_to_cart(self):
        pass

    def open_invalid_quantity_error_window(self, err):
        pass
