from typing import List
import pandas as pd
import re
from ..helper.DateTimeHelper import DateTimeHelper


class DataFrameProvider:
    csv_file_paths: List[str] = list()

    def __init__(self, source_list: List[str]):
        self.csv_file_paths = source_list.copy()

    def get_file_date(self, file_name: str) -> str:
        YYYY_MM_DD_reg_ex = '([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))'
        return re.search(YYYY_MM_DD_reg_ex, file_name).group(0)

    def get_raw_history_between(self, begin_date: str, end_date: str) -> pd.DataFrame:
        combined_csv_df: pd.DataFrame = pd.DataFrame()
        begin_date_obj = DateTimeHelper.to_datetime(begin_date)
        end_date_obj = DateTimeHelper.to_datetime(end_date)
        try:
            for csv_file_path in self.csv_file_paths:
                stock_date_str = self.get_file_date(csv_file_path)
                stock_date_obj = DateTimeHelper.to_datetime(stock_date_str)
                if begin_date_obj <= stock_date_obj <= end_date_obj:
                    df = pd.read_csv(csv_file_path)
                    df['date'] = stock_date_str
                    combined_csv_df = pd.concat(combined_csv_df, df)
        except Exception:
            raise
        return combined_csv_df
