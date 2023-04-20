#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 21:08:23 2023

@author: mu
"""

# gpt3_module.py

# Import the required libraries and modules
import openai
from config import API_KEYS

# Set the API key for the OpenAI library
openai.api_key = API_KEYS['openai']

# Function to generate text using GPT-3


def generate_text(prompt):
    # Call the OpenAI API to generate text using the specified engine (model)
    response = openai.Completion.create(
        engine="text-davinci-002",  # Use the "text-davinci-002" model
        prompt=prompt,  # Pass the input prompt
        # Set the maximum number of tokens (words) in the response
        max_tokens=150,
        n=1,  # Number of generated responses
        stop=None,  # No specific token to stop the generation
        # Controls the creativity of the response (lower value: more focused, higher value: more random)
        temperature=0.5,
    )

    # Return the generated text from the first response choice, removing leading and trailing whitespace
    return response.choices[0].text.strip()
