from PyQt5 import QtWidgets,QtGui
from fatorial import Ui_Fatorial

class FatorialWindow(QtWidgets.QMainWindow,Ui_Fatorial):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        
        self.setWindowIcon(QtGui.QIcon('symbol.png'))
        self.Confirmar.clicked.connect(self.exibir)
        #self.resultado.setText('Resultado' + resp)

    def exibir(self):
        valor = self.spinBox.value()
        #resp = self.resultado.text()
        c = valor
        count = 1
        if valor == 0:
            self.resultado.setText(str(1))
        else:
            while count<valor:
                c = c*count
                count = count + 1
            self.resultado.setText(str(c))

    

        
    