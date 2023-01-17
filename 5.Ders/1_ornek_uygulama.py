"""

1- Veri isimli bir klasor olusturun

2- zip dosyasini veri kloserine cikartin

3- zip dosyasi icindeki csv dosyalarinin tum icerigini
tek bir csv dosyasinda birlestirin
volume olmasin

4- Bu kayitlarin tamamini sqlite veritabanina bir tablo
olusturarak yukleyin

5- kullanicinin belirledigi paritenin
   kullanicinin belirledigi araliginin
   kullanicinin belirledigi degerin
   grafigini cizdirin (veriler sqlite tan cekilecek)

"""


import os
import zipfile
import pandas as pd
import sqlite3

bag = sqlite3.connect("kripto.vt")
cursor = bag.cursor()

if not os.path.exists("veri"):
    os.mkdir('veri')
    arsiv = zipfile.ZipFile('pariteler_cikti_1hour_2022_2022.zip')
    arsiv.extractall("veri/")

    tum_dosyalar = os.listdir("veri")
    pandas_csv_listesi = []
    for csv_dosya in tum_dosyalar:
        veri = pd.read_csv("veri/" + csv_dosya)
        del veri["volume"]
        veri["parite"] = csv_dosya.split("_")[0]
        pandas_csv_listesi.append(veri)

    birlesmis_csv_ler = pd.concat(pandas_csv_listesi)
    birlesmis_csv_ler.to_csv('hepsi.csv', index=False)
    cursor.execute("CREATE TABLE IF NOT EXISTS parite("
                   +"id INTEGER PRIMARY KEY AUTOINCREMENT,"
                   +"parite TEXT, otime TEXT, open FLOAT, "
                   +"high FLOAT, low FLOAT, close FLOAT);")

    kayitlar = pd.read_csv("hepsi.csv")
    for row in kayitlar.itertuples():
        cursor.execute("INSERT INTO "
                       + "parite(parite,otime,open,high,low,close)"
                       + " VALUES("
                       + "'"+row.parite+"',"
                       + "'"+row.otime+"',"
                       + ""+str(row.open)+","
                       + ""+str(row.high)+","
                       + ""+str(row.low)+","
                       + ""+str(row.close)+")")
    bag.commit()


parite = input("Parite Giriniz :")
bas_tarih = input("Başlangıç Tarihi :")
bit_tarih = input("Bitiş Tarihi :")

sorgu = "SELECT * FROM parite WHERE " \
        "(otime BETWEEN '"+bas_tarih+"' " \
        "AND '"+bit_tarih+"') " \
        "AND parite='"+parite+"'"
cursor.execute(sorgu)
sonuc = cursor.fetchall()
print(sonuc)

bag.close()