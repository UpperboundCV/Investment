
from datetime import datetime
from typing import Any, Type


class First:

    def get_type(self, x: Any) -> Type[object]:
        assert isinstance(x, object)
        return type(x)

    def get_time_now(self) -> datetime:
        return datetime.now()

    def format_YYYYMMDD_HMS(self, dt: datetime) -> str:
        return dt.strftime("%Y%m%d %H:%M:%S")
