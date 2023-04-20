#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 11:54:12 2023

@author: mu
"""


from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QScrollArea, QWidget, QPushButton
from PyQt5.QtCore import Qt
from collections import defaultdict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from config import AI_tools


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
