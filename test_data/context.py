import json
import codecs
from copy import deepcopy
from typing import Any


class TestContext:
    """Контекст тестового сценария"""

    def __init__(self):
        self.__context_data = dict()

    def add(self, key: str, value: Any) -> None:
        """
        Добавить данные в контекст
            :param key: ключ
            :param value: любой объект
        """
        self.__context_data[key] = value

    def get(self, key: str) -> Any:
        """
        Получить данные из контекста
            :param key: ключ
            :return: данные из контекста
        """
        return self.__context_data.get(key)

    def get_dict(self):
        """Получить копию словаря с данными контекста"""
        return deepcopy(self.__context_data)

    @staticmethod
    def from_dict(data: dict) -> Any:
        """
        Создать контекст с данными из словаря
            :param data: словарь с данными
            :return: экземпляр контекста с данными из словаря
        """
        context = TestContext()
        for key, value in data.items():
            context.add(key, value)
        return context

    @staticmethod
    def from_json_file(path_to_file: str) -> Any:
        """
        Создать контекст с данными из json файла
            :param path_to_file: путь до json файла
            :return: экземпляр контекста с данными из json файла
        """
        with codecs.open(path_to_file, 'r', encoding='utf-8') as json_file:
            json_content: dict = json.load(json_file)
        return TestContext.from_dict(json_content)
