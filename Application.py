from tkinter import *
from LoginView import LoginView
from Organisation import Organisation

class Application:
    def __init__(self, root):
        #super().__init__()

        org = Organisation()
            
        LoginView(root, org)


if __name__ == "__main__":
    root = Tk()
    Application(root)
    root.mainloop()

