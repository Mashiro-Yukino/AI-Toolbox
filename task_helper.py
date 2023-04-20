#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 12:02:46 2023

@author: mu
"""

import openai
from config import AI_tools
# Import the required libraries and modules
import openai
from config import API_KEYS
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Set the API key for the OpenAI library
openai_api_key = API_KEYS['openai']


class TaskHelper:
    def __init__(self, task_description):
        self.task_description = task_description

    def get_steps_and_tools(self):
        steps = self.generate_steps_with_gpt3()
        steps_with_tools = self.assign_tools_to_steps(steps)
        return steps_with_tools

    def generate_steps_with_gpt3(self):
        prompt = f"Please provide a list of steps to perform the following task: {self.task_description}"
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.5,
        )
        steps = response.choices[0].text.strip().split("\n")
        return steps

    def assign_tools_to_steps(self, steps):
        steps_with_tools = []
        for step in steps:
            tools = self.find_relevant_tools(step)
            steps_with_tools.append({"step": step, "tools": tools})
        return steps_with_tools

    def find_relevant_tools(self, step):
        relevant_tools = []

        # Combine keywords of each tool into a single string
        tools_keywords = [' '.join(tool["keywords"]) for tool in AI_tools]

        # Add the step as the first element in the list
        tools_keywords.insert(0, step)

        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform(tools_keywords)

        # Calculate cosine similarity between the step and each tool
        step_vector = vectors[0]
        tools_vectors = vectors[1:]
        similarities = cosine_similarity(step_vector, tools_vectors)

        # Get indices of tools sorted by their similarity in descending order
        sorted_indices = similarities.argsort(axis=1)[:, ::-1].flatten()

        # Add tools to the relevant_tools list based on their sorted similarity
        for index in sorted_indices:
            relevant_tools.append(AI_tools[index])

        return relevant_tools
