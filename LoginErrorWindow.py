import tkinter as tk
from Utils import Utils
import os

class LoginErrorWindow:

    def __init__(self, error):
        #Open Error Window
        self.errorWindow = Utils.Toplevel("Error")

        #Set Icon
        self.errorWindow.wm_iconphoto(False, Utils.Icon(os.path.dirname(__file__) + "../image/error_icon.png"))

        #Add Widgets
        errImg = Utils.Image(self.errorWindow, os.path.dirname(__file__) + "../image/error.png")
        errImg.pack()

        Utils.Separator(self.errorWindow).pack(fill='x', pady=(10,10))
        errorLbl = Utils.Label(self.errorWindow, text_="Error")
        errorLbl.pack()
        Utils.Separator(self.errorWindow).pack(fill='x', pady=(10,10))
        errorTypeLbl = Utils.Label(self.errorWindow, text_=type(error).__name__)
        errorTypeLbl.config(foreground="#ff0000")
        errorTypeLbl.pack(fill='x', pady=(10,5))
        errorMsgLbl = Utils.Label(self.errorWindow, text_="Invalid Credentials")
        errorMsgLbl.pack(fill='x', pady=(5,10))

        closeBtn = Utils.Button(self.errorWindow, "Close", lambda:self.close_error_window())
        closeBtn.pack(expand=True, fill='x')
    
    
    def close_error_window(self):
        self.errorWindow.destroy()