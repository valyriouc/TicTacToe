import os
import time
import json

def save(path, data):
    with open(path, 'w') as fobj:
        json.dump(data, fobj)

def load(path):
    if (os.path.exists(path)):
        with open(path, 'r') as fobj:
            return json.load(fobj)
                
        
def delete(path):
    if (os.path.exists(path)):
        os.remove(path)