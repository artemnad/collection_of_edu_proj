# работа с оконными приложениями
# python -m pip install PyQt5

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QDesktopWidget, QMainWindow, QAction, QLabel, QLineEdit, QTextEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication, pyqtSlot


class ExampleApp(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        self.resize(450, 550)
        self.setWindowTitle('ExampleApp')
        self.setWindowIcon(QIcon('icon.png'))
        
        self.center()
        
        self.statusBar().showMessage('')
        
        btn = QPushButton('Push me', self)
        btn.clicked.connect(self.myBtn)
        btn.move(175, 150)
        
        # Действие по закрытию приложения
        exitAction = QAction(QIcon('icon.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+X')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)
        
        # СТрока меню
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')
        fileMenu.addAction(exitAction)
        
        # Панель инструментов
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)
        
        # Текстовые метки
        self.label1 = QLabel('Математика', self)
        self.label1.adjustSize()
        self.label1.move(10, 100)
        
        label2 = QLabel('Программирование', self)
        label2.adjustSize()
        label2.move(30, 120)
        
        # Текстовые поля
        lineField = QLineEdit(self)
        lineField.move(100, 200)
        lineField.resize(200, 30)
        
        textField = QTextEdit(self)
        textField.move(100, 250)
        textField.resize(200, 200)
        
        lineLabel = QLabel('Line', self)
        lineLabel.move(30, 200)
        
        textLabel = QLabel('Text', self)
        textLabel.move(30, 250)
        
        self.show()
        
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Quit', 'Are you sure?', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
   
    def myBtn(self):
        # Замена текста в label1
        self.label1.setText('Button pushed')
        self.label1.adjustSize()
            
    def center(self):
        fg = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        fg.moveCenter(cp)
        self.move(fg.topLeft())

app = QApplication([])
ew = ExampleApp()
app.exec_()
