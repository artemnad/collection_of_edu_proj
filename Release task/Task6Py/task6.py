import socket
import sys
import requests
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QAction, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PIL import Image, ImageOps

my_num_task = int(input('Введите номер задачи: '))


def drawThreeRectangle(saveFile):
    img = Image.new('RGB', (128, 128), color='white')
    img.paste((255, 0, 0), (0, 0, 42, 128))
    img.paste((0, 255, 0), (42, 0, 84, 128))
    img.paste((0, 0, 255), (84, 0, 128, 128))
    img.save(saveFile)


def doInverseColorPic(this_name):
    img = Image.open(this_name)
    img_invert = ImageOps.invert(img)
    img_invert.save(this_name, quality=95)


def createGUICopyPasteApp():
    class App(QMainWindow):
        def __init__(self):
            super().__init__()
            self.title = 'CopyPasteApp'
            self.left = 200
            self.top = 100
            self.width = 680
            self.height = 400
            self.initUI()

        def initUI(self):
            self.setWindowTitle(self.title)
            self.setGeometry(self.left, self.top, self.width, self.height)
            # Create textbox one
            self.textbox_1 = QLineEdit(self)
            self.textbox_1.move(20, 20)
            self.textbox_1.resize(280, 240)
            # Create textbox two
            self.textbox_2 = QLineEdit(self)
            self.textbox_2.move(380, 20)
            self.textbox_2.resize(280, 240)
            self.textbox_2.setReadOnly(True)
            # Create a button in the window
            self.button = QPushButton('Paste text', self)
            self.button.move(292, 300)
            # connect button to function on_click
            self.button.clicked.connect(self.on_click)
            self.show()
            self.statusBar()
            pasteAction = QAction(QIcon('paste.png'), '&Paste', self)
            pasteAction.setStatusTip('Paste text from right window to left window')
            pasteAction.triggered.connect(self.paste_click)
            menubar = self.menuBar()
            fileMenu = menubar.addMenu('&Menu')
            fileMenu.addAction(pasteAction)

        @pyqtSlot()
        def on_click(self):
            self.textbox_2.setText(self.textbox_1.text())

        def paste_click(self):
            self.textbox_1.setText(self.textbox_2.text())

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex = App()
        sys.exit(app.exec_())


def copyFromFirstFileToSecondFile(argv):
    try:
        in_file = open(argv[0], "r")
        data = in_file.read()
        in_file.close()

        out_file = open(argv[1], "w")
        out_file.write(data)
        out_file.close()
    except:
        print('Oops, first file not found')


def connectToAddress(argv):
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = argv[0]
    port = argv[1]
    try:
        soc.connect((host, int(port)))
        print('Connected ' + host)
        soc.shutdown(socket.SHUT_WR)
    except:
        print('Oops, something went wrong')
        sys.exit()
    while True:
        data = soc.recv(1024)
        if data == "":
            break
        print('Received:')
        repr(data)
    print('Connection closed')
    soc.close()


def myTask(i):
    if i == 1:
        return drawThreeRectangle(input('Введите название изображения: '))
    elif i == 2:
        return doInverseColorPic(input('Введите название изображения: '))
    elif i == 3:
        return createGUICopyPasteApp()
    elif i == 4:
        return copyFromFirstFileToSecondFile(sys.argv[1:])
    elif i == 5:
        return connectToAddress(sys.argv[1:])


myTask(my_num_task)
