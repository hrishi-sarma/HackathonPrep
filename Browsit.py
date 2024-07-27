import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWebEngineWidgets import *  # Ensure this import is included

class HoverSidebar(QWidget):
    def __init__(self, parent, width, extended_width):
        super().__init__(parent)
        self.normal_width = width
        self.extended_width = extended_width
        self.setFixedWidth(10)  
        self.setMaximumWidth(250) 
        
        self.layout = QVBoxLayout()

        self.title_label = QLabel("Notes", self)
        self.title_label.setFont(QFont("Courier", 16, QFont.Weight.Bold))
        self.title_label.setStyleSheet("color: #FFFFFF; margin-bottom: 5px;")  # White text color and margin
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.title_label)
        
        self.note_area = QTextEdit(self)
        self.note_area.setPlaceholderText("Take notes here...")
        self.note_area.setStyleSheet("background-color: #555555; color: #FFFFFF; border: none;")
        self.layout.addWidget(self.note_area)
        
        self.setLayout(self.layout)

        # Enable hover events
        self.setAttribute(Qt.WidgetAttribute.WA_Hover)
        

    def event(self, event):
        if event.type() == QEvent.Type.HoverEnter:
            self.setFixedWidth(self.extended_width)
        elif event.type() == QEvent.Type.HoverLeave:
            self.setFixedWidth(self.normal_width)
        return super().event(event)

    def set_normal_width(self, width):
        self.normal_width = width
        self.setFixedWidth(self.normal_width)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the URL bar
        self.url_bar = QLineEdit()
        self.url_bar.setPlaceholderText("Enter URL and press Enter")
        self.url_bar.setFixedHeight(30)  # Increase the height of the URL bar
        self.url_bar.setMinimumWidth(300)  # Optional: Set a minimum width for the URL bar

        self.url_bar.returnPressed.connect(self.navigate_to_url)
        

        # Set up the toolbar and add the URL bar
        navbar = QToolBar("Navigation")
        self.addToolBar(navbar)
        

        self.go_btn = QPushButton("Go")
        self.go_btn.clicked.connect(self.navigate_to_url)
        navbar.addWidget(self.go_btn)

        home_btn = QAction("Home", self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        navbar.addWidget(self.url_bar)

        # Set the main window properties
        self.setWindowTitle("Browsit")
        self.setGeometry(100, 100, 1920, 1080)
        self.setStyleSheet("""
            QMainWindow {
                background-image: url(images/eagan-hsu-sdewdKGHl5A-unsplash.jpg);
                background-repeat: no-repeat;
                background-position: center;
            }
        """)  # Change background to the image
        self.showMaximized()

        # Create the central widget and set layout
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
       
        self.initUI()

        # Connect returnPressed signals
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        self.text_input.returnPressed.connect(self.perform_search)

    def initUI(self):
        # Create the main layout
        main_layout = QVBoxLayout(self.central_widget)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Create the Browsit label
        browsit_label = QLabel("Browsit", self)
        browsit_label.setFont(QFont("Courier", 40))  # Smaller font size
        browsit_label.setStyleSheet("color: #FFFFFF;")  # White text color
        browsit_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        browsit_label.setMargin(20)
        main_layout.addWidget(browsit_label, alignment=Qt.AlignmentFlag.AlignCenter)

        # Create the text input area
        input_container = QWidget(self)
        input_container.setFixedSize(600, 50)  # Smaller size
        input_container.setStyleSheet("background-color: #000000; border-radius: 15px;")

        input_layout = QHBoxLayout(input_container)
        input_layout.setContentsMargins(25, 12, 25, 12)  # Adjust margins

        self.text_input = QLineEdit(input_container)
        self.text_input.setStyleSheet("color: #ffffff;")
        self.text_input.setFont(QFont("Courier", 15, QFont.Weight.Bold))  # Smaller font size
        input_layout.addWidget(self.text_input)
        
        self.go_button = QPushButton("GO", input_container)
        self.go_button.setFont(QFont("Courier", 7, QFont.Weight.Bold, italic=True))  # Smaller font size
        self.go_button.setStyleSheet("color: #FFFFFF;")  # White text color
        self.go_button.clicked.connect(self.perform_search)
        input_layout.addWidget(self.go_button)

        main_layout.addWidget(input_container, alignment=Qt.AlignmentFlag.AlignCenter)

        # Create the tab widget for web pages
        self.tab_widget = QTabWidget(self)
        main_layout.addWidget(self.tab_widget)

        # Add the first empty tab with a default web view
        self.add_new_tab()

        # Create the icons container
        icons_container = QWidget(self)
        icons_container.setFixedSize(500, 150)  # Smaller size
        icons_container.setStyleSheet("background-color: #000000;")
        
        icons_layout = QHBoxLayout(icons_container)
        icons_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        icons_layout.setContentsMargins(4, 4, 4, 4)
        icons_layout.setSpacing(35)  # Adjust spacing

        # Create the Chrome button
        self.chrome_button = QPushButton(self)
        self.chrome_button.setStyleSheet("background-image : url(notas.jpeg);")
        self.chrome_button.setIconSize(self.chrome_button.size())
        self.chrome_button.setCheckable(True)
        self.chrome_button.setFixedSize(142, 142)  # Smaller size
        self.chrome_button.setStyleSheet("background-color: none;")

        # Create the Opera button
        opera_button = QPushButton(self)
        opera_button.setIcon(QIcon("images/Opera_free_icons_designed_by_Freepik.jpeg"))
        opera_button.setIconSize(opera_button.size())
        opera_button.setCheckable(True)
        opera_button.setFixedSize(142, 142)  # Smaller size
        opera_button.setStyleSheet("background-color: none;")

        # Create the Brave button
        brave_button = QPushButton(self)
        brave_button.setIcon(QIcon("images/icon_brave_black.jpeg"))
        brave_button.setIconSize(brave_button.size())
        brave_button.setCheckable(True)
        brave_button.setFixedSize(140, 142)  # Smaller size
        brave_button.setStyleSheet("background-color: none;")

        # Add buttons to the icons container layout
        icons_layout.addWidget(self.chrome_button)
        icons_layout.addWidget(opera_button)
        icons_layout.addWidget(brave_button)

        # Add icons container to the main layout
        main_layout.addWidget(icons_container, alignment=Qt.AlignmentFlag.AlignCenter)

        # Create round button B
        round_button2 = QPushButton("B", self)
        round_button2.setGeometry(1640, 30, 30, 30)  # Place on the leftmost side, same height as round_button1
        round_button2.setFont(QFont("Courier", 8, QFont.Weight.Bold, italic=True))  # Smaller font size
        round_button2.setStyleSheet("color: #FFFFFF;")  # White text color

        round_button2.show()

        # Create and add the sidebar
        self.sidebar = HoverSidebar(self, width=10, extended_width=250)
        self.sidebar.setStyleSheet("background-color: rgba(51, 51, 51, 150);")  # Translucent background
        self.sidebar.setFixedHeight(self.height())
        self.sidebar.move(0, 0)
        self.sidebar.show()

    def add_new_tab(self):
        web_view = QWebEngineView(self)
        self.tab_widget.addTab(web_view, "New Tab")
        web_view.setUrl(QUrl(""))

    def perform_search(self):
        query = self.text_input.text() or self.url_bar.text()
        if not query:
            return

        search_url = f"https://duckduckgo.com/?q={query}"
        
        # Open the search URL in a new tab within the application
        web_view = QWebEngineView(self)
        web_view.setUrl(QUrl(search_url))
        self.tab_widget.addTab(web_view, f"Search Results for '{query}'")

    def navigate_home(self):
        self.add_new_tab()  # For now, just add a new tab as the home page

    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith("https://"):
            url = "https://" + url
        web_view = QWebEngineView(self)
        web_view.setUrl(QUrl(url))
        self.tab_widget.addTab(web_view, f"Results for:{url}")

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec())
