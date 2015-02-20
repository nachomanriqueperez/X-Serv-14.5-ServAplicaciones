#!/usr/bin/python
import webapp;

class miservi(webapp.webApp):

    def process(self,parsedRequest):
        """Parse"""
        return ("200 OK","<html><body><b>Adios mundo cruel!</h1></body></html>")

if __name__ == "__main__":
    testWebApp = miservi("localhost",1234);
