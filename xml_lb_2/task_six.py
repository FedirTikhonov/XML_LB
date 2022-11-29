import random
import xml.dom.minidom


def main():
    tree = xml.dom.minidom.parse("deliveries.xml")
    articles = tree.getElementsByTagName("article")
    articleDict = {}
    productDict = {}
    is_changed = False
    for article in articles:
        id = article.getAttribute('id')
        if id in articleDict:
            print(f"\nRepeated Article ID detected; Generating new ID:\nOld ID: {id}")
            while id in articleDict:
                id = str(random.randint(1000, 9999))
            articleDict[id] = {}
            print(f"New ID: {id}")
        else:
            articleDict[id] = {}
        print(f"\nAtricle № {id}:")
        name = article.getElementsByTagName("name")[0]
        supplier = article.getElementsByTagName("supplier")[0]
        price = article.getElementsByTagName("price")[0]
        price_attr = price.getAttribute('unitprice')

        if name.firstChild.data not in productDict:
            productDict[name.firstChild.data] = float(price.firstChild.data)
            is_changed = False
        else:
            is_changed = True
            if float(price.firstChild.data) < productDict[name.firstChild.data]:
                productDict[name.firstChild.data] = float(price.firstChild.data)
        articleDict[id]['name'] = name.firstChild.data
        print(' ' * 3 + f"Name: {name.firstChild.data}")
        articleDict[id]['price'] = productDict[name.firstChild.data]
        if is_changed:
            print(' ' * 3 + f"Adjusting price on the existing product:\nOld price: {price.firstChild.data}\nNew price: {productDict[name.firstChild.data]}")
        else:
            print(' ' * 3 + f'Price: {productDict[name.firstChild.data]}, Unitprice is {price_attr}')
        articleDict[id]['supplier'] = supplier.firstChild.data
        print(' ' * 3 + f"Supplier: {supplier.firstChild.data}")
    print(articleDict)
    print(productDict)