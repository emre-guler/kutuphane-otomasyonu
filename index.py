import sys
import hashlib
import datetime
from functools import partial
from database import userOperation
from PyQt5 import QtCore, QtGui, QtWidgets
class loginPage(object):
    def __init__(self):
        self.qlinecss = "background-color:rgb(31,31,31);border: 0 solid #ffdd00; border-bottom-width: 2px; font: normal 12px/normal; font-family:sans-serif; color: white;"
        self.qbuttoncss = "QPushButton{background-color:transparent;border-radius:20px;border:1px solid #ffdd00;color:#ffdd00;font-family:sans-serif;font-size:12px;padding:10px 25px;text-decoration:none;} QPushButton:hover{color:rgb(31, 31, 31);background-color:#ffdd00;border:none;}"
        self.left = 450
        self.top = 200
        self.width = 1100
        self.height = 600
        self.backgroundColor = "background-color:rgb(31,31,31); color:white;"
        self.iconName = "icon.png"
    def initUi(self, Window):
        self.loginPage = Window
        Window.setWindowIcon(QtGui.QIcon(self.iconName))
        self.title = "Kullanıcı Girişi"
        Window.setWindowTitle(self.title)
        Window.setGeometry(self.left, self.top, self.width, self.height)
        Window.setStyleSheet(self.backgroundColor)
        Window.setAutoFillBackground(True)
        self._translate = QtCore.QCoreApplication.translate
        # Username textbox ayarlarının başlangıcı
        self.username = QtWidgets.QLineEdit(Window)
        self.username.setGeometry(QtCore.QRect(510, 180, 133, 31))
        self.username.setStyleSheet(self.qlinecss)
        self.username.setObjectName("username")
        # Username textbox ayarlarının bitişi
        # Password textbox ayarlarının başlangıcı
        self.password = QtWidgets.QLineEdit(Window)
        self.password.setGeometry(QtCore.QRect(510, 240, 133, 31))
        self.password.setStyleSheet(self.qlinecss)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        # Password textbox ayarlarının bitisi
        # Giriş Yap Buttonu ayarlarının baslangıcı
        self.loginButton = QtWidgets.QPushButton(Window)
        self.loginButton.setGeometry(QtCore.QRect(640, 300, 131, 41))
        self.loginButton.setStyleSheet(self.qbuttoncss)
        self.loginButton.setObjectName("loginButton")
        self.loginButton.setText(self._translate("Window", "Giriş Yap!"))
        self.loginButton.clicked.connect(self.loginButtonClicked)
        # Giriş Yap Buttonu ayarlarının bitisi
        # Kayıt Ekranı Button başlangıç
        self.signinButton = QtWidgets.QPushButton(Window)
        self.signinButton.setGeometry(QtCore.QRect(500,300,131,41))
        self.signinButton.setStyleSheet(self.qbuttoncss)
        self.signinButton.setObjectName("signinButton")
        self.signinButton.setText(self._translate("Window","Kayıt Ol!"))
        self.signinButton.clicked.connect(self.gosigninButtonClicked)
        # Kayıt Ekranı Button biitş
        # Büyük Başlık ayarlarının başlangıcı
        self.bigTextLabel = QtWidgets.QLabel(Window)
        self.bigTextLabel.setGeometry(QtCore.QRect(270, 90, 554, 37))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        self.bigTextLabel.setFont(font)
        self.bigTextLabel.setStyleSheet("color:#ffdd00")
        self.bigTextLabel.setObjectName("bigTextLabel")
        self.bigTextLabel.setText(self._translate("Window","<html><head/><body><p><span style=\" font-size:24pt; color:#ffdd00;\">Kütüphane Otomasyonu Kullanıcı Girişi</span></p></body></html>"))
        # Büyük Başlık ayarlarının bitişi
        # Username Label ayarlarının başangıcı
        self.usernameLabel = QtWidgets.QLabel(Window)
        self.usernameLabel.setGeometry(QtCore.QRect(400, 190, 88, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setStyleSheet("color:#ffdd00")
        self.usernameLabel.setObjectName("label_2")
        self.usernameLabel.setText(self._translate("Window","<html><head/><body><p><span style=\" color:#ffdd00;\">Kullanıcı Adı</span></p></body></html>"))
        # Username Label ayarının bitişi
        # Password Label ayarının başlangıcı
        self.passwordLabel = QtWidgets.QLabel(Window)
        self.passwordLabel.setGeometry(QtCore.QRect(400, 250, 33, 20))
        self.passwordLabel.setFont(font)
        self.passwordLabel.setStyleSheet("color:#ffdd00")
        self.passwordLabel.setObjectName("label_3")
        self.passwordLabel.setText(self._translate("Window", "<html><head/><body><p><span style=\" font-size:12pt;\">Şifre</span></p></body></html>"))
        # Password Label ayarının bitişi
        # Noktalı Virgüller başlangıç
        self.Label_1 = QtWidgets.QLabel(Window)
        self.Label_1.setGeometry(QtCore.QRect(490, 250, 4, 20))
        self.Label_1.setStyleSheet("color:#ffdd00")
        self.Label_1.setObjectName("Label_1")
        self.Label_1.setText(self._translate("Window", "<html><head/><body><p><span style=\" font-size:12pt;\">:</span></p></body></html>"))
        self.Label_2 = QtWidgets.QLabel(Window)
        self.Label_2.setGeometry(QtCore.QRect(490, 190, 4, 20))
        self.Label_2.setStyleSheet("color:#ffdd00")
        self.Label_2.setObjectName("Label_1")
        self.Label_2.setText(self._translate("Window", "<html><head/><body><p><span style=\" font-size:12pt;\">:</span></p></body></html>"))
        self.tcNo = QtWidgets.QLineEdit()
        self.kitapAdi = QtWidgets.QLineEdit()
        self.kitapSayfa = QtWidgets.QLineEdit()
        self.kitapYazar = QtWidgets.QLineEdit()
        self.adSoyad = QtWidgets.QLineEdit()
        self.kitapYazarText = QtWidgets.QLabel()
        self.tarihAlinma = QtWidgets.QDateTimeEdit()
        self.tarihVerilme = QtWidgets.QDateTimeEdit()
        # Noktalı Virgüller bitiş
        # Login Def
    def loginButtonClicked(self):
        self.database = userOperation()
        inputUsername = self.username.text()
        inputPassword = self.password.text()
        hashPassword = hashlib.md5(inputPassword.encode()).hexdigest()
        data = self.database.loginOperation(inputUsername, hashPassword)
        if (data == "noData"):
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText("Kullanıcı adınızı ve şifrenizi kontrol ediniz.")
            msgBox.setWindowTitle("Hata Oluştu!")
            msgBox.setEscapeButton(QtWidgets.QMessageBox.Cancel)
            reply = msgBox.exec_()
        else:
            self.mainPage = QtWidgets.QMainWindow()
            page = mainPage.initUi(self, self.mainPage)
            self.mainPage.show()
            self.loginPage.hide()
    def gosigninButtonClicked(self):
        self.loginPage.hide()
        self.signin = QtWidgets.QMainWindow()
        page = signinPage.initUi(self,self.signin)
        self.signin.show()


        # Signin Def
    def girisYapClicked(self):
        self.signin.hide()
        self.loginPage.show()
    def signinButtonClicked(self):
        self.database = userOperation()
        signUsername = self.username.text()
        signPassword = self.password.text()
        signTc = self.tcNo.text()
        if (signUsername != "" and signPassword != "" and signTc != ""):
            try:
                signTc = int(signTc)
                if(len(signPassword) >= 6):
                    hashPassword = hashlib.md5(signPassword.encode()).hexdigest()
                    control = self.database.signinOperation(signUsername, hashPassword, signTc)
                    if (control == "alreadyHave"):
                        msgBox = QtWidgets.QMessageBox()
                        msgBox.setText("Bu kullanıcı adı veya TC NO kullanmılmış tekrar deneyin.")
                        msgBox.setWindowTitle("Hesap Oluşturulamadı!")
                        msgBox.setEscapeButton(QtWidgets.QMessageBox.Cancel)
                        reply = msgBox.exec_()
                    else:
                        msgBox = QtWidgets.QMessageBox()
                        msgBox.setText("Anasayfaya yönlendiriliyorsun.")
                        msgBox.setWindowTitle("Hesap Oluşturuldu!")
                        msgBox.setEscapeButton(QtWidgets.QMessageBox.Cancel)
                        reply = msgBox.exec_()
                        self.getMainMenu()
                else:
                    msgBox = QtWidgets.QMessageBox()
                    msgBox.setText("Şifreniz en az 6 karakterden oluşmalıdır.")
                    msgBox.setWindowTitle("Hesap Oluşturulamadı!")
                    msgBox.setEscapeButton(QtWidgets.QMessageBox.Cancel)
                    reply = msgBox.exec_()
            except Exception:
                msgBox = QtWidgets.QMessageBox()
                msgBox.setText("TC kimlik numarası 11 rakamdan oluşmalıdır.")
                msgBox.setWindowTitle("Hesap Oluşturulamadı!")
                msgBox.setEscapeButton(QtWidgets.QMessageBox.Cancel)
                reply = msgBox.exec_()
        else:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText("Tüm alanları eksiksiz olarak girdiğinizden emin olun.")
            msgBox.setWindowTitle("Hatalı Giriş!")
            msgBox.setEscapeButton(QtWidgets.QMessageBox.Cancel)
            reply = msgBox.exec_()
    def getMainMenu(self):
        self.signin.hide()
        self.mainPage = QtWidgets.QMainWindow()
        page = mainPage.initUi(self, self.mainPage)
        self.mainPage.show()


        # Main Menu Def
    def exitButtonClicked(self):
        QtWidgets.QApplication.quit()
    def emanetKitapClicked(self):
        self.mainPage.hide()
        self.emanetKitaplarPage = QtWidgets.QMainWindow()
        page = oduncKitap.initUi(self,self.emanetKitaplarPage)
        self.emanetKitaplarPage.show()
    def kitapIslemleriClicked(self):
        self.mainPage.hide()
        self.kitapIslemleriPage = QtWidgets.QMainWindow()
        page = bookOperaiton.initUi(self, self.kitapIslemleriPage)
        self.kitapIslemleriPage.show()
    def musteriIslemleriClicked(self):
        self.mainPage.hide()
        self.MusteriIslemleriPage = QtWidgets.QMainWindow()
        page = customeroperationPage.initUi(self, self.MusteriIslemleriPage)
        self.MusteriIslemleriPage.show()
    def emanetteOlanKitaplarClicked(self):
        self.mainPage.hide()
        self.emanettekiKitaplarPage = QtWidgets.QMainWindow()
        page = emanettekikitaplarPage.initUi(self, self.emanettekiKitaplarPage)
        self.emanettekiKitaplarPage.show()




        # Kitap İşlemleri def
    def kitaptanMainDon(self):
        self.kitapIslemleriPage.hide()
        self.mainPage.show()
    def bookOperationDataCek(self):
        self.database = userOperation()
        self.data = self.database.bookListOperation()
        if (self.data == "noData"):
            return
        else:
            j = 0
            for i in self.data:
                self.bookTable.setRowCount(len(self.data))
                self.bookTable.setItem(j,0, QtWidgets.QTableWidgetItem(str(self.data[j][0])))
                self.bookTable.setItem(j,1, QtWidgets.QTableWidgetItem(self.data[j][2]))
                self.bookTable.setItem(j,2, QtWidgets.QTableWidgetItem(self.data[j][3]))
                self.bookTable.setItem(j,3, QtWidgets.QTableWidgetItem(str(self.data[j][4])))
                if (self.data[j][5] == "1"):
                    self.bookTable.setItem(j,4, QtWidgets.QTableWidgetItem("Ödünç verilmiş."))
                else:
                    self.bookTable.setItem(j, 4, QtWidgets.QTableWidgetItem("Kütüphane'de"))
                j = j + 1
    def yeniKitapClicked(self):
        self.kitapIslemleriPage.hide()
        self.yeniKitapPage = QtWidgets.QMainWindow()
        page = addBook.initUi(self, self.yeniKitapPage)
        self.yeniKitapPage.show()
    def kitapSec(self, item):
        id = self.bookTable.item(item.row(), 0).text()
        self.bookOperationSecilenler = self.bookOperationSecilenler + [id]
        for i in range(5):
            self.bookTable.item(item.row(), i).setBackground(QtGui.QColor(243, 32, 19))
    def kitapSilClicked(self):
        for i in self.bookOperationSecilenler:
            j = 0
            try:
                id = self.bookOperationSecilenler[j]
                if(id != ""):
                    self.data = self.database.deleteBook(self.bookOperationSecilenler[j])
                    if(self.data == "Ok"):
                        msgBox = QtWidgets.QMessageBox()
                        msgBox.setText("Kitap başarıyla kütüphaneden silindi.")
                        msgBox.setWindowTitle("Başarılı!")
                        msgBox.setEscapeButton(QtWidgets.QMessageBox.Cancel)
                        reply = msgBox.exec_()
                    else:
                        msgBox = QtWidgets.QMessageBox()
                        msgBox.setText("Şuan emanet edilmiş bir kitap silinemez. Önce kitabın geri alınmış olması gerekir.")
                        msgBox.setWindowTitle("Hata Oluştu!")
                        msgBox.setEscapeButton(QtWidgets.QMessageBox.Cancel)
                        reply = msgBox.exec_()
                else:
                    msgBox = QtWidgets.QMessageBox()
                    msgBox.setText("Kitabı silmek için bir seçim yapmış olmanız gerekmekte.")
                    msgBox.setWindowTitle("Hata Oluştu!")
                    msgBox.setEscapeButton(QtWidgets.QMessageBox.Cancel)
                    reply = msgBox.exec_()
                    pass
            except:
                msgBox = QtWidgets.QMessageBox()
                msgBox.setText("Kitabı silmek için bir seçim yapmış olmanız gerekmekte.")
                msgBox.setWindowTitle("Hata Oluştu!")
                msgBox.setEscapeButton(QtWidgets.QMessageBox.Cancel)
                reply = msgBox.exec_()
            j += 1

        # add book def
    def kitapIslemDon(self):
        self.yeniKitapPage.hide()
        self.kitapIslemleriPage.show()
        self.bookOperationDataCek()
    def kitapEkleClicked(self):
        yeniKitapAd = self.kitapAdi.text()
        yeniKitapYazar = self.kitapYazar.text()
        yeniKitapSayfa = self.kitapSayfa.text()
        if(yeniKitapAd != "" and yeniKitapSayfa != "" and yeniKitapYazar != ""):
            try:
                yeniKitapSayfa = int(yeniKitapSayfa)
                operation = userOperation()
                result = operation.addBook(yeniKitapAd, yeniKitapYazar, yeniKitapSayfa)
                if(result == "Ok"):
                    msgBox = QtWidgets.QMessageBox()
                    msgBox.setText("Kitap başarıyla eklendi.")
                    msgBox.setWindowTitle("Başarılı!")
                    msgBox.setEscapeButton(QtWidgets.QMessageBox.Cancel)
                    reply = msgBox.exec_()
                    pass
                else:
                    msgBox = QtWidgets.QMessageBox()
                    msgBox.setText("Bir hata oluştu.")
                    msgBox.setWindowTitle("Kitap eklenemedi!")
                    msgBox.setEscapeButton(QtWidgets.QMessageBox.Cancel)
                    reply = msgBox.exec_()
            except:
                msgBox = QtWidgets.QMessageBox()
                msgBox.setText("Kitap sayfası kısmı sayısal bir değer içermeli.")
                msgBox.setWindowTitle("Kitap Eklenemedi!")
                msgBox.setEscapeButton(QtWidgets.QMessageBox.Cancel)
                reply = msgBox.exec_()
            self.kitapIslemDon()
        else:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText("Tüm alanlar eksiksiz olarak tamamlanmalıdır.")
            msgBox.setWindowTitle("Kitap Eklenemedi!")
            msgBox.setEscapeButton(QtWidgets.QMessageBox.Cancel)
            reply = msgBox.exec_()



            # müşteri işlemleri def
    def musteriDonAnasayfa(self):
        self.MusteriIslemleriPage.hide()
        self.mainPage.show()
        self.musteriVeriCek()
    def musteriVeriCek(self):
        self.database = userOperation()
        self.data = self.database.customerListOperation()
        if (self.data == "noData"):
            return 0
        else:
            j = 0
            for i in self.data:
                self.musteriTable.setRowCount(len(self.data))
                self.musteriTable.setItem(j,0, QtWidgets.QTableWidgetItem(str(self.data[j][0])))
                self.musteriTable.setItem(j,1, QtWidgets.QTableWidgetItem(self.data[j][1]))
                self.musteriTable.setItem(j,2, QtWidgets.QTableWidgetItem(str(self.data[j][2])))
                j = j + 1
    def yeniMusteriClicked(self):
        self.MusteriIslemleriPage.hide()
        self.yenimusteriPage = QtWidgets.QMainWindow()
        page = addCustomer.initUi(self, self.yenimusteriPage)
        self.yenimusteriPage.show()
    def musteriSec(self, item):
        id = self.musteriTable.item(item.row(), 0).text()
        self.musteriIslemleriSecilenler = self.musteriIslemleriSecilenler + [id]
        for i in range(3):
            self.musteriTable.item(item.row(), i).setBackground(QtGui.QColor(243, 32, 19))
    def musteriSilClicked(self):
        for i in self.musteriIslemleriSecilenler:
            j = 0
            try:
                id = self.musteriIslemleriSecilenler[j]
                if (id != ""):
                    self.data = self.database.deleteCustomer(self.musteriIslemleriSecilenler[j])
                    if (self.data == "Ok"):
                        self.musteriVeriCek()
                        msgBox = QtWidgets.QMessageBox()
                        msgBox.setText("Müşteri kaydı başarıyla silindi.")
                        msgBox.setWindowTitle("Başarılı!")
                        msgBox.setEscapeButton(QtWidgets.QMessageBox.Cancel)
                        reply = msgBox.exec_()
                    else:
                        msgBox = QtWidgets.QMessageBox()
                        msgBox.setText("Emanet kitap sahibi birisinin hesabı silinemez. Önce kitabın geri alınmış olması gerekir.")
                        msgBox.setWindowTitle("Hata Oluştu!")
                        msgBox.setEscapeButton(QtWidgets.QMessageBox.Cancel)
                        reply = msgBox.exec_()
                else:
                    msgBox = QtWidgets.QMessageBox()
                    msgBox.setText("Müşteir kaydını silmek için bir seçim yapmış olmanız gerekmekte.")
                    msgBox.setWindowTitle("Hata Oluştu!")
                    msgBox.setEscapeButton(QtWidgets.QMessageBox.Cancel)
                    reply = msgBox.exec_()
                    pass
            except:
                msgBox = QtWidgets.QMessageBox()
                msgBox.setText("Müşteri kaydını silmek için bir seçim yapmış olmanız gerekmekte.")
                msgBox.setWindowTitle("Hata Oluştu!")
                msgBox.setEscapeButton(QtWidgets.QMessageBox.Cancel)
                reply = msgBox.exec_()
            j += 1


            # müşteri ekleme def
    def addToList(self):
        self.yenimusteriPage.hide()
        self.MusteriIslemleriPage.show()
        self.musteriVeriCek()
    def musteriEkleClicked(self):
        yeniMusteriAdSoyad = self.adSoyad.text()
        yeniMusteriTCNO = self.tcNo.text()
        if (yeniMusteriAdSoyad != "" and yeniMusteriTCNO != ""):
            try:
                yeniMusteriTCNO = int(yeniMusteriTCNO)
                operation = userOperation()
                response = operation.addCustomer(yeniMusteriAdSoyad, yeniMusteriTCNO)
                if (response == "Ok"):
                    msgBox = QtWidgets.QMessageBox()
                    msgBox.setText("Müşteri başarıyla oluşturuldu.")
                    msgBox.setWindowTitle("Müşteri Oluşturuldu!")
                    msgBox.setEscapeButton(QtWidgets.QMessageBox.Cancel)
                    reply = msgBox.exec_()
                    self.addToList()
                    pass
            except:
                msgBox = QtWidgets.QMessageBox()
                msgBox.setText("TC kimlik numarası 11 rakamdan oluşmalıdır.")
                msgBox.setWindowTitle("Hata oluştu")
                msgBox.setEscapeButton(QtWidgets.QMessageBox.Cancel)
                reply = msgBox.exec_()
        else:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText("Tüm alanlar eksiksiz şekilde oluşturulmalı.")
            msgBox.setWindowTitle("Hata oluştu")
            msgBox.setEscapeButton(QtWidgets.QMessageBox.Cancel)
            reply = msgBox.exec_()



            # emanet def
    def emanetMain(self):
        self.emanettekiKitaplarPage.hide()
        self.mainPage.show()
    def selectRow(self, item):
        id = self.emanetTable.item(item.row(), 0).text()
        self.emanetteSecilenler = self.emanetteSecilenler + [id]
        for i in range(5):
            self.emanetTable.item(item.row(), i).setBackground(QtGui.QColor(243, 32, 19))
    def emanetSecClicked(self):
        for i in self.emanetteSecilenler:
            j = 0
            try:
                id = self.emanetteSecilenler[j]
                if (id != ""):
                    self.data = self.database.kitabiGeriAl(self.emanetteSecilenler[j])
                    if (self.data == "Ok"):
                        msgBox = QtWidgets.QMessageBox()
                        msgBox.setText("Kitap başarı ile geri alındı.")
                        msgBox.setWindowTitle("Başarılı!")
                        msgBox.setEscapeButton(QtWidgets.QMessageBox.Cancel)
                        reply = msgBox.exec_()
                    else:
                        msgBox = QtWidgets.QMessageBox()
                        msgBox.setText("Bir hata oluştu.")
                        msgBox.setWindowTitle("Hata Oluştu!")
                        msgBox.setEscapeButton(QtWidgets.QMessageBox.Cancel)
                        reply = msgBox.exec_()
                else:
                    msgBox = QtWidgets.QMessageBox()
                    msgBox.setText("Kitabı geri almak için bir seçim yapmış olmanız gerekmekte.")
                    msgBox.setWindowTitle("Hata Oluştu!")
                    msgBox.setEscapeButton(QtWidgets.QMessageBox.Cancel)
                    reply = msgBox.exec_()
                    pass
            except:
                msgBox = QtWidgets.QMessageBox()
                msgBox.setText("Kitabı geri almak için bir seçim yapmış olmanız gerekmekte.")
                msgBox.setWindowTitle("Hata Oluştu!")
                msgBox.setEscapeButton(QtWidgets.QMessageBox.Cancel)
                reply = msgBox.exec_()
            j += 1
    def emanetDataCek(self):
        self.today = datetime.datetime.now().date().strftime('%d/%m/%Y')
        self.today = datetime.datetime.strptime(self.today,'%d/%m/%Y')
        self.database = userOperation()
        data = self.database.emanettekiKitaplar()
        if(data == "noData"):
            return
        else:
            j = 0
            for i in data:
                self.emanetTable.setRowCount(len(data))
                self.emanetTable.setItem(j, 0, QtWidgets.QTableWidgetItem(str(data[j][0])))
                self.emanetTable.setItem(j, 1, QtWidgets.QTableWidgetItem(str(data[j][1])))
                self.emanetTable.setItem(j, 2, QtWidgets.QTableWidgetItem(str(data[j][2])))
                self.emanetTable.setItem(j, 3, QtWidgets.QTableWidgetItem(str(data[j][3])))
                data[j][4] = datetime.datetime.strptime(data[j][4], '%d/%m/%Y').date()
                data[j][4] = datetime.datetime.combine(data[j][4], datetime.time(0, 0))
                if (data[j][4] <= self.today):
                    self.emanetTable.setItem(j, 4, QtWidgets.QTableWidgetItem(str(data[j][4])))
                    self.emanetTable.item(j, 4).setBackground(QtGui.QColor(243, 32, 19))
                else:
                    self.emanetTable.setItem(j, 4, QtWidgets.QTableWidgetItem(str(data[j][4])))
                j += 1

            # emanet kitap işlemleri def
    def oduncverMain(self):
        self.emanetKitaplarPage.hide()
        self.mainPage.show()
    def buttonClicked(self):
        try:
            kitapId = self.secilenKitapId
            musteriId = self.secilenMusteriId
            if (kitapId != "" and musteriId != ""):
                self.database = userOperation()
                tarihVerilme = self.tarihVerilme.text()
                tarihAlinma = self.tarihAlinma.text()
                data = self.database.addbookUser(kitapId, musteriId, tarihVerilme,tarihAlinma)
                if(data == "alreadHave"):
                    msgBox = QtWidgets.QMessageBox()
                    msgBox.setText("Bu kitap zaten birisine verilmiş.")
                    msgBox.setWindowTitle("Hata Oluştu!")
                    msgBox.setEscapeButton(QtWidgets.QMessageBox.Cancel)
                    reply = msgBox.exec_()
                else:
                    msgBox = QtWidgets.QMessageBox()
                    msgBox.setText("Kitap başarıyla verildi.")
                    msgBox.setWindowTitle("Başarıyla Tamamlandı")
                    msgBox.setEscapeButton(QtWidgets.QMessageBox.Cancel)
                    reply = msgBox.exec_()
            else:
                msgBox = QtWidgets.QMessageBox()
                msgBox.setText("İki alandan da bir seçim yapmış olmanız gerekmekte.")
                msgBox.setWindowTitle("Hata Oluştu!")
                msgBox.setEscapeButton(QtWidgets.QMessageBox.Cancel)
                reply = msgBox.exec_()
        except:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText("İki alandan da seçim yapmış olmanız gerekmekte.")
            msgBox.setWindowTitle("Hata Oluştu!")
            msgBox.setEscapeButton(QtWidgets.QMessageBox.Cancel)
            reply = msgBox.exec_()
    def kitapDoubleClicked(self, item):
        sonuc = self.kitapTable.item(item.row(), 0).text()
        self.secilenKitapId = sonuc
    def musteriDoubleClicked(self, item):
        sonuc = self.musteriTableOdunc.item(item.row(),0).text()
        self.secilenMusteriId = sonuc
    def dataCek(self):
        self.database = userOperation()
        data = self.database.booklistOperationForOdunc()
        if (data == "noData"):
            print("Data yok devam.")
        else:
            j = 0
            for i in data:
                self.kitapTable.setRowCount(len(data))
                self.kitapTable.setItem(j,0, QtWidgets.QTableWidgetItem(str(data[j][0])))
                self.kitapTable.setItem(j,1, QtWidgets.QTableWidgetItem(data[j][2]))
                self.kitapTable.setItem(j,2, QtWidgets.QTableWidgetItem(data[j][3]))
                self.kitapTable.setItem(j,3, QtWidgets.QTableWidgetItem(data[j][4]))
                j += 1
        data = self.database.customerListOperationForOdunc()
        if (data == "noData"):
            print("Data yok devam.")
        else:
            j = 0
            for i in data:
                self.musteriTableOdunc.setRowCount(len(data))
                self.musteriTableOdunc.setItem(j,0, QtWidgets.QTableWidgetItem(str(data[j][0])))
                self.musteriTableOdunc.setItem(j,1, QtWidgets.QTableWidgetItem(str(data[j][1])))
                self.musteriTableOdunc.setItem(j,2, QtWidgets.QTableWidgetItem(str(data[j][2])))
                j += 1

class signinPage(object):
    def initUi(self, Window):
        self.title = "Kayıt Ol!"
        Window.setWindowIcon(QtGui.QIcon(self.iconName))
        Window.setAutoFillBackground(True)
        self._translate = QtCore.QCoreApplication.translate
        Window.setObjectName("Window")
        Window.resize(1100, 600)
        Window.setWindowTitle(self.title)
        Window.setGeometry(self.left, self.top, self.width, self.height)
        Window.setStyleSheet("QMainWindow{" + self.backgroundColor + "}QMenu{background-color:none}")
        mainMenu = Window.menuBar()
        menuBar = mainMenu.addMenu("Geri Dön")
        girisYap = QtWidgets.QAction("Kullanıcı Girişi Ekranına Dön", Window)
        menuBar.addAction(girisYap)
        girisYap.triggered.connect(self.girisYapClicked)
        # Username textbox başlangıc
        self.username = QtWidgets.QLineEdit(Window)
        self.username.setGeometry(QtCore.QRect(510, 160, 133, 31))
        self.username.setStyleSheet(self.qlinecss)
        self.username.setObjectName("username")
        # Username textbox bitiş
        # Büyük başlık başlangıç
        self.bigTitleLabel = QtWidgets.QLabel(Window)
        self.bigTitleLabel.setGeometry(QtCore.QRect(270, 90, 554, 37))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        self.bigTitleLabel.setFont(font)
        self.bigTitleLabel.setStyleSheet("color:#ffdd00")
        self.bigTitleLabel.setObjectName("bigTitleLabel")
        self.bigTitleLabel.setText(self._translate("Window","<html><head/><body><p><span style=\" font-size:24pt; color:#ffdd00;\">Kütüphane Otomasyonu Kullanıcı Kaydı</span></p></body></html>"))
        # Büyük başlık bitiş
        # username label baslagnıc
        self.usernameLabel = QtWidgets.QLabel(Window)
        self.usernameLabel.setGeometry(QtCore.QRect(400, 170, 88, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.usernameLabel.setFont(font)
        self.usernameLabel.setStyleSheet("color:#ffdd00")
        self.usernameLabel.setObjectName("usernameLabel")
        self.usernameLabel.setText(self._translate("Window","<html><head/><body><p><span style=\" color:#ffdd00;\">Kullanıcı Adı</span></p></body></html>"))
        # username label bitiş
        # password label başlangıç
        self.passwordLabel = QtWidgets.QLabel(Window)
        self.passwordLabel.setGeometry(QtCore.QRect(400, 250, 33, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setStyleSheet("color:#ffdd00")
        self.passwordLabel.setObjectName("passwordLabel")
        self.passwordLabel.setText(self._translate("Window", "<html><head/><body><p><span style=\" font-size:12pt;\">Şifre</span></p></body></html>"))
        # password label bitiş
        # password textbox başlangıç
        self.password = QtWidgets.QLineEdit(Window)
        self.password.setGeometry(QtCore.QRect(510, 240, 133, 31))
        self.password.setStyleSheet(self.qlinecss)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        # password textbox bitiş
        # tc textbox baslangıc
        self.tcNo = QtWidgets.QLineEdit(Window)
        self.tcNo.setMaxLength(11)
        self.tcNo.setGeometry(QtCore.QRect(510, 320, 133, 31))
        self.tcNo.setStyleSheet(self.qlinecss)
        self.onlyInt = QtGui.QIntValidator()
        self.tcNo.setObjectName("tcNo")
        # tc textbox bitiş
        # button başlangıç
        self.signinButton = QtWidgets.QPushButton(Window)
        self.signinButton.clicked.connect(self.signinButtonClicked)
        self.signinButton.setGeometry(QtCore.QRect(640, 390, 131, 41))
        self.signinButton.setStyleSheet(self.qbuttoncss)
        self.signinButton.setObjectName("signinButton")
        self.signinButton.setText(self._translate("Window", "Kayıt Ol!"))
        # button bitiş
        # label1 başlangıç
        self.label = QtWidgets.QLabel(Window)
        self.label.setGeometry(QtCore.QRect(490, 250, 4, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("color:#ffdd00")
        self.label.setObjectName("label")
        self.label.setText(self._translate("Window", "<html><head/><body><p><span style=\" font-size:12pt;\">:</span></p></body></html>"))
        # label1 bitiş
        # label2 başlangıç
        self.label2 = QtWidgets.QLabel(Window)
        self.label2.setGeometry(QtCore.QRect(490, 170, 4, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        self.label2.setFont(font)
        self.label2.setStyleSheet("color:#ffdd00")
        self.label2.setObjectName("label2")
        self.label2.setText(self._translate("Window", "<html><head/><body><p><span style=\" font-size:12pt;\">:</span></p></body></html>"))
        # label2 bitiş
        # label3 başlangıc
        self.label3 = QtWidgets.QLabel(Window)
        self.label3.setGeometry(QtCore.QRect(490, 330, 4, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        self.label3.setFont(font)
        self.label3.setStyleSheet("color:#ffdd00")
        self.label3.setObjectName("label3")
        self.label3.setText(self._translate("Window", "<html><head/><body><p><span style=\" font-size:12pt;\">:</span></p></body></html>"))
        # label3 bitiş
        # label4 başlangıc
        self.label4 = QtWidgets.QLabel(Window)
        self.label4.setGeometry(QtCore.QRect(400, 330, 88, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        self.label4.setFont(font)
        self.label4.setStyleSheet("color:#ffdd00")
        self.label4.setObjectName("label4")
        self.label4.setText(self._translate("Window","<html><head/><body><p><span style=\" font-size:12pt;\">TC Kimlik No</span></p></body></html>"))
        # label4 bitiş
class mainPage(object):
    def initUi(self, Window):
        self.title = "Anasayfa"
        Window.setWindowIcon(QtGui.QIcon(self.iconName))
        Window.setWindowTitle(self.title)
        Window.setGeometry(self.left, self.top, self.width, self.height)
        Window.setStyleSheet(self.backgroundColor)
        Window.setAutoFillBackground(True)
        self._translate = QtCore.QCoreApplication.translate
        # Çıkış button başlangıç
        self.exitButton = QtWidgets.QPushButton(Window)
        self.exitButton.setGeometry(QtCore.QRect(460, 430, 181, 41))
        self.exitButton.setStyleSheet(self.qbuttoncss)
        self.exitButton.setObjectName("exitButton")
        self.exitButton.clicked.connect(self.exitButtonClicked)
        # Çıkış button bitiş
        # emanetkitap button başlangıç
        self.emanetKitap = QtWidgets.QPushButton(Window)
        self.emanetKitap.setGeometry(QtCore.QRect(460, 190, 181, 41))
        self.emanetKitap.setStyleSheet(self.qbuttoncss)
        self.emanetKitap.setObjectName("emanetKitap")
        self.emanetKitap.clicked.connect(self.emanetKitapClicked)
        # emanetkitap button bitiş
        # kitap işlemleri button başlangıç
        self.kitapIslemleri = QtWidgets.QPushButton(Window)
        self.kitapIslemleri.setGeometry(QtCore.QRect(460, 370, 181, 41))
        self.kitapIslemleri.setStyleSheet(self.qbuttoncss)
        self.kitapIslemleri.setObjectName("kitapIslemleri")
        self.kitapIslemleri.clicked.connect(self.kitapIslemleriClicked)
        # kitap işlemleri button bitiş
        # müşteri işlemleri button başlangıç
        self.musteriIslemleri = QtWidgets.QPushButton(Window)
        self.musteriIslemleri.setGeometry(QtCore.QRect(460, 310, 181, 41))
        self.musteriIslemleri.setStyleSheet(self.qbuttoncss)
        self.musteriIslemleri.setObjectName("musteriIslemleri")
        self.musteriIslemleri.clicked.connect(self.musteriIslemleriClicked)
        # müşteri işlemleri button bitiş
        # Emanette olan kitaplar
        self.emanetteOlanKitaplar = QtWidgets.QPushButton(Window)
        self.emanetteOlanKitaplar.setGeometry(QtCore.QRect(460, 250, 181, 41))
        self.emanetteOlanKitaplar.setStyleSheet(self.qbuttoncss)
        self.emanetteOlanKitaplar.setObjectName("emanetteOlanKitaplar")
        self.emanetteOlanKitaplar.clicked.connect(self.emanetteOlanKitaplarClicked)
        #bitiş
        # label başlangıç
        self.baslik = QtWidgets.QLabel(Window)
        self.baslik.setEnabled(True)
        self.baslik.setGeometry(QtCore.QRect(370, 110, 385, 29))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        self.baslik.setFont(font)
        self.baslik.setStyleSheet("color: #FFDD00")
        self.baslik.setObjectName("baslik")
        # label bitiş
        self.exitButton.setText(self._translate("Window", "Uygulamadan Çık"))
        self.emanetKitap.setText(self._translate("Window", "Emanet Kitap İşlemleri"))
        self.kitapIslemleri.setText(self._translate("Window", "Kitap İşlemleri"))
        self.musteriIslemleri.setText(self._translate("Window", "Müşteri İşlemleri"))
        self.baslik.setText(self._translate("Window","<html><head/><body><p align=\"center\"><span style=\" color:#ffdd00;\">Kütüphane Programına Hoşgeldiniz!</span></p></body></html>"))
        self.emanetteOlanKitaplar.setText(self._translate("Winow","Emanetteki Kitaplar"))
class bookOperaiton(object):
    def initUi(self, Window):
        self.title = "Kitap İşlemleri"
        Window.setWindowIcon(QtGui.QIcon(self.iconName))
        Window.setAutoFillBackground(True)
        self._translate = QtCore.QCoreApplication.translate
        Window.setObjectName("Window")
        Window.resize(1100, 600)
        Window.setWindowTitle(self.title)
        Window.setGeometry(self.left, self.top, self.width, self.height)
        Window.setStyleSheet("QMainWindow{" + self.backgroundColor + "}QMenu{background-color:none}")
        mainMenu = Window.menuBar()
        menuBar = mainMenu.addMenu("Geri Dön")
        don = QtWidgets.QAction("Ana Sayfaya Geri Dön", Window)
        menuBar.addAction(don)
        menuBar.triggered.connect(self.kitaptanMainDon)
        self.bookOperationSecilenler = []
        self.baslik = QtWidgets.QLabel(Window)
        self.baslik.setGeometry(QtCore.QRect(370, 40, 413, 29))
        self.baslik.setObjectName("baslik")
        self.baslik.setText(self._translate("Window","<html><head/><body><p><span style=\" font-size:18pt; color:#ffdd00;\">Kütüphane Otomasyonu Kitap İşlemleri</span></p></body></html>"))
        self.yeniKitap = QtWidgets.QPushButton(Window)
        self.yeniKitap.setGeometry(QtCore.QRect(730, 470, 131, 41))
        self.yeniKitap.setStyleSheet(self.qbuttoncss)
        self.yeniKitap.setObjectName("yeniKitap")
        self.yeniKitap.setText(self._translate("Window", "Yeni Kitap Ekle"))
        self.yeniKitap.clicked.connect(self.yeniKitapClicked)
        self.kitapSil = QtWidgets.QPushButton(Window)
        self.kitapSil.setGeometry(QtCore.QRect(580, 470, 131, 41))
        self.kitapSil.setStyleSheet(self.qbuttoncss)
        self.kitapSil.setObjectName("kitapSil")
        self.kitapSil.setText(self._translate("Window", "Kitap Sil"))
        self.kitapSil.clicked.connect(self.kitapSilClicked)
        self.bookTable = QtWidgets.QTableWidget(Window)
        self.bookTable.setGeometry(QtCore.QRect(250, 90, 661, 361))
        self.bookTable.setShowGrid(True)
        self.bookTable.setColumnCount(5)
        self.bookTable.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.bookTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.bookTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.bookTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.bookTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.bookTable.setHorizontalHeaderItem(4, item)
        self.bookTable.horizontalHeader().setCascadingSectionResizes(False)
        self.bookTable.horizontalHeader().setSortIndicatorShown(False)
        self.bookTable.horizontalHeader().setStretchLastSection(True)
        self.bookTable.verticalHeader().setVisible(True)
        self.bookTable.verticalHeader().setCascadingSectionResizes(False)
        self.bookTable.verticalHeader().setSortIndicatorShown(False)
        self.bookTable.verticalHeader().setStretchLastSection(False)
        self.bookTable.setSortingEnabled(False)
        self.bookTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        item = self.bookTable.horizontalHeaderItem(0)
        item.setText(self._translate("Window", "ID"))
        item = self.bookTable.horizontalHeaderItem(1)
        item.setText(self._translate("Window", "Kitabın Adı"))
        item = self.bookTable.horizontalHeaderItem(2)
        item.setText(self._translate("Window", "Kitabın Yazarı"))
        item = self.bookTable.horizontalHeaderItem(3)
        item.setText(self._translate("Window", "Kitabın Sayfası"))
        item = self.bookTable.horizontalHeaderItem(4)
        item.setText(self._translate("Window", "Sahiplik Durumu"))
        self.bookOperationDataCek()
        self.bookTable.doubleClicked.connect(self.kitapSec)
class addBook(object):
    def initUi(self, Window):
        self.title = "Kitap Ekle"
        Window.setWindowIcon(QtGui.QIcon(self.iconName))
        Window.setAutoFillBackground(True)
        self._translate = QtCore.QCoreApplication.translate
        Window.setObjectName("Window")
        Window.resize(1100, 600)
        Window.setWindowTitle(self.title)
        Window.setGeometry(self.left, self.top, self.width, self.height)
        Window.setStyleSheet("QMainWindow{" + self.backgroundColor + "}QMenu{background-color:none}")
        mainMenu = Window.menuBar()
        kitapIslemDon = mainMenu.addMenu("Geri Dön")
        kitapDon = QtWidgets.QAction("Kitap İşlemleri Sayfasına Geri Dön", Window)
        kitapIslemDon.addAction(kitapDon)
        mainMenu.triggered.connect(self.kitapIslemDon)
        self.kitapAdi = QtWidgets.QLineEdit(Window)
        self.kitapAdi.setGeometry(QtCore.QRect(510, 180, 133, 31))
        self.kitapAdi.setStyleSheet(self.qlinecss)
        self.kitapAdi.setObjectName("kitapAdi")
        self.baslik = QtWidgets.QLabel(Window)
        self.baslik.setGeometry(QtCore.QRect(300, 90, 554, 37))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        self.baslik.setFont(font)
        self.baslik.setStyleSheet("color:#ffdd00")
        self.baslik.setObjectName("baslik")
        self.baslik.setText(self._translate("Window","<html><head/><body><p><span style=\" font-size:24pt; color:#ffdd00;\">Kütüphane Otomasyonu Kitap Ekle</span></p></body></html>"))
        self.kitapAdiText = QtWidgets.QLabel(Window)
        self.kitapAdiText.setGeometry(QtCore.QRect(390, 190, 63, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.kitapAdiText.setFont(font)
        self.kitapAdiText.setStyleSheet("color:#ffdd00")
        self.kitapAdiText.setObjectName("kitapAdiText")
        self.kitapAdiText.setText(self._translate("Window","<html><head/><body><p><span style=\" color:#ffdd00;\">Kitap Adı</span></p></body></html>"))
        self.kitapYazar = QtWidgets.QLineEdit(Window)
        self.kitapYazar.setGeometry(QtCore.QRect(510, 240, 133, 31))
        self.kitapYazar.setStyleSheet(self.qlinecss)
        self.kitapYazar.setObjectName("kitapYazar")
        self.kitapEkle = QtWidgets.QPushButton(Window)
        self.kitapEkle.setGeometry(QtCore.QRect(650, 400, 131, 41))
        self.kitapEkle.setStyleSheet(self.qbuttoncss)
        self.kitapEkle.setObjectName("kitapEkle")
        self.kitapEkle.setText(self._translate("Window", "Kitap Ekle!"))
        self.kitapEkle.clicked.connect(self.kitapEkleClicked)
        self.labelNoktali = QtWidgets.QLabel(Window)
        self.labelNoktali.setGeometry(QtCore.QRect(490, 250, 4, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        self.labelNoktali.setFont(font)
        self.labelNoktali.setStyleSheet("color:#ffdd00")
        self.labelNoktali.setObjectName("labelNoktali")
        self.labelNoktali.setText(self._translate("Window", "<html><head/><body><p><span style=\" font-size:12pt;\">:</span></p></body></html>"))
        self.labelNoktali2 = QtWidgets.QLabel(Window)
        self.labelNoktali2.setGeometry(QtCore.QRect(490, 190, 4, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        self.labelNoktali2.setFont(font)
        self.labelNoktali2.setStyleSheet("color:#ffdd00")
        self.labelNoktali2.setObjectName("labelNoktali2")
        self.labelNoktali2.setText(self._translate("Window", "<html><head/><body><p><span style=\" font-size:12pt;\">:</span></p></body></html>"))
        self.kitapYazarText = QtWidgets.QLabel(Window)
        self.kitapYazarText.setGeometry(QtCore.QRect(390, 250, 97, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.kitapYazarText.setFont(font)
        self.kitapYazarText.setStyleSheet("color:#ffdd00")
        self.kitapYazarText.setObjectName("kitapAdiText")
        self.kitapYazarText.setText(self._translate("Window","<html><head/><body><p><span style=\" color:#ffdd00;\">Kitabın Yazarı</span></p></body></html>"))
        self.kitapSayfaText = QtWidgets.QLabel(Window)
        self.kitapSayfaText.setGeometry(QtCore.QRect(390, 310, 41, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.kitapSayfaText.setFont(font)
        self.kitapSayfaText.setStyleSheet("color:#ffdd00")
        self.kitapSayfaText.setObjectName("kitapSayfaText")
        self.kitapSayfaText.setText(self._translate("Window", "<html><head/><body><p><span style=\" color:#ffdd00;\">Sayfa</span></p></body></html>"))
        self.labelNoktali3 = QtWidgets.QLabel(Window)
        self.labelNoktali3.setGeometry(QtCore.QRect(490, 310, 4, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        self.labelNoktali3.setFont(font)
        self.labelNoktali3.setStyleSheet("color:#ffdd00")
        self.labelNoktali3.setObjectName("labelNoktali3")
        self.labelNoktali3.setText(self._translate("Window", "<html><head/><body><p><span style=\" font-size:12pt;\">:</span></p></body></html>"))
        self.kitapSayfa = QtWidgets.QLineEdit(Window)
        self.kitapSayfa.setGeometry(QtCore.QRect(510, 300, 133, 31))
        self.kitapSayfa.setStyleSheet(self.qlinecss)
        self.kitapSayfa.setObjectName("sayfaSayisi")
class customeroperationPage(object):
    def initUi(self, Window):
        self.title = "Müşteri İşlemleri"
        Window.setWindowIcon(QtGui.QIcon(self.iconName))
        Window.setAutoFillBackground(True)
        self._translate = QtCore.QCoreApplication.translate
        Window.setObjectName("Window")
        Window.resize(1100, 600)
        Window.setWindowTitle(self.title)
        Window.setGeometry(self.left, self.top, self.width, self.height)
        Window.setStyleSheet("QMainWindow{" + self.backgroundColor + "}QMenu{background-color:none}")
        self.musteriIslemleriSecilenler = []
        mainMenu = Window.menuBar()
        mainDon = mainMenu.addMenu("Geri Dön")
        don = QtWidgets.QAction("Ana Sayfaya Dön", Window)
        mainDon.addAction(don)
        mainMenu.triggered.connect(self.musteriDonAnasayfa)
        self.baslik = QtWidgets.QLabel(Window)
        self.baslik.setGeometry(QtCore.QRect(370, 40, 413, 29))
        self.baslik.setObjectName("baslik")
        self.baslik.setText(self._translate("Window","<html><head/><body><p><span style=\" font-size:16pt; color:#ffdd00;\">Kütüphane Otomasyonu Müşteri İşlemleri</span></p></body></html>"))
        self.yeniMusteri = QtWidgets.QPushButton(Window)
        self.yeniMusteri.setGeometry(QtCore.QRect(730, 470, 131, 41))
        self.yeniMusteri.setStyleSheet(self.qbuttoncss)
        self.yeniMusteri.setObjectName("yeniMusteri")
        self.yeniMusteri.setText(self._translate("Window", "Müşteri Ekle"))
        self.yeniMusteri.clicked.connect(self.yeniMusteriClicked)
        self.musteriSil = QtWidgets.QPushButton(Window)
        self.musteriSil.setGeometry(QtCore.QRect(580, 470, 131, 41))
        self.musteriSil.setStyleSheet(self.qbuttoncss)
        self.musteriSil.setObjectName("musteriSil")
        self.musteriSil.setText(self._translate("Window", "Müşteri Sil"))
        self.musteriSil.clicked.connect(self.musteriSilClicked)
        self.musteriTable = QtWidgets.QTableWidget(Window)
        self.musteriTable.setGeometry(QtCore.QRect(250, 90, 661, 361))
        self.musteriTable.setShowGrid(True)
        self.musteriTable.setColumnCount(3)
        self.musteriTable.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.musteriTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.musteriTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.musteriTable.setHorizontalHeaderItem(2, item)
        self.musteriTable.horizontalHeader().setCascadingSectionResizes(False)
        self.musteriTable.horizontalHeader().setSortIndicatorShown(False)
        self.musteriTable.horizontalHeader().setStretchLastSection(True)
        self.musteriTable.verticalHeader().setVisible(True)
        self.musteriTable.verticalHeader().setCascadingSectionResizes(False)
        self.musteriTable.verticalHeader().setSortIndicatorShown(False)
        self.musteriTable.verticalHeader().setStretchLastSection(False)
        self.musteriTable.setSortingEnabled(False)
        self.musteriTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        item = self.musteriTable.horizontalHeaderItem(0)
        item.setText(self._translate("Window", "Id "))
        item = self.musteriTable.horizontalHeaderItem(1)
        item.setText(self._translate("Window", "Ad Soyad"))
        item = self.musteriTable.horizontalHeaderItem(2)
        item.setText(self._translate("Window", "T.C Kimlik No"))
        self.musteriVeriCek()
        self.musteriTable.doubleClicked.connect(self.musteriSec)
class addCustomer(object):
    def initUi(self, Window):
        self.title = "Müşteri Ekle"
        Window.setWindowIcon(QtGui.QIcon(self.iconName))
        Window.setAutoFillBackground(True)
        self._translate = QtCore.QCoreApplication.translate
        Window.setObjectName("Window")
        Window.resize(1100, 600)
        Window.setWindowTitle(self.title)
        Window.setGeometry(self.left, self.top, self.width, self.height)
        Window.setStyleSheet("QMainWindow{" + self.backgroundColor + "}QMenu{background-color:none}")
        mainMenu = Window.menuBar()
        menuBar = mainMenu.addMenu("Geri Dön")
        don = QtWidgets.QAction("Müşteri Listesine Geri Dön", Window)
        menuBar.addAction(don)
        mainMenu.triggered.connect(self.addToList)
        self.adSoyad = QtWidgets.QLineEdit(Window)
        self.adSoyad.setGeometry(QtCore.QRect(510, 180, 133, 31))
        self.adSoyad.setStyleSheet(self.qlinecss)
        self.adSoyad.setObjectName("adSoyad")
        self.baslik = QtWidgets.QLabel(Window)
        self.baslik.setGeometry(QtCore.QRect(300, 90, 554, 37))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        self.baslik.setFont(font)
        self.baslik.setStyleSheet("color:#ffdd00")
        self.baslik.setObjectName("baslik")
        self.baslik.setText(self._translate("Window","<html><head/><body><p><span style=\" font-size:24pt; color:#ffdd00;\">Kütüphane Otomasyonu Müşteri Ekle</span></p></body></html>"))
        self.adSoyadText = QtWidgets.QLabel(Window)
        self.adSoyadText.setGeometry(QtCore.QRect(390, 190, 63, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.adSoyadText.setFont(font)
        self.adSoyadText.setStyleSheet("color:#ffdd00")
        self.adSoyadText.setObjectName("kitapAdiText")
        self.adSoyadText.setText(self._translate("Window","<html><head/><body><p><span style=\" color:#ffdd00;\">Adsoyad</span></p></body></html>"))
        self.tcNo = QtWidgets.QLineEdit(Window)
        self.tcNo.setGeometry(QtCore.QRect(510, 240, 133, 31))
        self.tcNo.setStyleSheet(self.qlinecss)
        self.tcNo.setMaxLength(11)
        self.tcNo.setObjectName("tcNo")
        self.musteriEkle = QtWidgets.QPushButton(Window)
        self.musteriEkle.setGeometry(QtCore.QRect(550, 350, 131, 41))
        self.musteriEkle.setStyleSheet(self.qbuttoncss)
        self.musteriEkle.setObjectName("musteriEkle")
        self.musteriEkle.setText(self._translate("Window", "Müşteri Ekle!"))
        self.musteriEkle.clicked.connect(self.musteriEkleClicked)
        self.labelNoktali = QtWidgets.QLabel(Window)
        self.labelNoktali.setGeometry(QtCore.QRect(490, 250, 4, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        self.labelNoktali.setFont(font)
        self.labelNoktali.setStyleSheet("color:#ffdd00")
        self.labelNoktali.setObjectName("labelNoktali")
        self.labelNoktali.setText(self._translate("Window", "<html><head/><body><p><span style=\" font-size:12pt;\">:</span></p></body></html>"))
        self.labelNoktali2 = QtWidgets.QLabel(Window)
        self.labelNoktali2.setGeometry(QtCore.QRect(490, 190, 4, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(18)
        self.labelNoktali2.setFont(font)
        self.labelNoktali2.setStyleSheet("color:#ffdd00")
        self.labelNoktali2.setObjectName("labelNoktali2")
        self.labelNoktali2.setText(self._translate("Window", "<html><head/><body><p><span style=\" font-size:12pt;\">:</span></p></body></html>"))
        self.kitapYazarText = QtWidgets.QLabel(Window)
        self.kitapYazarText.setGeometry(QtCore.QRect(390, 250, 97, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        self.kitapYazarText.setFont(font)
        self.kitapYazarText.setStyleSheet("color:#ffdd00")
        self.kitapYazarText.setObjectName("kitapAdiText")
        self.kitapYazarText.setText(self._translate("Window","<html><head/><body><p><span style=\" color:#ffdd00;\">TC NO</span></p></body></html>"))
class emanettekikitaplarPage(object):
    def initUi(self, Window):
        self.title = "Emanette Olan Kitaplar"
        Window.setWindowIcon(QtGui.QIcon(self.iconName))
        Window.setWindowTitle(self.title)
        Window.setGeometry(self.left, self.top, self.width, self.height)
        Window.setStyleSheet("QMainWindow{" + self.backgroundColor + "}QMenu{background-color:none}")
        Window.setAutoFillBackground(True)
        self.emanetteSecilenler = []
        self._translate = QtCore.QCoreApplication.translate
        mainMenu = Window.menuBar()
        menuBar = mainMenu.addMenu("Geri Dön")
        don = QtWidgets.QAction("Ana Sayfaya Geri Dön", Window)
        menuBar.addAction(don)
        menuBar.triggered.connect(self.emanetMain)
        self.baslik = QtWidgets.QLabel(Window)
        self.baslik.setGeometry(QtCore.QRect(470, 40, 413, 29))
        self.baslik.setObjectName("baslik")
        self.baslik.setText(self._translate("Window","<html><head/><body><p><span style=\" font-size:18pt; color:#ffdd00;\">Emanetteki Kitaplar</span></p></body></html>"))
        self.emanetSec = QtWidgets.QPushButton(Window)
        self.emanetSec.setGeometry(QtCore.QRect(730, 470, 131, 41))
        self.emanetSec.setStyleSheet(self.qbuttoncss)
        self.emanetSec.setObjectName("emanetSecClicked")
        self.emanetSec.setText(self._translate("Window", "Kitabı Geri Al"))
        self.emanetSec.clicked.connect(self.emanetSecClicked)
        self.emanetTable = QtWidgets.QTableWidget(Window)
        self.emanetTable.setGeometry(QtCore.QRect(250, 90, 661, 361))
        self.emanetTable.setShowGrid(True)
        self.emanetTable.setColumnCount(5)
        self.emanetTable.setObjectName("emanetTable")
        item = QtWidgets.QTableWidgetItem()
        self.emanetTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.emanetTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.emanetTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.emanetTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.emanetTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.emanetTable.setHorizontalHeaderItem(5, item)
        self.emanetTable.horizontalHeader().setCascadingSectionResizes(False)
        self.emanetTable.horizontalHeader().setSortIndicatorShown(False)
        self.emanetTable.horizontalHeader().setStretchLastSection(True)
        self.emanetTable.verticalHeader().setVisible(True)
        self.emanetTable.verticalHeader().setCascadingSectionResizes(False)
        self.emanetTable.verticalHeader().setSortIndicatorShown(False)
        self.emanetTable.verticalHeader().setStretchLastSection(False)
        self.emanetTable.setSortingEnabled(False)
        self.emanetTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        item = self.emanetTable.horizontalHeaderItem(0)
        item.setText(self._translate("Window", "Id "))
        item = self.emanetTable.horizontalHeaderItem(1)
        item.setText(self._translate("Window", "Kullanıcı Adı"))
        item = self.emanetTable.horizontalHeaderItem(2)
        item.setText(self._translate("Window", "Kitap Adı"))
        item = self.emanetTable.horizontalHeaderItem(3)
        item.setText(self._translate("Window", "Veriliş Tarihi"))
        item = self.emanetTable.horizontalHeaderItem(4)
        item.setText(self._translate("Window", "Geri Alınış Tarihi"))
        item = self.emanetTable.horizontalHeaderItem(5)
        self.emanetDataCek()
        self.emanetTable.doubleClicked.connect(self.selectRow)
class oduncKitap(object):
    def initUi(self, Window):
        self.title = "Ödünç Kitap"
        Window.setWindowIcon(QtGui.QIcon(self.iconName))
        Window.setWindowTitle(self.title)
        Window.setGeometry(self.left, self.top, self.width, self.height)
        Window.setStyleSheet("QMainWindow{" + self.backgroundColor + "}QMenu{background-color:none}")
        Window.setAutoFillBackground(True)
        self._translate = QtCore.QCoreApplication.translate
        mainMenu = Window.menuBar()
        menuBar = mainMenu.addMenu("Geri Dön")
        don = QtWidgets.QAction("Ana Sayfaya Geri Dön", Window)
        menuBar.addAction(don)
        menuBar.triggered.connect(self.oduncverMain)
        self.kitapTable = QtWidgets.QTableWidget(Window)
        self.kitapTable.setGeometry(QtCore.QRect(40, 70, 441, 351))
        self.kitapTable.setStyleSheet("background-color:none")
        self.kitapTable.setObjectName("kitapTable")
        self.kitapTable.setColumnCount(4)
        self.kitapTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.kitapTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.kitapTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.kitapTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.kitapTable.setHorizontalHeaderItem(3, item)
        self.kitapTable.horizontalHeader().setCascadingSectionResizes(False)
        self.kitapTable.horizontalHeader().setSortIndicatorShown(False)
        self.kitapTable.horizontalHeader().setStretchLastSection(True)
        self.kitapTable.verticalHeader().setVisible(True)
        self.kitapTable.verticalHeader().setCascadingSectionResizes(False)
        self.kitapTable.verticalHeader().setSortIndicatorShown(False)
        self.kitapTable.verticalHeader().setStretchLastSection(False)
        self.kitapTable.setSortingEnabled(False)
        self.kitapTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        item = self.kitapTable.horizontalHeaderItem(0)
        item.setText(self._translate("Window","Id"))
        item = self.kitapTable.horizontalHeaderItem(1)
        item.setText(self._translate("Window", "Kitabın Adı"))
        item = self.kitapTable.horizontalHeaderItem(2)
        item.setText(self._translate("Window", "Kitabın Yazarı"))
        item = self.kitapTable.horizontalHeaderItem(3)
        item.setText(self._translate("Window", "Kitabın Sayfası"))
        self.musteriTableOdunc = QtWidgets.QTableWidget(Window)
        self.musteriTableOdunc.setGeometry(QtCore.QRect(620, 70, 441, 351))
        self.musteriTableOdunc.setStyleSheet("background-color:none")
        self.musteriTableOdunc.setObjectName("musteriTableOdunc")
        self.musteriTableOdunc.setColumnCount(3)
        self.musteriTableOdunc.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.musteriTableOdunc.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.musteriTableOdunc.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.musteriTableOdunc.setHorizontalHeaderItem(2, item)
        self.musteriTableOdunc.horizontalHeader().setCascadingSectionResizes(False)
        self.musteriTableOdunc.horizontalHeader().setSortIndicatorShown(False)
        self.musteriTableOdunc.horizontalHeader().setStretchLastSection(True)
        self.musteriTableOdunc.verticalHeader().setVisible(True)
        self.musteriTableOdunc.verticalHeader().setCascadingSectionResizes(False)
        self.musteriTableOdunc.verticalHeader().setSortIndicatorShown(False)
        self.musteriTableOdunc.verticalHeader().setStretchLastSection(False)
        self.musteriTableOdunc.setSortingEnabled(False)
        self.musteriTableOdunc.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        item = self.musteriTableOdunc.horizontalHeaderItem(0)
        item.setText(self._translate("Window", "Id"))
        item = self.musteriTableOdunc.horizontalHeaderItem(1)
        item.setText(self._translate("Window", "Ad Soyad"))
        item = self.musteriTableOdunc.horizontalHeaderItem(2)
        item.setText(self._translate("Window", "T.C Kimlik No"))
        self.labelVerilme = QtWidgets.QLabel(Window)
        self.labelVerilme.setGeometry(QtCore.QRect(310, 450, 168, 22))
        self.labelVerilme.setStyleSheet("font-size:18px; color:#ffdd00;")
        self.labelVerilme.setObjectName("labelVerilme")
        self.tarihVerilme = QtWidgets.QDateTimeEdit(Window)
        self.tarihVerilme.setGeometry(QtCore.QRect(550, 450, 194, 22))
        self.tarihVerilme.setStyleSheet("background-color:none")
        self.tarihVerilme.setObjectName("tarihVerilme")
        self.tarihVerilme.setDisplayFormat('dd/MM/yyyy')
        self.today = datetime.date.today()
        self.yesterday = self.today + datetime.timedelta(days=1)
        self.tarihVerilme.setMinimumDate(self.today)
        self.tarihVerilme.setCalendarPopup(True)
        self.labelAlinma = QtWidgets.QLabel(Window)
        self.labelAlinma.setGeometry(QtCore.QRect(310, 510, 175, 22))
        self.labelAlinma.setStyleSheet("font-size:18px; color:#ffdd00;")
        self.labelAlinma.setObjectName("labelAlinma")
        self.tarihAlinma = QtWidgets.QDateTimeEdit(Window)
        self.tarihAlinma.setGeometry(QtCore.QRect(550, 510, 194, 22))
        self.tarihAlinma.setStyleSheet("background-color:none")
        self.tarihAlinma.setObjectName("tarihAlinma")
        self.tarihAlinma.setDisplayFormat('dd/MM/yyyy')
        self.tarihAlinma.setMinimumDate(self.yesterday)
        self.tarihAlinma.setCalendarPopup(True)
        self.onayla = QtWidgets.QPushButton(Window)
        self.onayla.setGeometry(QtCore.QRect(830, 470, 131, 41))
        self.onayla.setStyleSheet(self.qbuttoncss)
        self.onayla.setObjectName("onayla")
        self.labelVerilme.setText(self._translate("Window", "Kitabın Verildiği Tarih"))
        self.labelAlinma.setText(self._translate("Window", "Kitabın Alınacağı Tarih"))
        self.onayla.setText(self._translate("Window", "Tamamla"))
        self.dataCek()
        self.kitapTable.doubleClicked.connect(self.kitapDoubleClicked)
        self.musteriTableOdunc.doubleClicked.connect(self.musteriDoubleClicked)
        self.onayla.clicked.connect(self.buttonClicked)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QMainWindow()
    ui = loginPage()
    ui.initUi(Window)
    Window.show()
    sys.exit(app.exec_())