"""Provides an example for how one could realize a string encoding pipeline for plugin resources.

Warning:

    This is NOT a product in any sense, it is an EXAMPLE. Please USE IT AT YOUR OWN RISK. We cannot 
    guarantee that it will work for all use-cases or add features that you might need.

Note:

    This script can be run with any Python interpreter that supports the standard library; you do
    not need to run it in Cinema 4D or with c4dpy.

The idea is simple: users write the plugin resources in Unicode, e.g., use 'ä' or 'é' in their
string files, and this script encodes these Unicode characters to their escape sequences in ASCII.
The script can be used to encode, decode, restore, or clean up string files in a given directory. It
does not matter if these string files are used by dialogs, descriptions, or other parts of a
Cinema 4D plugin, as long as they end in ".str".

The script will create backups of the original files before encoding them, when asked to do so. It
will also create a log file in the same directory as the script.

The script can be run without any arguments; it will then use the 'res' directory next to the
script and ask the user for details, or it can be run with command line arguments. The four modes
are:

- 'e': This will encode all Unicode characters in the string files to their escape
  sequences in ASCII, e.g., "ä" becomes "\u00e4".
- 'd': This will decode all escape sequences in the string files back to their original
  Unicode characters.
- 'r': This will restore all string files from their backups, which are expected to be
  in the same directory as the original files, with the ".bak" suffix.
- 'c': This will clean (delete) all backup files in the given directory, which are expected to
  have the ".str.bak" suffix.

The command line arguments syntax is as follows:

    usage: unicode_encode_strings.py [-h] [--path [PATH]] [--mode {e,d,r,c}] [--verbose]

    optional arguments:
    -h, --help        show this help message and exit
    --path [PATH]     The path to the directory containing the files to process. If not provided, 
                      defaults to the 'res' directory in the script's location.
    --mode {e,d,r,c}  Mode: 'e' for encode, 'd' for decode, 'r' for restore, 'c' for clean. 
                      Default is 'e'.
    --verbose         Enable verbose output. Default is False (no verbose output).

Examples:

    Encode all .str files in the default 'res' directory next to this script:
        python unicode_encode_strings.py --mode e

    Decode all .str files in a custom absolute directory:
        python unicode_encode_strings.py --mode d --path /path/to/res

    Decode all .str files in a custom directory relative to this script:
        python unicode_encode_strings.py --mode d --path ./res

    Restore .str files in the default 'res' directory from possibly existing backups:
        python unicode_encode_strings.py --mode r

    Clean (delete) all .str.bak files in a custom directory:
        python unicode_encode_strings.py --mode c --path /path/to/res

    Enable verbose output while encoding .str files in the default 'res' directory:
        python unicode_encode_strings.py --mode e --verbose

"""
import argparse
import os
import re
import sys
import time

def EncodeStringFiles(path: str, createBackups: bool = True, verboseOutput: bool = True) -> None:
    """Escapes all unicode characters in string files in #path to their escape sequences in ASCII.

    Args:
        path (str): The path to the directory containing the files to encode.
        createBackups (bool): If True, creates a backup of each file before encoding. A file is
            only backed up once, I.e., existing backups will not be overwritten.
    """
    # Walk through the directory and its subdirectories.
    for root, _, files in os.walk(path):
        for filename in files:
            # Only process files with the .str extension.
            if not filename.endswith(".str"):
                continue

            fPath: str = os.path.join(root, filename)
            try:
                os.chmod(fPath, 0o600)  # Read/write for user only
            except Exception as e:
                print(f"Error setting permissions for {fPath}: {e}")

            content: str = ""
            with open(fPath, "r", encoding="utf-8") as f:
                content = f.read()

            if not content:
                print(f"Warning: The file {fPath} is empty or could not be read.")
                continue

            # Python's `string.encode("unicode_escape")` will yield hexadecimal escape sequences
            # (e.g. "\xXX"), but our C++ API expects unicode escape sequences (e.g. "\uXXXX"). I do 
            # not see a way how Python can do this out of the box, so we use this little function.
            def EscapeUnicode(item: str) -> str:
                return re.sub(r"([^\x00-\x7f])",
                              lambda m: "\\u{:04x}".format(ord(m.group(1))), item
                )
            
            # Escape all unicode characters in the content, e.g. "ä" becomes "\u00e4".
            newContent: str = EscapeUnicode(content)
            if newContent == content:
                continue

            bakPath: str = fPath + ".bak"
            if createBackups and not os.path.exists(bakPath):
                try:
                    with open(bakPath, "w", encoding="utf-8") as f:
                        f.write(content)
                    print(f"Created backup for {fPath} at {bakPath}.")
                except Exception as e:
                    print(f"Error creating backup for {fPath}: {e}")
            
            with open(fPath, "w", encoding="ascii") as f:
                f.write(newContent)

            if verboseOutput:
                print(f"Encoded {fPath} to ASCII.")
                print("-" * 120)
                print("\nOriginal content:\n")
                print(content)
                print("\nEscaped content:\n")
                print(newContent)
            else:
                print(f"Encoded {fPath} to ASCII.")

