import configparser
import os
import platform
from typing import List
import pandas as pd
from . import LINUX, STOCK_LINUX, STOCK_WINDOWS, STOCK_THAI_PATH, STOCK_CONFIG_PATH, CSV_FILE, OLDEST_DATE
from ..data_center.DataFrameProvider import DataFrameProvider as DfProvider
from ..helper.DateTimeHelper import DateTimeHelper as DtHelper
from .common.StockColumn import StockColumn as StockCol
from tabulate import tabulate


class ThaiStock:
    df_provider: DfProvider = DfProvider()

    def __init__(self) -> None:
        print(f'{self.__class__.__name__.__str__()} init')
        self.df_provider.set_csv_file_paths(self.file_list())

    def get_all_csv_path(self) -> str:
        print('get_all_csv_path')
        config = configparser.RawConfigParser()
        config.read(filenames=STOCK_CONFIG_PATH)
        return config.get(STOCK_LINUX, STOCK_THAI_PATH) if platform.system() == LINUX else config.get(STOCK_WINDOWS,
                                                                                                      STOCK_THAI_PATH)

    def file_list(self) -> List[str]:
        print('file_list')
        csv_paths = list()
        for r, d, f in os.walk(self.get_all_csv_path()):
            for file in f:
                if file.endswith(CSV_FILE):
                    csv_paths.append(str(os.path.join(r, file)))
        return csv_paths

    def get_all_stock_between(self, begin_date: str = OLDEST_DATE,
                              end_date: str = DtHelper.csv_today_date) -> pd.DataFrame:
        return self.df_provider.get_raw_history_between(begin_date, end_date)

    def get_stock_between(self, stock_name: str, begin_date: str = OLDEST_DATE,
                          end_date: str = DtHelper.csv_today_date) -> pd.DataFrame:
        all_stock = self.get_all_stock_between(begin_date, end_date)
        # print(tabulate(all_stock[all_stock[StockCol.NAME] == stock_name],headers='keys',tablefmt='psql'))
        return all_stock[all_stock[StockCol.NAME] == stock_name].reset_index()
