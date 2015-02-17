#!/usr/bin/python

import webapp
import random


class myServ(webapp.webApp):

    def process(self, parsedRequest):
        """Process the relevant elements of the request.

        Returns the HTTP code for the reply, and an HTML page.
        """

        num = str(random.randint(1, 10000000))
        resp = "<a href= http://localhost:1234/" + num + " >Dame Otra! </a>"
        return ("200 OK", "<html><body><h1>"+resp+"</h1></body></html>")
if __name__ == "__main__":
    try:
        testServaleat = myServ("localhost", 1234)
    except KeyboardInterrupt:
            print "Closing binded socket"
