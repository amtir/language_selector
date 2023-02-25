import os
import sys
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QComboBox, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTranslator, QLocale

class MyWindow(QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.init_ui()
        
    def init_ui(self):
        vbox = QVBoxLayout()
        self.label = QLabel()
        self.combo = QComboBox()
        
        # Add flag images to combo box
        for lang in ['English', 'French', 'German', 'Italian']:
            flag_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), lang.lower() + '.png')
            pixmap = QPixmap(flag_path)
            self.combo.addItem(QIcon(pixmap), lang)
        
        self.combo.currentIndexChanged.connect(self.print_text)
        vbox.addWidget(self.label)
        vbox.addWidget(self.combo)
        self.setLayout(vbox)
        
        self.retranslate_ui()
        
        self.show()
        
    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        
        # Set the text of the label and combo box items for the current language
        self.label.setText(_translate("MyWindow", "Select a language:"))
        self.combo.setItemText(0, _translate("MyWindow", "English"))
        self.combo.setItemText(1, _translate("MyWindow", "French"))
        self.combo.setItemText(2, _translate("MyWindow", "German"))
        self.combo.setItemText(3, _translate("MyWindow", "Italian"))
    
    def print_text(self, i):
        # Print the current text and index of the selected item
        print(self.combo.currentText())
        print(i)
        
        global translator
        
        # Load the translation file for the selected language and update the UI
        if self.combo.currentIndex() == 0:
            print(0)
            translator.load('lang.eng.qm')
            self.app.installTranslator(translator)
            self.retranslate_ui()
        elif self.combo.currentIndex() == 1:
            print(1)
            translator.load('lang.fr.qm')
            self.app.installTranslator(translator)
            self.retranslate_ui()
        elif self.combo.currentIndex() == 2:
            print(2)
            translator.load('lang.de.qm')
            self.app.installTranslator(translator)
            self.retranslate_ui()
        elif self.combo.currentIndex() == 3:
            print(3)
            translator.load('lang.it.qm')
            self.app.installTranslator(translator)
            self.retranslate_ui()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    # Load the default translations for the English language
    translator = QTranslator()
    translator.load("lang.eng.qm")
    app.installTranslator(translator)
    
    window = MyWindow(app)
    sys.exit(app.exec_())
