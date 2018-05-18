import os
import json
from functools import reduce

def firstElem(ary):
    return ary[0] if len(ary)>0 else None

# take the file extension and use as key
def reducer(x, y):
    ext = y.split('.')[-1]
    x[ext] = y
    return x

# given a directory, find the relevant obj, mtl, and image files
def process_dir(d):
    name = d
    files = [d+'/'+f for f in os.listdir(d) if os.path.isfile(d+'/'+f) and not f.startswith('.')]
    # add each file type into the same object
    obj = reduce(reducer, [{}]+files)
    if 'json' in obj:
        obj['fbx'] = obj['json']
        del obj['json']
    obj['name'] = d
    return obj

dirs = os.listdir('./')
l = [ process_dir(d) for d in dirs if os.path.isdir(d) and not d.startswith('.')]


print(json.dumps(l, indent=4,separators=(',', ': ')))

