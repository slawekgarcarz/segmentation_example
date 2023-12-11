# Segmentation example
**Note: This example is relevant for python language and doesn't cover all possibilities**

## Description
This repository contains example of code segmentation for codebase bot.
The repository is organized into tree-like structure, where each folder 
represents a node in a tree and `snippet.py` file represents the code 
snippet that is in particular node. Full example code is presented below:

```python
import json
import math
import random
import itertools
import statistics
import http.client


class Segmentation1:
    def __init__(self, data):
        self.data = data

    def method_one(self):
        """
        Randomly shuffles the data.
        """
        random.shuffle(self.data)
        return self.data

    def method_two(self):
        """
        Calculates the square root of each element in the data.
        """
        return [math.sqrt(x) for x in self.data if x >= 0]

    def method_three(self):
        """
        Calculates the mean of the data.
        """
        return statistics.mean(self.data)


class Segmentation2:
    def __init__(self, items):
        self.items = items

    def method_one(self):
        """
        Generates all possible pairs from the items.
        """
        return list(itertools.combinations(self.items, 2))

    def method_two(self):
        """
        Converts the items list to a JSON string.
        """
        return json.dumps(self.items)

    def method_three(self):
        """
        Makes a simple HTTP GET request and returns the response status.
        """
        conn = http.client.HTTPConnection("example.com")
        conn.request("GET", "/")
        res = conn.getresponse()
        return res.status

```

The idea is to segment the code into smaller meaningful segments, so that each part
is runnable code with all relevant imports and variables. The segmentation is done
on either class or function level.

Code above would be segmented as follows:

```
└── root
    |
    ├── Segmentation1
    |   ├── method_one
    |   ├── method_two
    |   └── method_three
    |
    └── Segmentation2
        ├── method_one
        ├── method_two
        └── method_three
```

Where each node contain only code for that particular segment. For example,
code for `method_one` in `Segmentation1` would be:

```python
import random

class Segmentation1:
    def __init__(self, data):
        self.data = data

    def method_one(self):
        """
        Randomly shuffles the data.
        """
        random.shuffle(self.data)
        return self.data
```

and the code for `method_two` in `Segmentation2` would be:

```python
import json

class Segmentation2:
    def __init__(self, items):
        self.items = items

    def method_two(self):
        """
        Converts the items list to a JSON string.
        """
        return json.dumps(self.items)
```

Advantage of this approach is that each code snippet is runnable and contains all
relevant information for particular class/function/method and the tree can be easily traversed to
account for context limits of the LLM.

Disadvantage is that some snippets might be too big for the LLM even after segmentation.
