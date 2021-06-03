# работа с оконными приложениями
# python -m pip install PyQt5

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QDesktopWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication


class ExampleApp(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        self.resize(450, 250)
        self.setWindowTitle('ExampleApp')
        self.setWindowIcon(QIcon('icon.png'))
        
        self.center()
        
        btn = QPushButton('Push me', self)
        btn.clicked.connect(QCoreApplication.instance().quit)
        btn.move(50, 50)
        
        self.show()
        
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Quit', 'Are you sure?', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
            
    def center(self):
        fg = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        fg.moveCenter(cp)
        self.move(fg.topLeft())

app = QApplication([])
ew = ExampleApp()
app.exec_()
