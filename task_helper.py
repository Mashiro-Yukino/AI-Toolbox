from config import fetch_tools
import openai
from config import API_KEYS
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
import nltk


class TaskHelper:
    def __init__(self, task_description):
        self.task_description = task_description

        # Set the API key for the OpenAI library
        openai.api_key = API_KEYS['openai']

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
        AI_tools = fetch_tools("API")

        # Remove stop words from tool keywords
        stop_words = set(stopwords.words('english'))
        for tool in AI_tools:
            tool["keywords"] = [word for word in tool["keywords"].split() if word not in stop_words]
            tool["keywords"] = ' '.join(tool["keywords"])

        # Filter out tools with keywords that contain only stop words
        AI_tools = [tool for tool in AI_tools if tool["keywords"]]

        # Combine keywords of each tool into a single string
        tools_keywords = [tool["keywords"] for tool in AI_tools]

        # Add the step as the first element in the list
        tools_keywords.insert(0, step)

        vectorizer = TfidfVectorizer(stop_words='english')
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

