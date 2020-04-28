
from PyQt5 import QtCore, QtGui, QtWidgets
import ctypes


class Ui_Fatorial(object):
    def setupUi(self, MainWindow):

        #MainWindow.setWindowTitle("Fatorial Calculator")
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(338, 347)
        MainWindow.setStyleSheet("background-color: rgb(102, 102, 102);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 10, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 216, 115);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.Confirmar = QtWidgets.QPushButton(self.centralwidget)
        self.Confirmar.setGeometry(QtCore.QRect(100, 270, 141, 31))
        self.Confirmar.setStyleSheet("background-color: rgb(255, 216, 115);\n")
        #impede que eu altere o tamanho da caixa
        self.setFixedSize(self.size())

        self.Confirmar.setObjectName("Confirmar")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setEnabled(False)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(60, 150, 221, 41))
        self.spinBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.spinBox.setObjectName("spinBox")

        self.resultado = QtWidgets.QLineEdit(self.centralwidget)
        self.resultado.setEnabled(True)
        self.resultado.setGeometry(QtCore.QRect(60, 209, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.resultado.setFont(font)
        #self.resultado.setMouseTracking(False)
        self.resultado.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(102, 102, 102);\n"
"border-color: rgb(102, 102, 102);")
        #self.resultado.setDragEnabled(True)
        self.resultado.setObjectName("resultado")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 338, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Fatorial Calculator", "Fatorial Calculator"))
        #adicionar icone na janela
        #Icons made by <a href="https://www.flaticon.com/authors/roundicons" title="Roundicons">Roundicons</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
        #self.setWindowIcon(QtGui.QIcon('symbol.png'))
        self.setWindowIcon(QtGui.QIcon('symboltaskbar.png'))
        

        
        self.label.setText(_translate("MainWindow", "FATORIAL\n"
"CALCULATOR"))
        self.Confirmar.setText(_translate("MainWindow", "Calcular"))
        self.label_2.setText(_translate("MainWindow", "Fatorial é o produto do números inteiros positivos consecutivos de\n"
"um número natural n, menores ou iguais a n.\n"
"A notação do fatorial de um número n é: n!."))
        #comando para desativar a função de maximizar a tela
        MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

#Definindo o icone na barra de tarefas no Windows 7
myappid = 'mycompany.myproduct.subproduct.version' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
