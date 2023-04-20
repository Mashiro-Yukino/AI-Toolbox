#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 21:09:58 2023

@author: mu
"""

# Import the required libraries and modules
import tkinter as tk
from tkinter import ttk
from gpt3_module import generate_text as generate_text_gpt3
from myai_module import generate_text as generate_text_myai

# Define the main AI_Toolbox class, which inherits from tk.Tk


class AI_Toolbox(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set the window title and size
        self.title("AI Toolbox")
        self.geometry("600x400")

        # Create and display the widgets in the window
        self.create_widgets()

    # Method to create and display widgets
    def create_widgets(self):
        # Create and display the "Enter your prompt" label
        self.prompt_label = ttk.Label(self, text="Enter your prompt:")
        self.prompt_label.pack(pady=10)

        # Create and display the prompt entry field
        self.prompt_entry = ttk.Entry(self, width=50)
        self.prompt_entry.pack(pady=10)

        # Create and display the "Generate Text" button
        self.submit_button = ttk.Button(
            self, text="Generate Text", command=self.generate_text_from_gpt3)
        self.submit_button.pack(pady=10)

        self.submit_button_myai = ttk.Button(
            self, text="Generate Text (MyAI)", command=self.generate_text_from_myai)
        self.submit_button_myai.pack(pady=10)

        # Create and display the "Generated Text" label
        self.result_label = ttk.Label(self, text="Generated Text:")
        self.result_label.pack(pady=10)

        # Create and display the text area to show the generated text
        self.result_text = tk.Text(self, wrap=tk.WORD, width=50, height=10)
        self.result_text.pack(pady=10)

    # Method to generate text using GPT-3 and display it in the result_text widget
    def generate_text_from_gpt3(self):
        # Get the input prompt from the entry field
        prompt = self.prompt_entry.get()

        # Call the generate_text function from gpt3_module to get the generated text
        generated_text = generate_text(prompt)

        # Clear the result_text widget and insert the generated text
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, generated_text)

    def generate_text_from_myai(self):
        prompt = self.prompt_entry.get()
        generated_text = generate_text_myai(prompt)
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, generated_text)


# Run the AI_Toolbox application
if __name__ == "__main__":
    app = AI_Toolbox()
    app.mainloop()
