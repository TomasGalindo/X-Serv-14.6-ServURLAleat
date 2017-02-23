#! /usr/bin/python3

import webapp


class urlaleat(webapp.webApp):
    def process(self, parsedRequest):
        import random

        num = random.randint(0, 999999999)
        return("200 OK",
               "<html><body><a href = " +
               str(num) +
               ">Dame mas</a></body></html>"
               )

if __name__ == "__main__":  # si esto es el programa principal.
    testWebApp = urlaleat("localhost", 1234)  # hacer urlaleat
