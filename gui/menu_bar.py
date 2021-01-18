# coding: utf-8
""" Classe de gestion de la barre de menu """
from tkinter import Menu
from json_mod import JsonMod

class MBar:
    def __init__(self, win):
        self.menu_bar = Menu(win)
        self.js_conf = JsonMod()
        self.set_menu_bar(win)

        win.config(menu = self.menu_bar)

    def set_menu_bar(self, win):
        """ construit la barre de menu à partir du fichier menuBar.json
        ./confsLibs/menuBar.json """
        confs = self.js_conf.get_confs("menuBar")

        for conf in confs:
            self.set_label(win, conf, confs)

    def set_label(self, win, lab, confs):
        """ construit un label du menu et lui assigne une commande """
        self.menu_bar.add_command(
            label = lab,
            command = eval("win." + confs[lab])
        )
