#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 10:43:47 2023

@author: mu
"""


from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
import config
import pickle


class AddToolDialog(QDialog):
    def __init__(self, parent=None):
        super(AddToolDialog, self).__init__(parent)

        layout = QVBoxLayout()

        self.name_label = QLabel("Tool Name")
        layout.addWidget(self.name_label)
        self.name_input = QLineEdit()
        layout.addWidget(self.name_input)

        self.keywords_label = QLabel("Keywords (comma separated)")
        layout.addWidget(self.keywords_label)
        self.keywords_input = QLineEdit()
        layout.addWidget(self.keywords_input)

        self.save_button = QPushButton("Save Tool")
        self.save_button.clicked.connect(self.save_tool)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def save_tool(self):
        tool_name = self.name_input.text().strip()
        tool_keywords = [kw.strip()
                         for kw in self.keywords_input.text().split(',')]

        new_tool = {
            "name": tool_name,
            "keywords": tool_keywords
        }

        config.AI_tools.append(new_tool)

        with open('ai_tools.pkl', 'wb') as f:
            pickle.dump(config.AI_tools, f)

        self.accept()
