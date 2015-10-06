import unittest
# Подключаем тестируемую библиотеку
import lib

# Класс, описывающий набор тестов
class LibTest(unittest.TestCase):

    # Тестируем работу sqrt с положительными аргументами
    def test_sqrt_non_negative_arg(self):
        # Набор проверок
        self.assertEqual(lib.even(2), 1)
        self.assertEqual(lib.even(1), 0)
        self.assertEqual(lib.even(0), 1)
        self.assertEqual(lib.even(22), 1)

    def test_sqrt_negative(self):
        # Набор проверок
        self.assertEqual(lib.even(-1), 0)
        self.assertEqual(lib.even(-2), 1)


# Запускаем тесты на исполнение
unittest.main(verbosity=2)
