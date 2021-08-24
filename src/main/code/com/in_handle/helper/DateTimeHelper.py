
from datetime import datetime
from typing import Any, Type


class DateTimeHelper:

    def get_type(cls, x: Any) -> Type[object]:
        assert isinstance(x, object)
        return type(x)

    def get_time_now(cls) -> datetime:
        return datetime.now()

    def to_datetime_str(cls, dt: datetime) -> str:
        return dt.strftime("%Y%m%d %H:%M:%S")

    def to_time_str(cls, dt: datetime) -> str:
        return dt.strftime("%H:%M:%S")
    
    def to_datetime(cls, date_time_str: str) -> datetime:
        return datetime.strptime(date_time_str,'%Y-%m-%d')

