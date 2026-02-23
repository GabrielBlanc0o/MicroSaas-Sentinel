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
        
        titulo_principal = tk.Label(text="Business Health Status", font=("Helvetica", 20, "bold"), bg= "#1e1e2e",fg="#ffffff")
        titulo_principal.pack(pady=40,  anchor="w",padx=150)
        
        self.barra_menu_literal = tk.Frame (self.parent,bg="#2b2b3b", width=300)
        self.barra_menu_literal.pack(side="left", fill="y")
        self.barra_menu_literal.pack_propagate(False)
        
        #texto_prueba = tk.Label(self.parent, text = "Hola")
        #texto_prueba.pack()

if __name__ == "__main__":
    ROOT = tk.Tk()
    ROOT.geometry("800x600")
    ROOT.configure(bg="#1e1e2e")
    APP = interfaz(parent=ROOT)
    APP.mainloop()
    ROOT.destroy()