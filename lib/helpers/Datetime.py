import pytz
from datetime import datetime
class Datetime:
    def execute(self, text: str) -> str:
        try:
            return datetime.strptime(text, '%d %b %Y').strftime("%Y-%m-%d");
        except Exception as e:
            return e;

    # def now(self) -> str:
    #     tz = pytz.timezone("Asia/Jakarta");
    #     date = datetime.now().strftime("%Y%m%d%H%M%S%f");
    #     return tz.localize(date).strftime('%z');
    def now(self) -> str:
        tz = pytz.timezone("Asia/Jakarta")
        date = datetime.now(tz).strftime("%Y-%m-%dT%H:%M:%S")
        return date