import os
import json

# returns an object at origin with no rotation
def process_file(f):
    obj = {}
    obj["Asset"] = f
    obj["Offset"] = [0,0,0]
    obj["Rotation"] = [0,0,0]
    obj["Scale"] = [1,1,1]
    return obj
    

fbx_files = [process_file(f) for f in os.listdir('./') if f.endswith('fbx')]

dir_name = os.path.basename(os.getcwd())

print(json.dumps({"AssetID":dir_name, "Components":fbx_files}, indent=4,separators=(',', ': ')))
