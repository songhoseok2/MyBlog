import os


class Config:
    cur_path = os.path.dirname(__file__)
    secret_key_file = open(cur_path + "/private_variables/secret_key.txt", 'r')
    SECRET_KEY = secret_key_file.read()
    secret_key_file.close()

    database_URI_file = open(cur_path + "/private_variables/database_URI.txt", 'r')
    SQLALCHEMY_DATABASE_URI = database_URI_file.read()
    database_URI_file.close()

    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True

    email_address_file = open(cur_path + "/private_variables/email_address.txt", 'r')
    email_password_file = open(cur_path + "/private_variables/email_password.txt", 'r')
    MAIL_USERNAME = email_address_file.read()
    MAIL_PASSWORD = email_password_file.read()
    email_address_file.close()
    email_password_file.close()