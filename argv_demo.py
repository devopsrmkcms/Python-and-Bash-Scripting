# argv_demo.py
import sys

print("Script name:", sys.argv[0])
print("All arguments:", sys.argv)

if len(sys.argv) > 1:
    print("First argument:", sys.argv[1])
else:
    print("No arguments provided")
