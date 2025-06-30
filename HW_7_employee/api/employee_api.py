import requests

class EmployeeApi:
    def __init__(self, url):
        self.url = url

    def get_auth_token(self, username, password):
        payload = {
            "username": username,
            "password": password
        }
        response = requests.post(f"{self.url}/auth/login", json=payload)
        print("\n🔐 Получение токена:", response.status_code)
        print("Ответ:", response.text)
        assert response.status_code == 200, f"Ошибка при получении токена: {response.status_code}"
        return response.json()["user_token"]

    def create_company(self, name, description):
        company = {
            "name": name,
            "description": description,
            "is_active": True,
        }
        response = requests.post(f"{self.url}/company/create", json=company)
        print("\n🌸 Company creation status:", response.status_code)
        print("Ответ:", response.text)
        assert response.status_code in [200, 201], f"Ошибка создания компании: {response.status_code}"
        return response.json()

    def add_new_employee(self, first_name, last_name, middle_name, company_id, email, phone, birthdate, is_active):
        employee = {
            "first_name": first_name,
            "last_name": last_name,
            "middle_name": middle_name,
            "company_id": company_id,
            "email": email,
            "phone": phone,
            "birthdate": birthdate,
            "is_active": is_active,
        }
        response = requests.post(f"{self.url}/employee/create", json=employee)
        print("\n🌸 Сотрудник создан:", response.status_code)
        print("Ответ:", response.text)
        assert response.status_code in [200, 201], f"Ошибка: ожидался статус 200 или 201, получен {response.status_code}"
        return response.json()

    def get_employee_data_by_id(self, employee_id):
        response = requests.get(f"{self.url}/employee/info/{employee_id}")
        print("\n🌸 Статус получения данных:", response.status_code)
        print("Ответ:", response.text)
        assert response.status_code == 200, f"Ошибка: ожидался статус 200, получен {response.status_code}"
        return response.json()

    def update_employee_by_id(self, employee_id, last_name, email, phone, is_active):
        update_payload = {
            "last_name": last_name,
            "email": email,
            "phone": phone,
            "is_active": is_active,
        }
        response = requests.patch(f"{self.url}/employee/change/{employee_id}", json=update_payload)
        print("\n🌸 Статус обновления:", response.status_code)
        print("Ответ:", response.text)
        assert response.status_code in [200, 201], f"Ошибка: ожидался статус 200 или 201, получен {response.status_code}"
        return response.json()