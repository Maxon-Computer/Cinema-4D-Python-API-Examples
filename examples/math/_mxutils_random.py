"""Demonstrates deterministic random values with mxutils.Random.

Run this example in the Cinema 4D Script Manager. Re-running it prints the same
values because the random generator is initialized with a fixed seed.

Topics:
    * mxutils.Random
    * Deterministic random values
    * Hash-based random values
"""
__author__ = "Ferdinand Hoppe"
__copyright__ = "Copyright (C) 2026 MAXON Computer GmbH"
__license__ = "Apache-2.0 License"
__version__ = "2027.0"

import c4d
import maxon
import mxutils

import random


def main() -> None:
    """Generates sequential and hash-based pseudo-random values.
    """
    # Create a random object. We could also use the global random object mxutils.g_random.
    rand: mxutils.Random = mxutils.Random(seed=42)

    # Deterministic random values

    # Create a list of 100 random points in the interval [0, 1000] using RandomVector. This is 
    # based on the random module from the Python standard library because the function name starts 
    # with 'Random', and will produce different values each time the code is run.
    points: list[c4d.Vector] = [rand.RandomVector(c4d.Vector(1000)) for _ in range(100)]

    # Associate each point with a random float value using RandomFloat. The tuples will be different 
    # each time the code is run unless we reset the seed before each call (which is a very expensive 
    # operation).
    pairs1: list[tuple[c4d.Vector, float]] = [(p, rand.RandomFloat()) for p in points]
    print(f"First ten random vector-float pairs: {pairs1[:10]} ...")

    # Generate point, random float pairs using a hash function, here hashing the point index. The tuples 
    # will be the same each time the code is run unless the point order/indices in #points change.
    pairs2: list[tuple[c4d.Vector, float]] = [(p, rand.HashNumberToNumber(i)) 
                                              for i, p in enumerate(points)]
    print(f"First ten hash index-based vector-float pairs: {pairs2[:10]} ...")

    # Will change, because the points have now a different order/index.
    print("Shuffling input.")
    random.shuffle(points)
    pairs3: list[tuple[c4d.Vector, float]] = [(p, rand.HashNumberToNumber(i))
                                              for i, p in enumerate(points)]
    print(f"First ten hash index-based vector-float pairs after shuffling: {pairs3[:10]} ...")

    # And finally generate the tuples using the point values itself. A given point will always be 
    # associated with the same random float value, no matter the count and order of points in #obj.
    pairs4: list[tuple[c4d.Vector, float]] = [(p, rand.HashVectorToNumber(p)) for p in points]
    random.shuffle(points)
    pairs5: list[tuple[c4d.Vector, float]] = [(p, rand.HashVectorToNumber(p)) for p in points]

    # The outputs would still be in a different order because we shuffled the data. But each point 
    # will always be associated with the same random float value, no matter the count and order of 
    # points in #points. So, when we sort our results by value, the outputs will be identical.
    pairs4.sort(key=lambda pair: pair[1])
    pairs5.sort(key=lambda pair: pair[1])
    print(f"First ten hash vector-based vector-float pairs after shuffling: {pairs5[:10]} ...")
    print(f"Are the hash vector-based pairs identical after shuffling? {pairs4 == pairs5}")

    ## Specialized hash functions (most of these also have a Random* equivalent)

    # Hash 42 to a pseudo-random RGBA color in the intervals hue(0, 90), saturation(0.5, 1.0), 
    # value(0.5, 1.0), and alpha(0.5, 1.0) using the global random instance and the c4d.Vector4d type.
    rgba: c4d.Vector4d = rand.HashNumberToColor(
        value=42, hueInterval=(0, 90), saturationInterval=(0.5, 1.0), valueInterval=(0.5, 1.0), 
        alphaInterval=(0.5, 1.0), dtype=c4d.Vector4d)
    print(f"Hash number to color: 42 -> {rgba}")

    deg45: float = c4d.utils.DegToRad(45.0) # 45° in radians

    # Hash 42 into a matrix whose offset lies in the interval [[0, 0, 0], [100, 100, 100]], 
    # but has no rotation and a scale of 1.
    m: c4d.Matrix = rand.HashNumberToMatrix(42, positionInterval=(c4d.Vector(0), c4d.Vector(100)))
    print(f"Hash number to matrix: 42 -> {m}")

    # Hash 42 into a matrix with a rotation in the interval [[-45, -45, -45], [45, 45, 45]] degrees.
    m: c4d.Matrix = rand.HashNumberToMatrix(42, rotationInterval=(c4d.Vector(-deg45), c4d.Vector(deg45)))
    print(f"Hash number to matrix with rotation: 42 -> {m}")

    # Hash 42 into a transform that has an offset in the interval [0, 0, 0], [0, 0, 100], 
    # a rotation in the interval [[-45, 0, 0], [45, 0, 0]] degrees, and a scale in the interval 
    # [1, 1, 0.5], [1 1, 2.0].
    m: c4d.Matrix = rand.HashNumberToMatrix(
        value=42, 
        positionInterval=(c4d.Vector(0), c4d.Vector(0, 0, 100)),
        rotationInterval=(c4d.Vector(-deg45, 0, 0), c4d.Vector(deg45, 0, 0)),
        scaleInterval=(c4d.Vector(1, 1, 0.5), c4d.Vector(1, 1, 2.0))
    )
    print(f"Hash number to matrix with position, rotation, and scale: 42 -> {m}")

    # There are many more specialized hash functions available, check the docs for details.


if __name__ == "__main__":
    main()