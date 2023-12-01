from lib import Bps;

# "https://www.bps.go.id/indicator/7/1157/1/rasio-penggunaan-gas-rumah-tangga.html" 

search = Bps();

data = search.execute('https://www.bps.go.id/subject/7/energi.html#subjekViewTab3')

print(data);