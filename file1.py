from PyQt5.QtWidgets import *
from PyQt5.QtCore import * 
from PyQt5.QtGui import *  
from PyQt5.QtWebEngineWidgets import *

class MyWebBrowser(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MyWebBrowser, self).__init__(*args, **kwargs)

        self.setWindowTitle('Web Browser')
        
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://www.google.com'))
        
        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText('Enter URL and press Enter')
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        
        self.go_btn = QPushButton('Go')
        self.go_btn.clicked.connect(self.navigate_to_url)
        
        self.back_btn = QPushButton('<')
        self.back_btn.clicked.connect(self.browser.back)
        
        self.forward_btn = QPushButton('>')
        self.forward_btn.clicked.connect(self.browser.forward)
        
        self.reload_btn = QPushButton('Reload')
        self.reload_btn.clicked.connect(self.browser.reload)
        
        self.navbar = QToolBar()
        self.navbar.addWidget(self.url_bar)
        self.navbar.addWidget(self.go_btn)
        self.navbar.addWidget(self.back_btn)
        self.navbar.addWidget(self.forward_btn)
        self.navbar.addWidget(self.reload_btn)
        
        self.addToolBar(self.navbar)
        self.setCentralWidget(self.browser)
        
    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

app = QApplication([])
window = MyWebBrowser()
window.show()
app.exec_()
