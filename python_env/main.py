import os
import time

while True: 
    for k, v in os.environ.items():
        print(f'{k}={v}')
    time.sleep(5)