import unittest
# Подключаем тестируемую библиотеку
import lib

# Класс, описывающий набор тестов
class LibTest(unittest.TestCase):

    # Тестируем работу sqrt с положительными аргументами
    def test_sqrt_non_negative_arg(self):
        # Набор проверок
        self.assertEqual(lib.factorial(1), 1)
        self.assertEqual(lib.factorial(2), 2)
        self.assertEqual(lib.factorial(3), 6)


    def test_sqrt_negative(self):
        # Набор проверок
        self.assertEqual(lib.factorial(-1), 1)
        self.assertEqual(lib.factorial(-2), 1)
        self.assertEqual(lib.factorial(0), 0)


# Запускаем тесты на исполнение
unittest.main(verbosity=2)
