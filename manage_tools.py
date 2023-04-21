#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 10:57:11 2023

@author: mu
"""


import pickle
import sys
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox


class ManageToolsDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.tool_name_label = QLabel("Tool Name:")
        layout.addWidget(self.tool_name_label)

        self.tool_name_input = QLineEdit()
        layout.addWidget(self.tool_name_input)

        self.tool_keywords_label = QLabel("Keywords (comma separated):")
        layout.addWidget(self.tool_keywords_label)

        self.tool_keywords_input = QLineEdit()
        layout.addWidget(self.tool_keywords_input)

        self.add_tool_button = QPushButton("Add Tool")
        self.add_tool_button.clicked.connect(self.add_tool)
        layout.addWidget(self.add_tool_button)

        self.setLayout(layout)
        self.setWindowTitle("Manage AI Tools")

    def add_tool(self):
        tool_name = self.tool_name_input.text().strip()
        tool_keywords = [keyword.strip()
                         for keyword in self.tool_keywords_input.text().split(',')]

        if not tool_name or not tool_keywords:
            QMessageBox.warning(
                self, "Error", "Please enter a tool name and at least one keyword.")
            return

        new_tool = {
            "name": tool_name,
            "keywords": tool_keywords
        }

        with open('ai_tools.pkl', 'rb') as f:
            AI_tools = pickle.load(f)

        AI_tools.append(new_tool)

        with open('ai_tools.pkl', 'wb') as f:
            pickle.dump(AI_tools, f)

        QMessageBox.information(
            self, "Success", f"Tool '{tool_name}' added successfully.")
        self.tool_name_input.clear()
        self.tool_keywords_input.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    manage_tools_dialog = ManageToolsDialog()
    manage_tools_dialog.show()
    sys.exit(app.exec_())
