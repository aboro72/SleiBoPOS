import os
import time
import main
import libDoli

def dol1_menu():
    os.system('cls')
    global choice
    choice = '0'
    while choice == '0':
        print("Dolibarr Menu: Wähle von 1 - 5")
        print("---------------------------")
        print("auswahl1")
        print("auswahl2")
        print("auswahl3")
        print("auswahl4")
        print("5) Hauptmenu")
        choice = input("Bitte Auswählen: ")

# Auswahl Menu 5 (Benden)
    if choice == "5":
        main.menu5()
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
        dol1_menu()