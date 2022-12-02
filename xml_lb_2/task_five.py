import xml.dom.minidom


def main():
    tree = xml.dom.minidom.parse("deliveries.xml")
    articles = tree.getElementsByTagName("article")
    supplierDict = {}
    supplierNames = []
    for article in articles:
        name = article.getElementsByTagName("name")[0]
        supplier = article.getElementsByTagName("supplier")[0]
        if supplier.firstChild.data not in supplierDict:
            supplierDict[supplier.firstChild.data] = []
            supplierNames.append(supplier.firstChild.data)
            supplierDict[supplier.firstChild.data].append(name.firstChild.data)
        else:
            supplierDict[supplier.firstChild.data].append(name.firstChild.data)
    for supplier in supplierNames:
        print(f"{supplier} supplies: ", end=' ')
        for product_id in range(len(supplierDict[supplier])):
            print(supplierDict[supplier][product_id], end=' ')
        print()
