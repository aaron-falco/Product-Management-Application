from tkinter import *
from tkinter import ttk
from Utils import Utils
from SupplierView import SupplierView
import os
from Manager import Manager
from ManageSupplierView import ManageSupplierView

class SupplierListView():
    def __init__(self, window, org):        
        self.window = window
        self.org = org
        self.window.wm_iconphoto(False, Utils.Icon(os.path.dirname(__file__) + "../image/supplier_icon.png"))
        self.supplier_tree = None
        self.supplier_selected = None
        
        ttk.Style().configure('Treeview', font='Arial 11', foreground='black', rowheight=20)

        self.header()

        self.body()
        
        self.footer()
    
    def header(self):
        Utils.Image(self.window, os.path.dirname(__file__) + "../image/supplier.png").pack()

    def body(self):
        Utils.Separator(self.window).pack(expand=True, fill=X, pady=(10, 15))
        bodyFrame = Utils.Frame(self.window)
        Utils.Label(self.window, "Select a Supplier").pack(fill=X)
        Utils.Separator(self.window).pack(expand=True, fill=X, pady=(15, 15))

        #Add Tree View of Suppliers
        self.supplier_tree = ttk.Treeview(bodyFrame, selectmode="browse", show='tree')

        suppliers = None
        if isinstance(self.org.logged_in_user, Manager):
            suppliers = self.org.logged_in_user.suppliers.suppliers
        else:
            suppliers = self.org.suppliers.suppliers

        for sup in suppliers:
            self.supplier_tree.insert('' , END, text=str(sup))
        self.supplier_tree.pack(expand=True, fill=X)
        
        self.supplier_tree.bind("<<TreeviewSelect>>", self.shop_button_enabler)

        bodyFrame.pack(expand=True, fill=X)

    def footer(self):
        footerFrame = Utils.Frame(self.window)
        self.shop_button = Utils.Button(footerFrame, "Shop", lambda:self.open_shop_window())
        self.shop_button.config(state=DISABLED)
        self.shop_button.pack(expand=True, fill=X, side='left')
        Utils.Button(footerFrame, "Close", lambda:self.window.destroy()).pack(expand=True, fill=X, side='left')
        footerFrame.pack(expand=True, fill=X, pady=(10,0))

    
    def open_shop_window(self):
        self.window.destroy()
        if isinstance(self.org.logged_in_user, Manager):
            ManageSupplierView(Utils.Toplevel("Supplier: " + self.supplier_selected.region), self.org, self.supplier_selected)
        else:
            SupplierView(Utils.Toplevel("Supplier: " + self.supplier_selected.region), self.org, self.supplier_selected)
    
    def get_selection(self):
        return self.supplier_tree.item(self.supplier_tree.selection()[0], option='text')
    
    def get_supplier(self):
        supplier_str = self.get_selection()
        for sup in self.org.suppliers.suppliers:
            if(str(sup) == supplier_str):
                self.supplier_selected = sup

    def shop_button_enabler(self, *args):
        if(self.get_selection() == None):
            self.shop_button.config(state=DISABLED)
        else:
            self.get_supplier()
            self.shop_button.config(state=NORMAL)

        