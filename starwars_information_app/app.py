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
    QStackedLayout,
    QVBoxLayout,
    QHBoxLayout,
    QTextEdit,
)
import controller

# Subclass QMainWindow to customize your application's main window
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Star Wars Information App")
        self.resize(640, 480)
        self.setStyleSheet("background-color: #3399FF;")

        self.layout = QVBoxLayout()

        # add nav buttons to the layout
        nav_layout = QHBoxLayout()
        self.home_button = QPushButton("Home")
        self.home_button.clicked.connect(self.home_page)
        self.luke_button = QPushButton("Luke Skywalker")
        self.luke_button.clicked.connect(self.people_luke)
        self.vader_button = QPushButton("Darth Vader")
        self.vader_button.clicked.connect(self.people_vader)
        self.kenobi_button = QPushButton("Obi-Wan Kenobi")
        self.kenobi_button.clicked.connect(self.people_kenobi)
        self.falcon_button = QPushButton("Millennium Falcon")
        self.falcon_button.clicked.connect(self.starship_falcon)
        self.bwing_button = QPushButton("B-Wing")
        self.bwing_button.clicked.connect(self.starship_bwing)
        self.death_button = QPushButton("Death Star")
        self.death_button.clicked.connect(self.starship_death)

        # add nav buttons to the layout
        nav_layout.addWidget(self.home_button)
        nav_layout.addWidget(self.luke_button)
        nav_layout.addWidget(self.vader_button)
        nav_layout.addWidget(self.kenobi_button)
        nav_layout.addWidget(self.falcon_button)
        nav_layout.addWidget(self.bwing_button)
        nav_layout.addWidget(self.death_button)


        # Create the stacked layout
        self.stacked_layout = QStackedLayout()

        # Create the home screen
        self.home_screen = QWidget()
        self.home_layout = QGridLayout()

        # Home screen widgets

        # title label
        self.title_label = QLabel("Star Wars Information")
        font = self.title_label.font()
        font.setPointSize(24)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("QLabel {color : #DDE6ED; font: bold 32px;}");

        # people label
        self.people_label = QLabel("People")
        font = self.people_label.font()
        font.setPointSize(18)
        self.people_label.setFont(font)
        self.people_label.setStyleSheet("QLabel {color : #DDE6ED; font: bold 24px;}");

        # starship label
        self.starship_label = QLabel("Starships")
        font = self.starship_label.font()
        font.setPointSize(18)
        self.starship_label.setFont(font)
        self.starship_label.setStyleSheet("QLabel {color : #DDE6ED; font: bold 24px;}");

        # planet label
        self.planet_label = QLabel("Planets")
        font = self.planet_label.font()
        font.setPointSize(18)
        self.planet_label.setFont(font)
        self.planet_label.setStyleSheet("QLabel {color : #DDE6ED; font: bold 24px;}");

        # Add home layout and widgets to stacked layout
        self.home_layout.addWidget(self.title_label)
        self.home_layout.addWidget(self.people_label)
        self.home_layout.addWidget(self.starship_label)
        self.home_layout.addWidget(self.planet_label)
        self.home_screen.setLayout(self.home_layout)
        self.stacked_layout.addWidget(self.home_screen)

        # People pages for star wars information

        # Create Luke Skywalker page
        self.luke_screen = QWidget()
        self.luke_layout = QGridLayout()
        self.luke_label = QLabel("Information on Luke Skywalker:")
        self.luke_result_text = QTextEdit()

        # Add Luke page layout and widgets to stacked layout
        self.luke_layout.addWidget(self.luke_label)
        self.luke_screen.setLayout(self.luke_layout)
        self.luke_layout.addWidget(self.luke_result_text)
        self.stacked_layout.addWidget(self.luke_screen)

        # Create Darth Vader page
        self.vader_screen = QWidget()
        self.vader_layout = QGridLayout()
        self.vader_label = QLabel("Information on Darth Vader:")
        self.vader_result_text = QTextEdit()

        # add Vader page layout and widgets to stacked layout
        self.vader_layout.addWidget(self.vader_label)
        self.vader_screen.setLayout(self.vader_layout)
        self.vader_layout.addWidget(self.vader_result_text)
        self.stacked_layout.addWidget(self.vader_screen)

        # Create Obi-Wan Kenobi page
        self.kenobi_screen = QWidget()
        self.kenobi_layout = QGridLayout()
        self.kenobi_label = QLabel("Information on Obi-Wan Kenobi:")
        self.kenobi_result_text = QTextEdit()

        # add Kenobi page layout and widgets to stacked layout
        self.kenobi_layout.addWidget(self.kenobi_label)
        self.kenobi_screen.setLayout(self.kenobi_layout)
        self.kenobi_layout.addWidget(self.kenobi_result_text)
        self.stacked_layout.addWidget(self.kenobi_screen)

        # Starship pages for star wars information

        # Create Millennium Falcon page
        self.falcon_screen = QWidget()
        self.falcon_layout = QGridLayout()
        self.falcon_label = QLabel("Information on the Millennium Falcon:")
        self.falcon_result_text = QTextEdit()

        # add Falcon page layout and widgets to stacked layout
        self.falcon_layout.addWidget(self.falcon_label)
        self.falcon_screen.setLayout(self.falcon_layout)
        self.falcon_layout.addWidget(self.falcon_result_text)
        self.stacked_layout.addWidget(self.falcon_screen)

        # Create B-Wing page
        self.bwing_screen = QWidget()
        self.bwing_layout = QGridLayout()
        self.bwing_label = QLabel("Information on the B-Wing:")
        self.bwing_result_text = QTextEdit()

        # add B-Wing page layout and widgets to stacked layout
        self.bwing_layout.addWidget(self.bwing_label)
        self.bwing_screen.setLayout(self.bwing_layout)
        self.bwing_layout.addWidget(self.bwing_result_text)
        self.stacked_layout.addWidget(self.bwing_screen)

        # Create Death Star page
        self.death_screen = QWidget()
        self.death_layout = QGridLayout()
        self.death_label = QLabel("Information on the Death Star:")
        self.death_result_text = QTextEdit()

        # add Death Star page layout and widgets to stacked layout
        self.death_layout.addWidget(self.death_label)
        self.death_screen.setLayout(self.death_layout)
        self.death_layout.addWidget(self.death_result_text)
        self.stacked_layout.addWidget(self.death_screen)

        # Add nav and stacked layouts to the main layout
        self.layout.addLayout(nav_layout)
        self.layout.addLayout(self.stacked_layout)

        self.setLayout(self.layout)

    def home_page(self):
        self.stacked_layout.setCurrentIndex(0)

    def people_luke(self):
        self.stacked_layout.setCurrentIndex(1)
        luke_results = controller.get_api_data("people", "1")
        self.luke_result_text.setText(luke_results)

    def people_vader(self):
        self.stacked_layout.setCurrentIndex(2)
        vader_results = controller.get_api_data("people", "4")
        self.vader_result_text.setText(vader_results)

    def people_kenobi(self):
        self.stacked_layout.setCurrentIndex(3)
        kenobi_results = controller.get_api_data("people", "10")
        self.kenobi_result_text.setText(kenobi_results)

    def starship_falcon(self):
        self.stacked_layout.setCurrentIndex(4)
        falcon_results = controller.get_api_data("starships", "10")
        self.falcon_result_text.setText(falcon_results)

    def starship_bwing(self):
        self.stacked_layout.setCurrentIndex(5)
        bwing_results = controller.get_api_data("starships", "29")
        self.bwing_result_text.setText(bwing_results)

    def starship_death(self):
        self.stacked_layout.setCurrentIndex(6)
        death_results = controller.get_api_data("starships", "9")
        self.death_result_text.setText(death_results)

def searching(self):

    # When starship combobox gets an item clicked get the data on the starship
    if self.starship_combo.activated():
        results = controller.get_api_data(self)
        print(results)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
