import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

class exProQT(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("example.ui", self)
        self.btnDesactivar.setEnabled(False)
        self.btnActivar.clicked.connect(self.fn_activar)
        self.btnDesactivar.clicked.connect(self.fn_desactivar)

    def fn_activar(self):
        self.btnDesactivar.setEnabled(True)
        self.btnActivar.setEnabled(False)
        self.lblActivacion.setText("Activado")

    def fn_desactivar(self):
        self.btnDesactivar.setEnabled(False)
        self.btnActivar.setEnabled(True)
        self.lblActivacion.setText("Desactivado")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = exProQT()
    GUI.show()
    sys.exit(app.exec_())