import itertools


class CombinationGenerator(object):
    allCombsList = []
    pick_split_list = []
    node_name1 = "node1-name-placeholder"
    node_name2 = "node2-name-placeholder"

    def __init__(self):
        pass

    def process_combination(self, total_attributes_count, subset_seq, node_count):
        # split num of elements per combination range into two. Eg/- (1,3,5) (2,4,6).
        split_range = [range(1, total_attributes_count+1)[i::node_count] for i in range(node_count)]

        # if CombinationGenerator.node_name1 == "node1-name-placeholder":
        #     pick_split_list = split_range[1]
        # else:
        #     pick_split_list = split_range[0]
        #     print "For node list initaited has length = "+ str(len(pick_split_list))

        self.create_combinations(split_range[subset_seq], total_attributes_count)
        return CombinationGenerator.allCombsList

    def create_combinations(self, split_range, total_attributes_count):
        unformatted_list = []
        attribute_list = range(1, total_attributes_count + 1)
        for i in split_range:
            unformatted_list += itertools.combinations(attribute_list, i)
        CombinationGenerator.allCombsList = [list(t) for t in unformatted_list]
        print ("total length:::" + str(len(CombinationGenerator.allCombsList)))
