from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        # Only parse the 'anchor' tag.
        x = []
        if tag == "a":
           # Check the list of defined attributes.
           for name, value in attrs:
               # If href is defined, print it.
               if name == "href":
                   x.append(value)
                #    print(name, "=", value)
        print(x)


parser = MyHTMLParser()
f = open("2022/wpcd/wp/A/A_cappella.htm", "r")
s = f.read()
parser.feed(s)