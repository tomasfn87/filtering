import json

def verify(jsonFile):
    with open(jsonFile, "r") as fh:
        json_str = fh.read()
    
    try:
        json_data = json.loads(json_str)
        print(1)
        return
    except:
        print(0)
        return

if __name__ == "__main__":
    import sys
    verify(str(sys.argv[1]))
