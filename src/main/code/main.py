import time

from com.in_handle.initiate.First import First
from com.in_handle.stock.ThaiStock import ThaiStock

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    freq: float = 1.0

    while True:
        firstObj = First()
        thai_stock = ThaiStock()
        print(thai_stock.get_all_csv_path())
        paths = thai_stock.file_list()
        for path in paths:
            print(path)
        print(firstObj.format_YYYYMMDD_HMS(firstObj.get_time_now()))
        time.sleep(freq)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# http://siamchart.com/download.php?type=old
