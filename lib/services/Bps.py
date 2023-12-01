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

            url: str = self.__parser.execute(tr, 'td:nth-child(2) a').attr('href');  
            
            urls.append(url if self.__base_URL in url else self.__base_URL + url);

        return urls;

    def __get_data_table(self, urls: list[str]):
        i = 1;
        for url in urls:
            res: Response = self.__request.get(urls[0]);

            table: PyQuery = self.__parser.execute(res.text, '#tablex');

            key_col1: str = table('thead tr:first-child th:first-child').text().replace(' ', '_');
            key_col2: str = table('thead tr:first-child th:last-child').text().replace(' ', '_');
    
            key_thn1: str = table('thead tr:last-child th:first-child').text();
            key_thn2: str = table('thead tr:last-child th:nth-child(2)').text();
            key_thn3: str = table('thead tr:last-child th:last-child').text();

            print(key_thn1);
            print(key_thn2);
            print(key_thn3);

            for tr in table('tbody tr'):
                self.__parser.execute(tr, 'td:nth-child(1)').text()


            # while(True):
            #     newUrl = url.split('/');
            #     newUrl[6] = str(i);

            #     req: Response = self.__request.get('/'.join(newUrl));

            #     if(req.status_code != 200): break;

            #     print('{} ==> {}'.format(req.status_code, '/'.join(newUrl)));

            #     i += 1
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
    
    # with open('trash/test_result.json', 'w') as file:
    #     file.write(data);



