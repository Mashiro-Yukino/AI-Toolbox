#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 06:03:09 2023

@author: mu
"""

# api_toolbox.py


from config import fetch_tools
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout,
                             QScrollArea, QWidget, QLabel)
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QComboBox, QLineEdit, QPushButton, QTextEdit, QWidget
import importlib


# class API_Toolbox(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("API Toolbox")
#         self.resize(600, 400)
#
#         self.initUI()
#
#     def initUI(self):
#         layout = QVBoxLayout()
#
#         self.tool_label = QLabel("Select an API tool:")
#         layout.addWidget(self.tool_label)
#
#         self.tool_combobox = QComboBox()
#         tools_by_type = [tool["name"]
#                          for tool in AI_tools if tool["type"] == "API"]
#         self.tool_combobox.addItems(tools_by_type)
#         layout.addWidget(self.tool_combobox)
#
#         self.prompt_label = QLabel("Enter your prompt:")
#         layout.addWidget(self.prompt_label)
#
#         self.prompt_entry = QLineEdit()
#         layout.addWidget(self.prompt_entry)
#
#         self.submit_button = QPushButton("Generate Text")
#         self.submit_button.clicked.connect(self.generate_text_from_tool)
#         layout.addWidget(self.submit_button)
#
#         self.result_label = QLabel("Generated Text:")
#         layout.addWidget(self.result_label)
#
#         self.result_text = QTextEdit()
#         self.result_text.setReadOnly(True)
#         layout.addWidget(self.result_text)
#
#         self.back_button = QPushButton("Back")
#         self.back_button.clicked.connect(self.go_back_to_cover)
#         layout.addWidget(self.back_button)
#
#         self.setLayout(layout)
#
#     def generate_text_from_tool(self):
#         selected_tool = self.tool_combobox.currentText()
#
#         for tool in AI_tools:
#             if tool["name"] == selected_tool:
#                 if tool["type"] == "API":
#                     module = __import__(tool["module_name"])
#                     generate_text_function = getattr(
#                         module, tool["function_name"])
#
#                     prompt = self.prompt_entry.text()
#                     generated_text = generate_text_function(prompt)
#
#                     self.result_text.setPlainText(generated_text)
#
#     def go_back_to_cover(self):
#         self.close()
#         CoverPage = importlib.import_module("cover_page").CoverPage
#         self.cover_page = CoverPage()
#         self.cover_page.show()


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 06:03:09 2023

@author: mu
"""


class API_Toolbox(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("API Toolbox")
        self.resize(600, 300)

        self.initUI()

    def initUI(self):
        tools = fetch_tools("API")

        layout = QVBoxLayout()

        for tool in tools:
            tool_label = QLabel(
                f"{tool['name']}: {tool['module_name']}.{tool['function_name']}")

            layout.addWidget(tool_label)

        scroll_widget = QWidget()
        scroll_widget.setLayout(layout)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(scroll_widget)

        self.setCentralWidget(scroll_area)


if __name__ == "__main__":
    app = QApplication([])
    window = API_Toolbox()
    window.show()
    app.exec_()
