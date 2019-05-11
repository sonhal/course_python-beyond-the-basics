import sys

import reader

r = reader.Reader(sys.argv[1])
try:
    print(r.read())
except Exception:
    print("Could not read the file")
finally:
    r.close()
