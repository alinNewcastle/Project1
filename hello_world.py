import sys
import platform

print("Hello World")

print( 1, sys.version)
print( 2, platform.python_implementation())
print( 3, sys.executable)

if sys.version_info[0] > 2:
    print("\n Good version!")
    sys.exit(1)