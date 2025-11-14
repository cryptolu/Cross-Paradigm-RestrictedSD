from sage.all import (
    ZZ, RR, QQ, binomial, log, pi, e, gamma,
    vector, math, exp, matrix,
)
from sage.matrix.matrix_integer_dense import Matrix_integer_dense
from fpylll import FPLLL, LLL, BKZ, GSO, Enumeration, IntegerMatrix, EvaluatorStrategy

from tqdm import tqdm  # sage -pip install tqdm


def LOG2(x):
    return RR(log(x, 2))


def matrix_to_fpylll(mat):
    if not isinstance(mat, IntegerMatrix):
        mat = IntegerMatrix.from_matrix(mat)
    return mat


def matrix_to_sage(mat):
    if not isinstance(mat, Matrix_integer_dense):
        buf = [[0] * mat.ncols for _ in range(mat.nrows)]
        mat = matrix(ZZ, mat.to_matrix(buf))
    return mat


def ball_vol(n, r=1):
    """Volume of an `n`-dimensional ball of radius `r`."""
    return r**n * RR(pi**(QQ(n)/2) / gamma(QQ(n)/2 + 1))


def enum_cost(A, r, pruning=True):
    """Cost of enumeration assuming GH, using concrete (reduced) basis.

    `pruning`=True enables linear pruning. Success probability is 1/n, workload
    is multiplied by n.
    """
    A = matrix_to_fpylll(A)
    assert A.ncols == A.nrows
    n = A.ncols
    M = GSO.Mat(A)
    M.update_gso()
    
    vol = 1
    work = 0 
    dim = 0
    for y in reversed(range(n)):
        dim += 1
        vol *= M.get_r(y, y)**0.5
        if pruning:
            rk = r * (dim/n)**0.5  # spherical bound
        else:
            rk = r
        num = ball_vol(dim, rk) / vol
        work += RR(num)
    if pruning:
        return work * n
    else:
        return work


def enum_cost_delta(n, vol, r, delta0, pruning=True):
    """Cost of enumeration assuming GH+GSA with delta0 (root Hermite factor)

    `pruning`=True enables linear pruning. Success probability is 1/n, workload
    is multiplied by n.
    """
    work = 0 
    det1n = abs(vol)**(1/n)
    delta = delta0**(-n/(n-1))
    for dim in range(1, n+1):
        vol = det1n**dim * delta**(dim*(n-dim))
        if pruning:
            rk = r * (dim/n)**0.5  # spherical bound
        else:
            rk = r
        num = ball_vol(dim, rk) / vol
        work += RR(num)
    if pruning:
        return work * n
    else:
        return work
