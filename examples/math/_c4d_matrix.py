"""Demonstrates working with matrices.

Topics:
    - Instantiation and access of matrices
    - Arithmetic operations with matrices
    - Inversion, normalization, tensor, and scale
    - Arithmetic operations between matrices and vectors
    - Constructing matrices from vectors
    - Randomization of matrices

Related:
    math/_c4d_vector.py
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

    # Instantiate the identity matrix.
    identity: c4d.Matrix = c4d.Matrix()
    print(f"{identity = }")

    # Matrices are often also constructed with c4d.utils helper functions.

    # A matrix representing a translation by 100 units along the X axis.
    move: c4d.Matrix = c4d.utils.MatrixMove(c4d.Vector(100, 0, 0))
    print(f"\n{move = }")

    # A matrix representing a rotation by 90 degrees around the Z axis.
    rotate: c4d.Matrix = c4d.utils.MatrixRotY(c4d.utils.DegToRad(90))
    print(f"{rotate = }")

    # A matrix representing a scaling by a factor of 2 along all axes.
    scale: c4d.Matrix = c4d.utils.MatrixScale(c4d.Vector(2, 2, 2))
    print(f"{scale = }")

    # Matrices can also be manually constructed.

    # A matrix that only sets the offset component.
    offset: c4d.Matrix = c4d.Matrix(off=c4d.Vector(1, 2, 3))
    print(f"\n{offset = }")

    # A matrix that sets the three frame components (the basis vectors) v1, v2, and v3. v1 is the
    # x-axis, v2 is the y-axis, and v3 is the z-axis. In this case we manually define the identity 
    # frame.
    frame: c4d.Matrix = c4d.Matrix(
        v1=c4d.Vector(1, 0, 0),
        v2=c4d.Vector(0, 1, 0),
        v3=c4d.Vector(0, 0, 1)
    )
    print(f"{frame = }")

    # Or everything together: translation, rotation, and scaling.
    combined: c4d.Matrix = c4d.Matrix(
        v1=c4d.Vector(2, 0, 0),
        v2=c4d.Vector(0, 2, 0),
        v3=c4d.Vector(0, 0, 2),
        off=c4d.Vector(1, 2, 3)
    )

    # Accessing the individual components of the combined matrix.
    print(f"\n{combined = }")
    print(f"{combined.off = }")
    print(f"{combined.v1 = }")
    print(f"{combined.v2 = }")
    print(f"{combined.v3 = }")

    print(f"\n--- Arithmetic Operations between two Matrices -----------------------------------\n")

    a: c4d.Matrix = c4d.Matrix(c4d.utils.MatrixMove(c4d.Vector(1, 2, 3)))
    b: c4d.Matrix = c4d.Matrix(c4d.utils.MatrixRotY(c4d.utils.DegToRad(30)))

    print(f"{a = }")
    print(f"{b = }")

    # Matrix addition and subtraction.
    print(f"\n{a + b = }")
    print(f"{b + a = }")
    print(f"{a - b = }")
    print(f"{b - a = }")

    # Matrix multiplication (this is not commutative, i.e., a * b != b * a in general).
    print(f"{a * b = }")
    print(f"{b * a = }") # not the same as a * b

    # Practical example: combining a translation and a rotation.
    transform: c4d.Matrix = (c4d.utils.MatrixMove(c4d.Vector(10, 0, 0)) * 
                             c4d.utils.MatrixRotY(c4d.utils.DegToRad(90)))

    # Divide a matrix by a scalar (not commonly used, but possible). Only the form matrix / scalar is 
    # supported, not scalar / matrix.
    print(f"{a / 2 = }")

    print(f"\n--- Inversion, Normalization, Tensor, and Scale ----------------------------------\n")

    # A matrix can be inverted with the ~ operator.
    print(f"{~a = }")

    # A matrix can be normalized to remove any scaling.
    print(f"{a.GetNormalized() = }")

    # The tensor of a matrix can be accessed via the .GetTensorMatrix() method.
    print(f"{a.GetTensorMatrix() = }")
    
    # The scale of a matrix can be accessed via the .GetScale() method.
    print(f"{scale.GetScale() = }")

    print(f"\n--- Arithmetic Operations between Matrices and Vectors ---------------------------\n")

    # Multiplying a matrix by a vector applies the transformation to the vector. Both sides are
    # supported in both orders: matrix * vector and vector * matrix.
    v: c4d.Vector = c4d.Vector(0, 1, 0)

    print(f"{transform * v = }")
    print(f"{v * transform = }")

    print(f"\n--- Constructing Matrices --------------------------------------------------------\n")

    # A common task is to construct a matrix from either one or two vectors. Shown is here the case
    # of constructing a matrix from a single vector (and an up vector), where the input vector 
    # defines the z-axis of the resulting matrix. This can for example be useful when you have a
    # surface or spline normal and what to construct a frame/transform on it.

    p: c4d.Vector = c4d.Vector(1, 2, 3)      # Example input vector representing the z-axis
    up: c4d.Vector = c4d.Vector(0, 1, 0)     # Example up vector.
    epsilon: float = 1e-6                    

    # Make sure our up-vector is not parallel or anti-parallel to the input vector. When this is the
    # case, we slightly perturb the up vector to avoid numerical issues.
    up = up if 1. - abs(p * up) > epsilon else c4d.Vector(epsilon, 1, 0)

    z: c4d.Vector = p.GetNormalized()            # Normalize the input vector representing the z-axis
    x: c4d.Vector = up.Cross(z).GetNormalized()  # Compute the x-axis as the cross product of up and z
    y: c4d.Vector = z.Cross(x).GetNormalized()   # Compute the y-axis as the cross product of z and x

    # Construct the matrix from the orthonormal basis vectors x, y, and z.
    mg: c4d.Matrix = c4d.Matrix(v1=x, v2=y, v3=z)
    print(f"{mg = }")

    print(f"\n--- Randomization ----------------------------------------------------------------\n")

    # mxutils.Random offers a wide range of matrix randomization functions, see _mxutils_random.py
    # example for more details.
    print(f"{mxutils.g_random.HashNumberToMatrix(42) = }")
    print(f"{mxutils.g_random.HashVectorToMatrix(c4d.Vector(1, 2, 3)) = }")
    print(f"{mxutils.g_random.RandomMatrix() = }")


if __name__ == "__main__":
    c4d.ClearPythonConsole()
    main()
