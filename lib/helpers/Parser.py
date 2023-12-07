from pyquery import PyQuery

class Parser:
    def execute(self, source: str, selector: str) -> PyQuery:
        try:
            return PyQuery(source)(selector)
        except Exception as e:
            print(e)


# testing
if(__name__ == '__main__'):
    parser: Parser = Parser()
    print(parser.execute('<h1>test<span>this is keyyy</span></h1>', 'span').text())