from PyQt5.QtWidgets import QVBoxLayout, QLabel, QComboBox, QLineEdit, QPushButton, QTextEdit
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QComboBox, QPushButton
from PyQt5.QtCore import Qt
from config import AI_tools
import webbrowser
from gpt3_module import generate_text


class CoverPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("AI Toolbox Cover Page")
        self.resize(300, 200)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.type_label = QLabel("Select a tool type:")
        layout.addWidget(self.type_label)

        self.type_combobox = QComboBox()
        self.type_combobox.addItems(
            list(set([tool["type"] for tool in AI_tools])))
        layout.addWidget(self.type_combobox)

        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.open_toolbox)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def open_toolbox(self):
        selected_type = self.type_combobox.currentText()

        if selected_type == "API":
            self.api_toolbox = API_Toolbox()
            self.api_toolbox.show()
            self.close()
        elif selected_type == "Web":
            self.web_toolbox = Web_Toolbox()
            self.web_toolbox.show()
            self.close()


class API_Toolbox(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("API Toolbox")
        self.resize(600, 400)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.tool_label = QLabel("Select an API tool:")
        layout.addWidget(self.tool_label)

        self.tool_combobox = QComboBox()
        tools_by_type = [tool["name"]
                         for tool in AI_tools if tool["type"] == "API"]
        self.tool_combobox.addItems(tools_by_type)
        layout.addWidget(self.tool_combobox)

        self.prompt_label = QLabel("Enter your prompt:")
        layout.addWidget(self.prompt_label)

        self.prompt_entry = QLineEdit()
        layout.addWidget(self.prompt_entry)

        self.submit_button = QPushButton("Generate Text")
        self.submit_button.clicked.connect(self.generate_text_from_tool)
        layout.addWidget(self.submit_button)

        self.result_label = QLabel("Generated Text:")
        layout.addWidget(self.result_label)

        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)
        layout.addWidget(self.result_text)

        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.go_back_to_cover)
        layout.addWidget(self.back_button)

        self.setLayout(layout)

    def generate_text_from_tool(self):
        selected_tool = self.tool_combobox.currentText()

        for tool in AI_tools:
            if tool["name"] == selected_tool:
                if tool["type"] == "API":
                    module = __import__(tool["module_name"])
                    generate_text_function = getattr(module, tool["function_name"])

                    prompt = self.prompt_entry.text()
                    generated_text = generate_text_function(prompt)

                    self.result_text.setPlainText(generated_text)

    def go_back_to_cover(self):
        self.close()
        self.cover_page = CoverPage()
        self.cover_page.show()



class Web_Toolbox(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Web Toolbox")
        self.resize(600, 400)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.tool_label = QLabel("Select a Web tool:")
        layout.addWidget(self.tool_label)

        self.tool_combobox = QComboBox()
        tools_by_type = [tool["name"]
                         for tool in AI_tools if tool["type"] == "Web"]
        self.tool_combobox.addItems(tools_by_type)
        layout.addWidget(self.tool_combobox)

        self.open_link_button = QPushButton("Open Link")
        self.open_link_button.clicked.connect(self.open_link_for_tool)
        layout.addWidget(self.open_link_button)

        self.back_button = QPushButton("Back")
        self.back_button.clicked.connect(self.go_back_to_cover)
        layout.addWidget(self.back_button)

        self.setLayout(layout)

    def open_link_for_tool(self):
        selected_tool = self.tool_combobox.currentText()

        for tool in AI_tools:
            if tool["name"] == selected_tool:
                if tool["type"] == "Web":
                    webbrowser.open(tool["website"])

    def go_back_to_cover(self):
        self.close()
        self.cover_page = CoverPage()
        self.cover_page.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    cover_page = CoverPage()
    cover_page.show()
    sys.exit(app.exec_())
