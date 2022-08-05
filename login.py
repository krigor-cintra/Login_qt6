# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets

from Login_qt6.bancodedados import login, login_creat


class Ui_Login(object):


    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(463, 216)
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")
        self.email = QtWidgets.QLineEdit(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(60, 50, 331, 22))
        self.email.setObjectName("email")
        self.senha = QtWidgets.QLineEdit(self.centralwidget)
        self.senha.setGeometry(QtCore.QRect(60, 80, 131, 22))
        self.senha.setEchoMode(QtWidgets.QLineEdit.EchoMode.PasswordEchoOnEdit)
        self.senha.setObjectName("senha")
        self.tx_email = QtWidgets.QLabel(self.centralwidget)
        self.tx_email.setGeometry(QtCore.QRect(10, 50, 49, 16))
        self.tx_email.setObjectName("tx_email")
        self.tx_senha = QtWidgets.QLabel(self.centralwidget)
        self.tx_senha.setGeometry(QtCore.QRect(10, 80, 49, 16))
        self.tx_senha.setObjectName("tx_senha")
        self.login = QtWidgets.QPushButton(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(260, 120, 75, 24))
        self.login.setObjectName("login")
        self.login.clicked.connect(self.botao_login)

        self.Creat = QtWidgets.QPushButton(self.centralwidget)
        self.Creat.setGeometry(QtCore.QRect(180, 120, 75, 24))
        self.Creat.setObjectName("Creat")
        Login.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Login)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 463, 22))
        self.menubar.setObjectName("menubar")
        Login.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Login)
        self.statusbar.setObjectName("statusbar")
        Login.setStatusBar(self.statusbar)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "MainWindow"))
        self.tx_email.setText(_translate("Login", "E-mail"))
        self.tx_senha.setText(_translate("Login", "Senha"))
        self.login.setText(_translate("Login", "Login"))
        self.Creat.setText(_translate("Login", "Criar Conta"))

    def botao_login(self):
        email=(self.email.text())
        senha=(self.senha.text())
        login_creat(email,senha)
    def botao_criar(self):
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec())
