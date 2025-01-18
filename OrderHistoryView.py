from tkinter import *
from Utils import Utils
from tkinter import ttk
import os

class OrderHistoryView:
    def __init__(self, root, org):
        self.root = root
        self.org = org
        self.root.wm_iconphoto(False, Utils.Icon(os.path.dirname(__file__) + "../image/user_icon.png"))
        self.order_history_tree = None
        self.bodyFrame = None
        
        ttk.Style().configure('Treeview', rowheight=40)
        ttk.Style().configure('Treeview.Heading', background='lightgrey', foreground=Utils.python_blue)

        self.header()
        self.body()
        self.footer()
    
    def header(self):
        Utils.Image(self.root, os.path.dirname(__file__) + "../image/user.png").pack()
    
    def body(self):
        self.bodyFrame = Utils.Frame(self.root)
        Utils.Separator(self.bodyFrame).pack(expand=True, fill='x', pady=(10, 15))
        Utils.Label(self.bodyFrame, "Order History").pack()
        Utils.Separator(self.bodyFrame).pack(expand=True, fill='x', pady=(15, 10))
        self.bodyFrame.pack(fill=X)
        
        self.setup_tree_view()



    def footer(self):
        footerFrame = Utils.Frame(self.root)
        Utils.Button(footerFrame, "Close", lambda:self.root.destroy()).pack(fill=X, expand=True, side=LEFT)
        footerFrame.pack(expand=True, fill=X, pady=(10, 0))
    
    def setup_tree_view(self):
        self.order_history_tree = ttk.Treeview(self.bodyFrame, selectmode='none', show='tree')
        
        if len(self.org.logged_in_user.purchases) > 0:
            ttk.Style().configure('Treeview', rowheight=100)
            self.order_history_tree.config(height=len(self.org.logged_in_user.purchases))
            for order in self.org.logged_in_user.purchases:
                self.order_history_tree.insert('' , END, text=str(order))
        else:
            
            for col in self.order_history_tree['columns']:
                self.order_history_tree.column(col, anchor=CENTER, stretch=NO)

            self.order_history_tree.config(height=1)
            ttk.Style().configure('Treeview', rowheight=300, font='Arial 11 bold', foreground=Utils.python_blue)
            self.order_history_tree.insert('', END, text="Empty")
        
        self.order_history_tree.pack(expand=True, fill=X)


