import re;

from requests import Session, Response;
from pyquery import PyQuery;
from json import dumps;

from ..helpers.Parser import Parser;
from ..helpers.Hasher import Hasher;
from ..helpers.Datetime import Datetime;

class Bps: 
    def __init__(self) -> None:
        self.__request: Session = Session();
        self.__parser: Parser = Parser();
        self.__hasher: Hasher = Hasher();
        self.__datetime: Datetime = Datetime();
        self.__result: list[dict] = [];
        self.__base_URL: str = 'https://www.bps.go.id';

    def __filter_link(self, tbody: PyQuery) -> list[str]:
        urls =[];

        for tr in tbody('tr'):
            self.__result.append({
                'id': self.__hasher.execute(self.__parser.execute(tr, 'td:nth-child(2) a').text()),
                'judul_tabel': self.__parser.execute(tr, 'td:nth-child(2) a').text(),
                'update': self.__datetime.execute(self.__parser.execute(tr, 'td:nth-child(3)').text()),
                'keterangan': self.__parser.execute(tr, 'td:nth-child(4)').text(),
            });

            url: str = self.__parser.execute(tr, 'td:nth-child(2) a').attr('href');  
            
            urls.append(url if self.__base_URL in url else self.__base_URL + url);

        return urls;

    def __str_2_num(self, text: str):
        text = text.replace(',', '.').replace('\u2009', '').replace(' ', '');

        try:
            number = float(text) if '.' in text else int(text);
        except ValueError:
            number = None;

        return number;

    def __get_data_table(self, urls: list[str]) -> None:
        for i, url in enumerate(urls):
            data_tables: list[dict] = [];
            url_tables: list[str] = [];
            j = 1;

            while(True):
                newUrl = url.split('/');
                newUrl[6] = str(j);

                res: Response = self.__request.get('/'.join(newUrl));

                if(res.status_code != 200): break;
                print('/'.join(newUrl))

                url_tables.append('/'.join(newUrl));

                table: PyQuery = self.__parser.execute(res.text, '#tablex');

                key_col1: str = table('thead tr:first-child th:first-child').text().replace(' ', '_');
                key_col2: str = table('thead tr:first-child th:last-child').text().replace(' ', '_');
        
                key_thn1: str = table('thead tr:last-child th:first-child').text();
                key_thn2: str = table('thead tr:last-child th:nth-child(2)').text();
                key_thn3: str = table('thead tr:last-child th:last-child').text();


                for tr in table('tbody tr'):
                    data_table: dict = {
                        key_col1: self.__parser.execute(tr, 'td:first-child').text(),
                        key_col2: {
                            key_thn1: self.__str_2_num(self.__parser.execute(tr, 'td:nth-child(2)').text()),
                            key_thn2: self.__str_2_num(self.__parser.execute(tr, 'td:nth-child(3)').text()),
                            key_thn3: self.__str_2_num(self.__parser.execute(tr, 'td:last-child').text())
                        }
                    };

                
                    existing_data = next((item for item in data_tables if item.get(key_col1) == data_table[key_col1]), None);

                    if existing_data:
                        existing_data[key_col2].update(data_table[key_col2]);
                    else:
                        data_tables.append(data_table)

                j += 1;
                

            self.__result[i].update({
                'data_tables': data_tables,
                'url_tabel': url_tables
            });

            break;


    def execute(self, url: str) -> str:
        res: Response = self.__request.get(url);

        if(res.status_code != 200): return;
    
        urls: list[str] = self.__filter_link(self.__parser.execute(res.text, '#listTabel1 tbody'));
        self.__get_data_table(urls);

        return self.__result;

# testing
if(__name__ == '__main__'):
    bps: Bps = Bps();
    data = dumps(bps.execute('https://www.bps.go.id/subject/7/energi.html#subjekViewTab3'));

    with open('trash/test_result.json', 'w') as file:
        file.write(data);