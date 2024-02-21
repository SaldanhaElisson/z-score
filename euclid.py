import math
from typing import List

pointA: List[int] = [2, 2, 4, 5]
pointB: List[int] = [2, 2, 2, 2]

def calEuclidiana(pointA: List[float], pointB: List[float]) -> None | float:
    if len(pointA) != len(pointB):
        return
    resultSums: int = 0

    for i in range(len(pointA)):
        resultSums += pow(pointA[i] - pointB[i], 2)

    return math.sqrt(resultSums)

def calChebyshev(pointA: List[float], pointB: List[float]) -> None | float:
    if len(pointA) != len(pointB):
        return
    resultSums: float = 0

    for i in range(len(pointA)):
        resultLes: float = abs(pointA[i] - pointB[i])
        if (resultLes > resultSums):
            resultSums = resultLes

    return resultSums

print(f"Euclidiana A: {pointA} & B:{pointB}: {calEuclidiana(pointA, pointB):.2f}")

print(f"Chebysgev A: {pointA} & B:{pointB}: {calChebyshev(pointA, pointB):.2f}")
