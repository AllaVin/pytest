# from HW.HW_7_employee.api.employee_api import base_url, EmployeeApi
# from HW.HW_7_employee.test_data.employee_data import employee
#
# def test_employee_create():
#     api = EmployeeApi(base_url)
#
#     token = api.get_auth_token("admin", "admin")
#
#     # Сначала создаём компанию
#     company = api.create_company("QA Test Company", "Temporary company for employee creation")
#     company_id = company["id"]
#
#     # Создание нового сотрудника (аргументы из словаря)
#     response = api.add_new_employee(
#         employee["first_name"],
#         employee["last_name"],
#         employee["middle_name"],
#         company_id,
#         employee["email"],
#         employee["phone"],
#         employee["birthdate"],
#         employee["is_active"]
#     )
#     print("Сотрудник создан", response)
#
#     # Получение ID сотрудника из ответа
#     employee_id = response["id"]
#
#     # Получение данных сотрудника по ID
#     emp_data = api.get_employee_data_by_id(employee_id)
#     print("Данные сотрудника:", emp_data)
#
#     # Можно сделать assert по нужному полю
#     assert emp_data["email"] == employee["email"]
#
#     # Обновляем данные сотрудника
#     updated = api.update_employee_by_id(
#         employee_id,
#         "Grey",
#         "grey.grey@example.com",
#         phone= "444-555-666",
#         is_active=True
#     )
#     print("Данные после обновления", updated)

from HW.HW_7_employee.api.employee_api import EmployeeApi
from HW.HW_7_employee.test_data.employee_data import employee, company, auth_data

base_url = "http://5.101.50.27:8000"

def test_employee_create():
    api = EmployeeApi(base_url)

    # 🔐 Получаем токен
    token = api.get_auth_token(auth_data["username"], auth_data["password"])

    # ✅ Создаём компанию
    new_company = api.create_company(company["name"], company["description"])
    company_id = new_company["id"]

    # ✅ Создаём сотрудника
    created_employee = api.add_new_employee(
        employee["first_name"],
        employee["last_name"],
        employee["middle_name"],
        company_id,
        employee["email"],
        employee["phone"],
        employee["birthdate"],
        employee["is_active"]
    )
    employee_id = created_employee["id"]

    # ✅ Получаем данные сотрудника
    emp_data = api.get_employee_data_by_id(employee_id)
    assert emp_data["email"] == employee["email"]

    # ✅ Обновляем сотрудника (с токеном)
    updated = api.update_employee_by_id(
        employee_id,
        last_name="Grey",
        email="grey.grey@example.com",
        phone="444-555-666",
        is_active=True,
        token=token
    )

    assert updated["last_name"] == "Grey"
    assert updated["email"] == "grey.grey@example.com"
