from crqasoap.xmlparser import SoapXMLParser

class FeedFileUtil(object):

    def __init__(self):
        pass

    def clearfilecontent(self, feed_files):
        for file in feed_files:
            raw_file = open(file, "r+")
            contents = raw_file.read().split("\n")
            raw_file.seek(0)
            raw_file.truncate(0)
            raw_file.close()

    def writecombinationstofiles(self, feed_files, split_list):
        for single_file, part_list in zip(feed_files, split_list):
            raw_file = open(single_file, "r+")
            raw_file.write("\n".join(map(lambda x: str(x), part_list)))
            raw_file.close()

    def fetchcombinationlistfromfile(self, filename):
        comb_list = []
        t = SoapXMLParser.SoapXMLParser()
        file = t.fetchfile("../properties/feedfiles/", filename)
        with open(file) as f:
            comb_list = [line.strip() for line in f]
            # print str(len(comb_list))
        # file.close()
        return comb_list



