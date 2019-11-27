import sqlite3
class userOperation():
    def __init__(self):
        self.databaseOperation()
    def databaseOperation(self):
        self.database = sqlite3.connect("library.db")
        self.cursor = self.database.cursor()
        # adminAccount Table
        sql = "CREATE TABLE IF NOT EXISTS adminAccount (ID INTEGER PRIMARY KEY AUTOINCREMENT, kullaniciadi TEXT, sifre TEXT, tcNo INTEGER)"
        self.cursor.execute(sql)
        self.database.commit()
        # book Table
        sql = "CREATE TABLE IF NOT EXISTS book (ID INTEGER PRIMARY KEY AUTOINCREMENT, barkod TEXT, kitapAdi TEXT, kitapYazar TEXT, kitapSayfa TEXT, oduncDurum INT, silDurum INT)"
        self.cursor.execute(sql)
        self.database.commit()
        # userAccount Table
        sql = "CREATE TABLE IF NOT EXISTS userAccount (ID INTEGER PRIMARY KEY AUTOINCREMENT, adsoyad TEXT, tcNo INTEGER, silDurum INT)"
        self.cursor.execute(sql)
        self.database.commit()
        # bookUser Table (Emanet kitapların tutulduğu tablo)
        sql = "CREATE TABLE IF NOT EXISTS bookUser (ID INTEGER PRIMARY KEY AUTOINCREMENT, bookId INTEGER, userId INTEGER, kitapVerilme DATETIME, kitapAlinma DATETIME, durum INT)"
        self.cursor.execute(sql)
        self.database.commit()
    def loginOperation(self, username, password):
        sqlSorgu = "SELECT * FROM adminAccount WHERE kullaniciadi = ? AND sifre = ?"
        self.cursor.execute(sqlSorgu, (username, password))
        data = self.cursor.fetchall()
        if(len(data) != 0):
            return data[0][0]
        else:
            return "noData"
    def signinOperation(self, username, password, tc):
        sqlSorgu = "SELECT * FROM adminAccount WHERE kullaniciadi = ? OR tcNo = ?"
        self.cursor.execute(sqlSorgu, (username,tc))
        data = self.cursor.fetchall()
        if(len(data) == 0):
            sqlSorgu = "INSERT INTO adminAccount (kullaniciadi,sifre,tcNo) VALUES(?,?,?)"
            self.cursor.execute(sqlSorgu, (username,password,tc))
            self.database.commit()
            return "ok"
        else:
            return "alreadyHave"
    def bookListOperation(self):
        sqlSorgu = "SELECT * FROM book WHERE silDurum = 0"
        self.cursor.execute(sqlSorgu)
        data = self.cursor.fetchall()
        if(len(data) == 0):
            return "noData"
        else:
            return data
    def addBook(self, kitapAd, kitapYazar, kitapSayfa):
        sql = "INSERT INTO book (barkod, kitapAdi, kitapYazar, kitapSayfa, oduncDurum, silDurum) VALUES(?,?,?,?,?,?)"
        bos = ""
        self.cursor.execute(sql, (bos, kitapAd, kitapYazar, kitapSayfa,"0","0"))
        self.database.commit()
        return "Ok"
    def deleteBook(self, ID):
        id = int(ID)
        sql = "SELECT durum FROM bookUser WHERE durum = 1 AND bookId = ?"
        self.cursor.execute(sql, (id,))
        data = self.cursor.fetchall()
        if (len(data) == 0):
            sql = "UPDATE book SET silDurum = 1 WHERE ID = ?"
            self.cursor.execute(sql, (id,))
            self.database.commit()
            return "Ok"
        else:
            return "odunc"
    def deleteCustomer(self, ID):
        id = int(ID)
        sql = "SELECT durum FROM bookUser WHERE durum = 1 AND userId = ?"
        self.cursor.execute(sql, (id,))
        data = self.cursor.fetchall()
        if(len(data) == 0):
            sql = "UPDATE userAccount SET silDurum = 1 WHERE ID = ?"
            self.cursor.execute(sql, (id,))
            self.database.commit()
            return "Ok"
        else:
            return "odunc"
    def kitabiGeriAl(self, bookUserId):
        sql = "SELECT bookId FROM bookUser WHERE ID = ?"
        self.cursor.execute(sql, (bookUserId,))
        data = self.cursor.fetchall()
        if (len(data) != 0):
            sql = "UPDATE bookUser SET durum = 0 WHERE ID = ?"
            self.cursor.execute(sql, (bookUserId,))
            sql = "UPDATE book SET oduncDurum = 0 WHERE ID = ?"
            self.cursor.execute(sql, (data[0][0],))
            self.database.commit()
            return "Ok"
        else:
            return "bos"
    def customerListOperation(self):
        sql = "SELECT * FROM userAccount WHERE silDurum = 0"
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        if(len(data) == 0):
            return "noData"
        else:
            return data
    def booklistOperationForOdunc(self):
        sqlSorgu = "SELECT * FROM book WHERE oduncDurum = 0 AND silDurum = 0"
        self.cursor.execute(sqlSorgu)
        data = self.cursor.fetchall()
        if (len(data) == 0):
            return "noData"
        else:
            return data
    def customerListOperationForOdunc(self):
        sql = "SELECT * FROM userAccount WHERE silDurum = 0"
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        if (len(data) == 0):
            return "noData"
        else:
            return data
    def addCustomer(self, adSoyad, tcNo):
        sql = "INSERT INTO userAccount (adsoyad, tcNo, silDurum) VALUES(?,?,?)"
        self.cursor.execute(sql, (adSoyad, tcNo,"0"))
        self.database.commit()
        return "Ok"
    def addbookUser(self, kitapId, customerId, verilme, alinma):
        sql = "SELECT * FROM book WHERE ID = ? AND oduncDurum = 1 AND silDurum = 0"
        self.cursor.execute(sql, (kitapId,))
        data = self.cursor.fetchall()
        if (len(data) == 0):
            sql = "INSERT INTO bookUser (bookId, userId, kitapVerilme, kitapAlinma, durum) VALUES(?,?,?,?,?)"
            self.cursor.execute(sql, (kitapId, customerId, verilme, alinma, "1"))
            sql = "UPDATE book SET oduncDurum = 1 WHERE ID = ?"
            self.cursor.execute(sql, (kitapId,))
            self.database.commit()
            return "Ok"
        else:
            return "alreadHave"
    def emanettekiKitaplar(self):
        sql = "SELECT ID, bookId, userId, kitapVerilme, kitapAlinma FROM bookUser WHERE durum = 1"
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        list = []
        if (len(data) != 0):
            j = 0
            for i in data:
                sql = "SELECT kitapadi FROM book WHERE ID = ?"
                self.cursor.execute(sql, (data[j][1],))
                bookResult = self.cursor.fetchall()
                sql = "SELECT ID, adsoyad FROM userAccount WHERE ID = ?"
                self.cursor.execute(sql, (data[j][2],))
                userResult = self.cursor.fetchall()
                # bookUser id, user adsoyad, book ad, verilme,alinma,,user id
                list = list + [[data[j][0],userResult[0][1],bookResult[0][0],data[j][3],data[j][4]]]
                j += 1
                self.database.commit()
            return list
        else:
            return "noData"