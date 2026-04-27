import sys

if len(sys.argv) > 1:
    print(f"Hello, World! Message: {' '.join(sys.argv[1:])}")
else:
    print("Hello, World!")