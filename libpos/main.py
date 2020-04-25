import os
import time
from libpos import DoliDBmenu
from libpos import mysql
from libpos import libDoli
from libpos import uebungsDBmenu


# Menu 5 Menupunkte
def menu5():
    os.system('cls')
    libDoli.logo()
    global choice
    choice = '0'
    while choice == '0':
        print("Hauptmenu: Wähle von 1 - 5")
        print("---------------------------")
        print("1) Funktionstest abfrage")
        print("2) UebungsDB")
        print("3) Dolibarr")
        print("4) ISPConfig3")
        print("5) Benden")
        choice = input("Bitte Auswählen: ")

    # Auswahl Menu 5 (Benden)
    if choice == "5":
        mysql.abmeldungSQL()
        time.sleep(3)
        os.system('cls')
        exit()
    # Auswahl Menu 4
    elif choice == "4":
        pass

    # Auswahl Menu 3
    elif choice == "3":
        mysql.doliDB()
        DoliDBmenu.dol1_menu()

    # Auswahl Menu 2
    elif choice == "2":
        mysql.uebungsDB()
        uebungsDBmenu.ue_menu()


    # Auswahl Menu 1
    elif choice == "1":
        mysql.uebungsDB()
        mysql.test()
        time.sleep(2)
        os.system('cls')
        print("-------------------")
        print("|Test erfolgreich |")
        print("-------------------")
        input("Press Enter to continue...")
        menu5()

    # Fehler Abfangen bei der Eingabe
    else:
        print("Nur Zahlen sonst klappt dat nicht.")
        time.sleep(2)
        menu5()
