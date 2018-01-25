class CombinationGenerator:
    allCombsList = []

    def __init__(self):
        pass

    def process_combination(self, attribute_list):

        """
        Combination generation process starts here
        Args:
            attribute_list: list of n (optional) attributes for combination generation

        Returns:

        """
        attribute_list.remove("matterNumber")
        attribute_list.remove("clientNumber")
        attribute_list.remove("clientName")

        listlength = len(attribute_list)
        for r in range(1, listlength+1):
            # self.generate_combination(r, listlength)
            comb_Array = [None] * r;
            # print str(comb_Array)
            self.combination_util(comb_Array, 0, listlength, 0, r)
        print "total length:::" + str(len(CombinationGenerator.allCombsList))
        return

    def combination_util(self, comb_Array, start, end, index, numofelementincomb):
        """
        Formula goes here, to generate each combination
        Args:
            comb_Array: each unique combination generated, is put into this temp list
            start: the pointer held on to the element in attibute list
            eg/- for first iteration of list, [a,b,c,d,e,f] : START will be fixed on to 'a', and END will be fixed on to 'f' and then,
            elements other than 'a' are combined with START(a), i.e [a,b] [a,c] [a,d] [a,e] [a,f] : until END is reached. And INDEX holds the index on the list
        """
        if index == numofelementincomb:
            if (numofelementincomb > 1):
                temp = ':'.join(str(x) for x in comb_Array)
                CombinationGenerator.allCombsList.append(temp)
            else:
                CombinationGenerator.allCombsList.append(str(comb_Array[0]))
            return
        for i in range(start, end):
            if i <= end and end-i+1 >= numofelementincomb-index:
                comb_Array[index] = i
                self.combination_util(comb_Array, i + 1, end, index + 1, numofelementincomb)
        return

    def initiate_process(self, attrlist):
        """
        Process initiator
        Args:
            attrlist: list of attributes to generate combinations
        """
        self.process_combination(attrlist)
        split_list = self.splitcombinations(CombinationGenerator.allCombsList, 2)
        return split_list

    def splitcombinations(self, lst, n):
        """
        Splits the whole combination list into two sub-list
            Args:
        n: number of sub-list required
        lst: list to be split
       """
        return [lst[i::n] for i in xrange(n)]


