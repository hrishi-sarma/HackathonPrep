from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *


class MyWebBrowser(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MyWebBrowser, self).__init__(*args, **kwargs)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://www.google.com"))

        self.setWindowTitle("Web Browser")
        self.setCentralWidget(self.browser)
        self.showMaximized()

        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText("Enter URL and press Enter")
        self.url_bar.returnPressed.connect(self.navigate_to_url)

        navbar = QToolBar()
        self.addToolBar(navbar)

        self.go_btn = QPushButton("Go")
        self.go_btn.clicked.connect(self.navigate_to_url)

        self.back_btn = QPushButton("<")
        self.back_btn.clicked.connect(self.browser.back)

        self.forward_btn = QPushButton(">")
        self.forward_btn.clicked.connect(self.browser.forward)

        self.reload_btn = QPushButton("Reload")
        self.reload_btn.clicked.connect(self.browser.reload)
        
        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)
        
        shortcutPrevPage = QKeySequence(Qt.ALT + Qt.Key_Left)
        self.shortcutPrevPage = QShortcut(shortcutPrevPage,self)
        self.shortcutPrevPage.activated.connect(self.browser.back)
        
        shortcutForwPage = QKeySequence(Qt.ALT + Qt.Key_Right)
        self.shortcutForwPage = QShortcut(shortcutForwPage,self)
        self.shortcutForwPage.activated.connect(self.browser.forward)
        
        shortcutJumpSearch = QKeySequence(Qt.ALT + Qt.Key_Slash)
        self.shortcutJumpSearch = QShortcut(shortcutJumpSearch,self)
        self.shortcutJumpSearch.activated.connect(self.focus_url_bar)

        self.navbar = QToolBar()
        self.navbar.addWidget(self.url_bar)
        self.navbar.addWidget(self.go_btn)
        self.navbar.addWidget(self.back_btn)
        self.navbar.addWidget(self.forward_btn)
        self.navbar.addWidget(self.reload_btn)

        self.addToolBar(self.navbar)
        self.setCentralWidget(self.browser)

    def focus_url_bar(self):
        self.url_bar.setFocus()

    def navigate_home(self):
        self.browser.setUrl(QUrl('https://www.google.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith("http"):
            self.url_bar.setText(url)
            url = "https://" + url
        self.browser.setUrl(QUrl(url))

app = QApplication([])
window = MyWebBrowser()
window.show()
app.exec_()
