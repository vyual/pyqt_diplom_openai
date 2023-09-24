import sys
import openai
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTextEdit, QPushButton, QHBoxLayout

# Замените на ваш API-ключ от OpenAI
openai.api_key = "ВАШ_API_КЛЮЧ"

class ChatApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Chat with GPT-3")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.text_edit = QTextEdit(self)
        self.layout.addWidget(self.text_edit)

        self.send_button = QPushButton("Send", self)
        self.send_button.clicked.connect(self.send_message)
        self.layout.addWidget(self.send_button)

        self.response_text_edit = QTextEdit(self)
        self.response_text_edit.setReadOnly(True)
        self.layout.addWidget(self.response_text_edit)

        self.central_widget.setLayout(self.layout)

    def send_message(self):
        user_input = self.text_edit.toPlainText()
        self.text_edit.clear()

        # Отправляем сообщение пользователя в GPT-3 для генерации ответа
        response = generate_response(user_input)

        # Отображаем ответ в текстовом поле
        self.response_text_edit.append("User: " + user_input)
        self.response_text_edit.append("AI: " + response)
        self.response_text_edit.append("\n")

def generate_response(user_input):
    # Задайте параметры запроса к GPT-3
    prompt = f"User: {user_input}\nAI:"
    max_tokens = 50  # Максимальное количество токенов в ответе
    temperature = 0.7  # Параметр температуры для разнообразия ответов

    # Запрос к GPT-3
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=temperature,
    )

    return response.choices[0].text.strip()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    chat_app = ChatApp()
    chat_app.show()
    sys.exit(app.exec_())
