import os
import time
import pymysql
from libpos import libDoli


def isp_menu():
    os.system('cls')
    global choice
    choice = '0'
    while choice == '0':
        print("ISPConfig3 Menu: Wähle von 1 - 5")
        print("---------------------------")
        print("auswahl1")
        print("auswahl2")
        print("auswahl3")
        print("auswahl4")
        print("5) Hauptmenu")
        choice = input("Bitte Auswählen: ")

    # Auswahl Menu 5 (Benden)
    if choice == "5":
        libDoli.menu5()

    # Auswahl Menu 4
    elif choice == "4":
        pass

    # Auswahl Menu 3
    elif choice == "3":
        pass

    # Auswahl Menu 2
    elif choice == "2":
        pass

    # Auswahl Menu1
    elif choice == "1":
        pass

    # Fehler Abfangen bei der Eingabe
    else:
        print("Nur Zahlen sonst klappt dat nicht.")
        time.sleep(2)
        isp_menu()