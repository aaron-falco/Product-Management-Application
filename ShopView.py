from tkinter import *
from tkinter import ttk
from Utils import Utils
from Cart import Cart
from CartView import CartView
from AddOrderView import AddOrderView
from Manager import Manager
import os

class ShopView:
    def __init__(self, window, org, supplier, supplier_view):
        self.window = window
        self.supplier = supplier
        self.org = org
        self.window.wm_iconphoto(False, Utils.Icon(os.path.dirname(__file__) + "../image/cart_icon.png"))
        self.cart = Cart(supplier, org.logged_in_user)
        self.products_for_purchase = self.supplier.products.get_available_products()
        self.supplier_view = supplier_view
        self.add_button = None
        self.products_tree = None
        self.products_tree_frame = None
        self.selected_items = None

        self.header()
        self.body()
        self.footer()
    
    def header(self):
        Utils.Image(self.window, os.path.dirname(__file__) + "../image/cart.png").pack()

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
        self.add_button = Utils.Button(footerFrame, "Add", lambda:self.open_products_windows())
        self.add_button.config(state=DISABLED)
        self.add_button.pack(expand=True, fill=X, side=LEFT)
        Utils.Button(footerFrame, "View", lambda:self.view_cart()).pack(expand=True, fill=X, side=LEFT)
        Utils.Button(footerFrame, "Cancel", lambda:self.window.destroy()).pack(expand=True, fill=X, side=LEFT)
        Utils.Button(footerFrame, "Checkout", lambda:self.checkout()).pack(expand=True, fill=X, side=LEFT)
        footerFrame.pack(expand=True, fill=X)

    def setup_treeview(self):
        self.products_tree = ttk.Treeview(self.products_tree_frame, columns=('Name', 'Price', 'Stock'), show='headings', selectmode='extended')

        self.products_tree.bind("<<TreeviewSelect>>", self.add_button_enabler)

        for col in self.products_tree['columns']:
            self.products_tree.column(col, anchor=CENTER, stretch=NO)

        self.products_tree.heading('Name', text='Name')
        self.products_tree.heading('Price', text='Price')
        self.products_tree.heading('Stock', text='Stock')

        for prod in self.products_for_purchase:
            self.products_tree.insert('', END, values=[prod.name, f'{prod.price:.2f}', prod.stock])
        
        self.products_tree.pack(expand=True, fill=X)

    def open_products_windows(self):
        for item in self.get_selection():
            for prod in self.products_for_purchase:
                if item == prod.name:
                    AddOrderView(Utils.Toplevel("Add " + prod.name), self.cart, prod)
                    self.products_for_purchase.remove(prod)
                    break
        self.add_button.config(state=DISABLED)
        self.update_treeview()

    def update_treeview(self):
        self.products_tree.pack_forget()
        self.setup_treeview()
    
    def view_cart(self):
        CartView(Utils.Toplevel("View Cart"), self.cart, self)

    def checkout(self):
        prof = self.supplier.profit
        self.supplier.process_cart(self.cart)
        if isinstance(self.org.logged_in_user, Manager):
            self.supplier.profit = prof
        self.supplier_view.update_header_label()
        self.supplier_view.update_tree_view()
        self.org.logged_in_user.add_purchase(self.cart)
        self.window.destroy()
    
    def get_selection(self):
        selected_products_names = []
        for id in self.products_tree.selection():
            selected_products_names.append(self.products_tree.item(id, option='values')[0])
        return selected_products_names

    def add_button_enabler(self, *args):
        if(len(self.get_selection()) > 0):
            self.add_button.config(state=NORMAL)
        else:
            self.add_button.config(state=DISABLED)
