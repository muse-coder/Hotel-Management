# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ForgetPwd.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("\n"
"*{\n"
"font-size:24px;\n"
"font-family:Century Gothic;\n"
"}\n"
"QFrame{\n"
"background:rgba(0,0,0,0.8);\n"
"border-radius:15px;\n"
"}\n"
"#centralwidget{\n"
"border-image:url(../pictures/login3.jpg) strectch；\n"
"}\n"
"\n"
"QToolButton{\n"
"background:red;\n"
"border-radius:60px;\n"
"}\n"
"QLabel{\n"
"color:white;\n"
"background:transparent;\n"
"}\n"
"QPushButton{\n"
"background:red;;\n"
"border-radius:15px;\n"
"}\n"
"QPushButton:hover{\n"
"background:#333;\n"
"border-radius:15px;\n"
"background:#49ebff;\n"
"}\n"
"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"color:#717072;\n"
"border-bottom:1px solid #717072;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(160, 70, 491, 511))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.frame.setFont(font)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(180, 70, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_idcard = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_idcard.setGeometry(QtCore.QRect(70, 160, 361, 31))
        self.lineEdit_idcard.setText("")
        self.lineEdit_idcard.setObjectName("lineEdit_idcard")
        self.lineEdit_id = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_id.setGeometry(QtCore.QRect(70, 260, 361, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(-1)
        self.lineEdit_id.setFont(font)
        self.lineEdit_id.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit_id.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.lineEdit_id.setText("")
        self.lineEdit_id.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_id.setObjectName("lineEdit_id")
        self.commitButton = QtWidgets.QPushButton(self.frame)
        self.commitButton.setGeometry(QtCore.QRect(40, 430, 421, 51))
        self.commitButton.setObjectName("commitButton")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(70, 120, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(-1)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(70, 220, 121, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(70, 320, 121, 31))
        self.label_4.setObjectName("label_4")
        self.lineEdit_newpwd = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_newpwd.setGeometry(QtCore.QRect(70, 360, 361, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(-1)
        self.lineEdit_newpwd.setFont(font)
        self.lineEdit_newpwd.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lineEdit_newpwd.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.lineEdit_newpwd.setText("")
        self.lineEdit_newpwd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_newpwd.setObjectName("lineEdit_newpwd")
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton.setGeometry(QtCore.QRect(360, 10, 121, 121))
        self.toolButton.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.toolButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../pictures/login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(150, 150))
        self.toolButton.setObjectName("toolButton")
        self.retLogin = QtWidgets.QToolButton(self.centralwidget)
        self.retLogin.setGeometry(QtCore.QRect(660, 520, 141, 81))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(-1)
        self.retLogin.setFont(font)
#         self.retLogin.setStyleSheet("border:none;\n"
# "background:none\n"
# "")
        self.retLogin.setStyleSheet("background:none;color:white;border:none;font-size:30px;font-weight:bold;")
        self.retLogin.setObjectName("retLogin")
        # self.label_5 = QtWidgets.QLabel(self.centralwidget)
        # self.label_5.setGeometry(QtCore.QRect(670, 560, 131, 31))
        # self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        # MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setWindowTitle("小福酒店管理系统")
        self.label.setText(_translate("MainWindow", "LOGIN HERE"))
        self.lineEdit_idcard.setPlaceholderText(_translate("MainWindow", "id card"))
        self.lineEdit_id.setPlaceholderText(_translate("MainWindow", "staff id"))
        self.commitButton.setText(_translate("MainWindow", "尝试找回"))
        self.label_2.setText(_translate("MainWindow", "身份证号"))
        self.label_3.setText(_translate("MainWindow", "员工号"))
        self.label_4.setText(_translate("MainWindow", "新密码"))
        self.lineEdit_newpwd.setPlaceholderText(_translate("MainWindow", "new password"))
        self.retLogin.setText(_translate("MainWindow", "返回登录"))
        # self.label_5.setText(_translate("MainWindow", "返回登录"))
