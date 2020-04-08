import datetime
import logging
import random
from contextlib import contextmanager

start_time = datetime.datetime.utcnow()
 
@contextmanager
def logger():
    logger = logging.getLogger("password_generation")
    logger.setLevel(logging.INFO)

    fh = logging.StreamHandler()
 
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)

    logger.addHandler(fh)
    
    logger.info("Program started")
    print('Пароль сгенерирован: ')
    print(''.join([random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM')) for x in range(12)]))
    logger.info("Done!")
    yield
    end_time = datetime.datetime.utcnow()
    print('Время работы: {}'.format(end_time - start_time))
 
main = logger()
with main:
    pass