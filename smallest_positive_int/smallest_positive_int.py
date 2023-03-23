"""
Write a function that given an array A of N integers, returns the smallest positive integer (greater than 0)
that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
Given A = [1, 2, 3], the function should return 4.
Given A = [−1, −3], the function should return 1.
"""

def solution(arr):
    arr = sorted(arr)

    smallest = 1

    for i in range(len(arr)):
        if arr[i] == smallest:
            smallest += 1

    return smallest


def main():
    print(solution([1, 3, 6, 4, 1, 2])) 
    print(solution([1, 2, 3]))
    print(solution([-1, -3]))


if __name__ == "__main__":
    main()