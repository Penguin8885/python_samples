import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt

class SampleWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    #初期化
    def initUI(self):
        self.setGeometry(300, 300, 300, 200) #ウィンドウの(位置, サイズ)
        self.setWindowTitle('Title')         #タイトル
        self.show()

    #キーイベント
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SampleWidget()
    sys.exit(app.exec_())
