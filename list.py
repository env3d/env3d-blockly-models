import os
import json
from functools import reduce

def firstElem(ary):
    return ary[0] if len(ary)>0 else None

def reducer(x, y):
    x[y[-3::]] = y
    return x

# given a directory, find the relevant obj, mtl, and image files
def process_dir(d):
    name = d
    files = [d+'/'+f for f in os.listdir(d) if os.path.isfile(d+'/'+f) and not f.startswith('.')]
    obj = reduce(reducer, [{}]+files)
    obj['name'] = d
    return obj

dirs = os.listdir('./')
l = [ process_dir(d) for d in dirs if os.path.isdir(d)]


print(json.dumps(l, indent=4,separators=(',', ': ')))

