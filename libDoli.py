import pymysql
import os
import time
import sys
import dispconfig
import mysql


def todo_start():
    help1 = open("todo.txt", "r").readline()
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


# MySQL Hauptverzeichnis

# MySQL Anmeldung





def testSQL():
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print("Database version : %s " % data)
    time.sleep(3)

# MySQL Abfrage uebungsdatenbank


# Test der SQL DB Verbindung
