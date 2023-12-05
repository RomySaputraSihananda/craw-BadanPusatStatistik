[![Twitter: romy](https://img.shields.io/twitter/follow/RomySihananda)](https://twitter.com/RomySihananda)

# craw-BadanPusatStatistik

![](https://raw.githubusercontent.com/RomySaputraSihananda/RomySaputraSihananda/main/images/frecrop.jpeg)

craw-BadanPusatStatistik adalah program untuk mengambil data dari website Badan Pusat Statistik Indonesia.

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

# Change Current Working Directory
cd craw-BadanPusatStatistik;

# Install Requirement Dependency Modules
pip install -r requirements.txt
```

## Example Usages

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
python main.py --server=true
```

## License

This project is licensed under the [MIT License](LICENSE).
