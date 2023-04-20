#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 07:45:32 2023

@author: mu
"""

import numpy as np
from config import AI_tools
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Extract textual features
text_data = []
for tool in AI_tools:
    text_data.append(" ".join([tool["name"], tool["type"], tool.get(
        "module_name", ""), tool.get("function_name", "")]))

# Vectorize the text data using the TfidfVectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(text_data)

# Perform K-Means clustering
num_clusters = 2
kmeans = KMeans(n_clusters=num_clusters, random_state=0).fit(X)

# Print the clustering result
print("Clustering result:")
for idx, label in enumerate(kmeans.labels_):
    print(f"{AI_tools[idx]['name']} belongs to cluster {label}")


def cluster_ai_tools(ai_tools):
    # Extract text data from the AI tools list
    text_data = [tool["name"] for tool in ai_tools]

    # Vectorize the text data using the TfidfVectorizer
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(text_data)

    # Perform K-Means clustering
    num_clusters = 2
    kmeans = KMeans(n_clusters=num_clusters, random_state=0).fit(X)

    # Return the clustering result as a list of tuples
    return [(ai_tools[idx]["name"], label) for idx, label in enumerate(kmeans.labels_)]
