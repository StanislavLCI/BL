from bitrix24 import *
from PIL import Image

class Loader:
    def __init__(self):
        self.bx24 = Bitrix24('https://ys-group.bitrix24.ru/rest/1/gx4teahzdry7uxaa')



    def run(self):
        f = open('z.jpg')

        self.bx24.callMethod('crm.product.add', fields={'NAME': 'Тестовой название',
                                                        'PRICE': 2600,
                                                        'PREVIEW_PICTURE': f})


if __name__ == '__main__':
    a = Loader()
    a.run()