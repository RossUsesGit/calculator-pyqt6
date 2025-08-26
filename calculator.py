from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from themes import *
import sys,os

class MainWindow(QMainWindow,Themes):
    def __init__(self):
        super().__init__()
        self.setFixedSize(300, 550)
        self.setWindowTitle("Calculator by Ross")
        self.setStyleSheet(Themes.Default.background())
        self.setupUI()
        self.setupMenu()

    def setupUI(self):

        # Main Layout
        self.main_layout = QVBoxLayout()

        # Screen

        self.screen = QLineEdit()
        self.screen.setReadOnly(True)
        self.screen.setFixedWidth(280)
        self.screen.setFixedHeight(200)
        self.screen.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.screen.setStyleSheet(Themes.Default.screen())
        self.main_layout.addWidget(self.screen)

     
        # Calc Layout
        self.calc_layout = QGridLayout()
        self.calc_layout.setSpacing(0)
        

        # Buttons
        self.button1 = QPushButton("1")
        self.button1.clicked.connect(lambda: self.screen.insert("1"))
        self.button2 = QPushButton("2")
        self.button2.clicked.connect(lambda: self.screen.insert("2"))
        self.button3 = QPushButton("3")
        self.button3.clicked.connect(lambda: self.screen.insert("3"))
        self.button4 = QPushButton("4")
        self.button4.clicked.connect(lambda: self.screen.insert("4"))
        self.button5 = QPushButton("5")
        self.button5.clicked.connect(lambda: self.screen.insert("5"))
        self.button6 = QPushButton("6")
        self.button6.clicked.connect(lambda: self.screen.insert("6"))
        self.button7 = QPushButton("7")
        self.button7.clicked.connect(lambda: self.screen.insert("7"))
        self.button8 = QPushButton("8")
        self.button8.clicked.connect(lambda: self.screen.insert("8"))
        self.button9 = QPushButton("9")
        self.button9.clicked.connect(lambda: self.screen.insert("9"))
        self.button0 = QPushButton("0")
        self.button0.clicked.connect(lambda: self.screen.insert("0"))
        self.clear_button = QPushButton("C")
        self.clear_button.clicked.connect(self.clear_screen)

        self.add_button = QPushButton("+")
        self.add_button.clicked.connect(self.operator_clicked)

        self.percent_button = QPushButton("%")
        self.percent_button.clicked.connect(self.percent)

        self.subtract_button = QPushButton("-")
        self.subtract_button.clicked.connect(self.operator_clicked)

        self.multiply_button = QPushButton("*")
        self.multiply_button.clicked.connect(self.operator_clicked)

        self.divide_button = QPushButton("/")
        self.divide_button.clicked.connect(self.operator_clicked)

        self.decimal_button = QPushButton(".")
        self.decimal_button.clicked.connect(lambda: self.screen.insert("."))

        self.equal_button = QPushButton("=")
        self.equal_button.clicked.connect(self.calculate)

        self.button_list =  [self.button0, self.button1, self.button2, self.button3, self.button4,
            self.button5, self.button6, self.button7, self.button8, self.button9,
            self.add_button, self.subtract_button, self.multiply_button, 
            self.divide_button, self.equal_button, self.decimal_button,
            self.percent_button,self.clear_button]
    
        ## Layout

        # First Row, Clear, Percent, Divide
        self.calc_layout.addWidget(self.clear_button,0,0,1,2)
        self.calc_layout.addWidget(self.percent_button,0,2)
        self.calc_layout.addWidget(self.divide_button,0,3)

        # 2nd Row, 789, Multiply
        self.calc_layout.addWidget(self.button7,1,0)
        self.calc_layout.addWidget(self.button8,1,1)
        self.calc_layout.addWidget(self.button9,1,2)
        self.calc_layout.addWidget(self.multiply_button,1,3)

        # 3rd Row, 456, Add
        self.calc_layout.addWidget(self.button4, 2, 0)
        self.calc_layout.addWidget(self.button5, 2, 1)
        self.calc_layout.addWidget(self.button6, 2, 2)
        self.calc_layout.addWidget(self.add_button,2,3)

        # 4th Row, 123, Subtract
        self.calc_layout.addWidget(self.button1, 3, 0)
        self.calc_layout.addWidget(self.button2, 3, 1)
        self.calc_layout.addWidget(self.button3, 3, 2)
        self.calc_layout.addWidget(self.subtract_button,3,3)

        # 5th Row, 0, Decimal, Equals
        self.calc_layout.addWidget(self.button0,4,0)
        self.calc_layout.addWidget(self.decimal_button,4,1)
        self.calc_layout.addWidget(self.equal_button,4,2,1,2)

        # Default Button Design
        for button in self.button_list:
            button.setStyleSheet(Themes.Default.buttons())

        self.button_container = QWidget()
        self.button_container.setLayout(self.calc_layout)

        self.main_layout.addWidget(self.button_container)

        self.main_container = QWidget()
        self.main_container.setLayout(self.main_layout)

        self.setCentralWidget(self.main_container)
        
    def setupMenu(self):

        self.menu_bar = self.menuBar()
        self.menu_bar.setStyleSheet(Themes.Default.menu())

        self.options_menu = self.menu_bar.addMenu("Options")

        self.about_section = self.options_menu.addAction("About")
        self.about_section.triggered.connect(self.show_about_window)

        self.help_section = self.options_menu.addAction("Help")
        self.help_section.triggered.connect(self.show_help_window)

        self.exit_button = self.options_menu.addAction("Exit")
        self.exit_button.triggered.connect(lambda: self.close())

        self.themes_menu = self.menu_bar.addMenu("Themes")
        self.default_theme = self.themes_menu.addAction("Default")
        self.iris_theme = self.themes_menu.addAction("Iris")
        self.blush_theme = self.themes_menu.addAction("Blush")
        self.oracle_theme = self.themes_menu.addAction("Oracle")
        self.joker_theme = self.themes_menu.addAction("Joker")

        self.default_theme.triggered.connect(lambda: self.change_theme("default"))
        self.iris_theme.triggered.connect(lambda: self.change_theme("iris"))
        self.blush_theme.triggered.connect(lambda: self.change_theme("blush"))
        self.oracle_theme.triggered.connect(lambda: self.change_theme("oracle"))
        self.joker_theme.triggered.connect(lambda: self.change_theme("joker"))

    def show_about_window(self):
        self.msg_box = QMessageBox(self)
        self.msg_box.setIcon(QMessageBox.Icon.Information)
        self.msg_box.setWindowTitle("About")
        self.msg_box.setText("[Calculator]\n"
        "Created by Ross (obviously)\n"
        "A personal project\n"
        '"I had a lot of fun making this. - Ross probably"')
        self.msg_box.setStyleSheet("""
        background: #FFFFFF;
        color: #000000;
        """)
        self.msg_box.exec()

    def show_help_window(self):
        self.msg_box = QMessageBox(self)
        self.msg_box.setIcon(QMessageBox.Icon.Information)
        self.msg_box.setWindowTitle("Help")
        self.msg_box.setInformativeText("This app is pretty much self explanatory since I highly doubt that anybody above the age of 5 hadn't already used a calculator atleast once. However, I am not one to judge so IN CASE you're either below 5 or had never used a calculator before (sheesh), here's how it works: \n\n"
        "Number Buttons: input numbers to the screen \n"
        "+-*/ Buttons: either add, subtract, multiply, or divide. You must first enter a number before clicking these unless you want nothing to happen. \n"
        "C Button: stands for clear; removes everything in the screen.\n"
        "% Button (Percent): Divides the given number on screen by 100. Raises an error if there are no numbers on screen. \n"
        "= Button (Equal): Shows the number that the calculator calculated. If you calculated a number, are you a calculator? \n"
        ". Button (Decimal): Used for floating point numbers. More specifically, base-10 fractions. \n\n"
        "If you encounter any bugs, please do hesistate to contact me, I will not respond.\n"
        "Kidding aside, thank you for testing out this app! :3")
        self.msg_box.setStyleSheet("""
        background: #FFFFFF;
        color: #000000;
        """)
        self.msg_box.exec()


    def clear_screen(self):
        self.screen.setText("")
        self.result = 0
        self.num1 = 0
        self.num2 = 0
        self.enable_input()

    def percent(self):

        try:
            self.num1 = float(self.screen.text())
            self.result = self.num1 / 100
        except ValueError:
            self.result = "Error"
            self.disable_input()

        if isinstance(self.result,str):
            self.screen.setText(self.result)
        elif abs(self.result) >= 1e12 or abs(self.result) < 1e-12 and self.result != 0:
            self.screen.setText("{:.4e}".format(self.result))
        elif self.result.is_integer():
            self.screen.setText(str(int(self.result))) 
        else:
            self.screen.setText(str(round(self.result, 4)))

        self.num1 = 0

    def operator_clicked(self):
        
        self.operator = self.sender().text()

        if self.sender().text() not in ["+","-","/","*"]:
            return

        try:
            self.num1 = self.screen.text()
            if not self.num1 or self.num1 == "Error":
                return
            else:
                self.num1 = float(self.num1)
            self.screen.clear()
        except ValueError:
            self.screen.setText("Error")
            self.disable_input() 

    def calculate(self):

        if not hasattr(self, 'operator') or not self.screen.text():
            return
        
        try:
            self.num2 = self.screen.text()
            if not self.num2 or self.num2 == "Error":
                return
            else:
                self.num2 = float(self.num2)
        except ValueError:
            self.screen.setText("Error")
            self.disable_input() 

        self.result = 0

        if self.operator == "+":
            self.result = self.num1 + self.num2

        elif self.operator == "-":
            self.result = self.num1 - self.num2

        elif self.operator == "*":
            self.result = self.num1 * self.num2

        elif self.operator == "/":

            try:
                if self.num1 == 0:
                    self.result = 0
                else:
                    self.result = self.num1 / self.num2
            except ZeroDivisionError:
                self.result = "Error"
                self.disable_input() 

        else:
            self.screen.setText("Error")
            self.disable_input()

        self.num1 = 0
        self.num2 = 0
            

        if isinstance(self.result,str):
            self.screen.setText(self.result)
        elif abs(self.result) >= 1e12 or abs(self.result) < 1e-12 and self.result != 0:
            self.screen.setText("{:.4e}".format(self.result))
        elif self.result.is_integer():
            self.screen.setText(str(int(self.result))) 
        else:
            self.screen.setText(str(round(self.result, 4)))


    def disable_input(self):
    
        for button in self.button_list:
            if button == self.clear_button:
                continue
            else:
                button.setDisabled(True)

    def enable_input(self):
    
        for button in self.button_list:
                button.setDisabled(False)


    def change_theme(self,theme_name):
        if theme_name == "default":
            for button in self.button_list:
                button.setStyleSheet(Themes.Default.buttons())
            self.setStyleSheet(Themes.Default.background())
            self.menu_bar.setStyleSheet(Themes.Default.menu())
            self.screen.setStyleSheet(Themes.Default.screen())

        elif theme_name == "iris":
            for button in self.button_list:
                button.setStyleSheet(Themes.Iris.buttons())
            self.setStyleSheet(Themes.Iris.background())
            self.screen.setStyleSheet(Themes.Iris.screen())
            self.menu_bar.setStyleSheet(Themes.Iris.menu())

        elif theme_name == "blush":
            for button in self.button_list:
                button.setStyleSheet(Themes.Blush.buttons())
            self.setStyleSheet(Themes.Blush.background())
            self.screen.setStyleSheet(Themes.Blush.screen())
            self.menu_bar.setStyleSheet(Themes.Blush.menu())

        elif theme_name == "oracle":
            for button in self.button_list:
                button.setStyleSheet(Themes.Oracle.buttons())
            self.setStyleSheet(Themes.Oracle.background())
            self.screen.setStyleSheet(Themes.Oracle.screen())
            self.menu_bar.setStyleSheet(Themes.Oracle.menu())

        elif theme_name == "joker":
            for button in self.button_list:
                button.setStyleSheet(Themes.Joker.buttons())
            self.setStyleSheet(Themes.Joker.background())
            self.screen.setStyleSheet(Themes.Joker.screen())
            self.menu_bar.setStyleSheet(Themes.Joker.menu())



app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
