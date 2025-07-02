# Для загрузки пароля из .env:
import os
from dotenv import load_dotenv

load_dotenv()
import requests

class EmployeeApi:
    """Класс для работы с API сотрудников"""
    def __init__(self, url):
        """Инициализация с базовым URL"""
        self.url = url

    def create_employee(self, first_name, last_name, middle_name, company_id,
                        email, phone, birthdate, is_active=True):
        """Создание нового сотрудника"""
        employee_data = {
            "first_name": first_name,
            "last_name": last_name,
            "middle_name": middle_name,
            "company_id": company_id,
            "email": email,
            "phone": phone,
            "birthdate": birthdate,
            "is_active": is_active
        }

        resp = requests.post(f"{self.url}/employee/create", json=employee_data)
        assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
        return resp.json()

    def get_employee(self, employee_id):
        """Получение информации о сотруднике по ID"""
        resp = requests.get(f"{self.url}/employee/info/{employee_id}")
        assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
        return resp.json()

    def get_token(self):
        """Получить токен авторизации (добавьте корректные данные)"""
        # creds = {"username": "harrypotter", "password": "expelliarmus"}  # Если не использовать переменные из .env
        creds = {"username": os.getenv("LOGIN"), "password": os.getenv("PASSWORD")}
        resp = requests.post(self.url + '/auth/login', json=creds)
        assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"
        return resp.json()["user_token"]

    def update_employee(self, employee_id, **kwargs):
        """Изменение данных сотрудника (передаются только изменяемые параметры)"""
        client_token = self.get_token()
        url_with_token = f"{self.url}/employee/change/{employee_id}?client_token={client_token}"
        update_data = {key: value for key, value in kwargs.items() if value is not None}
        resp = requests.patch(url_with_token, json=update_data)

        assert resp.status_code == 200, f"Ошибка: ожидался статус 200, получен {resp.status_code}"

        print(f"\n\t\t\033[90;33m {'____ ПРОВЕРКА, обновлены ли данные сотрудника ':_<{50}}")
        print(f"\n\t\t\033[90;33m Запрос:\033[0m {self.url}/employee/info/{employee_id}")
        print(f"\t\t\033[90;33m Код ответа:\033[0m {resp.status_code}")
        print(f"\t\t\033[90;33m Тело ответа:\033[0m {resp.text}")

        return resp.json()

