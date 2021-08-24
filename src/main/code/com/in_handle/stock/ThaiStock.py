import configparser
from typing import List
import os
import pathlib
import glob


class ThaiStock:
    CSV_FILE = ".csv"

    def get_all_csv_path(self) -> str:
        config = configparser.RawConfigParser()
        config.read(filenames=r"..\resources\stock.conf")
        return config.get("STOCK_WINDOWS", "stock_thai_path")

    def file_list(self) -> List[str]:
        # print(fr"{self.get_all_csv_path()}")
        # r=root, d=directories, f = files
        csv_paths = list()
        for r, d, f in os.walk(fr"{self.get_all_csv_path()}"):
            for file in f:
                if file.endswith(self.CSV_FILE):
                    print(os.path.join(r, file))
                    csv_paths.append(str(os.path.join(r, file)))
        return csv_paths#glob.glob(self.CSV_FILE, recursive=True)#list(pathlib.Path(this_dir).glob(f'{self.CSV_FILE}'))

