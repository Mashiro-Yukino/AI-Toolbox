#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 06:03:56 2023

@author: mu
"""


from PyQt5.QtCore import Qt
from config import fetch_tools
import webbrowser
import importlib
from PyQt5.QtWidgets import QPushButton

from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QScrollArea, QWidget
import sqlite3


class Web_Toolbox(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Web Toolbox")
        self.resize(600, 300)

        self.initUI()

    def initUI(self):
        tools = fetch_tools("Web")

        layout = QVBoxLayout()

        for tool in tools:
            tool_label = QLabel(
                f'<a href="{tool["website"]}">{tool["name"]}</a>')
            tool_label.setOpenExternalLinks(True)
            tool_label.setTextInteractionFlags(Qt.TextBrowserInteraction)
            tool_label.setWordWrap(True)

            layout.addWidget(tool_label)

        # Add the Back button
        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.close)
        # Set the button color to blue
        self.back_button.setStyleSheet("background-color: blue; color: white")
        layout.addWidget(self.back_button)

        scroll_widget = QWidget()
        scroll_widget.setLayout(layout)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(scroll_widget)

        self.setCentralWidget(scroll_area)


if __name__ == "__main__":
    app = QApplication([])
    window = Web_Toolbox()
    window.show()
    app.exec_()
