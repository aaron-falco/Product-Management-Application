from View import View
from tkinter import *
from tkinter import ttk
from Utils import Utils
from NoSuchUserException import NoSuchUserException
from LoginErrorWindow import LoginErrorWindow
from Manager import Manager
from CustomerDashboardView import CustomerDashboardView
from ManagerDashboardView import ManagerDashboardView
import os


class LoginView(View):
    def __init__(self, root, org):
        super().__init__(root, org)

        self.login_window()
        self.root.resizable(False, False)
        self.root.protocol("WM_DELETE_WINDOW", Utils.disable)
        
        ttk.Style().configure('Treeview.Heading', foreground=Utils.python_blue) 


    def login_window(self):
        self.root.title("Login")
        
        self.root.wm_iconphoto(False, Utils.Icon(os.path.dirname(__file__) + "../image/login_icon.png"))

        self.login_header()
        self.login_body()
        self.login_footer()
    
    def login_header(self):
        Utils.Frame(self.root).pack()
        headerFrame = Utils.Frame(self.root)
        Utils.Label(headerFrame, text_="Login").pack()
        Utils.Separator(headerFrame).pack(fill=X, pady=(5, 10))
        headerFrame.pack(expand=True, fill=X)

    def login_body(self):
        #Body
        bodyFrameUpper = Utils.Frame(self.root)
        self.my_username_str = StringVar(self.root)
        usernameLbl = Utils.Label(bodyFrameUpper, text_="Username:")
        usernameLbl.pack(side=LEFT)
        self.usernameEnt = Entry(bodyFrameUpper, textvariable=self.my_username_str)
        self.usernameEnt.pack(side=LEFT)
        bodyFrameUpper.pack(expand=True, pady=(5,5))

        bodyFrameLower = Utils.Frame(self.root)
        self.my_password_str = StringVar(self.root)
        passwordLbl = Utils.Label(bodyFrameLower, text_="Password:")
        passwordLbl.pack(side=LEFT)
        self.passwordEnt = Entry(bodyFrameLower, textvariable=self.my_password_str, show='*')
        self.passwordEnt.pack(side=LEFT)
        bodyFrameLower.pack(expand=True, pady=(5,5))
        
        #Tracing/Event Handling
        self.my_password_str.trace_add('write', self.login_button_enabler)
        self.my_username_str.trace_add('write', self.login_button_enabler)
    
    def login_footer(self):
        #Footer
        footerFrame = Utils.Frame(self.root)
        self.loginBtn = Utils.Button(footerFrame, text_="Login", callback=lambda:self.try_login(str(self.my_password_str.get()), str(self.my_password_str.get())))
        self.loginBtn.config(state='disabled')
        self.loginBtn.pack(expand=True, fill=X, side=LEFT)
        quitBtn = Utils.Button(footerFrame, text_="Exit", callback=lambda:self.root.destroy())
        quitBtn.pack(expand=True, fill=X, side=LEFT)
        footerFrame.pack(fill=X, expand=True, pady=(10, 0))

    def try_login(self, username, password):
        try:
            self.org.logged_in_user = self.org.users.validate_user(username, password)
            if isinstance(self.org.logged_in_user, Manager):
                ManagerDashboardView(self.root, self.org)
            else:
                CustomerDashboardView(self.root, self.org)
        except NoSuchUserException as err:
            LoginErrorWindow(err)

    def login_button_enabler(self, *args):
        if(len(self.my_username_str.get()) > 0 and len(self.my_password_str.get()) > 0):
            self.loginBtn.config(state='normal')
        else:
            self.loginBtn.config(state='disabled')