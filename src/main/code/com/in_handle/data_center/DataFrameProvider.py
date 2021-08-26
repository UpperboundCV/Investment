from typing import List
import pandas as pd
import re
from ..helper.DateTimeHelper import DateTimeHelper
from tabulate import tabulate


class DataFrameProvider:
    csv_file_paths: List[str] = list()

    def set_csv_file_paths(self, source_list: List[str]):
        self.csv_file_paths = source_list.copy()

    def get_file_date(self, file_name: str) -> str:
        YYYY_MM_DD_reg_ex = '([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))'
        return re.search(YYYY_MM_DD_reg_ex, file_name).group(0)

    def get_raw_history_between(self, begin_date: str, end_date: str) -> pd.DataFrame:
        combined_csv_df: pd.DataFrame = pd.DataFrame()
        begin_date_obj = DateTimeHelper.to_datetime(date_time_str=begin_date)
        end_date_obj = DateTimeHelper.to_datetime(date_time_str=end_date)
        try:
            for path in (filter_paths for filter_paths in self.csv_file_paths if
                         begin_date_obj <= DateTimeHelper.to_datetime(
                             self.get_file_date(filter_paths)) <= end_date_obj):
                print(path)
                df = pd.read_csv(path)
                df['date'] = self.get_file_date(path)
                combined_csv_df = pd.concat([combined_csv_df, df])
        except Exception:
            raise
        return combined_csv_df
