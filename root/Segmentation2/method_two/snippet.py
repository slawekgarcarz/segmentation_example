# import json
# import math
# import random
# import itertools
# import statistics
import http.client


# class Segmentation1:
#     def __init__(self, data):
#         self.data = data
#
#     def method_one(self):
#         """
#         Randomly shuffles the data.
#         """
#         random.shuffle(self.data)
#         return self.data
#
#     def method_two(self):
#         """
#         Calculates the square root of each element in the data.
#         """
#         return [math.sqrt(x) for x in self.data if x >= 0]
#
#     def method_three(self):
#         """
#         Calculates the mean of the data.
#         """
#         return statistics.mean(self.data)

class Segmentation2:
    def __init__(self, items):
        self.items = items

    # def method_one(self):
    #     """
    #     Generates all possible pairs from the items.
    #     """
    #     return list(itertools.combinations(self.items, 2))
    #
    # def method_two(self):
    #     """
    #     Converts the items list to a JSON string.
    #     """
    #     return json.dumps(self.items)

    def method_three(self):
        """
        Makes a simple HTTP GET request and returns the response status.
        """
        conn = http.client.HTTPConnection("example.com")
        conn.request("GET", "/")
        res = conn.getresponse()
        return res.status
