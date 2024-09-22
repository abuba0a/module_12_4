
import logging
import rt_with_exceptions as runner_
from unittest import TestCase

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                    encoding='UTF-8', format='%(levelname)s , %(message)s')


class RunnerTest(TestCase):

    def test_walk(self):
        try:
            runner = runner_.Runner('Вася', -10)
            for i in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info(f'"test_walk" выполнен успешно')
        except:
            logging.warning(f'Неверная скорость для Runner')

    def test_run(self):
        try:
            runner = runner_.Runner(1, 2)
            for i in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info(f'"test_run" выполнен успешно')
        except:
            logging.warning(f'Неверный тип данных для объекта Runner')


RunnerTest()
