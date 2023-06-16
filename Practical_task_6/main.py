import task_1 as t1
from sys import argv

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print(t1.checking_leap(*(str(i) for i in argv[1:])))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
