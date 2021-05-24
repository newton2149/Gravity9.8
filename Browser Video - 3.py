import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow ,self).__init__()
        self.showMaximized()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)

        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('Back' , self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('forward ' , self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        home_btn = QAction('Home' , self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)


        reload_btn = QAction('Refresh',self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        self.search_bar = QLineEdit()
        self.search_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.search_bar)

        self.browser.urlChanged.connect(self.update_url)


    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def navigate_to_url(self):
        url = self.search_bar.text()
        url='https://'+url
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.search_bar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName('My First Browser')
window = MainWindow()
app.exec_()

