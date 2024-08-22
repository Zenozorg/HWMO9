from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QTextEdit, QPushButton, QComboBox, QFileDialog
import requests
import os

class JsonPlaceholderClient(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("JSONPlaceholder Client")
        self.setGeometry(100, 100, 800, 600)
        
        # Main layout
        layout = QVBoxLayout()

        # URL input
        self.url_label = QLabel("TakeandSend.png")
        self.url_input = QLineEdit()
        self.url_input.setText("https://jsonplaceholder.typicode.com/posts")
        
        # Request type dropdown
        self.request_type = QComboBox()
        self.request_type.addItems(["GET", "POST", "PUT", "DELETE"])
        
        # Send request button
        self.send_button = QPushButton("Send Request")
        self.send_button.clicked.connect(self.send_request)
        
        # Response display
        self.response_area = QTextEdit()
        self.response_area.setReadOnly(True)
        
        # Save response button
        self.save_button = QPushButton("Save Response")
        self.save_button.clicked.connect(self.save_response)
        
        # Adding widgets to layout
        layout.addWidget(self.url_label)
        layout.addWidget(self.url_input)
        layout.addWidget(self.request_type)
        layout.addWidget(self.send_button)
        layout.addWidget(self.response_area)
        layout.addWidget(self.save_button)
        
        # Setting the central widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def send_request(self):
        url = self.url_input.text()
        method = self.request_type.currentText()
        
        try:
            if method == "GET":
                response = requests.get(url)
            elif method == "POST":
                response = requests.post(url)
            elif method == "PUT":
                response = requests.put(url)
            elif method == "DELETE":
                response = requests.delete(url)
            
            self.response_area.setText(response.text)
        except Exception as e:
            self.response_area.setText(f"Error: {str(e)}")

    def save_response(self):
        response_text = self.response_area.toPlainText()
        if response_text:
            options = QFileDialog.Options()
            file_path, _ = QFileDialog.getSaveFileName(self, "Save Response", os.getcwd(), "Text Files (*.txt)", options=options)
            if file_path:
                with open(file_path, 'w') as file:
                    file.write(response_text)

if __name__ == '__main__':
    app = QApplication([])
    client = JsonPlaceholderClient()
    client.show()
    app.exec()
