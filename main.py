from bitrix24 import *

class Loader:
    def __init__(self):
        self.bx24 = Bitrix24('https://ys-group.bitrix24.ru/rest/1/gx4teahzdry7uxaa')



    def run(self):

        print(self.bx24.callMethod('crm.product.property.fields'))


if __name__ == '__main__':
    a = Loader()
    a.run()