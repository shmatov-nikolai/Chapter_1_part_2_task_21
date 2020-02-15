import random
import time


def summa_random_num():
    num_1 = random.randrange(1000)
    num_2 = random.randrange(1000)
    num_3 = random.randrange(1000)
    print(f"Сумма случайных чисел: {num_1}, {num_2}, {num_3} состaвляет: {num_1 + num_2 + num_3}")

while 1:
    summa_random = summa_random_num()
    time.sleep(5)