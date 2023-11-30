from hashlib import md5;

class Hasher:
    def execute(self, text: str) -> str:
        try:
            return md5(text.encode()).hexdigest();
        except Exception as e:
            print(e)

# testing
if(__name__ == '__main__'):
    hasher: Hasher = Hasher();
    print(hasher.execute('romy saputra cuyyy'));