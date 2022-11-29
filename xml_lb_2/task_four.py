import xml.dom.minidom

def main():
    tree = xml.dom.minidom.parse("deliveries_unsorted.xml")
    print("<deliveries>")
    articles = tree.getElementsByTagName("article")
    for article in articles:
        print(' ' * 3 + f'<article id="{article.getAttribute("id")}">')
        name = article.getElementsByTagName("name")[0]
        print(' ' * 6 + f"<name>{name.firstChild.data}</name>")
        price = article.getElementsByTagName("price")[0]
        price_attr = price.getAttribute("unitprice")
        print(' ' * 6 + f'<price unitprice="{price_attr}">{price.firstChild.data}</price>')
        supplier = article.getElementsByTagName("supplier")[0]
        print(' ' * 6 + f"<supplier>{supplier.firstChild.data}</supplier>")
        print(' ' * 3 + "</article>")
    print("</deliveries>")