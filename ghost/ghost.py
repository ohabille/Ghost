# coding: utf-8
""" analise un talk et retourne une réponse """

# Library de gestion de l'entrée user (le talk)
from ghost_talk import GTalk as GT
# Library de gestion de la sortie ghost
from ghost_response import GResponse as GR
# Library de gestion de l'aide
from ghost_help import GHelp as GH
# Library de simulation de frappe clavier
from ghost_write import GhostWrite as GW

class Ghost:
    def __init__(self, gui):
        self.gui = gui

        self.talk = GT()
        self.ghost = GR()

    def del_last_char(self, event):
        """ Efface la dernière lettre. """
        self.talk.del_last_char()
        self.gui.set_text(self.talk.get_talk())

    def set_talk(self, event):
        """ Affiche la saisie utilisateur """
        self.talk.set_talk(event.char)
        self.gui.set_text(self.talk.get_talk())

    def set_command(self, event = ""):
        """ Initialise une commande à effectuer """
        eval(self.ghost.find_command(self.talk.get_talk()))

    def send_response(self):
        """ Affiche la réponse du ghost """
        GW(self.gui, self.ghost.get_ghost(self.talk.get_talk()))
        self.talk.set_empty_talk()

    def reset_text(self, event = "x"):
        """ Construit une vue vide """
        self.talk.set_empty_talk()
        self.gui.reset_text()

    def get_help(self):
        """ Affiche l'aide """
        self.reset_text()
        help = GH()
        self.gui.set_text(help.get_tip())
