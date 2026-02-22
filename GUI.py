from engine import SentinelBusiness as eg

from main import GUIMenu as gui

import tkinter as tk
from tkinter import ttk

class interfaz(tk.Frame):
    """Docstring."""

    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        """Aqui colocariamos los widgets."""
        self.parent.title("MicroSaas-Sentinel")

if __name__ == "__main__":
    ROOT = tk.Tk()
    ROOT.geometry("800x600")
    APP = interfaz(parent=ROOT)
    APP.mainloop()
    ROOT.destroy()