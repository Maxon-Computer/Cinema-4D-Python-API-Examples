"""Demonstrates instantiation and usage of various Maxon data types.

Warning:

    Maxon API data types only rarely are of relevance for developers. They only can occur in specific 
    scenarios when interacting with the Maxon API in Python. Data is usually converted to native Python 
    types and users often also only interact with the Cinema API.

    You do not have to read this example unless you are specifically encountering Maxon API data types 
    in Python.

Topics:
    - maxon.BaseArray
    - maxon.DataDictionary
    - maxon.Tuple
"""
__author__ = "Ferdinand Hoppe"
__copyright__ = "Copyright (C) 2026 MAXON Computer GmbH"
__license__ = "Apache-2.0 License"
__version__ = "2027.0.0"

import maxon


def main() -> None:
    """Runs the example.
    """
    # BaseArray is the fundamental array type in the Maxon API. This can sometimes be encountered 
    # when dealing asset metadata or more exotic functions in the Python Maxon API. Just like its
    # C++ counterpart, BaseArray is statically typed, i.e., unlike Python lists, all elements must 
    # be of the same type.

    # Create an array of integers, based on the Python list [1, 2, 3, 4].
    data: maxon.BaseArray[int] = maxon.BaseArray(maxon.Int, [1, 2, 3, 4])
    print(f"Initial data: {data}")

    # BaseArrays can be iterated over and bracket operator accessed just like Python lists.
    for item in data:
        print(f"Iterated item: {item}")

    print(f"Before modification: {data[1]}")
    data[1] = 10
    print(f"After modification: {data[1]}")

    # Writing a string would raise a type error, because this BaseArray is typed to hold integers only.
    try:
        data[1] = "hello world"
    except TypeError as e:
        print(f"Caught expected TypeError when using __setitem__: {e}")

    # BaseArray has just like Python lists an Append method. Which is uppercase though and just like
    # the bracket operator, would raise an error if the appended element is of the wrong type.
    data.Append(20)
    print(f"After appending: {data}")
    try:
        data.Append("hello world")
    except TypeError as e:
        print(f"Caught expected TypeError when appending: {e}")

    # BaseArrays also support insertion and resizing.
    data.Insert(1, 15)
    print(f"After insertion: {[n for n in data]}")

    data.Resize(6)
    data[5] = 25
    print(f"After resizing: {[n for n in data]}")


if __name__ == "__main__":
    main()