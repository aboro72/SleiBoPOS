import os
import time
from libpos import main
from libpos import mysql
from libpos import libDoli


def ue_menu():
    os.system('cls')
    libDoli.logo()
    global choice
    choice = '0'
    while choice == '0':
        print("uebungsDB Menu: Wähle von 1 -?")
        print("------------------------------")
        print("1) Abfrage Name nach Stunden pro Monat")
        print("auswahl2")
        print("auswahl3")
        print("4) Freies SQL")
        print("5) Hauptmenu")
        choice = input("Bitte Auswählen: ")

    # Auswahl Menu 5 (Benden)
    if choice == "5":
        main.menu5()
    # Auswahl Menu 4
    elif choice == "4":
        libDoli.cls()
        libDoli.logo()
        mysql.SQLeingabe()
        time.sleep(2)
        input("Press Enter to continue...")
        libDoli.cls()
        ue_menu()


    # Auswahl Menu 3
    elif choice == "3":
        pass

    # Auswahl Menu 2
    elif choice == "2":
        pass

    # Auswahl Menu1
    elif choice == "1":
        libDoli.cls()
        libDoli.logo()
        mysql.ue_abfrageName()
        time.sleep(2)
        input("Press Enter to continue...")
        libDoli.cls()
        ue_menu()

    # Fehler Abfangen bei der Eingabe
    else:
        print("Nur Zahlen sonst klappt dat nicht.")
        time.sleep(2)
        ue_menu()
