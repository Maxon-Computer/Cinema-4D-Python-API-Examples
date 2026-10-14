"""Demonstrates type and iterable validation with mxutils.

Run this example in the Cinema 4D Script Manager. Type checks provide meaningful error 
messages when a value is not of the expected type. For example:

    TypeError: Expected iterable 'data' to be composed of type <class 'str'>. Found item of 
    type: <class 'int'>

Note:
    For type checking to fully work, i.e., provide meaningful symbol hints on failure, you must
    work with a saved file. The type check will also work on unsaved files, but the symbol discovery
    will only work properly on saved files.

Topics:
    * mxutils.CheckType
    * mxutils.CheckIterable
"""
__author__ = "Ferdinand Hoppe"
__copyright__ = "Copyright (C) 2026 MAXON Computer GmbH"
__license__ = "Apache-2.0 License"
__version__ = "2027.0"

import c4d
import mxutils
import math

MY_INT: int = 42

def main() -> None:
    """Demonstrates type and iterable validation.
    """

    # --- Type Checks

    # Type checks are important to ensure that larger code bases remain robust and maintainable. 
    # While they might seem tedious for small scripts, they are invaluable for larger projects and 
    # when working in teams.
   
    # Asserts that `MY_INT` is of type `int` or `float`.
    mxutils.CheckType(MY_INT, (int, float))

    # Asserts that `MY_INT` is of type `int` or `float` and assigns its int value to `my_int`.
    myInt: int = int(mxutils.CheckType(MY_INT, (int, float)))

    # Asserts that `math.pi` is of type `int`. This will raise a TypeError because math.pi is a float.
    try:
        mxutils.CheckType(math.pi, int)
    except TypeError as e:
        print(e)

    # Type checking is important when checking function arguments but also when instantiating objects.
    # Cinema will return `None` when object allocation fails (for example due to insufficient memory). 
    # Early checking makes sure that we later do not run into cryptic errors when trying to use the 
    # object. Here we can also make use of the shorthand without a type, where CheckType will only 
    # ensure that the value is not None.
    obj: c4d.BaseObject = mxutils.CheckType(c4d.BaseObject(c4d.Ocube))

    # --- Container and Iterable Checks

    # Checks if `data` is composed of strings only; this will fail as there is an `int` in it.
    data: list[str|int] = ["1", "2", "3", 4, "5"]
    try:
        mxutils.CheckIterable(data, str)
    except TypeError as e:
        print(e)

    # The common use case is checking type composition assumptions of function arguments passed 
    # by unsafe sources, in order to avoid carrying out expensive computations which fail in a 
    # very late stage due to encountering a malformed item in the input data.
    class Foo:
        def __init__(self, nodes: list[c4d.BaseObject | c4d.BaseTag]) -> None:
            # Assure that _nodes will be a list of tags and objects.
            self._nodes = mxutils.CheckIterable(nodes, (c4d.BaseObject, c4d.BaseTag), list)

    try:
        foo = Foo([c4d.BaseObject(c4d.Ocube), c4d.BaseTag(c4d.Tphong), 42])
    except TypeError as e:
        print(e)

    # Tested can also be the length of the iterable.

    # Assures that `data` has at least the length of one. No specific type checks are performed 
    # in this case, but `data` is still being tested for being an iterable. This is a very low
    # cost call, no matter how large data is, as the first argument `tElement` has is `None` and
    # `data` is therefore never traversed as elements of any type are accepted.
    mxutils.CheckIterable(data, minCount=1)

    # Assures that `data` is not longer than five elements.
    mxutils.CheckIterable(data, maxCount=5)

    # Assures that the length of `data` lies in the interval [1, 5].
    mxutils.CheckIterable(data, minCount=1, maxCount=5)

    # The function will always test if ``item`` is an iterable, even when both type tests are
    # set to None. So, this will raise an error as `int` does not implement `__iter__`.
    try:
        mxutils.CheckIterable(1, minCount=1, maxCount=5)
    except TypeError as e:
        print(e)

    # but this will not, as `c4d.BaseContainer` does implement `__iter__`:
    data: c4d.BaseContainer = c4d.BaseContainer()
    mxutils.CheckIterable(data)

    # All forms of iterable are supported, but only `c4d.BaseContainer` and `dict` are handled
    # manually to type test values in key, value pairs instead of testing the type of the pair.
    bc: c4d.BaseContainer = c4d.BaseContainer()
    bc[0] = "Hello world"
    bc[1] = 42
    # Will test data for being of type BaseContainer, holding only values of type str or int. 
    # One thing to watch out for is that BaseContainer stores bool as int. So, even when you store
    # a bool, you have to check for int.
    mxutils.CheckIterable(bc, (str, int), c4d.BaseContainer)

    # The same thing for dict. Key type testing is not supported for dicts, tested are only the values.
    data: dict = {1: "Hello World", "my_key": True}
    mxutils.CheckIterable(data, (str, bool), dict)


if __name__ == "__main__":
    main()