from lib import Bps;
from json import dumps;

# "https://www.bps.go.id/indicator/7/1157/1/rasio-penggunaan-gas-rumah-tangga.html" 

search = Bps();

data = dumps(search.execute('https://www.archive.bps.go.id/subject/7/energi.html#subjekViewTab3'));
data2 = dumps(search.execute('https://www.archive.bps.go.id/subject/7/energi.html#subjekViewTab3'));

with open('data/result.json', 'w') as file:
    file.write(data);

with open('data/result2.json', 'w') as file:
    file.write(data);