import os
import locale
import sys
def debug_open(path, mode="r", encoding=None):
    print("=== DEBUG FILE OPEN ===")
    print(f"Requested path      : {path}")
    print(f"Absolute path       : {os.path.abspath(path)}")
    print(f"Current directory   : {os.getcwd()}")
    print(f"File exists?        : {os.path.exists(path)}")
    if os.path.exists(path):
        print(f"file size           : {os.path.getsize(path)}")
    print(f"Is file?            : {os.path.isfile(path)}")
    print(f"Preferred encoding  : {locale.getpreferredencoding()}")
    print(f"sys.stdout.encoding : {sys.stdout.encoding}")
    print(f"sys.getdefaultencoding(): {sys.getdefaultencoding()}")
    print("------------------------")

    try:
        f = open(path, mode, encoding=encoding)
        print("Result              : SUCCESS 🎉")
        print("========================")
        f.close()
        return True
    except Exception as e:
        print("Result              : ERROR ❌")
        print(f"Exception           : {type(e).__name__}")
        print(f"Message             : {e}")
        print("========================")
        return False

#debug_open(INI_FILE)