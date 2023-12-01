from datetime import datetime

class Datetime:
    def execute(self, text: str) -> str:
        try:
            return datetime.strptime(text, '%d %b %Y').strftime("%Y-%m-%d");
        except Exception as e:
            return e;