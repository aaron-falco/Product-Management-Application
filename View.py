import tkinter as tk

class View:
    def __init__(self, root, org):
        self.root = root

        self.org = org

        self.clear_window()

    def set_message_text(self, mf, text):
        mf.configure(text=text)

    def set_text(self, tf, text):
        tf.delete(0, tk.END)
        tf.insert(0, text)
    
    def close_window(self):
        self.root.destroy()

    def clear_window(self):
        for widget in self.root.pack_slaves():
            widget.destroy()