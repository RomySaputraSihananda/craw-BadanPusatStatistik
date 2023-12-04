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

        self.__result: dict = {};
        self.__result['title']: str = None;
        self.__result['url']: str = None;
        self.__result['date_now']: str = None;
        self.__result['data']: list[dict] = [];

        self.__base_URL: str = 'https://www.archive.bps.go.id';

    def __filter_link(self, tbody: PyQuery) -> list[str]:
        urls: list[str] = [];

        for tr in tbody('tr'):
            self.__result['data'].append({
                'id': self.__hasher.execute(self.__parser.execute(tr, 'td:nth-child(2) a').text()),
                'judul_tabel': self.__parser.execute(tr, 'td:nth-child(2) a').text(),
                'update': self.__datetime.execute(self.__parser.execute(tr, 'td:nth-child(3)').text()),
                'keterangan': self.__parser.execute(tr, 'td:nth-child(4)').text(),
            });

            url: str = self.__parser.execute(tr, 'td:nth-child(2) a').attr('href');  
            
            urls.append(url if self.__base_URL in url else self.__base_URL + url);

        return urls;

    def __str_2_num(self, text: str) -> str:
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

                headers: list[str] = [PyQuery(th).text().replace(' ', '_') for th in table('thead tr:first-child th')]
                col_keys: list[str] = headers[1:-1]
                years: list[str] = [PyQuery(th).text() for th in table('thead tr:last-child th')]

                for tr in table('tbody tr'):
                    data_table = {
                        'judul_tabel':  self.__parser.execute(res.text, 'h4').text(),
                        headers[0]: self.__parser.execute(tr, 'td:first-child').text(),
                        headers[-1]: {
                            years[i]: self.__str_2_num(self.__parser.execute(tr, f'td:nth-child({i + 2})').text())
                            for i in range(len(years))
                        }
                    }

                    for i, col_key in enumerate(col_keys):
                        data_table[col_key] = self.__parser.execute(tr, f'td:nth-child({i + 2})').text()
                    
                
                    existing_data = next((item for item in data_tables if item.get(headers[0]) == data_table[headers[0]]), None)

                    if existing_data:
                        existing_data[headers[-1]].update(data_table[headers[-1]])
                    else:
                        data_tables.append(data_table)

                j += 1;
                

            self.__result['data'][i].update({
                'url_tabel': url_tables,
                'data_tables': data_tables
            });

            break;


    def execute(self, url: str) -> str:
        res: Response = self.__request.get(url);

        if(res.status_code != 200): return;

        parser: PyQuery = self.__parser.execute(res.text, 'body');

        self.__result['title'] = parser('.breadcrumbs span').text();
        self.__result['date_now'] = self.__datetime.now();
        self.__result['url'] = url.replace('#subjekViewTab3', '');

        urls: list[str] = self.__filter_link(parser('#listTabel1 tbody'));
        self.__get_data_table(urls);


        return self.__result;

# testing
if(__name__ == '__main__'):
    bps: Bps = Bps();
    data = dumps(bps.execute('https://www.archive.bps.go.id/subject/7/energi.html#subjekViewTab3'));

    with open('trash/test_result.json', 'w') as file:
        file.write(data);