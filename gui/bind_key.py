# coding: utf-8
""" Gère l'action des touches clavier"""
from json_mod import JsonMod

class BindK:
    def __init__(self, gui, app):
        self.app = app
        self.gui = gui
        self.js_conf = JsonMod()
        self.listen_key("keysBinding")

    def listen_key(self, file_conf):
        """ initialise les commandes à effectuer
        sur les évènements clavier à partir du fichier keysBinding.json """
        confs = self.js_conf.get_confs(file_conf)

        for cf in confs:
            self.set_bind(cf, confs)

    def set_bind(self, key, confs):
        """ initialise une commande sur un évènement clavier """
        self.gui.bind(
            "<" + key + ">",
            eval("self." + confs[key])
        )
