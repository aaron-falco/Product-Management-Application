from View import View
from Utils import Utils
import os
from SupplierListView import SupplierListView
from OrderHistoryView import OrderHistoryView

class CustomerDashboardView(View):
    def __init__(self, root, org):
        super().__init__(root, org)
        self.customer_dashboard_window()

    def customer_dashboard_window(self):
        #Setup
        self.root.title("Customer Dashboard")
        self.root.wm_iconphoto(False, Utils.Icon(os.path.dirname(__file__) + "../image/user_icon.png"))

        self.header()
        self.body()
        self.footer()


    def header(self):
        Utils.Image(self.root, os.path.dirname(__file__) + "../image/user.png").pack()


    def body(self):
        Utils.Separator(self.root).pack(expand=True, fill='x', pady=(10, 15))
        bodyFrame = Utils.Frame(self.root)
        users_first_name = str(self.org.logged_in_user).split(' ')[0]
        Utils.Label(self.root, "Welcome to the Customer Dashboard " + users_first_name).pack(fill='x', expand=True)
        bodyFrame.pack(expand=True, fill='x')
        Utils.Separator(self.root).pack(expand=True, fill='x', pady=(15, 10))

    def footer(self):
        footerFrame = Utils.Frame(self.root)
        #Shop Button
        Utils.Button(footerFrame, "Shop", lambda:self.open_shop_window()).pack(fill='x', expand=True, side='left')
        #Order History Button
        Utils.Button(footerFrame, "Order History", lambda:self.open_order_history()).pack(fill='x', expand=True, side='left')
        #Close Button
        Utils.Button(footerFrame, "Close", lambda:self.root.destroy()).pack(fill='x', expand=True, side='left')
        footerFrame.pack(fill='x', expand=True, pady=(10,0))

    def open_shop_window(self):
        SupplierListView(Utils.Toplevel("Supplier List"), self.org)


    def open_order_history(self):
        OrderHistoryView(Utils.Toplevel("Order History"), self.org)
        