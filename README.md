[![Twitter: romy](https://img.shields.io/twitter/follow/RomySihananda)](https://twitter.com/RomySihananda)

# craw-BadanPusatStatistik

![](https://raw.githubusercontent.com/RomySaputraSihananda/RomySaputraSihananda/main/images/frecrop.jpeg)

craw-BadanPusatStatistik adalah program untuk mengambil data dari website Badan Pusat Statistik Indonesia. </br>Menggunakan module **Requests** untuk mengambil content dari website Badan Pusat Statistik Indonesia </br>dan diparsing Menggunakan module **pyquery**, menggunakan **Flask** untuk web Server dan **flask_restx** </br> untuk swagger-ui documentation

## Requirements

- **Python** >= 3.11.4
- **Flask** >= 2.1.0
- **flask_restx** >= 0.5.1
- **gevent** >= 23.9.0.post1
- **pyquery** >= 2.0.0
- **pytz** >= 2023.3.post1
- **Requests** >= 2.31.0

## Installation

```sh
# Clonig Repository
git clone https://github.com/romysaputrasihananda/craw-BadanPusatStatistik

# Ganti Directory
cd craw-BadanPusatStatistik;

# Install Requirement
pip install -r requirements.txt
```

## Example Usages

craw-BadanPusatStatistik bisa diakses melalui docs rest API (Swagger-ui) atau melalui terminal

### CLI

```sh
# Sosial dan Kependudukan -> Sosial
python main.py --topic=Sosial

# Ekonomi dan Perdagangan  -> Ekonomi
python main.py --topic=Ekonomi

# Pertanian dan Pertambangan -> Pertanian
python main.py --topic=Pertanian
```

### Swagger-ui

```sh
# Jalankan server
python main.py --server=true --port=4444

# output
# [INFO] [2023-12-06 01:13:38,637] :: listening  -> http://localhost:4444 ....
# [INFO] [2023-12-06 01:13:38,637] :: swagger-ui -> http://localhost:4444/docs ....
```

### Sample Data

```json
{
  "title": "Energi",
  "url": "https://www.archive.bps.go.id/subject/7/energi.html",
  "date_now": "2023-12-05T17:38:45",
  "data": [
    {
      "id": "b5d5d9d3851d576d2ce42234e21951a5",
      "judul_tabel": "Volume Ekspor Migas-NonMigas, 2012-2023",
      "update": "2023-12-01",
      "keterangan": "Statistik Dasar",
      "url_tabel": [
        "https://www.archive.bps.go.id/indicator/7/1157/1/rasio-penggunaan-gas-rumah-tangga.html",
        "https://www.archive.bps.go.id/indicator/7/1157/2/rasio-penggunaan-gas-rumah-tangga.html",
        "https://www.archive.bps.go.id/indicator/7/1157/3/rasio-penggunaan-gas-rumah-tangga.html"
      ],
      "data_tables": [
        {
          "judul_tabel": "Rasio Penggunaan Gas Rumah Tangga 2020-2022",
          "Provinsi": "ACEH",
          "Rasio_Penggunaan_Gas_Rumah_Tangga": {
            "2020": 90.23,
            "2021": 91.89,
            "2022": 94.25,
            "2017": 82.96,
            "2018": 85.35,
            "2019": 87.06,
            "2015": 74.41,
            "2016": 77.94
          }
        }
        // ... more data
      ]
    }
    // more data
  ]
}
```

## License

This project is licensed under the [MIT License](LICENSE).
