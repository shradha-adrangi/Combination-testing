from crqasoap.nodes.distributor import FeedFileUtil


class NodeProcessorSecond(object):
        feed_filename = "node2-feed.txt"

        def __init__(self):
                pass

        #Node process initiates here
        def processfeedfile(self):
                t = FeedFileUtil.FeedFileUtil()
                comb_list = t.fetchcombinationlistfromfile(NodeProcessorSecond.feed_filename)
                print "SECOND - NODE list length :: " + str(len(comb_list))
