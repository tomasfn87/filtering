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
        # Error #1: not a JSON file
        return print(1)
    jsonFile = file
    with open(jsonFile, "r") as fh:
        json_str = fh.read()
    try:
        json_data = json.loads(json_str)
        #1: Ok, valid JSON
        return print(0)
    except:
        # Error #2: invalid JSON data
        return print(2)

if __name__ == "__main__":
    import sys
    verify(str(sys.argv[1]))
