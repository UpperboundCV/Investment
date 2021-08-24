import time

from com.in_handle.helper.DateTimeHelper import DateTimeHelper
from com.in_handle.stock.ThaiStock import ThaiStock

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    freq: float = 1.0

    while True:
        firstObj = DateTimeHelper()
        thai_stock = ThaiStock()
        print(thai_stock.get_all_csv_path())
        paths = thai_stock.file_list()
        for path in paths:
            print(path)
        print(firstObj.to_datetime_str(firstObj.get_time_now()))
        time.sleep(freq)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# http://siamchart.com/download.php?type=old
