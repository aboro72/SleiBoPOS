import pymysql


# SQL Allgemein
def anmeldungSQL(ip, db_nutzer, db_paswort):
    #    ip = input("Bitte Server IP eingeben: ")
    #    db_nutzer = input("Datenbanknutzer eingeben: ")
    #    db_paswort = input("Passwort eingeben: ")
    global db
    db = pymysql.connect(ip, db_nutzer, db_paswort)


def abmeldungSQL():
    db.close()
    print("Verbindung wurde zu Datenbank beendet!")


def doliDB():
    db.select_db(db="dolibarr")


def uebungsDB():
    db.select_db(db="uebungsdatenbank")


def ispconfigDB():
    db.select_db(db="dbispconfig")


# uebungsdatenbank
# def ueDB_verbindung():
#    global u_mysql
#    u_mysql = pymysql.connect("192.168.0.164", "aboro72", "quaSeu2i", "uebungsdatenbank")


def test():
    cursor = db.cursor()
    sql = "SELECT * FROM mitarbeiter"
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        MitarbeiterID = row[0]
        name = row[1]
        vorname = row[2]
        geburtsdatum = row[3]
        print("MitarbeiterID: %d | Name: %s | Vorname: %s | Geburtsdatum: %s " % (
            MitarbeiterID, name, vorname, geburtsdatum))


def ue_abfrageTest():
    pass


def ue_abfrageName():
    cursor = db.cursor()
    name = input("Nachname eingeben: ")
    sql = "SELECT * FROM mitarbeiter Where name='{0}'".format(name)
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        MitarbeiterID = row[0]
        name = row[1]
        vorname = row[2]
        gebdatum = row[3]
        monatsstunden = row[23]
        ueberstunden = row[22]
        print("MitarbeiterID: %d | Name: %s | Vorname: %s | Geburtsdatum: %s | Monatsstunden: %s | Ueberstunden: %s" % (
            MitarbeiterID, name, vorname, gebdatum, monatsstunden, ueberstunden))


def ue_abfrageAdresse():
    pass


def ue_abfrageBonus():
    pass


def ue_mitarbeiter_alle():
    cursor = db.cursor()
    sql = "SELECT * FROM mitarbeiter"
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        MitarbeiterID = row[0]
        name = row[1]
        vorname = row[2]
        geburtsdatum = row[3]
        print("MitarbeiterID: %d | Name: %s | Vorname: %s | Geburtsdatum: %s " % (
            MitarbeiterID, name, vorname, geburtsdatum))

def SQLeingabe():
    cursor = db.cursor()
    sql_eingabe = input("SQL eingeben: ")
    sql = "{0}".format(sql_eingabe)
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results).readline()
