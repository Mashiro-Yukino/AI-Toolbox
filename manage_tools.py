#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 10:57:11 2023

@author: mu
"""


import sys
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
import sqlite3


import sqlite3  # Add this line at the beginning of the file
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QLineEdit, QComboBox, QFormLayout, QMessageBox


class ManageToolsDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Manage AI Tools")
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        ai_tools = self.get_ai_tools()
        for tool in ai_tools:
            tool_layout = QHBoxLayout()
            tool_layout.addWidget(QLabel(f"ID: {tool['id']}"))
            tool_layout.addWidget(QLabel(tool['name']))
            tool_layout.addWidget(QLabel(tool['type']))
            tool_layout.addWidget(QLabel(', '.join(tool['keywords'])))
            layout.addLayout(tool_layout)

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

    def get_ai_tools(self):
        conn = sqlite3.connect("ai_tools.db")
        c = conn.cursor()
        c.execute("SELECT * FROM ai_tools")
        tools = c.fetchall()
        conn.close()

        ai_tools = []
        for tool in tools:
            ai_tool = {
                "id": tool[0],
                "name": tool[1],
                "type": tool[2],
                "keywords": tool[3].split(', ')
            }
            ai_tools.append(ai_tool)
        return ai_tools

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    manage_tools_dialog = ManageToolsDialog()
    manage_tools_dialog.show()
    sys.exit(app.exec_())
