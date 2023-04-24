#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 06:03:09 2023

@author: mu
"""

# api_toolbox.py


from task_helper import TaskHelper
from config import fetch_tools
from PyQt5.QtWidgets import (QApplication, QMainWindow, QVBoxLayout,
                             QScrollArea, QWidget, QLabel)
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QComboBox, QLineEdit, QPushButton, QTextEdit, QWidget
import importlib

import openai
from config import API_KEYS


class API_Toolbox(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("API Toolbox")
        self.resize(600, 400)

        # Set the API key for the OpenAI library
        openai.api_key = API_KEYS['openai']

        self.initUI()

    def initUI(self):
        tools = fetch_tools("API")

        layout = QVBoxLayout()

        self.tool_combobox = QComboBox()
        tools_by_type = [tool["name"] for tool in tools]
        self.tool_combobox.addItems(tools_by_type)
        layout.addWidget(self.tool_combobox)

        self.prompt_label = QLabel("Enter your prompt:")
        layout.addWidget(self.prompt_label)

        self.prompt_entry = QLineEdit()
        layout.addWidget(self.prompt_entry)

        self.submit_button = QPushButton("Generate Text")
        self.submit_button.clicked.connect(self.generate_text_from_tool)
        layout.addWidget(self.submit_button)

        self.result_label = QLabel("Generated Text:")
        layout.addWidget(self.result_label)

        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        layout.addWidget(self.result_text)

        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.close)
        self.back_button.setStyleSheet("background-color: blue; color: white")
        layout.addWidget(self.back_button)

        scroll_widget = QWidget()
        scroll_widget.setLayout(layout)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(scroll_widget)

        self.setCentralWidget(scroll_area)

    def generate_text_from_tool(self):
        selected_tool = self.tool_combobox.currentText()
        prompt = self.prompt_entry.text()

        for tool in fetch_tools("API"):
            if tool["name"] == selected_tool:
                task_helper = TaskHelper(prompt)
                steps_with_tools = task_helper.get_steps_and_tools()

                generated_text = "Steps and Tools:\n"
                for step_with_tool in steps_with_tools:
                    step = step_with_tool['step']
                    tools = ', '.join([tool['name']
                                      for tool in step_with_tool['tools']])
                    generated_text += f"{step}: {tools}\n"

                self.result_text.setPlainText(generated_text)


if __name__ == "__main__":
    app = QApplication([])
    window = API_Toolbox()
    window.show()
    app.exec_()
