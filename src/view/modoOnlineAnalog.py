
from PyQt4 import QtGui
from PyQt4.QtGui import QCheckBox
from PyQt4.QtGui import QGridLayout
from PyQt4.QtGui import QLabel
from PyQt4.QtGui import QLineEdit


class AnalogInputView(QtGui.QFrame):

    _nombreInput = ""
    mainLayout = None

    def __init__(self, nombre, parent=None):

        self._nombreInput = nombre
        super(AnalogInputView, self).__init__(parent)
        self.setObjectName("AnalogInputView")
        self.setStyleSheet(
            "#AnalogInputView {border:1px solid rgb(0, 0, 0); }")
        self.initUI()

    def initUI(self):
        self.mainLayout = QGridLayout()

        nombreInputLbl = QLabel(self._nombreInput)

        self.calibrarChk = QCheckBox("Calibrar")
        self.activadoChk = QCheckBox("Activar")

        self.activadoChk.setChecked(False)
        self.activadoChk.stateChanged.connect(self.activarChanged)

        self.calibrarChk.setChecked(False)
        self.calibrarChk.stateChanged.connect(self.calibrarChanged)

        self.nombreTxt = QLineEdit()
        self.unidadTxt = QLineEdit()
        self.pendienteTxt = QLineEdit()
        self.ordenadaTxt = QLineEdit()

        self.nombreTxt.setEnabled(False)
        self.unidadTxt.setEnabled(False)
        self.pendienteTxt.setEnabled(False)
        self.ordenadaTxt.setEnabled(False)

        self.mainLayout.addWidget(nombreInputLbl, 0, 0)
        self.mainLayout.addWidget(self.activadoChk, 0, 1)
        self.mainLayout.addWidget(self.calibrarChk, 0, 2)

        self.mainLayout.addWidget(QLabel("Nombre: "), 1, 0)
        self.mainLayout.addWidget(QLabel("Unidad: "), 2, 0)

        self.mainLayout.addWidget(self.nombreTxt, 1, 1)
        self.mainLayout.addWidget(self.unidadTxt, 2, 1)

        self.mainLayout.addWidget(QLabel("Pendiente: "), 1, 2)
        self.mainLayout.addWidget(QLabel("Ordenada: "), 2, 2)
        self.mainLayout.addWidget(self.pendienteTxt, 1, 3)
        self.mainLayout.addWidget(self.ordenadaTxt, 2, 3)

        self.setLayout(self.mainLayout)

    def calibrarChanged(self):
        if(self.calibrarChk.isChecked()):
            self.ordenadaTxt.setEnabled(True)
            self.pendienteTxt.setEnabled(True)
        else:
            self.ordenadaTxt.setEnabled(False)
            self.pendienteTxt.setEnabled(False)

    def activarChanged(self):
        if(self.activadoChk.isChecked()):
            self.nombreTxt.setEnabled(True)
            self.unidadTxt.setEnabled(True)
        else:
            self.nombreTxt.setEnabled(False)
            self.unidadTxt.setEnabled(False)

    def isActivated(self):
        return self.activadoChk.isChecked()

    def getSetUp(self):
        if(self.calibrarChk.isChecked()):
            pend = float(self.pendienteTxt.text())
            orde = float(self.ordenadaTxt.text())
        else:
            pend = 1
            orde = 0

        unidad = self.unidadTxt.text()
        nombre = self.nombreTxt.text()

        return (pend, orde, unidad, nombre)


class ModoOnlineAnalog(QtGui.QWidget):

    _mainLayout = None

    def __init__(self):
        super(ModoOnlineAnalog, self).__init__()

        self.init_gui()

    def init_gui(self):
        self._mainLayout = QGridLayout()

        self.miniForms = [AnalogInputView("Input 1"),
                          AnalogInputView("Input 2"),
                          AnalogInputView("Input 3"),
                          AnalogInputView("Input 4"),
                          AnalogInputView("Input 5"),
                          AnalogInputView("Input 6"),
                          AnalogInputView("Input 7"),
                          AnalogInputView("Input 8")]

        self._mainLayout.addWidget(self.miniForms[0], 0, 0)
        self._mainLayout.addWidget(self.miniForms[1], 0, 1)
        self._mainLayout.addWidget(self.miniForms[2], 1, 0)
        self._mainLayout.addWidget(self.miniForms[3], 1, 1)
        self._mainLayout.addWidget(self.miniForms[4], 2, 0)
        self._mainLayout.addWidget(self.miniForms[5], 2, 1)
        self._mainLayout.addWidget(self.miniForms[6], 3, 0)
        self._mainLayout.addWidget(self.miniForms[7], 3, 1)

        self.setLayout(self._mainLayout)

    def getGraficosSetUp(self):

        toRet = []

        for miniForm in self.miniForms:
            if miniForm.isActivated():
                toRet.append(miniForm.getSetUp())

        return toRet
