# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys
from PySide6 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.authors = QtWidgets.QLabel("Estudiantes Andres Felipe Mendez, Jeisson Steward Comba Ortega y Juan David Cárdenas Mesa")

        self.nameLabel = QtWidgets.QLabel("Ingresar su nombre")
        self.nameInput = QtWidgets.QLineEdit("")
        self.ageLabel = QtWidgets.QLabel("Ingresar su edad")
        self.ageInput = QtWidgets.QLineEdit("")
        self.text = QtWidgets.QLabel("")
        self.layout = QtWidgets.QVBoxLayout(self)


        self.layout.addWidget(self.nameLabel)
        self.layout.addWidget(self.nameInput)
        self.layout.addWidget(self.ageLabel)
        self.layout.addWidget(self.ageInput)
        self.ageInput.editingFinished.connect(self.checkAge)

    @QtCore.Slot()
    def checkAge(self):
        age = int(self.ageInput.displayText())
        if 18 < age < 70:
            self.addSecondQuestion()
        else:
            self.cantVoteLabel()

    def addSecondQuestion(self):
        self.idInscriptionLabel = QtWidgets.QLabel("inscribio su cedula?")
        self.layout.addWidget(self.idInscriptionLabel)
        self.yesButton = QtWidgets.QRadioButton("si", self)
        self.noButton = QtWidgets.QRadioButton("no", self)
        self.layout.addWidget(self.yesButton)
        self.layout.addWidget(self.noButton)
        self.noButton.clicked.connect(self.cantVote)
        self.yesButton.clicked.connect(self.canVote)

    @QtCore.Slot()
    def cantVote(self):
        self.cantVoteLabel()

    @QtCore.Slot()
    def canVote(self):
        self.greenCheck = QtGui.QImage("checkmark.png")
        self.imageLabel = QtWidgets.QLabel("image")
        self.imageLabel.setPixmap(QtGui.QPixmap(self.greenCheck).scaled(64, 64, QtCore.Qt.KeepAspectRatio))
        self.layout.addWidget(self.imageLabel, QtCore.Qt.AlignHCenter)
        self.layout.addWidget(self.text,QtCore.Qt.AlignHCenter)
        self.text.setText("puede votar")
        self.layout.addWidget(self.authors)

    def cantVoteLabel(self):
        self.greenCheck = QtGui.QImage("xmark.png")
        self.imageLabel = QtWidgets.QLabel("image")
        self.imageLabel.setPixmap(QtGui.QPixmap(self.greenCheck).scaled(64, 64, QtCore.Qt.KeepAspectRatio))
        self.layout.addWidget(self.imageLabel, QtCore.Qt.AlignHCenter)
        self.layout.addWidget(self.text, QtCore.Qt.AlignHCenter)
        self.text.setText("no puede votar")
        self.layout.addWidget(self.authors)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 300)
    widget.show()

    sys.exit(app.exec())
