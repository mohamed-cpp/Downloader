from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import os
from os import path
import sys
import urllib.request
from config import Config
import cgi


FORM_CLASS,_=loadUiType(path.join(path.dirname(__file__),"main.ui"))

class MainApp(QMainWindow, FORM_CLASS):
    def __init__(self, parent=None):
        super(MainApp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.config = Config()
        self.setupUi(self)
        self.Handel_UI()
        self.Handel_Buttons()
        self.Handel_Menu()




    def Handel_UI(self):
        self.setWindowTitle("Fire Downloader")
        self.setFixedSize(708,269)
        self.changeStyle(self.config.getSetting('DEFAULT','theme'))
        # self.setWindowIcon(QIcon('like (1).png'))

    def Handel_Buttons(self):
        self.pushButton.clicked.connect(self.Download)
        self.pushButton_3.clicked.connect(self.Handel_Browse)

    def Handel_Menu(self):
        self.actionElegantDark.triggered.connect( lambda: self.changeStyle("ElegantDark"))
        self.actionAqua.triggered.connect( lambda: self.changeStyle("Aqua"))
        self.actionManjaroMix.triggered.connect( lambda: self.changeStyle("ManjaroMix"))
        self.actionMaterialDark.triggered.connect( lambda: self.changeStyle("MaterialDark"))
        self.actionUbuntu.triggered.connect( lambda: self.changeStyle("Ubuntu"))

    def Handel_Browse(self):
        if self.lineEdit.text():
            path = self.config.getSetting('DEFAULT','path')
            filename = self.getFilename(self.lineEdit.text())
            save_place = QFileDialog.getSaveFileName(self, caption="Choose folder to download" , directory=path+filename,filter="(*.*)")
            text = str(save_place)
            name = (text[2:].split(',')[0].replace("'", ""))
            self.config.setSetting('DEFAULT','path',name.replace(name.split('/')[-1], ""))
            self.lineEdit_2.setText(name)
        else:
            QMessageBox.warning(self, "Url", "Please add url before choose folder")

    def changeStyle (self,styleName):
        if not styleName == None:
            self.config.setSetting('DEFAULT','theme',styleName)
            qss_file = open('style/'+styleName+'.qss').read()
            self.setStyleSheet(qss_file)

    def Handel_Progress(self,blocknum, blocksize , totalsize):
        read= blocknum * blocksize
        if totalsize > 0:
            percent= read * 100 / totalsize
            self.progressBar.setValue(percent)
            QApplication.processEvents()


    def getFilename(self,url):
        try:
            remotefile = urllib.request.urlopen(url)
            blah = remotefile.info()['Content-Disposition']
            value, params = cgi.parse_header(blah)
            filename = params["filename"]
        except:
            head, tail = os.path.split(url)
            filename = tail
        return filename;


    def Download(self):
        url = self.lineEdit.text()
        save_location = self.lineEdit_2.text()

        try:
            urllib.request.urlretrieve(url , save_location,self.Handel_Progress)
        except Exception:
            QMessageBox.warning(self, "Oops", "Error")
            return

        QMessageBox.information(self, "Done Download", "Enjoy")
        self.progressBar.setValue(0)
        self.lineEdit.setText('')
        self.lineEdit_2.setText('')

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()
	
if __name__ == '__main__':
    main()













