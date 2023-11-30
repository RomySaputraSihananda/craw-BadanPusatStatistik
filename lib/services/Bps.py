from requests import Session;
from ..helpers.Parser import Parser;
# from ..helpers.Hasher import hasher;
from pyquery import PyQuery;

class Bps: 
    def __init__(self) -> None:
        self.__request: Session = Session();
        self.__parser: Parser = Parser();
        self.__data: list[object] = None;

    def __filter_link(self, tbody: PyQuery) -> list[str]:
        for tr in tbody('tr'):
            print(self.__parser.execute(tr, 'td:nth-child(2)').text());
        
        return [];


    def execute(self, url: str) -> str:
        res: any = self.__request.get(url);

        if(res.status_code != 200): return;
    
        links: list[str] = self.__filter_link(self.__parser.execute(res.text, '#listTabel1 tbody'));

        print(links);

        return self.__data;


if(__name__ == '__main__'):
    bps: Bps = Bps();
    print(bps.execute('https://www.bps.go.id/subject/7/energi.html#subjekViewTab3'));



