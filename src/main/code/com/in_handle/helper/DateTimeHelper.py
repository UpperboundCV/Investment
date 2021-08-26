from datetime import datetime
from typing import Any, Type


class DateTimeHelper:
    csv_today_date: str = ''

    def __init__(self) -> None:
        self.csv_today_date = self.to_csv_date_str(self.get_time_now())

    @classmethod
    def get_type(cls, x: Any) -> Type[object]:
        assert isinstance(x, object)
        return type(x)

    @classmethod
    def get_time_now(cls) -> datetime:
        return datetime.now()

    @classmethod
    def to_datetime_str(cls, dt: datetime) -> str:
        return dt.strftime("%Y%m%d %H:%M:%S")

    @classmethod
    def to_time_str(cls, dt: datetime) -> str:
        return dt.strftime("%H:%M:%S")

    @classmethod
    def to_csv_date_str(cls, dt: datetime) -> str:
        return dt.strftime("%Y-%m-%d")

    @classmethod
    def to_datetime(cls, date_time_str: str) -> datetime:
        return datetime.strptime(date_time_str, '%Y-%m-%d')
