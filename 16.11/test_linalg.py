from linalg import LinearAlgebra
import numpy as np
from typing import List, Callable
import time


def test_simple_cumsum():
    vec = [1.0, 2.0, 3.0, 4.0]
    print(f"Check for vector: {vec}")
    cumsum = np.cumsum(vec)
    print(f"cumsum(vec) must be: {cumsum}")
    result = LinearAlgebra.cumSum(vec)
    assert len(result) == len(cumsum)
    for i in range(len(result)):
        assert result[i] == cumsum[i], f"Expected for i={i}: {cumsum[i]}, but got for i={i}: {result[i]}"


def check_timings(f, *args):
    _ = f(*args)
    start_time = time.time()
    _ = f(*args)
    end_time = time.time()
    return round(end_time - start_time, 5)


def compare(size: int) -> None:
    vec = list(np.random.random(size))
    print("-------------------")
    print(
        "numpy cumsum, size={0}: {1} seconds".format(
            size, check_timings(np.cumsum, vec)
        )
    )

    print(
        "binding cumsum, size={0}: {1} seconds".format(
            size, check_timings(LinearAlgebra.cumSum, vec)
        )
    )


if __name__ == "__main__":
    test_simple_cumsum()
    print("-------------------")
    print("Simple test passed!") 
    for size in [10_000, 100_000, 200_000, 1_000_000, 10_000_000]:
        compare(size)
    print("-------------------")
    print("Timings passed!")
