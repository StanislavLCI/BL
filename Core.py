import xml.dom.minidom as minidom
x = 1
y = 0
z = 2
m = 3
def getTitles(xml):
    """
    Выводим все заголовки из xml.
    """

    tovar = []
    doc = minidom.parse(xml)
    node = doc.documentElement
    books = doc.getElementsByTagName("food")



    titles = []
    for book in books:
        titleObj = book.getElementsByTagName("name")[0]
        titleObj1 = book.getElementsByTagName("price")[0]
        titleObj2 = book.getElementsByTagName("description")[0]
        titleObj3 = book.getElementsByTagName("calories")[0]
        titles.append(titleObj)
        titles.append(titleObj1)
        titles.append(titleObj2)
        titles.append(titleObj3)


    for title in titles:
        nodes = title.childNodes
        for node1 in nodes:
            if node1.nodeType == node1.TEXT_NODE:
                tovar.append(node1.data)

    s = len(tovar) /4
    for i in range(int(s)):
        global x, y, z, m
        print('Товар: '+tovar[y]+';', 'Цена: '+tovar[x]+';','Хорактеристики: '+tovar[z]+';', 'Номер: '+tovar[m]+';')
        z += 4
        x += 4
        y += 4
        m += 4

if __name__ == "__main__":
    document = 'simple.xml'
    getTitles(document)


