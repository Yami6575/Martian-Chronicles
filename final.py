from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import urllib
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders
import smtplib, ssl


class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(998, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.page)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_7 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_4 = QtWidgets.QLabel(self.frame_7)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 711, 291))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("defalt.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame_3)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 191))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.fetching)
        self.horizontalLayout_4.addWidget(self.pushButton_3)
        self.frame_15 = QtWidgets.QFrame(self.frame_8)
        self.frame_15.setMinimumSize(QtCore.QSize(100, 0))
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_15)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_15)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.backword)
        self.verticalLayout_6.addWidget(self.pushButton_7)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_15)
        self.pushButton_6.setMinimumSize(QtCore.QSize(20, 0))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.forword)
        self.verticalLayout_6.addWidget(self.pushButton_6)
        self.horizontalLayout_4.addWidget(self.frame_15)
        self.horizontalLayout_3.addWidget(self.frame_8, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.page)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setMinimumSize(QtCore.QSize(160, 0))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_6)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_2, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.frame_6)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.frame_6, 0, QtCore.Qt.AlignLeft)
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.frame_5)
        self.calendarWidget.setObjectName("calendarWidget")
        self.gridLayout_3.addWidget(self.calendarWidget, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.frame_5)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_9 = QtWidgets.QFrame(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_11 = QtWidgets.QFrame(self.frame_9)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_14 = QtWidgets.QFrame(self.frame_11)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_3 = QtWidgets.QLabel(self.frame_14)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_8.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_14)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.subject=self.lineEdit_3.text()
        self.horizontalLayout_8.addWidget(self.lineEdit_3)
        self.verticalLayout_5.addWidget(self.frame_14)
        self.frame_12 = QtWidgets.QFrame(self.frame_11)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label = QtWidgets.QLabel(self.frame_12)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_12)
        self.lineEdit_2.setObjectName("lineEdit_2")


        self.horizontalLayout_6.addWidget(self.lineEdit_2)

        self.verticalLayout_5.addWidget(self.frame_12)
        self.frame_13 = QtWidgets.QFrame(self.frame_11)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_2 = QtWidgets.QLabel(self.frame_13)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_7.addWidget(self.label_2)
        self.textEdit = QtWidgets.QTextEdit(self.frame_13)
        self.textEdit.setObjectName("textEdit")
        self.body=self.textEdit.toPlainText()
        self.horizontalLayout_7.addWidget(self.textEdit)
        self.verticalLayout_5.addWidget(self.frame_13)
        self.verticalLayout_4.addWidget(self.frame_11)
        self.verticalLayout_3.addWidget(self.frame_9)
        self.frame_10 = QtWidgets.QFrame(self.page_2)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 60))
        self.pushButton_4.setText("Attach")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.attach)
        self.horizontalLayout_5.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_5.setMinimumSize(QtCore.QSize(0, 60))
        self.pushButton_5.setText("Send Mail")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.send_email)
        self.horizontalLayout_5.addWidget(self.pushButton_5)
        self.verticalLayout_3.addWidget(self.frame_10, 0, QtCore.Qt.AlignBottom)
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout.addWidget(self.stackedWidget, 1, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.count=0
        self.index=0

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_3.setText(_translate("MainWindow", "Fetch"))
        self.pushButton_7.setText(_translate("MainWindow", "<"))
        self.pushButton_6.setText(_translate("MainWindow", ">"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Select Rover"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "CURIOSITY"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "SPIRIT"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "OPPERTUNITY"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Select camera"))
        self.comboBox.setItemText(1, _translate("MainWindow", "FHAZ"))
        self.comboBox.setItemText(2, _translate("MainWindow", "RHAZ"))
        self.comboBox.setItemText(3, _translate("MainWindow", "NAVCAM"))
        self.comboBox.setItemText(4, _translate("MainWindow", "PANCAM"))
        self.label_3.setText(_translate("MainWindow", "Subject"))
        self.label.setText(_translate("MainWindow", "Send To"))
        self.label_2.setText(_translate("MainWindow", "Body"))
        self.pushButton.setText(_translate("MainWindow", "Fetch Images"))
        self.pushButton.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.page))
        self.pushButton_2.setText(_translate("MainWindow", "Mail"))
        self.pushButton_2.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.page_2))
    def fetching(self):
        input1=self.comboBox.currentText()
        input2=self.comboBox_2.currentText()
        input3=self.calendarWidget.selectedDate().toPyDate()
        r = requests.get(f"https://api.nasa.gov/mars-photos/api/v1/rovers/{input2}/photos?camera={input1}&earth_date={input3}&api_key=5SmFOsZLd2pZod4q3aaBn0s0mGQg88B8iTG9y5WV")
        print(f"https://api.nasa.gov/mars-photos/api/v1/{input2}/photos?camera={input1}&earth_date={input3}&api_key=5SmFOsZLd2pZod4q3aaBn0s0mGQg88B8iTG9y5WV")
        req = r.json()
        print(req)
        self.count=0
        for i in req['photos']:
            self.count += 1 
            urllib.request.urlretrieve(f"{i['img_src']}",f"ph{self.count}.jpg")
            print("fetching data",self.count)
        
    def loadimages(self):
        self.label_4.setPixmap(QtGui.QPixmap(f"ph{self.index}"))
    

    def forword(self):
        if self.index<self.count:
            self.index+=1

            print(self.index)
            self.label_4.setPixmap(QtGui.QPixmap(f'ph{self.index}'))
        else:
            self.index = 0
            self.index+=1

            print(self.index)
            self.label_4.setPixmap(QtGui.QPixmap(f'ph{self.index}'))


            

    def backword(self):
        if self.index>1:
            self.index-=1
            print(self.index)
            self.label_4.setPixmap(QtGui.QPixmap(f'ph{self.index}'))
        else:
            self.index = self.count
            print(self.index)
            self.label_4.setPixmap(QtGui.QPixmap(f'ph{self.index}'))
            #self.label_6.setPixmap(QtGui.QPixmap(f'ph{self.index}'))

    def send_email(self):

      
        self.sendto=self.lineEdit_2.text()
        msg = MIMEMultipart()
        msg['From'] = "itachi.mishra69@gmail.com"
        msg['To'] = self.sendto
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = self.subject
 
        msg.attach(MIMEText(self.textEdit.toPlainText()))


        for i in self.filenames:
            part = MIMEBase('application', "octet-stream")
            part.set_payload(open(i, "rb").read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment', filename=i)
            msg.attach(part)

        smtp_server = "smtp.gmail.com"
        port = 587
        

        context = ssl.create_default_context()


        try:
            server = smtplib.SMTP(smtp_server,port)
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login("itachi.mishra69@gmail.com", "igpehlcudslsqwwb")
            print(msg['From'], msg["To"])

            server.sendmail(msg['From'], msg["To"], msg.as_string())
            print(msg['From'], msg["To"])
            server.close()
            QMessageBox.information(self, "Information", "Email sent Whooo!!.")
        except Exception as e:
            print(e)
    def attach(self):
        options = QFileDialog.Options()
        self.filenames,_ =QFileDialog.getOpenFileNames(self,"Open images","","Images (*.jpg)",options=options)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())