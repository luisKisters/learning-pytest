from bubble_sort import bubbleSort
import random


def test_bubbleSort_random_arr():
    arr = [random.randint(0, 100) for _ in range(10)]
    bubbleSort(arr)
    assert bubbleSort(arr) == sorted(arr)


def test_bubbleSort_single_item():
    assert bubbleSort([1]) == [1]


def test_bubbleSort_defined_arr():
    assert bubbleSort([3, 2, 1]) == [1, 2, 3]
