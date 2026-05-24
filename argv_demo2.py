import sys

print(f"Script Name: {sys.argv[0]}")
print(f"All arguments: {sys.argv}")

if len(sys.argv) > 1:
    print(f"First argument: {sys.argv[1]}")
else:
    print("No first argument")

if len(sys.argv) > 2:
    print(f"Second argument: {sys.argv[2]}")
else:
    print("No second argument")
