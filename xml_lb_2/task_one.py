import xml.sax

class CustomContentHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.isInArticle = False
        self.isInName = False
        self.isInDeliveries = False
        self.isInSupplier = False
        self.isInPrice = False
        self.currIndent = 0

    def startElement(self, tagName, attrs):
        if tagName == 'deliveries':
            print("<deliveries>", end="\n")
        elif tagName == 'article':
            self.currIndent += 3
            print(' ' * self.currIndent + f"<article id={attrs['id']}>")
            self.isInArticle = True
        elif tagName == 'name':
            if self.currIndent == 3:
                self.currIndent += 3
            print(' ' * self.currIndent + "<name>", end='')
            self.isInName = True
        elif tagName == 'price':
            if self.currIndent == 3:
                self.currIndent += 3
            self.isInPrice = True
            print(' ' * self.currIndent + f"<price unitprice={attrs['unitprice']}>", end='')
        elif tagName == 'supplier':
            if self.currIndent == 3:
                self.currIndent += 3
            print(' ' * self.currIndent + "<supplier>", end='')
            self.isInSupplier = True

    def characters(self, chars):
        if self.isInName:
            print(chars, end='')
        if self.isInPrice:
            print(chars, end='')
        if self.isInSupplier:
            print(chars, end='')


    def endElement(self, tagName):
        if tagName == 'deliveries':
            self.currIndent -= 3
            print(' ' * self.currIndent + "</deliveries>")
        elif tagName == 'name':
            print("</name>", end='\n')
            self.isInName = False
            self.currIndent -= 3
        elif tagName == 'supplier':
            self.currIndent -= 3
            self.isInSupplier = False
        elif tagName == 'price':
            print("</price>", end='\n')
            self.currIndent -= 3
            self.isInPrice = False
        elif tagName == 'article':
            self.isInArticle = False
            print(' ' * self.currIndent + "\n" + self.currIndent * ' ' + "</article>")
            self.currIndent -= 3

def main():
    handler = CustomContentHandler()
    xml.sax.parse("deliveries.xml", handler)