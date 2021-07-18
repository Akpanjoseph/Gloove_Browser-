import sys
# from idlelib import browser

from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.showMaximized()
        # self.setStyleSheet('background-image :url(screen-code-laptop-write.jpg)')
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        # self.setFixedWidth(1300)
        # self.setFixedHeight(700)
        self.setCentralWidget(self.browser)
        self.setWindowIcon(QIcon('Icons/browserIcon.png'))
        self.setMinimumWidth(700)
        self.setMinimumHeight(600)

        #         navBar

        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('Back\t', self)
        back_btn.setIcon(QIcon('Icons/back.jpg'))
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('forward\t', self)
        forward_btn.setIcon(QIcon('Icons/forward.png'))
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('refresh\t', self)
        # reload_btn.setIcon(QIcon(' Icons/reload.png '))
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        search = QLabel('Search\t', self)
        navbar.addWidget(search)

        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText('http://')
        self.url_bar.resize(3, 10)
        self.url_bar.returnPressed.connect(self.navigate_search)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

        search_btn = QAction(' Go\t', self)
        search_btn.triggered.connect(self.navigate_search)
        navbar.addAction(search_btn)

        home_btn = QAction('Home', self)
        home_btn.setIcon(QIcon('Icons/home.png'))
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def navigate_search(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self,q):
        self.url_bar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName('Funki Browser'.center(10).replace('','  '))
window = MainWindow()
window.show()
app.exec_()
