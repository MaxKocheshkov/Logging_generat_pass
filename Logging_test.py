import datetime
import logging
import random

start_time = datetime.datetime.utcnow()
 
def main():
    
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
 
if __name__ == "__main__":
    main()

end_time = datetime.datetime.utcnow()
print('Время работы: {}'.format(end_time - start_time))