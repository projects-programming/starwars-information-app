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

        # title label
        title_label = QLabel("Star Wars Information")
        font = title_label.font()
        font.setPointSize(24)
        title_label.setFont(font)
        title_label.setStyleSheet("QLabel {color : #DDE6ED; }");

        # people label
        people_label = QLabel("People")
        font = people_label.font()
        font.setPointSize(18)
        people_label.setFont(font)
        people_label.setStyleSheet("QLabel {color : #DDE6ED; }");

        # people combobox
        

        # starship label
        starship_label = QLabel("Starships")
        font = starship_label.font()
        font.setPointSize(18)
        starship_label.setFont(font)
        starship_label.setStyleSheet("QLabel {color : #DDE6ED; }");

        # planet label
        planet_label = QLabel("Planets")
        font = planet_label.font()
        font.setPointSize(18)
        planet_label.setFont(font)
        planet_label.setStyleSheet("QLabel {color : #DDE6ED; }");


        widget = QWidget()
        widget.setLayout(layout)

        # Add layout
        layout.addWidget(title_label, 0, 1, Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(people_label, 1, 0, Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(starship_label, 1, 1, Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(planet_label, 1, 2, Qt.AlignmentFlag.AlignHCenter)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
