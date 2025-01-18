from tkinter import *
from tkinter import ttk
from Utils import Utils
import os

class EditSupplierView:
    def __init__(self, window, org, supplier, supplier_view):
        self.window = window
        self.supplier = supplier
        self.org = org
        self.window.wm_iconphoto(False, Utils.Icon(os.path.dirname(__file__)  + "../image/cart_icon.png"))
        self.products = self.supplier.products.get_all_products()
        self.supplier_view = supplier_view
        self.delist_button = None
        self.products_tree = None
        self.products_tree_frame = None

        self.header()
        self.body()
        self.footer()
    
    def header(self):
        Utils.Image(self.window, "image/cart.png").pack()

    def body(self):
        bodyFrame = Utils.Frame(self.window)

        Utils.Separator(bodyFrame).pack(expand=True, fill=X, pady=(10, 15))
        Utils.Label(bodyFrame, "Ordering from " + self.supplier.name).pack()
        Utils.Separator(bodyFrame).pack(expand=True, fill=X, pady=(15, 10))

        bodyFrame.pack(expand=True, fill=X)

        self.products_tree_frame = Utils.Frame(self.window)

        self.setup_treeview()

        self.products_tree_frame.pack(expand=True, fill=X)

    def footer(self):
        footerFrame = Utils.Frame(self.window)
        Utils.Button(footerFrame, "Remove", lambda:self.remove_item()).pack(expand=True, fill=X, side=LEFT)
        self.delist_button = Utils.Button(footerFrame, "Delist", lambda:self.delist_item())
        self.delist_button.config(state=DISABLED)
        self.delist_button.pack(expand=True, fill=X, side=LEFT)
        Utils.Button(footerFrame, "Close", lambda:self.window.destroy()).pack(expand=True, fill=X, side=LEFT)
        footerFrame.pack(expand=True, fill=X)

    def setup_treeview(self):
        self.products_tree = ttk.Treeview(self.products_tree_frame, show='tree', selectmode='browse')

        self.products_tree.bind("<<TreeviewSelect>>", self.delist_button_enabler)

        for prod in self.products:
            self.products_tree.insert('', END, text=str(prod))
        
        self.products_tree.pack(expand=True, fill=X)

    def update_treeview(self):
        self.products_tree.pack_forget()
        self.setup_treeview()
    
    def remove_item(self):
        selection = self.get_selection()
        for prod in self.supplier.products.get_all_products():
            if selection == str(prod):
                self.supplier.products.get_all_products().remove(prod)
        self.update_treeview()
        self.delist_button.config(state=DISABLED)
        self.supplier_view.update_tree_view()

    def delist_item(self):
        selection = self.get_selection()
        for prod in self.supplier.products.get_all_products():
            if selection == str(prod):
                prod.available = False
        self.delist_button.config(state=DISABLED)
        self.supplier_view.update_tree_view()
        
    def get_selection(self):
        return self.products_tree.item(self.products_tree.selection()[0], option='text')

    def delist_button_enabler(self, *args):
        selection = self.get_selection()
        for prod in self.supplier.products.get_available_products():
            if selection == str(prod):
                self.delist_button.config(state=NORMAL)
                return
        self.delist_button.config(state=DISABLED)
