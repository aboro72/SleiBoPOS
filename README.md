<h1 xmlns="http://www.w3.org/1999/html">SleiBoPOS </h1>

<p>Falls jemand interesse dran hat da mit zu Fummeln, in libpos befinden sich die Funktionen.
in der Funktionssamlung mysql.py ist zum testen folgende Funktion wichtig:</p>
<p><i>anmeldungSQL()</i></p>
<p>Diese wird benötigt um sich an einen MariDB oder MySQL Server 
anzumelden. Dazu werden die Parameter ip,db_nutzer,db_paswort defeniert.</p>
<p><b>Beispiel:</b></p>
<p><i>mysql.anmeldungSQL(ip="127.0.0.1", db_nutzer="root",db_passwort="geheim")</i></p>
<p>Die Anmeldung an dem Server wird in der Variable <style="color:red">db</style> abgelegt.</p>
<p>Um die Verbindung zum Datenbank Server zu schließen wird folgendes eingegeben:</p>
<p><i>abmeldungSQL()</i></p>
<p><b>Beispiel Code:</b></p>
<p><code>from libpos import mysql</code><br>
<code>import time</code><br>
<br>
<code>mysql.anmeldungSQL(ip="127.0.0.1", db_nutzer="root",db_passwort="geheim")</code><br>
<code>print("Am Server Angemeldet")</code><br>
<code>mysql.test()</code><br>
<code>time.sleep(5)</code><br>
<code>mysql.abmeldungSQL()</code><br>
<code>print("Am Server abgemeldet")</code><br>
<code>mysql.test()</code></p>
<p>Jetzt solten am ende Fehlermeldungen kommen. Das ist so weil der Datenbankserver nicht mehr verbunden ist.</p>
<p> Auf dauer sollen die Parameter aber in die config.txt geschrieben und von da auch gelesen werden. </p>
<p> Des weiteren sollte in Python noch pyMysql installiert werden. Darauf bezieht sich auch die mysql.py.</p>
 
      











