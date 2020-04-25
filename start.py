import main
import mysql
import text
import libDoli
import pymysql

# Logo
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
