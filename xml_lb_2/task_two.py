import xml.sax


class CustomContentHandler(xml.sax.ContentHandler):

    def __init__(self):
        self.isInTh = False
        self.isInTd = False
        self.isInTitle = False
        self.isInH_One = False

    def startElement(self, tagName, attrs):
        if tagName == 'html':
            print("<html>", end='')
        elif tagName == 'head':
            print("<head>", end='')
        elif tagName == 'tr':
            print("<tr>", end='')
        elif tagName == 'table':
            print(f'\n<table border="{attrs["border"]}">', end='')
        elif tagName == 'title':
            print("<title>", end='')
            self.isInTitle = True
        elif tagName == 'td':
            print("<td>", end='')
            self.isInTd = True
        elif tagName == 'body':
            print("<body>", end='')
        elif tagName == 'h1':
            print("<h1>", end='')
            self.isInH_One = True
        elif tagName == 'th':
            print("<th>", end='')
            self.isInTh = True

    def characters(self, chars):
        if self.isInTitle:
            print(chars, end='')
        if self.isInH_One:
            print(chars, end='')
        if self.isInTh:
            print(chars, end='')
        if self.isInTd:
            print(chars, end='')

    def endElement(self, tagName):
        if tagName == 'h1':
            print("</h1>", end='\n')
            self.isInH_One = False
        elif tagName == 'title':
            self.isInTitle = False
            print("</title>", end='')
        elif tagName == 'th':
            self.isInTh = False
            print("</th>", end='')
        elif tagName == 'body':
            print("</body>", end='\n')
        elif tagName == 'table':
            print("\n</table>", end='\n')
        elif tagName == 'tr':
            print("</tr>", end='\n')
        elif tagName == 'head':
            print("</head>", end='\n')
        elif tagName == 'html':
            print("</html>", end='')
        elif tagName == 'td':
            self.isInTd = False
            print("</td>", end='')

def main():
    handler = CustomContentHandler()
    xml.sax.parse("tabelle.xml", handler)





