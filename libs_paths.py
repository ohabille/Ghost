# coding: utf-8
""" Gestion des paths des libraries homemade """

import os
import sys
from json_mod import JsonMod

js = JsonMod()
dirs = js.get_confs("libsDirs")

for dir in dirs:
    sys.path.insert(0, os.getcwd() + "\\" + dirs[dir]["path"])

del os
del sys
del JsonMod
