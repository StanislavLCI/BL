import xml.dom.minidom as minidom


def getTitles(xml):
    doc = minidom.parse(xml)
    recvizit = doc.getElementsByTagName('ЗначенияРеквизитов')

    titles2 = []
    for i in recvizit:
        tit = i.getElementsByTagName("Значение")[0]
        tit1 = i.getElementsByTagName("Значение")[3]
        tit2 = i.getElementsByTagName("Значение")[2]
        p1 = tit.firstChild.data
        p2 = tit1.firstChild.data
        p3 = tit2.firstChild.data
        titles2.append({'Раздел': p1, 'Номер': p2, 'Наименование': p3})
    ddd = []
    for i in titles2:
        if i['Раздел'] not in ddd:
            if i['Раздел'] in 'import_files/93/931253c5-4bbe-11e5-9d25-0cc47a04d252_15dcae97-32f5-11eb-914d-0cc47a04d252.jpg#85307.3':
                pass
            else:
                ddd.append(i['Раздел'])
        if i['Раздел'] in ddd:
            print(i['Раздел'], i['Наименование'], i['Номер'])


document = '1.xml'
p = getTitles(document)




"""f = {}
a = {}
for item in p:
    name = item['Раздел']
    value = item['Наименование']
    nomer = item['Номер']
    f[name] = f.get(name, []) + [value]
    a['nomer'] = f.get(name, []) + [nomer]
for i in f['Игрушки']:
        print(i+ ' ' + a)
"""
