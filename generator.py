from faker import Faker


def register_new_user():
    fake = Faker()
    email = fake.email()
    password = fake.password()
    firstName = fake.name()
    reg_data = {
        "email": email,
        "password": password,
        "name": firstName
    }
    return reg_data