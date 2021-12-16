
"""
Given a nested dictionary, flatten the dictionary, where nested dictionary keys can be represented through dot notation.

Example:
Input: {
  'a': 1,
  'b': {
    'c': 2,
    'd': {
      'e': 3
    }
  }
}
Output: {
  'a': 1,
  'b.c': 2,
  'b.d.e': 3
}
You can assume there will be no arrays, and all keys will be strings.

"""


d = {
    'a': 1,
    'b': {
        'c': 2,
        'd': {
            'e': 3
        }
    }
}

my_map = {"a" : 1,
        "b" : {
            "c": 2,
            "d": 3,
            "e": {
                "f":4,
                6:"a",
                5:{"g" : 6},
                "l":[1,"two"]
            }
    }
}
 
def flatten_dict(pyobj, keystring=''):
    if type(pyobj) == dict:
        keystring = keystring + '.' if keystring else keystring
        for k in pyobj:
            yield from flatten_dict(pyobj[k], keystring + str(k))
    else:
        yield keystring, pyobj
 
print("Input : %s\nOutput : %s\n\n" %
     (my_map, { k:v for k,v in flatten_dict(my_map) }))
 
print("Input : %s\nOutput : %s\n\n" %
     (d, { k:v for k,v in flatten_dict(d) }))



