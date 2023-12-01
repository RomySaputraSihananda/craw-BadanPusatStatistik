import re;
from requests import Session, Response;
from ..helpers.Parser import Parser;
# from ..helpers.Hasher import hasher;
from pyquery import PyQuery;
from json import dumps;

class Bps: 
    def __init__(self) -> None:
        self.__request: Session = Session();
        self.__parser: Parser = Parser();
        self.__data: list[object] = [];
        self.__base_URL: str = 'https://www.bps.go.id';

    def __filter_link(self, tbody: PyQuery) -> list[str]:
        urls =[];

        for tr in tbody('tr'):
            self.__data.append({
                'judul_tabel': self.__parser.execute(tr, 'td:nth-child(2) a').text(),
                'update': self.__parser.execute(tr, 'td:nth-child(3)').text(),
                'keterangan': self.__parser.execute(tr, 'td:nth-child(4)').text(),
            });

            urls.append(self.__base_URL + self.__parser.execute(tr, 'td:nth-child(2) a').attr('href'));
        
        print(urls);

        return urls;

    def __get_data_table(self, urls: list[str]):
        for url in urls:
            i = 1;

            while(True):
                # url: list[str] = url.split('/');
                print(url);
                # url[6] = str(i);
                # req: Response = self.__request.get('/'.join(url));
                # print(req.status_code);
                # i += 1
                # res: Response = self.__request.get(url);



    def execute(self, url: str) -> str:
        res: Response = self.__request.get(url);

        if(res.status_code != 200): return;
    
        urls: list[str] = self.__filter_link(self.__parser.execute(res.text, '#listTabel1 tbody'));

        self.__get_data_table(urls);

        return self.__data;

# testing
if(__name__ == '__main__'):
    bps: Bps = Bps();
    data: str = dumps(bps.execute('https://www.bps.go.id/subject/7/energi.html#subjekViewTab3'));
    
    with open('trash/test_result.json', 'w') as file:
        file.write(data);



