# Learning Pytest

![pytest](https://github.com/luisKisters/learning-pytest/actions/workflows/pytest.yaml/badge.svg)

This repository contains my personal notes and code as I learn how to use the [pytest](https://pytest.org) testing framework. I am following [this tutorial](https://youtu.be/YbpKMIUjvK8) to learn the basics of pytest.

As part of my learning process, I have implemented a bubble sort algorithm in Python using [this tutorial](https://youtu.be/g_xesqdQqvA) as a guide. I am using pytest to write and run tests for my bubble sort implementation to ensure that it works correctly.  

## CI/CD Setup

This repository uses GitHub Actions to run tests on every push and pull request using a self-hosted runner. The test workflow is defined in the `pytest.yaml` file in the `.github/workflows` directory, and runs the `pytest` test runner on the Python code in this repository.

To configure the self-hosted runner, a runner machine was set up and registered with GitHub using the instructions in the [GitHub Actions documentation](https://docs.github.com/en/actions/hosting-your-own-runners). The runner is then available to run the test workflow defined in this repository.

## Description

The `bubble_sort.py` file contains a Python implementation of the bubble sort algorithm. The `bubbleSort()` function takes an unsorted list of numbers and returns the list sorted in ascending order. The implementation uses a while loop to continue sorting until the list is fully sorted. Within the loop, a for loop is used to compare adjacent elements and swap them if they are in the wrong order.

## Output

When the `bubbleSort()` function is called with an unsorted list, it returns the list sorted in ascending order. For example:

```python
bubbleSort([4, 2, 8, 1, 3, 7, 5, 6])
[1, 2, 3, 4, 5, 6, 7, 8]
```

This implementation of the bubble sort algorithm has a time complexity of O(n^2), which makes it inefficient for large datasets. However, it is a simple algorithm to understand and can be useful for small datasets or for educational purposes.
