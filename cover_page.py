#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 06:03:09 2023

@author: mu
"""

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QScrollArea, QWidget, QDialog
from api_toolbox import API_Toolbox
from PyQt5.QtWidgets import QInputDialog, QMessageBox
from task_helper import TaskHelper
from web_toolbox import Web_Toolbox
from clustering_result_dialog import ClusteringResultDialog
from add_tool_dialog import AddToolDialog
from manage_tools import ManageToolsDialog


class CoverPage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("AI Toolbox")
        self.resize(300, 200)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.api_toolbox_button = QPushButton("API Toolbox")
        self.api_toolbox_button.clicked.connect(self.open_api_toolbox)
        layout.addWidget(self.api_toolbox_button)

        self.web_toolbox_button = QPushButton("Web Toolbox")
        self.web_toolbox_button.clicked.connect(self.open_web_toolbox)
        layout.addWidget(self.web_toolbox_button)

        self.cluster_button = QPushButton("Cluster AI Tools")
        self.cluster_button.clicked.connect(self.open_clustering_result)
        layout.addWidget(self.cluster_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.task_helper_button = QPushButton("Task Helper")
        self.task_helper_button.clicked.connect(self.open_task_helper)
        layout.addWidget(self.task_helper_button)

        # In the CoverPage class, add the following lines in the constructor
        self.add_tool_button = QPushButton("Add Tool")
        self.add_tool_button.clicked.connect(self.open_add_tool_dialog)
        layout.addWidget(self.add_tool_button)

        self.manage_tools_button = QPushButton("Manage AI Tools", self)
        self.manage_tools_button.clicked.connect(self.open_manage_tools_dialog)
        self.manage_tools_button.setGeometry(250, 300, 200, 40)
        layout.addWidget(self.manage_tools_button)

    def open_api_toolbox(self):
        self.close()
        self.api_toolbox = API_Toolbox()
        self.api_toolbox.show()

    def open_web_toolbox(self):
        self.web_toolbox = Web_Toolbox()
        self.web_toolbox.show()

    def open_clustering_result(self):
        self.clustering_result_dialog = ClusteringResultDialog(self)
        self.clustering_result_dialog.show()

    def open_task_helper(self):
        task_description, ok = QInputDialog.getText(
            self, "Task Helper", "Enter the task you want to perform:")

        if ok and task_description:
            task_helper = TaskHelper(task_description)
            steps_and_tools = task_helper.get_steps_and_tools()

            message = ""
            for idx, step_with_tools in enumerate(steps_and_tools, 1):
                message += f"Step {idx}: {step_with_tools['step']}\nAI Tools:\n"
                for tool in step_with_tools["tools"]:
                    message += f"  - {tool['name']}\n"
                message += "\n"

            QMessageBox.information(self, "Task Helper Results", message)

    # Add the open_add_tool_dialog method to the CoverPage class
    def open_add_tool_dialog(self):
        add_tool_dialog = AddToolDialog(self)
        add_tool_dialog.exec_()

    def open_manage_tools_dialog(self):
        self.manage_tools_dialog = ManageToolsDialog()
        self.manage_tools_dialog.exec_()


if __name__ == "__main__":
    app = QApplication([])
    window = CoverPage()
    window.show()
    app.exec_()
