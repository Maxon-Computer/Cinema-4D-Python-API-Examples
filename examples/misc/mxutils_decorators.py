"""Demonstrates mxutils helpers for diagnosing Cinema 4D scene data.

Run this example in the Cinema 4D Script Manager. It prints a container, parameter,
and scene graph tree for the active document and its selected object.

Topics:
    * mxutils.TIMEIT
    * mxutils.SET_STATUS
    * mxutils.REPORT
"""
__author__ = "Ferdinand Hoppe"
__copyright__ = "Copyright (C) 2026 MAXON Computer GmbH"
__license__ = "Apache-2.0 License"
__version__ = "2027.0"

import math
import time

import c4d
import mxutils

doc: c4d.documents.BaseDocument # The active Cinema 4D document.

def main() -> None:
    """Runs the example for the active document.
    """
    @mxutils.REPORT()
    def foo() -> None:
        print("foo called")

    # mxutils.REPORT() will simply report if a function was called. When it is attached to a method,
    # it will also report the object instance on which the method was called. This can help with
    # debugging call chains without setting breakpoints to see call stacks (which often also contain
    # a lot of unrelated information).
    foo()

    @mxutils.SET_STATUS("Computing ...")
    def bar() -> None:
        time.sleep(2)
        print("bar done")

    # SET_STATUS helps with providing visual feedback to the user while your code is running. It will 
    # set the status bar text to the provided message while the decorated function is running.
    bar()

    # And last but not least, there is the TIMEIT decorator, which can be used to measure the 
    # execution time of a function.
    IS_DEBUG: bool = True

    # We define a recursive function and decorate it with the default timeit decorator.
    @mxutils.TIMEIT(IS_DEBUG)
    def factorial(n: int) -> int:
        return 1 if n == 0 else n * factorial(n - 1)

    # We call the function and see the time measurements. Because the function is recursive, we 
    # see the a report for each call in the recursion chain.
    factorial(3)
    # --------------------------------------------------------------------------------
    # TIMEIT: Ran 'factorial()' in 0.0 sec
    # --------------------------------------------------------------------------------
    # TIMEIT: Ran 'factorial()' in 6e-05 sec
    # --------------------------------------------------------------------------------
    # TIMEIT: Ran 'factorial()' in 0.00011 sec
    # --------------------------------------------------------------------------------
    # TIMEIT: Ran 'factorial()' in 0.00013 sec

    # We redefine the function but this time enable in-call protection. We also enable seeing 
    # the arguments and result of a function call.
    @mxutils.TIMEIT(IS_DEBUG, showArgs=True, showResult=True, inCallProtection=True)
    def factorial(n: int) -> int:
        return 1 if n == 0 else n * factorial(n - 1)

    # Now we call the function again. This time we only see the the timing for the outmost
    # call of the recursion chain.
    factorial(10)
    # --------------------------------------------------------------------------------
    # TIMEIT: Ran 'factorial((10,), {}) -> 3628800' in 1e-05 sec

    # And finally a more complex example where we decorate class methods and use full profiling.
    class Processor: 
        # The arguments we pass to the timeit decorator in this class.
        TIMEIT_KWARGS: dict[str, any] = {
            "enabled": IS_DEBUG, "showArgs": True, 
            "showResult": True, "inCallProtection": True, 
            "useProfiler": True
        }

        def __init__(self, n: int) -> None:
            self.recursive(n)
            self.iterative(n)

        @mxutils.TIMEIT(**TIMEIT_KWARGS)
        def recursive(self, n: int) -> int:
            return 1 if n == 0 else n * self.recursive(n - 1)

        @mxutils.TIMEIT(**TIMEIT_KWARGS)
        def iterative(self, n: int) -> int:
            x: int = n
            for i in range(int(n * 1000)):
                x += math.sqrt(x)
                x *= math.sin(i)
            return x

    p: Processor = Processor(50)

    # The output will look something like this. For the recursive call we mostly see the overhead
    # of the decorator. Profiling recursive functions in this manner that are not very expensive 
    # (execute in the microsecond range) is not very useful.

    # --------------------------------------------------------------------------------
    # TIMEIT: Ran 'recursive((<__main__.Processor object at 0x7fd18c0696a0>, 50), {}) -> 
    #     30414093201713378043612608166064768844377641568960512000000000000' with 302 function 
    #     calls (203 primitive calls) in 0.000 seconds
    #
    #     Ordered by: cumulative time
    #
    #     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    #       51/1    0.000    0.000    0.000    0.000 scriptmanager:476(recursive)
    #       50/1    0.000    0.000    0.000    0.000 scriptmanager:401(wrapper)
    #         50    0.000    0.000    0.000    0.000 /Applications/Maxon Cinema 4D 2024.4.0/...
    #         50    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
    #         50    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
    #         50    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
    #         1     0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
    # --------------------------------------------------------------------------------
    # TIMEIT: Ran 'iterative((<__main__.Processor object at 0x7fd18c0696a0>, 50), {}) -> -0.0' with 
    #     100002 function calls in 0.037 seconds
    #
    #    Ordered by: cumulative time
    #
    #     ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    #          1    0.025    0.025    0.037    0.037 scriptmanager:480(iterative)
    #      50000    0.007    0.000    0.007    0.000 {built-in method math.sin}
    #      50000    0.005    0.000    0.005    0.000 {built-in method math.sqrt}
    #          1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


    
import importlib
if __name__ == "__main__":
    c4d.ClearPythonConsole()
    main()