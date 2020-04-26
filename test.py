import getpass

from libpos import libDoli
from libpos import main

libDoli.logo()
usr = input("Benutzername: ")
pwd = getpass.getpass("Bitte Passwort eingeben:")

if usr == 'admin' and pwd == 'test':
    main.menu5()
else:
    print("Murat sagt:Du kommst hier nicht rein!")
