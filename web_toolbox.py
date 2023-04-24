#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 06:03:56 2023

@author: mu
"""


from config import fetch_tools
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout,
                             QScrollArea, QWidget, QLabel)
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QComboBox, QPushButton, QWidget
import webbrowser
import importlib


# class Web_Toolbox(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("Web Toolbox")
#         self.resize(600, 400)
#
#         self.initUI()
#
#     def initUI(self):
#         layout = QVBoxLayout()
#
#         self.tool_label = QLabel("Select a Web tool:")
#         layout.addWidget(self.tool_label)
#
#         self.tool_combobox = QComboBox()
#         tools_by_type = [tool["name"]
#                          for tool in AI_tools if tool["type"] == "Web"]
#         self.tool_combobox.addItems(tools_by_type)
#         layout.addWidget(self.tool_combobox)
#
#         self.open_link_button = QPushButton("Open Link")
#         self.open_link_button.clicked.connect(self.open_link_for_tool)
#         layout.addWidget(self.open_link_button)
#
#         self.back_button = QPushButton("Back")
#         self.back_button.clicked.connect(self.go_back_to_cover)
#         layout.addWidget(self.back_button)
#
#         self.setLayout(layout)
#
#     def open_link_for_tool(self):
#         selected_tool = self.tool_combobox.currentText()
#
#         for tool in AI_tools:
#             if tool["name"] == selected_tool:
#                 if tool["type"] == "Web":
#                     webbrowser.open(tool["website"])
#
#     def go_back_to_cover(self):
#         self.close()
#         CoverPage = importlib.import_module("cover_page").CoverPage
#         self.cover_page = CoverPage()
#         self.cover_page.show()


from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QLabel, QScrollArea, QWidget
import sqlite3  # Add this line at the beginning of the file


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 06:03:09 2023

@author: mu
"""


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
            tool_label = QLabel(f"{tool['name']}: {tool['website']}")

            layout.addWidget(tool_label)

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
