import configparser
import os
import platform
from typing import List
import pandas as pd
from . import LINUX, STOCK_LINUX, STOCK_WINDOWS, STOCK_THAI_PATH, STOCK_CONFIG_PATH, CSV_FILE
from ..data_center.DataFrameProvider import DataFrameProvider as DF_provider

class ThaiStock:
    df_provider: DF_provider

    def __init__(self) -> None:
        self.df_provider = DF_provider(self.file_list())

    def get_all_csv_path(self) -> str:
        config = configparser.RawConfigParser()
        config.read(filenames=STOCK_CONFIG_PATH)
        return config.get(STOCK_LINUX,STOCK_THAI_PATH)if platform.system()==LINUX else config.get(STOCK_WINDOWS, STOCK_THAI_PATH)

    def file_list(self) -> List[str]:
        csv_paths = list()
        for r, d, f in os.walk(self.get_all_csv_path()):
            for file in f:
                if file.endswith(CSV_FILE):
                    print(os.path.join(r, file))
                    csv_paths.append(str(os.path.join(r, file)))
        return csv_paths

    def get_stock_between(self, begin_date: str = default_value!, end_date:str) -> pd.DataFrame:
        return pd.DataFrame()

