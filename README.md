## 📚 Список домашних заданий

---

### ✅ Home Work 1 — Unit-тестирование простых операций

<details>
<summary><strong>📋 Условие и инструкция</strong></summary>

**Задание**
Создать файл `simple_math.py` и реализовать в нём следующий класс:

```python
class SimpleMath:
    # Класс с простыми математическими операциями

    def square(self, x):
        # Возвращает квадрат числа
        return x * x

    def cube(self, x):
        # Возвращает куб числа
        return x * x * x
```

**Что нужно сделать**

* Написать **unit-тесты** для класса `SimpleMath`
* Шаги:

  1. Создать файл `test_simple_math.py`
  2. Написать тесты для методов `square()` и `cube()`
  3. Проверить поведение для положительных, отрицательных чисел и нуля

**Ожидаемое поведение**

* `square(2)` → `4`
* `cube(-3)` → `-27`

</details>

---

### ✅ Home Work 2 — Открытие сайта и скриншот

<details>
<summary><strong>📋 Задание</strong></summary>

**Что нужно сделать**

* Открыть браузер Firefox
* Перейти на любой сайт
* Открыть любую другую секцию на этом сайте
* Сделать скриншот этой секции

</details>

---

### ✅ Home Work 3 — UI-тестирование сайта ITCareerHub

<details>
<summary><strong>📋 Задание</strong></summary>

**Сайт для тестирования:**
[https://itcareerhub.de/ru](https://itcareerhub.de/ru)

**Что проверить:**

* Логотип ITCareerHub
* Ссылки:

  * "Программы"
  * "Способы оплаты"
  * "Новости"
  * "О нас"
  * "Отзывы"
* Кнопки переключения языка (ru / de)

**Дополнительно:**

* Кликнуть по иконке телефона
* Убедиться, что отображается текст:
  `"Если вы не дозвонились, заполните форму на сайте. Мы свяжемся с вами"`

</details>

---

### ✅ Home Work 4 — Проверка кнопки и изображений

<details>
<summary><strong>📋 Задания</strong></summary>

#### 🔹 Задание 1: Проверка изменения текста кнопки

**Сайт:**
[http://uitestingplayground.com/textinput](http://uitestingplayground.com/textinput)

**Шаги:**

1. Перейти на сайт
2. Ввести в поле `ITCH`
3. Нажать синюю кнопку
4. Проверить, что текст кнопки изменился на `ITCH`

---

#### 🔹 Задание 2: Проверка загрузки изображений

**Сайт:**
[https://bonigarcia.dev/selenium-webdriver-java/loading-images.html](https://bonigarcia.dev/selenium-webdriver-java/loading-images.html)

**Шаги:**

1. Перейти на сайт
2. Дождаться загрузки всех изображений
3. Получить значение `alt` у **третьего изображения**
4. Убедиться, что `alt` равно `"award"`

</details>

---

### ✅ Home Work 5 — iFrame + Drag & Drop

<details>
<summary><strong>📋 Задания</strong></summary>
🔹 Задание 1: Проверка наличия текста в iframe

Сайт:https://bonigarcia.dev/selenium-webdriver-java/iframes.html

Шаги:

1. Открыть страницу
2. Найти фрейм (iframe), содержащий искомый текст
3. Переключиться в этот iframe
4. Найти элемент с текстом: "semper posuere integer et senectus justo curabitur."
5. Убедиться, что текст отображается на странице

🔹 Задание 2: Drag & Drop — перетаскивание изображения в корзину

Сайт:https://www.globalsqa.com/demo-site/draganddrop/

Шаги:

1. Открыть страницу Drag & Drop Demo
2. Захватить первую фотографию (верхний левый элемент)
3. Перетащить её в область корзины (Trash)

Проверить:

1. В корзине появилась одна фотография
2. В основной области осталось 3 фотографии

Ожидаемый результат:

1. Фотография успешно переместилась в корзину
2. Вне корзины остаются 3 фотографии

</details>

___

### ✅ Home Work 6 — Page Object Model (POM)

<details>
<summary><strong>📋 Задания</strong></summary>
🔹 Напишите автоматизированный тест с использованием Page Object Model (POM), который выполняет следующие шаги:

1. Откройте сайт магазина: https://www.saucedemo.com/. 
2. Авторизуйтесь как пользователь standard_user. 
3. Добавьте в корзину товары:
   - Sauce Labs Backpack 
   - Sauce Labs Bolt T-Shirt 
   - Sauce Labs Onesie
4. Перейдите в корзину. 
5. Нажмите Checkout. 
6. Заполните форму своими данными:
   - Имя 
   - Фамилия 
   - Почтовый индекс
7. Прочтите со страницы итоговую стоимость (Total). 
8. Закройте браузер. 
9. Проверьте, что итоговая сумма равна $58.29.

### Требования:

- Использовать Page Object Model для организации кода. 
- Вынести все локаторы и методы работы со страницами в отдельные классы (Page Object). 
- Тест должен быть независимым и запускаться без предварительной подготовки данных

</details>

___

### ✅ Home Work 7 — API endpoints

<details>
<summary><strong>📋 Задания</strong></summary>
🔹 Разработать автоматические тесты, которые проверяют корректность работы API для управления сотрудниками.  

🔹 Создайте класс EmployeeApi для создания вспомогательных методов. API Методы

1. Создание нового работника
Метод: POST  
URL: http://5.101.50.27:8000/employee/create  
Описание: Создаёт нового сотрудника, принимает данные в JSON.

2. Получение информации о работнике
Метод: GET  
URL: http://5.101.50.27:8000/employee/info  
Описание: Получает данные о сотруднике по его ID.

3. Изменение данных о работнике
Метод: PATCH  
URL: http://5.101.50.27:8000/employee/change  
Описание: Позволяет изменить информацию о сотруднике по его ID.


#### ⚙️ Структура проекта
```text
HW_7_employee/
│
├── allure-results
│   ├── ...
│
├── employee_api.py        # Основной класс для запросов к API
│   
├── test_employee.py       # Автотесты с использованием pytest


```

#### 🧪 Запуск тестов
Из под корневой папки HW/HW_7_employee

```bash
pytest test_employee.py -s
```
#### 📌 Swagger-документация API
Ознакомиться с API можно по ссылке:
📎 Swagger UI — http://5.101.50.27:8000/docs#/

#### ✅ Покрытие тестами

test_employee_create	✅ Пройден Создание нового сотрудника  
test_get_employee_info	✅ Пройден	Получение данных по ID  
test_update_employee	✅ Пройден	Обновление данных (через токен)

#### Для генерации отчетов посредством фреймворка Allure

```bush
allure serve allure-results     # Для запуска веб-сервера с отчетом. 
                                # В результате откроется браузер с интерактивным HTML отчетом 
```
```bush
allure generate allure-results -o allure-report --clean    # Для генерации статического отчета
                                                           # После генерации отчет становится доступен в директории 
                                                           # allure-report. 

```
</details>