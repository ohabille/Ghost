# coding: utf-8
""" Classe de gestion du canvas de l'appli """

from tkinter import Canvas

class GuiCanv:
    def __init__(self, gui):
        self.w = 400
        self.h = 50
        self.x = int(self.w /2)
        self.y = int(self.h /2)

        self.canv = Canvas(gui, height = self.h, width = self.w,
            background = "black")
        self.canv.pack()

    def set_str(self, str = ""):
        """ construction d'une chaîne de charactères """
        self.reset_canvas()

        self.canv.create_text(self.x, self.y, text = str,
            font = "Arial 12", fill = "green", width = self.w)

    def reset_canvas(self):
        """ création d'un rectangle pour effacer le contenu du canvas """
        rect = self.canv.create_rectangle(
            0, 0, self.w, self.h, fill = "black")
