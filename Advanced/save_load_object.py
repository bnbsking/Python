import pickle
D = {'a':'1', 'b':'2'}
with open('object', 'wb') as f:
    pickle.dump(D, f)

with open('object', 'rb') as f:
    E = pickle.load(f)
    print(E, type(D))
    
#

import json
D = {'a':'1', 'b':'2'}
with open('object.json', 'w') as f:
    json.dump(D, f)
    
with open('object.json', 'r') as f:
    D = json.load(f)
    print(D, type(D))
