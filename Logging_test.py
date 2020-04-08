import datetime
import logging
import random
from contextlib import contextmanager

start_time = datetime.datetime.utcnow()

 
@contextmanager
def logger():
  try:
    logger = logging.getLogger("password_generation")
    logger.setLevel(logging.INFO)
    fh = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    logger.info("Program started")
    yield
    end_time = datetime.datetime.utcnow()
    print('Время работы: {}'.format(end_time - start_time))
  finally:
    logger.info("Done!")

 
main = logger()

with main:
    print('Пароль сгенерирован: ')
    print(''.join([random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')) for x in range(12)]))