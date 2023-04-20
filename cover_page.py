#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 06:02:21 2023

@author: mu
"""


from PyQt5.QtWidgets import QVBoxLayout, QLabel, QComboBox, QPushButton, QWidget
from config import AI_tools
from api_toolbox import API_Toolbox
from web_toolbox import Web_Toolbox


class CoverPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("AI Toolbox Cover Page")
        self.resize(300, 200)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.type_label = QLabel("Select a tool type:")
        layout.addWidget(self.type_label)

        self.type_combobox = QComboBox()
        self.type_combobox.addItems(
            list(set([tool["type"] for tool in AI_tools])))
        layout.addWidget(self.type_combobox)

        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.open_toolbox)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def open_toolbox(self):
        selected_type = self.type_combobox.currentText()

        if selected_type == "API":
            self.api_toolbox = API_Toolbox()
            self.api_toolbox.show()
            self.close()
        elif selected_type == "Web":
            self.web_toolbox = Web_Toolbox()
            self.web_toolbox.show()
            self.close()
