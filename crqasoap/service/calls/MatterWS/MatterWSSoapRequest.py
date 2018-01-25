from crqasoap.xmlparser import SoapXMLParser
import requests
import os
import filemapper as fm


class MatterWSSoapRequest:
    def __init__(self):
        pass

    def parserequest(self):
        url = "https://staging-api.chromeriver.com/ws_MatterV1"
        headers = {'content-type': 'text/xml'}

        t = SoapXMLParser.SoapXMLParser()
        body = t.fetchxmlasstring("../../requestxml/")
        print(body)

        response = requests.post(url, data=body, headers=headers)

        print ("resonse:::" + response.content)











