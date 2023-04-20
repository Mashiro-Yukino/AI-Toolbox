#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 06:03:09 2023

@author: mu
"""

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QLabel, QScrollArea, QWidget, QDialog
from PyQt5.QtCore import Qt
from api_toolbox import API_Toolbox
from config import AI_tools
from collections import defaultdict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from web_toolbox import Web_Toolbox
from clustering_result_dialog import ClusteringResultDialog


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


if __name__ == "__main__":
    app = QApplication([])
    window = CoverPage()
    window.show()
    app.exec_()
