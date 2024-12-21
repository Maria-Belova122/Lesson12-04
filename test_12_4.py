# ЗАДАНИЕ ПО ТЕМЕ "Логирование"

import unittest
import rt_with_exceptions as rt
import logging

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        """
        Тест для проверки функции walk класса Runner
        :return:
        """
        try:
            run2 = rt.Runner('Max', -3)
            for i in range(10):
                run2.run()
            self.assertEqual(run2.distance, 100)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as err:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        """
        Тест для проверки функции run класса Runner
        :return:
        """
        try:
            run1 = rt.Runner(35)
            for i in range(10):
                run1.walk()
            self.assertEqual(run1.distance, 50)
            logging.info('"test_run" выполнен успешно')
        except TypeError as err:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    def test_challenge(self):
        """
        Тест для проверки неравенства результатов функций run и walk
        :return:
        """
        run1 = rt.Runner('Alex')
        run2 = rt.Runner('Max')
        for i in range(10):
            run1.run()
            run2.walk()
        self.assertNotEqual(run1.distance, run2.distance)


if __name__ == '__main__':
    unittest.main()
