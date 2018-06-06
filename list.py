import os
import json
import itertools
from functools import reduce

def firstElem(ary):
    return ary[0] if len(ary)>0 else None

# take the file extension and use as key
def reducer(x, y):
    ext = y.split('.')[-1]
    x[ext] = y
    return x

def process_single_model(d):
    files = [d+'/'+f for f in os.listdir(d) if os.path.isfile(d+'/'+f) and not f.startswith('.')]
    # add each file type into the same object
    obj = reduce(reducer, [{}]+files)
    if 'json' in obj:
        obj['fbx'] = obj['json']
        del obj['json']
    obj['name'] = d
    return obj

# d is an assets directory, with a list of json
def process_assets(d):
    json_files = [ { 'fbx': d+'/assets/'+f, 'name': d+'/'+f.split('.')[0] }
                   for f in os.listdir(d+'/assets') if f.endswith('json') ]
    return json_files

    
# given a directory, find the relevant obj, mtl, and image files
def process_dir(d):
    name = d
    if (os.path.isdir(d+'/assets')):
        return process_assets(d)
    else:
        return [process_single_model(d)]

dirs = os.listdir('./')
l = [ process_dir(d) for d in dirs if os.path.isdir(d) and not d.startswith('.')]

ll = list(itertools.chain(*l));

print(json.dumps(ll, indent=4,separators=(',', ': ')))

