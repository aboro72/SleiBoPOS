import getpass
import os
import time

import pymysql

import text
from libpos import libDoli
from libpos import main
from libpos import mysql
from libpos import uebungsDBmenu


def launch():
    # Logo
    libDoli.cls()
    libDoli.logo()
    usr = input("Benutzername: ")
    pwd = getpass.getpass("Bitte Passwort eingeben:")

    if usr == 'admin' and pwd == 'test':
        # MySQL Server Anmeldung
        try:
            libDoli.cls()
            mysql.anmeldungSQL(ip="192.168.0.164", db_nutzer="admin", db_paswort="quaSeu2i")
        except pymysql.err.OperationalError:
            libDoli.logo()
            print("!!!Datenbank nicht Verbunden!!!!")
            print("Fehlermeldung: IP Adresse oder Nutzerdaten falsch")
            print("")
            print("")
            text.sql_error()
            input("Bitte enter drücken: ")
            exit()

        # Todo liste
        text.todo_liste()
        print("")
        input("Press Enter to continue...")

        # Hauptmenu
        main.menu5()
    elif usr == 'test' and pwd == 'test':
        # MySQL Server Anmeldung
        try:
            libDoli.cls()
            mysql.anmeldungSQL(ip="192.168.0.164", db_nutzer="admin", db_paswort="quaSeu2i")
        except pymysql.err.OperationalError:
            libDoli.logo()
            print("!!!Datenbank nicht Verbunden!!!!")
            print("Fehlermeldung: IP Adresse oder Nutzerdaten falsch")
            print("")
            print("")
            text.sql_error()
            input("Bitte enter drücken: ")
            exit()

        # Todo liste
        text.todo_liste()
        print("")
        input("Press Enter to continue...")
        libDoli.cls()
        uebungsDBmenu.ue_menu()

    else:
        libDoli.cls()
        libDoli.logo()
        print("")
        print("Murat sagt: Du kommst hier nicht rein!")


def todo_start():
    help1 = open("\text\todo.txt", "r").readline()
    print(help1)
    input("Bitte Enter druecken....")


def test():
    print("test")


def cls():
    os.system("cls")
#    os.system("clear")


def logo():
    print(" ____  __    ____  __  ____   __     __  ____ ")
    print("/ ___)(  )  (  __)(  )(  _ \ /  \   (  )(_  _)")
    print("\___ \/ (_/\ ) _)  )(  ) _ ((  O )   )(   )(  ")
    print("(____/\____/(____)(__)(____/ \__/   (__) (__) ")
    print("                                       (c)2020")
    print(" ")
    print(" ")


def testSQL():
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print("Database version : %s " % data)
    time.sleep(3)

# MySQL Abfrage uebungsdatenbank


# Test der SQL DB Verbindung
