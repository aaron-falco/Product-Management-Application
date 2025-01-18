from tkinter import *
from tkinter import ttk
from Utils import Utils
from ShopView import ShopView
import os

class SupplierView:
    def __init__(self, window, org, supplier):
        self.window = window
        self.window.wm_iconphoto(False, Utils.Icon(os.path.dirname(__file__) + "../image/supplier_icon.png"))
        self.org = org
        self.supplier = supplier
        self.products_tree = None
        self.body_tree = None
        self.header_label = None
        self.header_frame = None

        self.header()
        self.body()        
        self.footer()
    
    def header(self):
        self.header_frame = Utils.Frame(self.window)
        Utils.Image(self.header_frame, os.path.dirname(__file__) + "../image/supplier.png").pack()
        Utils.Separator(self.header_frame).pack(expand=True, fill=X, pady=(10, 15))
        self.setup_header_label()
        self.header_frame.pack(expand=True, fill=X, pady=(15, 10))

    def body(self):
        self.bodyFrame = Utils.Frame(self.window)

        self.setup_tree_view()

        self.bodyFrame.pack(expand=True, fill=X)

    def footer(self):
        footerFrame = Utils.Frame(self.window)
        Utils.Button(footerFrame, "Order", lambda:self.open_cart_window()).pack(expand=True, fill=X, side='left')
        Utils.Button(footerFrame, "Close", lambda:self.window.destroy()).pack(expand=True, fill=X, side='left')
        footerFrame.pack(expand=True, fill=X)
    
    def open_cart_window(self):
        ShopView(Utils.Toplevel("Cart"), self.org, self.supplier, self)
    
    def setup_header_label(self):
        self.header_label = Utils.Label(self.header_frame, "Welcome to " + self.supplier.name + f" (Total Profit: {self.supplier.profit:.2f})")
        self.header_label.pack()

    def update_header_label(self):
        self.header_label.pack_forget()
        self.setup_header_label()
    
    def setup_tree_view(self):
        self.products_tree = ttk.Treeview(self.bodyFrame, columns=('Name', 'Price', 'Stock'), show='headings', selectmode='none')

        for col in self.products_tree['columns']:
            self.products_tree.column(col, anchor=CENTER, stretch=NO)

        self.products_tree.heading('Name', text='Name')
        self.products_tree.heading('Price', text='Price')
        self.products_tree.heading('Stock', text='Stock')

        for prod in self.supplier.products.get_available_products():
            self.products_tree.insert('', END, values=[prod.name, f'{prod.price:.2f}', prod.stock])


        self.products_tree.pack(expand=True, fill=X)

    def update_tree_view(self):
        self.products_tree.pack_forget()
        self.setup_tree_view()