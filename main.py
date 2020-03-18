'''
Authors: Shirel Biton, 207276452
         Shani Waizman, 316440262
         Kobaivanov Yakir, 313566390
'''
import os
import sys
from time import sleep
from src.postal_code_class import PostalCode


def clear():
    '''
    :return:
    '''
    sleep(3)
    os.system('clear')


def close():
    '''
    :return:
    '''
    print("program has been closed")
    sleep(1)
    sys.exit(0)


def main():
    '''
    :return:
    '''
    while True:
        print("""
        1. check places names in a specific postal code 
        2. check sunrise and sunset in a specific lan and lng
        3. exit
        """)

        menu = input()

        switcher = {
            1: lambda x: PostalCode.input_location("p"),
            2: lambda x: PostalCode.input_location("t"),
            3: lambda x: close(),
        }
        switcher.get(int(menu))(0)


if __name__ == "__main__":
    main()