def DecodeStringFiles(path: str, verboseOutput: bool = True) -> None:
    """Unescapes all escape sequences in string files in #path back to their unicode characters.

    This is the reverse operation of `EncodeStringFiles`. It will decode escape sequences like
    "\u00e4" back to their original unicode characters like "ä".

    Args:
        path (str): The path to the directory containing the files to decode.
    """
    for root, _, files in os.walk(path):
        for filename in files:
            if filename.endswith(".str"):
                fPath: str = os.path.join(root, filename)
                try:
                    with open(fPath, "r", encoding="utf-8") as f:
                        content = f.read()
                    # Decode the escape sequences back to unicode characters.
                    decodedContent: str = content.encode("utf-8").decode("unicode_escape")

                    if decodedContent == content:
                        continue

                    with open(fPath, "w", encoding="utf-8") as f:
                        f.write(decodedContent)
       
                    if verboseOutput:
                        print(f"Decoded {fPath} from ASCII.")
                        print("-" * 120)
                        print("\nOriginal content:\n")
                        print(content)
                        print("\nDecoded content:\n")
                        print(decodedContent)
                    else:
                        print(f"Decoded {fPath} from ASCII.")

                except Exception as e:
                    print(f"Error decoding {fPath}: {e}")

def RestoreFilesFromBackups(path: str) -> None:
    """Restores all files from their backups in the given path.

    Args:
        path (str): The path to the directory containing the files to restore.
    """
    for root, _, files in os.walk(path):
        for filename in files:
            if filename.endswith(".str.bak"):
                fPath: str = os.path.join(root, filename)
                originalPath: str = fPath[:-4]  # Remove the ".bak" suffix
                try:
                    with open(fPath, "r", encoding="utf-8") as f:
                        content = f.read()
                    with open(originalPath, "w", encoding="utf-8") as f:
                        f.write(content)
                    os.remove(fPath)  # Remove the backup file after restoring
                    print(f"Restored {originalPath} from backup.")
                except Exception as e:
                    print(f"Error restoring {originalPath} from backup: {e}")

def DeleteBackupFiles(path: str) -> None:
    """Deletes all backup files in the given path.

    Args:
        path (str): The path to the directory containing the backup files to delete.
    """
    print(f"Warning: This will delete all string backup files (*.str.bak) in the directory '{path}'.")
    res: str = input("Do you want to continue (y/n): ").strip().lower()
    if res != 'y':
        print("Operation cancelled.")
        return
    
    for root, _, files in os.walk(path):
        for filename in files:
            if filename.endswith(".str.bak"):
                fPath: str = os.path.join(root, filename)
                try:
                    os.remove(fPath)
                    print(f"Deleted backup file: {fPath}")
                except Exception as e:
                    print(f"Error deleting {fPath}: {e}")

