import time

from com.in_handle.helper.DateTimeHelper import DateTimeHelper
from com.in_handle.stock.ThaiStock import ThaiStock

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    thai_stock = ThaiStock()
    stock_df = thai_stock.get_stock_between('BMSCG','2021-08-16','2021-08-20')



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# http://siamchart.com/download.php?type=old
