#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 06:03:56 2023

@author: mu
"""


from PyQt5.QtWidgets import QVBoxLayout, QLabel, QComboBox, QPushButton, QWidget
import webbrowser
from config import AI_tools
import importlib


class Web_Toolbox(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Web Toolbox")
        self.resize(600, 400)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.tool_label = QLabel("Select a Web tool:")
        layout.addWidget(self.tool_label)

        self.tool_combobox = QComboBox()
        tools_by_type = [tool["name"]
                         for tool in AI_tools if tool["type"] == "Web"]
        self.tool_combobox.addItems(tools_by_type)
        layout.addWidget(self.tool_combobox)

        self.open_link_button = QPushButton("Open Link")
        self.open_link_button.clicked.connect(self.open_link_for_tool)
        layout.addWidget(self.open_link_button)

        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.go_back_to_cover)
        layout.addWidget(self.back_button)

        self.setLayout(layout)

    def open_link_for_tool(self):
        selected_tool = self.tool_combobox.currentText()

        for tool in AI_tools:
            if tool["name"] == selected_tool:
                if tool["type"] == "Web":
                    webbrowser.open(tool["website"])

    def go_back_to_cover(self):
        self.close()
        CoverPage = importlib.import_module("cover_page").CoverPage
        self.cover_page = CoverPage()
        self.cover_page.show()
