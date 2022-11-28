import xml.sax

class CustomContentHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.articleDict = {}
        self.isInArticle = False
        self.isInName = False
        self.isInSupplier = False
        self.isInPrice = False
        self.currentArticleID = 0
        self.internalArticleDict = {}

    def startElement(self, tagName, attrs):
        if tagName == 'article':
            print('Article №: ' + attrs['id'])
            self.currentArticleID = attrs["id"]
            if self.currentArticleID in self.articleDict:
                print("Repeated input of Article with the same ID")
                self.currentArticleID = '0'
            else:
                self.currentArticleID = str(attrs['id'])
                self.articleDict[self.currentArticleID] = {}
            self.articleDict[attrs['id']] = {}
            self.isInArticle = True
            self.currentArticleID = attrs['id']
        elif tagName == 'name':
            self.isInName = True
        elif tagName == 'price':
            self.isInPrice = True
            if attrs['unitprice'] == 'true':
                print("Valid Price of", end=' ')
            else:
                print("Invalid Price of", end=' ')
        elif tagName == 'supplier':
            self.isInSupplier = True

    def characters(self, chars):
        if self.isInName:
            print(f"Name: {chars}", end='\n')
            self.articleDict[self.currentArticleID]['name'] = chars
        if self.isInPrice:
            print(chars)
            self.articleDict[self.currentArticleID]['price'] = float(chars)
        if self.isInSupplier:
            print(f"Supplier: {chars}", end='\n')
            self.articleDict[self.currentArticleID]['supplier'] = chars


    def endElement(self, tagName):
        if tagName == 'name':
            self.isInName = False
        elif tagName == 'supplier':
            self.isInSupplier = False
        elif tagName == 'price':
            self.isInPrice = False
        elif tagName == 'article':
            self.isInArticle = False
            print()

    def startDocument(self):
        print('Delivery list XML document deliveries.xml')

    # Handle endDocument
    def endDocument(self):
        self.articleDict.pop('0', None)
        print('Delivery list finished')


def main():
    handler = CustomContentHandler()
    xml.sax.parse("deliveries.xml", handler)