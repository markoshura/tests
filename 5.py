import unittest
# Подключаем тестируемую библиотеку
import lib
import math

# Класс, описывающий набор тестов
class LibTest(unittest.TestCase):

    # Тестируем работу sqrt с положительными аргументами
    def test_sqrt_non_negative_arg(self):
        # Набор проверок
        self.assertEqual(lib.sin(math.pi), 0)
        self.assertEqual(lib.sin(math.pi/2), 1)

    def test_sqrt_negative(self):
        # Набор проверок
        self.assertEqual(lib.sin(math.pi/6), 0.5)


# Запускаем тесты на исполнение
unittest.main(verbosity=2)
