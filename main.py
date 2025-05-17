import sys

from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QDialog, QApplication, QListWidget

from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.dodajButton.clicked.connect(self.dodaj)

        self.show()

    def dodaj(self):
        nazwa_napoju = self.ui.nazwaEdit.text()
        objetosc_napoju = int(self.ui.objetoscBox.text())
        self.ui.listaWidget.addItem(f"{nazwa_napoju} - {objetosc_napoju} ml")

        cala_objetosc = int(self.ui.objetoscWypitychEdit.text())
        cala_objetosc += objetosc_napoju
        self.ui.objetoscWypitychEdit.setText(str(cala_objetosc))

        kobieta = self.ui.kobietaButton.isChecked()
        mezczyzna = self.ui.mezczyznaButton.isChecked()
        mala_akywnosc = self.ui.malaAButton.isChecked()
        srednia_akywnosc = self.ui.sredniaAButton.isChecked()
        duza_akywnosc = self.ui.duzaAButton.isChecked()

        zapotrzebowanie = 0
        if kobieta:
            if mala_akywnosc:
                zapotrzebowanie = 2000
            elif srednia_akywnosc:
                zapotrzebowanie = 2300
            elif duza_akywnosc:
                zapotrzebowanie = 2600

        if mezczyzna:
            if mala_akywnosc:
                zapotrzebowanie = 2500
            elif srednia_akywnosc:
                zapotrzebowanie = 2800
            elif duza_akywnosc:
                zapotrzebowanie = 3000

        procent = cala_objetosc/zapotrzebowanie
        if procent < 0.8:
            self.ui.napisLabel.setStyleSheet("background-color: black;")
            self.ui.zdjecie.setPixmap(QPixmap("1.jpg"))
        if procent > 0.8 < 1:
            self.ui.napisLabel.setStyleSheet("background-color: red;")
            self.ui.zdjecie.setPixmap(QPixmap("2.jpg"))
        if procent > 1:
            self.ui.zdjecie.setPixmap(QPixmap("3.jpg"))
            self.ui.napisLabel.setStyleSheet("background-color: green;")



if __name__ == "__main__":
    app =  QApplication(sys.argv)
    window = MyForm()
    sys.exit(app.exec())