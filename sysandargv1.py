import sys

if len(sys.argv) !=2:
    print("missing command line argument\n ")
    sys.exit(1)


print(f"hello {sys.argv[1]}")
sys.exit(0)

