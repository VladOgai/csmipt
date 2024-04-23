from data import *
from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat


messages = [
    SystemMessage(
        content='Ты полезный ассистент, который умеет переводить с русского на английский.'
    ),
    HumanMessage(content='Переведи это предложение: Я люблю программирование.')
]

chat = GigaChat(credentials=credentials)
print(chat(messages))