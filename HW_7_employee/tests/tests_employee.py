from HW.HW_7_employee.api.employee_api import EmployeeApi
from HW.HW_7_employee.test_data.employee_data import employee, company, auth_data

base_url = "http://5.101.50.27:8000"
api = EmployeeApi(base_url)

def test_employee_create():
    created_employee = api.add_new_employee(
        employee["first_name"],
        employee["last_name"],
        employee["middle_name"],
        1,  # временно company_id = 1
        employee["email"],
        employee["phone"],
        employee["birthdate"],
        employee["is_active"]
    )
    assert "id" in created_employee
    assert created_employee["first_name"] == "Maria"

def test_get_employee_info():
    new_employee = api.add_new_employee(
        "Alice", "Brown", "Marie", 2,
        "alicebrown@example.com", "+9876543210",
        "1988-05-22", True
    )
    emp_id = new_employee["id"]
    fetched = api.get_employee_data_by_id(emp_id)
    assert fetched["id"] == emp_id
    assert fetched["first_name"] == "Alice"

def test_update_employee():
    new_employee = api.add_new_employee(
        "Bob", "Smith", "James", 3,
        "bobsmith@example.com", "+1357924680",
        "1985-07-30", True
    )
    emp_id = new_employee["id"]
    updated = api.update_employee_by_id(
        emp_id, "Smith", "robertsmith@example.com", "+111222333", False
    )
    assert updated["email"] == "robertsmith@example.com"
    assert updated["is_active"] is False
