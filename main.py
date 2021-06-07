# coding: utf-8
""" Gère une conversation entre l'utilisateur et l'appli """

# Import du script de gestion des paths des libraries
# à commenter pour la compilation d'un executable
# import libs_paths


""" write file """
def writeFile(file, content):
    file = open(file, 'a')
    file.write(content)
    file.close()

""" édition de la conf """
def setConfGhost(file, conf_name ,msg):
    q = "\""
    conf_name = q+conf_name+q
    msg = q+msg+q

    start = "\t"
    if isFileExist('test.txt'):
        start = ",\n" + start

    content = start + conf_name + " : " + msg
    writeFile(file, content)

"""  """
def setUserConf(file, confs):
    for conf_name, msg in confs.items():
        ask = input('set ' + msg + ' : ')
        setConfGhost(file, conf_name, ask)

"""  """
def getConfs():
    return {
    'user_name' : 'your name',
    'ghost_name' : 'ghost name'
    }

""" test de fichier """
def isFileExist(file):
    from pathlib import Path
    file_obj = Path(file)
    exist = file_obj.is_file()
    del Path

    return exist

""" set conf """
def userConf(file):
    if not isFileExist(file):
        setUserConf(file, getConfs())

""" read Confs """
def readConfs(file):
    import json as js

    with open(file) as conf:
        confs = js.loads('{'+conf.read()+'}')

    for k, v in confs.items():
        print(k+' : '+v)

    del js

""" """
file = 'test.txt'

userConf(file)

readConfs(file)
