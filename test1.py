# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# import sys
# import subprocess  # Import subprocess to run the external script

# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("QHBoxLayout Example")
#         # Create a QHBoxLayout instance
#         layout = QHBoxLayout()
#         layout.setAlignment(Qt.AlignCenter)  # Center the layout within the window
        
#         # Create buttons
#         self.left_button = QPushButton("Google Search Engine")
#         center_button = QPushButton("Center")
#         right_button = QPushButton("Right-Most")
        
#         # Set the fixed size for square buttons
#         button_size = 380  # Size of the square buttons (you can adjust this value)
#         self.left_button.setFixedSize(button_size, button_size)
#         center_button.setFixedSize(button_size, button_size)
#         right_button.setFixedSize(button_size, button_size)
        
#         # Set size policies to ensure the buttons are square
#         self.left_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
#         center_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
#         right_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        
#         # Add widgets to the layout with stretch factors
#         layout.addWidget(self.left_button)
#         layout.addWidget(center_button)
#         layout.addWidget(right_button)
        
#         # Connect the button click to the method
#         self.left_button.clicked.connect(self.run_browser_script)
        
#         # Set the layout on the application's window
#         self.setLayout(layout)
#         self.showMaximized()

#     def run_browser_script(self):
#         # Method to execute the browser.py script
#         subprocess.run(["python", "browser.py"])  # Adjust the path to your script as necessary
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = Window()
#     window.show()
#     sys.exit(app.exec_())
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# import sys
# import subprocess  # Import subprocess to run the external script

# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("QHBoxLayout Example")
#         # Create a QHBoxLayout instance
#         layout = QHBoxLayout()
#         layout.setAlignment(Qt.AlignCenter)  # Center the layout within the window
        
#         # Create buttons
#         self.left_button = QPushButton("Google Search Engine")
#         center_button = QPushButton("Center")
#         right_button = QPushButton("Right-Most")
        
#         # Set the fixed size for square buttons
#         button_size = 380  # Size of the square buttons (you can adjust this value)
#         self.left_button.setFixedSize(button_size, button_size)
#         center_button.setFixedSize(button_size, button_size)
#         right_button.setFixedSize(button_size, button_size)
        
#         # Set size policies to ensure the buttons are square
#         self.left_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
#         center_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
#         right_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        
#         # Add widgets to the layout with stretch factors
#         layout.addWidget(self.left_button)
#         layout.addWidget(center_button)
#         layout.addWidget(right_button)
        
#         # Connect the button click to the method
#         self.left_button.clicked.connect(self.run_browser_script)
        
#         # Set the layout on the application's window
#         self.setLayout(layout)
#         self.showMaximized()

#     def run_browser_script(self):
#         # Method to execute the browser.py script
#         subprocess.run(["python", "browser.py"])  # Adjust the path to your script as necessary

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = Window()
#     window.show()
#     sys.exit(app.exec_())
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import subprocess  # Import subprocess to run the external script

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QHBoxLayout Example")
        # Create a QHBoxLayout instance
        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignCenter)  # Center the layout within the window
        
        # Create buttons
        self.left_button = QPushButton("Google Search Engine")
        center_button = QPushButton("Center")
        right_button = QPushButton("Right-Most")
        
        # Set the fixed size for square buttons
        button_size = 380  # Size of the square buttons (you can adjust this value)
        self.left_button.setFixedSize(button_size, button_size)
        center_button.setFixedSize(button_size, button_size)
        right_button.setFixedSize(button_size, button_size)
        
        # Set size policies to ensure the buttons are square
        self.left_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        center_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        right_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        
        # Add widgets to the layout with stretch factors
        layout.addWidget(self.left_button)
        layout.addWidget(center_button)
        layout.addWidget(right_button)
        
        # Connect the button click to the method
        self.left_button.clicked.connect(self.run_browser_script)
        
        # Set the layout on the application's window
        self.setLayout(layout)
        self.showMaximized()

    def run_browser_script(self):
        # Method to execute the browser.py script
        subprocess.run(["python", "browser.py"])  # Adjust the path to your script as necessary
        QApplication.quit()  # Close the current PyQt5 application

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
