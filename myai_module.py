#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 21:24:34 2023

@author: mu
"""

# myai_module.py
import requests


def generate_text(prompt):
    # Replace the following URL and API_KEY with your MyAI tool's API endpoint and key
    MYAI_API_URL = "https://api.myai.com/generate"
    MYAI_API_KEY = "your_myai_api_key"

    response = requests.post(
        MYAI_API_URL,
        headers={"Authorization": f"Bearer {MYAI_API_KEY}"},
        json={"prompt": prompt}
    )

    if response.status_code == 200:
        return response.json()['generated_text']
    else:
        return f"Error: {response.status_code}, {response.text}"
