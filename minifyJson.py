import texto
import json

Texto = texto.Texto

def minify(jsonFile):
    with open(jsonFile, "r") as fh:
        json_str = fh.read()

    minifiedJson = Texto.cleanSpacesOutside(json_str)
    
    # json_value = json.loads(minifiedJson)

    print(minifiedJson)

if __name__ == "__main__":
    import sys
    minify(str(sys.argv[1]))
