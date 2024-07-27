import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QVBoxLayout, QHBoxLayout, QTabWidget
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt, QEvent, QSize, QUrl
from PyQt6.QtWebEngineWidgets import QWebEngineView

class HoverSidebar(QWidget):
    def __init__(self, parent, width, extended_width):
        super().__init__(parent)
        self.normal_width = width
        self.extended_width = extended_width
        self.setFixedWidth(self.normal_width)
        
        # Set up the layout and contents of the sidebar
        self.layout = QVBoxLayout()
        self.layout.addWidget(QLabel("Sidebar Content", self))
        self.setLayout(self.layout)

        # Enable hover events
        self.setAttribute(Qt.WidgetAttribute.WA_Hover)

    def event(self, event):
        if event.type() == QEvent.Type.HoverEnter:
            self.setFixedWidth(self.extended_width)
        elif event.type() == QEvent.Type.HoverLeave:
            self.setFixedWidth(self.normal_width)
        return super().event(event)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Browsit")
        self.setGeometry(100, 100, 1920, 1080)  # Smaller window size
        self.setStyleSheet("""
            MainWindow {
                background-image: url(images/eagan-hsu-sdewdKGHl5A-unsplash.jpg);
                background-repeat: no-repeat;
                background-position: center;
            }
        """)  # Change background to the image

        self.initUI()

    def initUI(self):
        # Create the main layout
        main_layout = QVBoxLayout(self)
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
        input_container.setFixedSize(300, 50)  # Smaller size
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
        self.chrome_button.setIcon(QIcon("images/basic_ios_14_app_icon_pack.jpeg"))
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

        # Create round buttons N and B
        round_button1 = QPushButton("N", self)
        round_button1.setGeometry(30, 30, 30, 30)  # Smaller size
        round_button1.setFont(QFont("Courier", 8, QFont.Weight.Bold, italic=True))  # Smaller font size
        round_button1.setStyleSheet("color: #FFFFFF;")  # White text color

        round_button2 = QPushButton("B", self)
        round_button2.setGeometry(1640, 30, 30, 30)  # Place on the leftmost side, same height as round_button1
        round_button2.setFont(QFont("Courier", 8, QFont.Weight.Bold, italic=True))  # Smaller font size
        round_button2.setStyleSheet("color: #FFFFFF;")  # White text color

        round_button1.show()
        round_button2.show()

        # Create and add the sidebar
        self.sidebar = HoverSidebar(self, width=50, extended_width=200)
        self.sidebar.setStyleSheet("background-color: #333333;")
        self.sidebar.setFixedHeight(self.height())
        self.sidebar.move(0, 0)
        self.sidebar.show()

    def add_new_tab(self):
        web_view = QWebEngineView(self)
        self.tab_widget.addTab(web_view, "New Tab")
        web_view.setUrl(QUrl("https://www.google.com"))

    def perform_search(self):
        query = self.text_input.text()
        if not query:
            return

        search_url = f"https://www.google.com/search?q={query}"
        
        # Open the search URL in a new tab within the application
        web_view = QWebEngineView(self)
        web_view.setUrl(QUrl(search_url))
        self.tab_widget.addTab(web_view, f"Search Results for '{query}'")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec())
