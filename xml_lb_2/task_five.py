import xml.dom.minidom


def main():
    tree = xml.dom.minidom.parse("deliveries.xml")
    articles = tree.getElementsByTagName("article")
    for article in articles:
        name = article.getElementsByTagName("name")[0]
        supplier = article.getElementsByTagName("supplier")[0]
        print(f"{supplier.firstChild.data} supplies: {name.firstChild.data}")