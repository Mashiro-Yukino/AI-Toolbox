import config
import pickle
import sqlite3
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QLineEdit, QComboBox, QFormLayout, QMessageBox


class AddToolDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Add AI Tool")
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        form_layout = QFormLayout()

        self.name_input = QLineEdit()
        form_layout.addRow("Name:", self.name_input)

        self.type_input = QComboBox()
        self.type_input.addItem("API")
        self.type_input.addItem("Web")
        form_layout.addRow("Type:", self.type_input)

        self.keywords_input = QLineEdit()
        form_layout.addRow("Keywords (comma-separated):", self.keywords_input)

        layout.addLayout(form_layout)

        add_tool_button = QPushButton("Add AI Tool")
        add_tool_button.clicked.connect(self.add_ai_tool)
        layout.addWidget(add_tool_button)

        self.setLayout(layout)

    def add_ai_tool(self):
        name = self.name_input.text().strip()
        tool_type = self.type_input.currentText()
        keywords = self.keywords_input.text().strip().split(',')

        if not name or not keywords:
            QMessageBox.warning(self, "Incomplete Information",
                                "Please fill in the required fields.")
            return

        conn = sqlite3.connect("ai_tools.db")
        c = conn.cursor()
        c.execute("INSERT INTO ai_tools (name, type, keywords) VALUES (?, ?, ?)",
                  (name, tool_type, ', '.join(keywords)))
        conn.commit()
        conn.close()

        self.accept()
