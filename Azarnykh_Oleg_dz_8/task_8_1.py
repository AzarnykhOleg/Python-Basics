import re


def email_parse(email: str) -> None:
    """
    Парсит переданную email-строку на атрибуты и возвращает словарь
    :param email: строковое входное значение обрабатываемого email
    :return: {'username': <значение до символа @>, 'domain': <значение за символом @>} | ValueError
    """
    try:
        RE_MAIL = re.compile(r'^[a-z0-9-_]+@[a-z0-9]+\.[a-z]+$', re.IGNORECASE)
        if RE_MAIL.findall(email):
            username, domain = email.split('@')
            return print({'username': username, 'domain': domain})
        else:
            raise ValueError
    except ValueError as er:
        print(f'{er}: wrong email: {email}')


if __name__ == '__main__':
    email_parse('someone@geekbrains.RU')
    email_parse('someone@geekbrainsru')