def main() -> None:
    """Runs the script.
    """
    # The three inputs for all actions.
    resPath: str = ""
    mode: str = ""
    verboseMode: bool = False

    # Handle logging
    class LogHandler:
        """Realizes a simple dual channel (stdin/stdout + file) log handler, because doing this 
        with the logging module of Python is unnecessarily complicated.
        """
        def __init__(self, stream: str):
            if stream == "out":
                self.stream = sys.stdout
                sys.stdout = self
            elif stream == "err":
                self.stream = sys.stderr
                sys.stderr = self
            else:
                raise ValueError("Stream must be 'out' or 'err'.")
            
            name: str = os.path.splitext(os.path.basename(__file__))[0]
            self.log: str = os.path.join(os.path.dirname(__file__), f"{name}.log")

            with open(self.log, "a", encoding="utf-8") as logFile:
                if stream == "out":
                    logFile.write("=" * 120 + "\n")
                logFile.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - "
                              "Opened new '{stream}' log handler.\n")
                if stream == "err":
                    logFile.write("=" * 120 + "\n")

        def write(self, message: str) -> None:
            """Write a message to the stream and log it.
            """
            if message.strip():
                self.stream.write(f"{message.strip()}\n")
                try:
                    with open(self.log, "a", encoding="utf-8") as logFile:
                        logFile.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {message.strip()}\n")
                except Exception as e:
                    pass

        def flush(self) -> None:
            """Flush the stream.
            """
            if hasattr(self.stream, 'flush'):
                self.stream.flush()
    
    # Attach our log handler to both stdout and stderr. 
    handlers: list[LogHandler] = [
        LogHandler("out"),
        LogHandler("err")
    ]

    # Attempt to parse the command line arguments, if there are any.
    if len(sys.argv) > 1:
        parser = argparse.ArgumentParser(
            description="Encode, decode, or restore string files in a directory.")
        parser.add_argument(
            "--path", type=str, nargs='?', default="",
            help=("The path to the directory containing the files to process. If not provided, "
                  "defaults to the 'res' directory in the script's location."))
        parser.add_argument(
            "--mode", type=str, choices=['e', 'd', 'r', 'c'],  default='e',
            help="Mode: 'e' for encode, 'd' for decode, 'r' for restore, 'c' for clean. Default is 'e'.")
        parser.add_argument(
            "--verbose", action='store_true', default=False, 
            help="Enable verbose output. Default is False (no verbose output).")
        args = parser.parse_args()

        resPath = args.path
        if resPath == "":
            resPath = os.path.join(os.path.dirname(__file__), "res")
            args.path = resPath

        mode = args.mode
        verboseMode = args.verbose
        print(f"Running with arguments: {args}")
        print("-" * 120)

    # Query the user instead.
    else:
        resPath = os.path.join(os.path.dirname(__file__), "res")
        if not os.path.isabs(resPath):
            resPath = os.path.abspath(resPath)
        if not os.path.exists(resPath):
            raise ValueError(f"The path '{resPath}' does not exist.")
        
        print(f"Using resource path: {resPath}")
        print("This script will encode or decode *.str files, restore therm from backups, or clean "
              "(delete) all backup files in a 'res' directory.")
        for i in range(3):
            mode = input(
                "Enter mode, 'e' for encode, 'd' for decode, 'r' for restore, 'c' for clean: ").strip().lower()
            if mode not in ("e", "d", "r", "c"):
                print("Invalid mode. Please enter 'e', 'd', 'r', or 'c'.")
            else:
                break
        if mode in ("e", "d"):
            for i in range(3):
                verbose: str = input(
                    "Verbose output? (y/n): ").strip().lower()
                if verbose not in ("y", "n"):
                    print("Invalid input. Please enter 'y' or 'n'.")
                else:
                    verboseMode = verbose == 'y'
                    break

        if mode not in ("e", "d", "r", "c"):
            raise ValueError("Invalid mode. Please enter 'e', 'd', 'r', or 'c'.")
    
    # Sort out all the path issues.
    if not isinstance(resPath, str):
        raise ValueError("The path must be a valid string.")
    if not os.path.isabs(resPath):
        cwd = os.getcwd()
        os.chdir(os.path.dirname(__file__))
        resPath = os.path.abspath(resPath)
        os.chdir(cwd)
        print(f"Using absolute path: {resPath}")
    if not os.path.exists(resPath):
        raise ValueError(f"The path '{resPath}' does not exist.")
    if not os.path.isdir(resPath):
        raise ValueError(f"The path '{resPath}' is not a directory.")
    if not resPath.endswith("res"):
        raise ValueError(
            f"The path '{resPath}' does not end with 'res'. This script is intended for "
             "encoding plugin resources, which should be in a directory ending with 'res'.")
        
    # Run the appropriate function based on the mode.
    if mode == 'e':
        EncodeStringFiles(resPath, createBackups=True, verboseOutput=verboseMode)
    elif mode == 'd':
        DecodeStringFiles(resPath, verboseOutput=verboseMode)
    elif mode == 'r':
        RestoreFilesFromBackups(resPath)
    elif mode == 'c':
        DeleteBackupFiles(resPath)

if __name__ == "__main__":
    main()