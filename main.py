# coding: utf-8
""" Gère une conversation entre l'utilisateur et l'appli """

# Import du script de gestion des paths des libraries
# à commenter pour la compilation d'un executable
import libs_paths

# Library de gestion du ghost
from ghost import Ghost
# Library de gestion du GUI
from gui import Gui
# Library de gestion des events clavier
from bind_key import BindK

# Initialisation du GUI
gui = Gui("Ghost")
# Initialisation du ghost
ghost = Ghost(gui)

# Initialisation des event clavier
BindK(gui, ghost)

# Initialisation de hello du ghost

# Mise en boucle du GUI
gui.mainloop()
