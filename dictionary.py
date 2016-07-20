# Get keys, values and items from a dictionary
def getKeyAndValues():
    dic = {"address":"81 Celestine Dr. Toronto", "name": "Johnny Cao", "family": "2"}

    for key in dic.keys():
        print key
        
    for value in dic.values():
        print value
        
    for key,value in dic.items():
        print key + "::" + value    

    print dic["name"] + " lives at " + dic["address"] + "and he has " + dic["family"] + " family members." 
    
getKeyAndValues()