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


class ClusteringResultDialog(QDialog):
    def __init__(self, parent=None):
        super(ClusteringResultDialog, self).__init__(parent)
        self.setWindowTitle("Clustering Result")
        self.resize(300, 400)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        clustering_result = self.cluster_ai_tools(AI_tools)
        clusters = defaultdict(list)

        for tool, label in clustering_result:
            clusters[label].append(tool)

        for label, tools in clusters.items():
            cluster_label = QLabel(f"Cluster {label + 1}:")
            layout.addWidget(cluster_label)

            for tool in tools:
                tool_label = QLabel(f"  - {tool['name']}")
                tool_label.setTextInteractionFlags(Qt.TextBrowserInteraction)
                tool_label.setOpenExternalLinks(True)
                if tool["type"] == "Web":
                    tool_label.setText(
                        f'  - <a href="{tool["website"]}">{tool["name"]}</a>')
                else:
                    tool_label.setText(f"  - {tool['name']}")
                layout.addWidget(tool_label)

            layout.addSpacing(10)

        self.back_button = QPushButton("Go Back")
        self.back_button.clicked.connect(self.close)
        layout.addWidget(self.back_button)

        container = QWidget()
        container.setLayout(layout)

        scroll = QScrollArea()
        scroll.setWidget(container)
        scroll.setWidgetResizable(True)

        layout = QVBoxLayout(self)
        layout.addWidget(scroll)

    def cluster_ai_tools(self, ai_tools):
        text_data = [tool["name"] + " " + tool["type"] for tool in ai_tools]

        vectorizer = TfidfVectorizer()
        X = vectorizer.fit_transform(text_data)

        num_clusters = 2
        kmeans = KMeans(n_clusters=num_clusters, random_state=0).fit(X)

        return [(ai_tools[idx], label) for idx, label in enumerate(kmeans.labels_)]


if __name__ == "__main__":
    app = QApplication([])
    window = CoverPage()
    window.show()
    app.exec_()
