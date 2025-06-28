# Form Matcher

Программа, которая находит подходящий шаблон формы по полям, переданным в командной строке. Если не найдено — определяет типы данных в запросе.

# Установка
pip3 install -r requirements.txt

# Запуск
python3 app.py get_tpl --customer=John Smith --дата_заказа=27.05.2025

# Тесты
pytest test_requests.py
