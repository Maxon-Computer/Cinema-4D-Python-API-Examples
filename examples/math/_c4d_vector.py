"""Demonstrates working with vectors.

Vectors are one of the fundamental data types in Cinema 4D. There exist different vector types in 
the Cinema and Maxon API of Cinema 4D. This manual covers only the more commonly used Cinema API 
type c4d.Vector.

Topics:
    - Instantiation and access of vectors
    - Arithmetic operations with vectors
    - Normalization and magnitude
    - Dot and cross products
    - Helper functions for vectors
    - Randomization of vectors

Related:
    math/_c4d_matrix.py
    math/_mxutils_random.py
"""
__author__ = "Ferdinand Hoppe"
__copyright__ = "Copyright (C) 2026 MAXON Computer GmbH"
__license__ = "Apache-2.0 License"
__version__ = "2027.0.0"
__date__ = "07/09/2026"

import c4d
import mxutils


doc: c4d.documents.BaseDocument # The active Cinema 4D document.
op: c4d.BaseObject | None # The currently selected object in the Cinema 4D document, can be None.


def main() -> None:
    """Runs the example.
    """
    print(f"\n--- Instantiation and Access -----------------------------------------------------\n")

    # Create four vectors used in the example. These are all 64bit floating point vectors.
    null: c4d.Vector = c4d.Vector()         # Same as c4d.Vector(0, 0, 0)
    a: c4d.Vector = c4d.Vector(1)           # Same as c4d.Vector(1, 1, 1)
    b: c4d.Vector = c4d.Vector(1, 2, 3)
    c: c4d.Vector = c4d.Vector(4, 5, 6)

    print(f"{null = }")
    print(f"{a = }")
    print(f"{b = }")
    print(f"{c = }")

    # Access the components of the vectors.
    print(f"\n{null.x = }, {null.y = }, {null.z = }")
    print(f"{a.x = }, {a.y = }, {a.z = }")
    print(f"{b.x = }, {b.y = }, {b.z = }")
    print(f"{c.x = }, {c.y = }, {c.z = }")

    # Or with the bracket notation.
    print(f"\n{null[0] = }, {null[1] = }, {null[2] = }")
    print(f"{a[0] = }, {a[1] = }, {a[2] = }")
    print(f"{b[0] = }, {b[1] = }, {b[2] = }")
    print(f"{c[0] = }, {c[1] = }, {c[2] = }")

    print(f"\n--- Arithmetic Operations --------------------------------------------------------\n")

    # Adding and subtracting vectors.
    print(f"{a + b = }")
    print(f"{a - b = }")

    # Multiplication by a scalar ('a number') is supported on both sides.
    print(f"\n{a * 2 = }")
    print(f"{2 * a = }")

    # Componentwise multiplication between two vectors is done with the ^ operator.
    print(f"{b ^ c = }")

    # And division by scalars is also supported (but only as left-side division). Two vectors cannot
    # be divided componentwise.
    print(f"\n{a / 2 = }")

    # You can also take the absolute and negative of a vector.
    print(f"\n{abs(b) = }")
    print(f"{-b = }")

    # For multiplications between vectors and matrices, see math/_c4d_matrix.py.

    print(f"\n--- Comparisons ------------------------------------------------------------------\n")

    # The only comparisons supported between vectors are equality and inequality. c4d.Vector does 
    # not support ordering comparisons.
    print(f"{a == b = }")
    print(f"{a != b = }")

    print(f"\n--- Normalization and Magnitude --------------------------------------------------\n")

    # You can normalize a vector using GetNormalized() or the ~ operator.
    print(f"{b.GetNormalized() = }")
    print(f"{~b = }")

    # There exist GetLength() and GetLengthSquared() for computing the magnitude and squared 
    # magnitude of a vector. GetLength() is relatively expensive, so avoid it when possible.
    print(f"\n{b.GetLength() = }")
    print(f"{b.GetLengthSquared() = }")

    print(f"\n--- Dot and Cross Products -------------------------------------------------------\n")

    # The dot product between two vectors can be computed using Dot() or the * operator.
    print(f"{b.Dot(c) = }")
    print(f"{b * c = }")

    # Cross product between two vectors can be computed using Cross() or the % operator.
    print(f"\n{b.Cross(c) = }")
    print(f"{b % c = }")

    print(f"\n--- Helper Functions -------------------------------------------------------------\n")

    # With c4d.utils.MixVec you can linearly interpolate between two vectors. Cinema 4D has no
    # builtin Slerp for vectors at the moment.
    print(f"{c4d.utils.MixVec(b, c, 0.5) = }")

    # With c4d.utils.GetAngle you can compute the angle between two vectors. The same can also be
    # done with Vector.GetAngle(). Both return a value in radians. In c4d.utils are helper functions
    # to convert between radians and degrees.
    print(f"\n{c4d.utils.GetAngle(b, c) = }")
    print(f"{b.GetAngle(c) = }")
    print(f"{c4d.utils.RadToDeg(c4d.utils.GetAngle(b, c)) = }")

    # Cinema has no projection function, only c4d.utils.PointLineDistance which does only half of 
    # the work and is therefore rather pointless. It the easiest to just do it manually.
    projectBc: c4d.Vector = c * (b.Dot(c) / c.GetLengthSquared()) # projection of b onto c
    print(f"\n{projectBc = }")

    print(f"\n--- Randomization ----------------------------------------------------------------\n")

    # mxutils.Random offers a wide range of vector randomization functions, see _mxutils_random.py
    # example for more details.
    print(f"{mxutils.g_random.HashNumberToVector(42) = }")
    print(f"{mxutils.g_random.HashVectorToVector(c) = }")
    print(f"{mxutils.g_random.RandomVector() = }")


if __name__ == "__main__":
    c4d.ClearPythonConsole()
    main()
