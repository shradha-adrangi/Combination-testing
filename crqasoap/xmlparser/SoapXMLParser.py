import os
import xml.etree.ElementTree as ET


class SoapXMLParser:
    def __init__(self):
        pass

    def fetchfile(self, path, fetchFeedFile):
        """
        Args:
            path(str): folder path to request xml
        Returns: request xml file located at the 'path'
        """
        file = ""
        if fetchFeedFile != "":
            ospath = os.listdir(path)
            print("feed-filename:::" + fetchFeedFile)
            file = os.path.join(os.path.abspath(path), fetchFeedFile)
        else:
            for foldername in os.listdir(path):
                if (foldername.startswith("matter")):
                    print("foldername:::" + foldername)
                    print (os.listdir(path + foldername))
                    filename = os.listdir(path + foldername)[0]
                    file = os.path.join(os.path.abspath(path + "matterws"), filename)
                    print("XML file with path:::"  + file)
        return file

    def fetchfeedfiles(self, path):
        files = []
        for i in os.listdir(path):
            files.append(os.path.join(os.path.abspath(path), i))
        return files

    def fetchxmlasstring(self, path):
        """
        Args:
            path(str): folder path to request xml
        Returns: xml as string, required to pass in the web service call
        """
        data = open(self.fetchxml(path), "r").read()
        print("data" + data)
        return data


    def fetchxmlnodes(self, path):
        """
        Used to fetch all the attribute from xml and reads into list
        Args:
            path(str): folder path to request xml
        """
        attribute_list = []
        element = ET.parse(self.fetchfile(path, ""))
        elem_list = element.getroot()[1][0]
        for elem in elem_list:
            attribute_list.append(elem.tag)
        return attribute_list


