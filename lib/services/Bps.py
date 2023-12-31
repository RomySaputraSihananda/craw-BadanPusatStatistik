from requests import Session, Response
from pyquery import PyQuery
from json import dumps
from typing import Union

from lib.helpers.Parser import Parser
from lib.helpers.Hasher import Hasher
from lib.helpers.Datetime import Datetime
from lib.helpers import logging

class Bps: 
    def __init__(self) -> None:
        self.__request: Session = Session()
        self.__parser: Parser = Parser()
        self.__hasher: Hasher = Hasher()
        self.__datetime: Datetime = Datetime()

        self.__result: dict = {}
        self.__result['title']: str = None
        self.__result['url']: str = None
        self.__result['date_now']: str = None
        self.__result['data']: list[dict] = []

        self.__base_URL: str = 'https://www.archive.bps.go.id'

    def __filter_link(self, tbody: PyQuery) -> list[str]:
        urls: list[str] = []

        for tr in tbody('tr'):
            self.__result['data'].append({
                'id': self.__hasher.execute(self.__parser.execute(tr, 'td:nth-child(2) a').text()),
                'judul_tabel': self.__parser.execute(tr, 'td:nth-child(2) a').text(),
                'update': self.__datetime.execute(self.__parser.execute(tr, 'td:nth-child(3)').text()),
                'keterangan': self.__parser.execute(tr, 'td:nth-child(4)').text(),
            })

            url: str = self.__parser.execute(tr, 'td:nth-child(2) a').attr('href')  
            
            urls.append(url if self.__base_URL in url else self.__base_URL + url)

        return urls

    def __str_2_num(self, text: str) -> Union[int, float, None]:
        text = text.replace(',', '.').replace('\u2009', '').replace(' ', '')

        try:
            number = float(text) if '.' in text else int(text)
        except ValueError:
            number = None

        return number

    def __get_data_table(self, url: str) -> list[dict]:
        data_tables: list[dict] = []
        url_tables: list[str] = []
        j: int = 1

        while(True):
            newUrl: list[str] = url.split('/')
            newUrl[6]: list[str] = str(j)

            res: Response = self.__request.get('/'.join(newUrl))
            
            j += 1

            if(res.status_code != 200): break

            logging.info('/'.join(newUrl))

            url_tables.append('/'.join(newUrl))

            table: PyQuery = self.__parser.execute(res.text, '#tablex')
            
            if (not len(table('thead tr')) > 2):
                headers: list[str] = [PyQuery(th).text().replace(' ', '_') for th in table('thead tr:first-child th')]
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
                    
                    existing_data = next((item for item in data_tables if item.get(headers[0]) == data_table[headers[0]]), None)

                    if existing_data:
                        existing_data[headers[-1]].update(data_table[headers[-1]])
                    else:
                        data_tables.append(data_table)
                
                continue
            
            headers: list[str] = [PyQuery(th).text().replace(' ', '_') for th in table('thead tr:first-child th')]
            col_keys: list[str] = [PyQuery(th).text().replace(' ', '_') for th in table('thead tr:nth-child(2) th')]
            years: list[str] = [PyQuery(th).text() for th in table('thead tr:last-child th')]

            for tr in table('tbody tr'):
                data_table = {
                    'judul_tabel':  self.__parser.execute(res.text, 'h4').text(),
                    headers[0]: self.__parser.execute(tr, 'td:first-child').text(),
                    headers[-1]: {
                        col_key: {
                            years[i]: self.__str_2_num(self.__parser.execute(tr, f'td:nth-child({i + 2 + (int(len(years) / len(col_keys)) * j)})').text())
                            for i in range(int(len(years) / len(col_keys)))
                        }for j, col_key in enumerate(col_keys)
                    }
                }
                
                existing_data = next((item for item in data_tables if item.get(headers[0]) == data_table[headers[0]]), None)

                if existing_data:
                    for col_key in col_keys:
                        try:
                            if(existing_data[headers[-1]][col_key].keys() == data_table[headers[-1]][col_key].keys()):
                                data_tables.append(data_table[headers[-1]][col_key]) 
                            else:
                                existing_data[headers[-1]][col_key].update(data_table[headers[-1]][col_key])
                        except:
                            data_tables.append(data_table)
                else:
                    data_tables.append(data_table)

            # break

        return [url_tables, data_tables]

    def execute(self, url: str) -> dict:
        res: Response = self.__request.get(url)

        if(res.status_code != 200): return

        parser: PyQuery = self.__parser.execute(res.text, 'body')

        self.__result['title']: str = parser('.breadcrumbs span').text()
        self.__result['date_now']: str = self.__datetime.now()
        self.__result['url']: str = url.replace('#subjekViewTab3', '')

        urls: list[str] = self.__filter_link(parser('#listTabel1 tbody'))

        for i, url in enumerate(urls):
            [url_tables, data_tables] =  self.__get_data_table(url)

            self.__result['data'][i].update({
                'url_tabel': url_tables,
                'data_tables': data_tables
            })

            # break

        return self.__result

# testing
if(__name__ == '__main__'):
    bps: Bps = Bps()
    data = dumps(bps.execute('https://www.archive.bps.go.id/subject/7/energi.html#subjekViewTab3'))

    with open('trash/test_result.json', 'w') as file:
        file.write(data)