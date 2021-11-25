from texto import Texto as T

def minify(file):
    with open(file, "r") as fh:
        fileContent = fh.read()
    
    print(T.cleanSpacesOutside(fileContent))

if __name__ == "__main__":
    import sys
    minify(str(sys.argv[1]))
