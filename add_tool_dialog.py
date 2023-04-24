#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 10:43:47 2023

@author: mu
"""


from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
import config
import pickle
import sqlite3

# class AddToolDialog(QDialog):
#     def __init__(self, parent=None):
#         super(AddToolDialog, self).__init__(parent)
#
#         layout = QVBoxLayout()
#
#         self.name_label = QLabel("Tool Name")
#         layout.addWidget(self.name_label)
#         self.name_input = QLineEdit()
#         layout.addWidget(self.name_input)
#
#         self.keywords_label = QLabel("Keywords (comma separated)")
#         layout.addWidget(self.keywords_label)
#         self.keywords_input = QLineEdit()
#         layout.addWidget(self.keywords_input)
#
#         self.save_button = QPushButton("Save Tool")
#         self.save_button.clicked.connect(self.save_tool)
#         layout.addWidget(self.save_button)
#
#         self.setLayout(layout)
#
#     def save_tool(self):
#         tool_name = self.name_input.text().strip()
#         tool_keywords = [kw.strip()
#                          for kw in self.keywords_input.text().split(',')]
#
#         new_tool = {
#             "name": tool_name,
#             "keywords": tool_keywords
#         }
#
#         config.AI_tools.append(new_tool)
#
#         with open('ai_tools.pkl', 'wb') as f:
#             pickle.dump(config.AI_tools, f)
#
#         self.accept()
#
#     def add_ai_tool(self, name, tool_type, keywords):
#         conn = sqlite3.connect("ai_tools.db")
#         c = conn.cursor()
#         c.execute("INSERT INTO ai_tools (name, type, keywords) VALUES (?, ?, ?)",
#                   (name, tool_type, ', '.join(keywords)))
#         conn.commit()
#         conn.close()


from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QLineEdit, QComboBox, QFormLayout, QMessageBox
import sqlite3  # Add this line at the beginning of the file

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
            QMessageBox.warning(self, "Incomplete Information", "Please fill in the required fields.")
            return

        conn = sqlite3.connect("ai_tools.db")
        c = conn.cursor()
        c.execute("INSERT INTO ai_tools (name, type, keywords) VALUES (?, ?, ?)", (name, tool_type, ', '.join(keywords)))
        conn.commit()
        conn.close()

        self.accept()
