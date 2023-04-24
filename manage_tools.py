import sys
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QLineEdit, QComboBox, QFormLayout, QMessageBox
import sqlite3
from config import fetch_tools


class ManageToolsDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Manage AI Tools")
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.ai_tools = self.get_ai_tools()
        self.tools_layout = QVBoxLayout()
        self.refresh_tools_layout()
        layout.addLayout(self.tools_layout)

        form_layout = QFormLayout()

        self.tool_id_input = QLineEdit()
        form_layout.addRow("Tool ID (for modify/delete):", self.tool_id_input)

        self.name_input = QLineEdit()
        form_layout.addRow("Name:", self.name_input)

        self.type_input = QComboBox()
        self.type_input.addItem("API")
        self.type_input.addItem("Web")
        form_layout.addRow("Type:", self.type_input)

        self.keywords_input = QLineEdit()
        form_layout.addRow("Keywords (comma-separated):", self.keywords_input)

        layout.addLayout(form_layout)

        add_tool_button = QPushButton("Add AI Tool")
        add_tool_button.clicked.connect(self.add_ai_tool)
        layout.addWidget(add_tool_button)

        modify_tool_button = QPushButton("Modify AI Tool")
        modify_tool_button.clicked.connect(self.modify_ai_tool)
        layout.addWidget(modify_tool_button)

        delete_tool_button = QPushButton("Delete AI Tool")
        delete_tool_button.clicked.connect(self.delete_ai_tool)
        layout.addWidget(delete_tool_button)

        self.setLayout(layout)

    def get_ai_tools(self):
        tools = fetch_tools("all")
        ai_tools = [
            {
                "id": tool["id"],
                "name": tool["name"],
                "type": tool["type"],
                "module_name": tool["module_name"],
                "function_name": tool["function_name"],
                "website": tool["website"],
                "keywords": tool["keywords"].split(', ')
            }
            for tool in tools
        ]
        return ai_tools

    def refresh_tools_layout(self):
        self.ai_tools = self.get_ai_tools()

        # Clear previous layout
        while self.tools_layout.count():
            child = self.tools_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
            elif child.layout():
                while child.layout().count():
                    sub_child = child.layout().takeAt(0)
                    if sub_child.widget():
                        sub_child.widget().deleteLater()

        # Add updated AI tools
        for tool in self.ai_tools:
            tool_layout = QHBoxLayout()
            tool_layout.addWidget(QLabel(f"ID: {tool['id']}"))
            tool_layout.addWidget(QLabel(tool['name']))
            tool_layout.addWidget(QLabel(tool['type']))
            tool_layout.addWidget(QLabel(', '.join(tool['keywords'])))
            self.tools_layout.addLayout(tool_layout)

    def add_ai_tool(self):
        name = self.name_input.text().strip()
        tool_type = self.type_input.currentText()
        keywords = self.keywords_input.text().strip().split(',')

        if not name or not keywords:
            QMessageBox.warning(self, "Incomplete Information",
                                "Please fill in the required fields.")
            return

        conn = sqlite3.connect("ai_tools.db")
        c = conn.cursor()
        c.execute("INSERT INTO ai_tools (name, type, keywords) VALUES (?, ?, ?)",
                  (name, tool_type, ', '.join(keywords)))
        conn.commit()
        conn.close()

        self.ai_tools = self.get_ai_tools()
        self.refresh_tools_layout()

    def modify_ai_tool(self):
        tool_id = self.tool_id_input.text().strip()
        name = self.name_input.text().strip()
        tool_type = self.type_input.currentText()
        keywords = self.keywords_input.text().strip().split(',')

        if not tool_id or not name or not keywords:
            QMessageBox.warning(self, "Incomplete Information",
                                "Please fill in the required fields.")
            return

        conn = sqlite3.connect("ai_tools.db")
        c = conn.cursor()
        c.execute("UPDATE ai_tools SET name=?, type=?, keywords=? WHERE id=?",
                  (name, tool_type, ', '.join(keywords), tool_id))
        conn.commit()
        conn.close()

        self.ai_tools = self.get_ai_tools()
        self.refresh_tools_layout()

    def delete_ai_tool(self):
        tool_id = self.tool_id_input.text().strip()

        if not tool_id:
            QMessageBox.warning(self, "Incomplete Information",
                                "Please fill in the Tool ID field.")
            return

        conn = sqlite3.connect("ai_tools.db")
        c = conn.cursor()
        c.execute("DELETE FROM ai_tools WHERE id=?", (tool_id,))
        conn.commit()
        conn.close()

        self.ai_tools = self.get_ai_tools()
        self.refresh_tools_layout()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    manage_tools_dialog = ManageToolsDialog()
    manage_tools_dialog.show()
    sys.exit(app.exec_())

