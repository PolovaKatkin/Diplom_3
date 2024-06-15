import allure
from faker import Faker


@allure.step('Генерируем данные для регистрации пользователя.')
def generate_info_for_registration():
    fake = Faker(locale="ru_RU")
    email = fake.email()
    password = fake.password()
    name = fake.name()
    return email, password, name


class Constants:
    TEST_EMAIL = 'ekaterina_polova_7_702@mail.ru'
    TEST_PASSWORD = 'Grut86'
