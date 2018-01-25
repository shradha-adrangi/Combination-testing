from crqasoap.nodes.distributor import FeedFileUtil
from crqasoap.xmlparser import SoapXMLParser
from crqasoap.master.controller import CombinationGenerator
from crqasoap.nodes.processor import NodeProcessorFirst, NodeProcessorSecond

class Distibutor(object):

    def __init__(self):
        pass

    # Fetch post-request xml and fetch all optiona attributes into a list
    f = FeedFileUtil.FeedFileUtil()
    t = SoapXMLParser.SoapXMLParser()
    attrlist = t.fetchxmlnodes("../../requestxml/")

    #Pass the attribute list to generate combination and split it into two sub-list
    comb = CombinationGenerator.CombinationGenerator()
    split_list = comb.initiate_process(attrlist)
    print str(len(split_list[0]))

    #Fetch the two feed files, clear them and write the sub-list to each of the feed files.
    feed_files = t.fetchfeedfiles("../properties/feedfiles/")
    f.clearfilecontent(feed_files)
    f.writecombinationstofiles(feed_files,split_list)

    #Trigger both nodes to process their respective feed files.
    NodeProcessorFirst.NodeProcessorFirst().processfeedfile()
    NodeProcessorSecond.NodeProcessorSecond().processfeedfile()
    print "finished processing nodes!!!!"

