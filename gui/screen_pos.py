# coding: utf-8
""" Gère la position du GUI dans l'écran """

class ScreenPos:
    def __init__(self, gui, gui_width):
        # Taille de l'écran divisé par 2
        w = int(gui.winfo_screenwidth() / 2)
        # moitié de l'écran moins la moitié de la taille du GUI
        x = str(w - int(gui_width / 2))

        gui.geometry("+" + x + "+0")
