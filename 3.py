import unittest
# Подключаем тестируемую библиотеку
import lib

# Класс, описывающий набор тестов
class LibTest(unittest.TestCase):

    # Тестируем работу sqrt с положительными аргументами
    def test_sqrt_non_negative_arg(self):
        # Набор проверок
        self.assertEqual(lib.palindrome('sss'), 1)
        self.assertEqual(lib.palindrome('spdps'), 1)
        self.assertEqual(lib.palindrome('sarsfytgf'), 0)

    def test_sqrt_negative(self):
        # Набор проверок
        self.assertEqual(lib.palindrome('s'), 1)


# Запускаем тесты на исполнение
unittest.main(verbosity=2)
