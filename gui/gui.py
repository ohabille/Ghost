# coding: utf-8
""" Gère le GUI de l'appli """
import tkinter as tk
from gui_canvas import GuiCanv
from tkinter import ttk
from screen_pos import ScreenPos

class Gui(tk.Tk):
    def __init__(self, title):
        tk.Tk.__init__(self)
        self.title(title)
        self.canv = GuiCanv(self)

        ScreenPos(self, self.canv.w)

        # Retire la barre de titre
        # self.overrideredirect(1)

    def set_text(self, text):
        """ Dessine le texte """
        self.canv.set_str(text)

    def reset_text(self, event = "x"):
        """ Construit une vue vide """
        self.canv.reset_canvas()

    def quit_app(self, event):
        """ Ferme le programme """
        self.quit()
