from requests import Session;
from ..helpers.Parser import Parser;
from pyquery import PyQuery;
        

class Bps: 
    def __init__(self) -> None:
        self.__request: Session = Session();
        self.__parser: Parser = Parser();
        self.__data: list[object] = None;

    def __filter_list():
        pass;

    def execute(self, url: str) -> str:
        res = self.__request.get(url);

        if(res.status_code != 200): return;
    
        tr = self.__parser.execute(res.text, '.vervar').map(lambda e, i: print(i));

        return 'ok';


if(__name__ == '__main__'):
    kompas: Bps = Bps();
    with open('test.html', 'w') as file:
        file.write(kompas.execute('https://www.bps.go.id/subject/7/energi.html#subjekViewTab3'));



