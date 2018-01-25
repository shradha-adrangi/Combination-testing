from crqasoap.nodes.distributor import FeedFileUtil


class NodeProcessorFirst(object):
    feed_filename = "node1-feed.txt"

    def __init__(self):
        pass

    # Node process initiates here
    def processfeedfile(self):
        f = FeedFileUtil.FeedFileUtil()
        comb_list = f.fetchcombinationlistfromfile(NodeProcessorFirst.feed_filename)
        print "FIRST - NODE list length :: " + str(len(comb_list))
