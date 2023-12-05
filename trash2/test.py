# https://www.bps.go.id/subject/8/ekspor-impor.html#subjekViewTab3
# https://www.bps.go.id/subject/7/energi.html#subjekViewTab3
# https://www.test.id/test/7/1157/1/index.html
# https://www.test.id/test/7/1157/2/index.html

data = {
    'judul_tabel': 'Pelanggan Perusahaan Listrik Negara, 1995-2021',
    'update': '06 Feb 2023',
    'keterangan': 'Statistic Dasar',
    'link_tabel': {
        '2017-2019' 'https://www.bps.go.id/indicator/7/1157/1/rasio-penggunaan-gas-rumah-tangga.html',
        '2017-2020' 'https://www.bps.go.id/indicator/7/1157/1/rasio-penggunaan-gas-rumah-tangga.html'
    },
    'data_tabel':[
        {
            'Provinsi': 'Aceh',
            'Rasio_Penggunaan_Gas_Rumah_Tangga_tahun': {
                '2015': 74.41,
                '2016': 77.94,
                '2017': 82.96,
                '2018': 85.35,
                '2019': 87.06,
                '2020': 90.23,
                '2021': 91.89,
                '2022': 94.25
            }
        }
    ] 
}

data2 = {
    'judul_tabel': 'Pelanggan Perusahaan Listrik Negara, 1995-2021',
    'update': '15 Feb 2023',
    'keterangan': 'Statistic Dasar',
    'data_tabel':[
        {
            'Indikator_Penting_Perusahaan_Listrik': 'Tenaga Listrik yang Terjual (000 MWh)',
            'Indikator_Penting_Perusahaan_Listrik_tahun': {
                '2015': 47995,
                '2016': 46675,
                # ...tahun
            }
        }
    ] 
}

tahun = {
    '2016': 77.94,
    '2021': 91.89,
    '2015': 74.41,
    '2018': 85.35,
    '2017': 82.96,
    '2020': 90.23,
    '2019': 87.06,
    '2022': 94.25
}

sorted_tahun = dict(sorted(tahun.items()))

print(sorted_tahun)

# data = {
#     'Judul_Table': str;
#     'update': str;
#     'keterangan': str;
#     'data_table': list[object] = [
#         {
#             'column_1':str;
#             'column_2': object = {
#                 'tahun': number;
#                 ...
#             }
#         }
#     ]
# }

num1: str = '12,22'
num2: str = '120 022' 


data = {
    'title': 'same',
    'data': {
        '2020': 12
    }
}

data2 = {
    'title': 'same',
    'data': {
        '2021': 112
    }
}
data3 = {
    'title': 'same',
    'data': {
        '2021': 112,
        '2020': 12
    }
}