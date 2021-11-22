import json

def isExtensionJson(file):
    if len(file) < 6:
        return False
    fileExtension = ""
    for i in range(-5, 0):
        fileExtension += file[i]
    if fileExtension != ".json":
        return False
    return True

def verify(file):
    if not isExtensionJson(file):
        print(1) # Error #1: not a JSON file
        return
    jsonFile = file
    with open(jsonFile, "r") as fh:
        json_str = fh.read()
    try:
        json_data = json.loads(json_str)
        print(0) #1: Ok, valid JSON
        return
    except:
        print(2) # Error #2: invalid JSON data
        return

if __name__ == "__main__":
    import sys
    verify(str(sys.argv[1]))
