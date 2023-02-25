import sys
from PyQt5.QtWidgets import QApplication, QComboBox, QWidget, QLabel, QVBoxLayout

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        vbox = QVBoxLayout()
        label = QLabel('Select a language:')
        self.combo = QComboBox()
        self.combo.addItems(['French', 'English', 'German', 'Italian'])
        self.combo.currentIndexChanged.connect(self.print_text)
        vbox.addWidget(label)
        vbox.addWidget(self.combo)
        self.setLayout(vbox)
        self.show()
    
    def print_text(self, i):
        print(self.combo.currentText())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
