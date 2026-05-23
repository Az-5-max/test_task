import unittest
from typing import List


def check_email(email: str) -> bool:
    if '@' in email and '.' in email and ' ' not in email:
        return True
    else:
        return False


def fio(initials: List[str]) -> str:
    res = initials[0][0] + initials[1][0] + initials[2][0]
    return res


def get_top_names(mentors):
    all_list = []
    for m in mentors:
        all_list.extend(m)

    all_names_list = []
    for mentor in all_list:
        name = mentor.split()[0]
        all_names_list.append(name)

    unique_names = set(all_names_list)

    popular = []
    for name in unique_names:
        popular.append([name, all_names_list.count(name)])

    popular.sort(key=lambda x: x[1], reverse=True)
    top_3 = popular[:3]

    output_list = []
    for item in top_3:
        output_list.append(f"{item[0]}: {item[1]} раз(а)")

    return ", ".join(output_list)


class TestEmail(unittest.TestCase):
    def test_check_email(self):
        test_cases = [
            ("helloworld@mail.ru", True),
            ("Helloworld@.ru", True),
            ("мояпочта@нетология.ру", True),
            ("python@email@net", False),
            (" em@il.ru", False),
            ("Hello world@ya.ru", False),
            ("test@test", False),
            ("test.test@mail.ru", True),
        ]
        for email, expected in test_cases:
            with self.subTest(email=email):
                self.assertEqual(check_email(email), expected)


class TestFIO(unittest.TestCase):
    def test_fio(self):
        test_cases = [
            (['Иванов', 'Иван', 'Иванович'], "ИИИ"),
            (['Жан', 'Клот', 'Вандамович'], "ЖКВ"),
            (['Павлов', 'Иван', 'Уралович'], "ПИУ"),
            (['Семейный', 'Доминик', 'Торретович'], "СДТ"),
        ]
        for initials, expected in test_cases:
            with self.subTest(initials=initials):
                self.assertEqual(fio(initials), expected)


class TestTopNames(unittest.TestCase):
    def setUp(self):
        self.mentors = [
            ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
             "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина",
             "Азамат Искаков", "Роман Гордиенко"],
            ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
             "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев",
             "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков",
             "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
            ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
             "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая",
             "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
            ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
             "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин",
             "Михаил Ларченко"]
        ]

    def test_top_names(self):
        result = get_top_names(self.mentors)
        self.assertIsInstance(result, str)
        self.assertIn("Александр", result)


if __name__ == '__main__':
    unittest.main()