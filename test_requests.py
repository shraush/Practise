import subprocess

def run_test(args, expected_output):
    result = subprocess.run(["python", "app.py", "get_tpl"] + args, capture_output=True, text=True)
    output = result.stdout.strip()
    assert output == expected_output, f"Expected: {expected_output}, Got: {output}"

run_test(["--f_name1=vasya@pukin.ru", "--f_name2=27.05.2025"], "Проба")

run_test([
    "--customer=Иван",
    "--order_id=123",
    "--дата_заказа=2025-05-27",
    "--contact=+7 123 456 78 90"
], "Форма заказа")

run_test(["--tumba=27.05.2025", "--yumba=+7 903 123 45 78"], "{'tumba': 'date', 'yumba': 'phone'}")

print("Все тесты прошли!")
