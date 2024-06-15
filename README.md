## Дипломный проект. Задание 2: API

### Автотесты для проверки UI сайта Stellar Burgers https://stellarburgers.nomoreparties.site/

### Структура проекта


- `allure_results` - пакет с отчетом о проведенном тестировании
- `locators` - пакет с локаторами
- `pages` - пакет для хранения методов тестируемых страниц
- `tests` - пакет, содержащий тесты, разделенные по страницам сайта
- `conftest.py` - фикстуры
- `data` - данные для тестов
- `helpers.py` - файл с вспомогательными функциями
- `README.md` - описание проекта
- `requirements` - файл с необходимыми библиотеками


### Запуск автотестов

**Установка зависимостей**

> `pip install -r requirements.txt`

**Запуск автотестов и создание отчета о тестировании в Allure**

> `pytest--alluredir=allure_results`

**Генерация отчета в html страницу**

>`allure serve allure_results`

