import unittest
# Подключаем тестируемую библиотеку
import lib

# Класс, описывающий набор тестов
class LibTest(unittest.TestCase):

    # Тестируем работу sqrt с положительными аргументами
    def test_sqrt_non_negative_arg(self):
        # Набор проверок
        self.assertEqual(lib.prime(2), 1)
        self.assertEqual(lib.prime(3), 1)
        self.assertEqual(lib.prime(4), 0)

    def test_sqrt_negative(self):
        # Набор проверок
        self.assertEqual(lib.prime(-2), 0)


# Запускаем тесты на исполнение
unittest.main(verbosity=2)
