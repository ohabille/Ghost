# coding: utf-8
""" Gère les fichier *.json dans le répertoire ./confsLibs/ """
import json as js

class JsonMod:
    def __init__(self):
        self.extens = ".json"
        self.conf_dir = "confsLibs/"

    def get_confs(self, file_name):
        """ retourne le json décodé """
        with open(self.conf_dir + file_name + self.extens) as file:
            return js.loads(file.read())
