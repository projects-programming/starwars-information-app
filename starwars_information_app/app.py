import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QLabel,
    QMainWindow,
    QPushButton,
    QGridLayout,
    QWidget,
)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Star Wars Information App")
        self.resize(640, 480)
        layout = QGridLayout()
        self.setStyleSheet("background-color: #3399FF;")
        # create the home screen

        # title label
        title_label = QLabel("Star Wars Information")
        font = title_label.font()
        font.setPointSize(24)
        title_label.setFont(font)
        title_label.setStyleSheet("QLabel {color : #DDE6ED; font: bold 32px;}");

        # people label
        people_label = QLabel("People")
        font = people_label.font()
        font.setPointSize(18)
        people_label.setFont(font)
        people_label.setStyleSheet("QLabel {color : #DDE6ED; font: bold 24px;}");

        # people combobox
        people_combo = QComboBox()
        people_combo.addItems(["Luke Skywalker", "Obi-Wan Kenobi", "Darth Vader"])

        # starship label
        starship_label = QLabel("Starships")
        font = starship_label.font()
        font.setPointSize(18)
        starship_label.setFont(font)
        starship_label.setStyleSheet("QLabel {color : #DDE6ED; font: bold 24px;}");

        # starship combobox
        starship_combo = QComboBox()
        starship_combo.addItems(["Millennium Falcon", "Death Star", "B-wing"])

        # planet label
        planet_label = QLabel("Planets")
        font = planet_label.font()
        font.setPointSize(18)
        planet_label.setFont(font)
        planet_label.setStyleSheet("QLabel {color : #DDE6ED; font: bold 24px;}");

        # planet combobox
        planet_combo = QComboBox()
        planet_combo.addItems(["Dagobah", "Utapau", "Coruscant"])

        # setting the layout
        widget = QWidget()
        widget.setLayout(layout)

        # Add layout
        layout.addWidget(title_label, 0, 1, Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(people_label, 1, 0, Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(starship_label, 1, 1, Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(planet_label, 1, 2, Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(people_combo, 2, 0, Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(starship_combo, 2, 1, Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(planet_combo, 2, 2, Qt.AlignmentFlag.AlignHCenter)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
