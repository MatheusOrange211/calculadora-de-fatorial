import sys
from PyQt5.QtWidgets import QApplication
from calc import FatorialWindow


app = QApplication(sys.argv)

fatorial = FatorialWindow()
sys.exit(app.exec_())