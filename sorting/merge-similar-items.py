class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        """
        :type items1: List[List[int]]
        :type items2: List[List[int]]
        :rtype: List[List[int]]
        """
        mapper = {}
        
        items = items1 + items2
        for item in items:
            if item[0] not in mapper:
                mapper[item[0]] = item[1]
            else:
                mapper[item[0]] += item[1]
        
        mykeys = sorted(list(mapper.keys()))
        res = []
        for i in mykeys:
            res.append([i, mapper[i]])
        return res
