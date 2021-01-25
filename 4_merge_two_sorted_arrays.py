# Function to in-place merge two sorted lists `X` and `Y`
# invariant: `X` and `Y` are sorted at any point
def merge(X, Y):

    m = len(X)
    n = len(Y)

    # Consider each element `X[i]` of list `X[]` and ignore the element if it is
    # already in the correct order; otherwise, swap it with the next smaller
    # element, which happens to be the first element of `Y[]`.
    for i in range(m):

        # compare the current element of `X[]` with the first element of `Y[]`
        if X[i] > Y[0]:

            # swap `X[i] with `Y[0]`
            temp = X[i]
            X[i] = Y[0]
            Y[0] = temp

            first = Y[0]

            # move `Y[0]` to its correct position to maintain the sorted
            # order of `Y[]`. Note: `Y[1…n-1]` is already sorted
            k = 1
            while k < n and Y[k] < first:
                Y[k - 1] = Y[k]
                k = k + 1

            Y[k - 1] = first


# ************************************************************************************************

# Merging two sorted arrays with O(1) extra space

# Function to find next gap.


def nextGap(gap):

    if gap <= 1:
        return 0
    return (gap // 2) + (gap % 2)


def merge(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    gap = n + m
    gap = nextGap(gap)
    while gap > 0:

        # comparing elements in
        # the first array.
        i = 0
        while i + gap < n:
            if arr1[i] > arr1[i + gap]:
                arr1[i], arr1[i + gap] = arr1[i + gap], arr1[i]

            i += 1

        # comparing elements in both arrays.
        j = gap - n if gap > n else 0
        while i < n and j < m:
            if arr1[i] > arr2[j]:
                arr1[i], arr2[j] = arr2[j], arr1[i]

            i += 1
            j += 1

        if j < m:

            # comparing elements in the
            # second array.
            j = 0
            while j + gap < m:
                if arr2[j] > arr2[j + gap]:
                    arr2[j], arr2[j + gap] = arr2[j + gap], arr2[j]

                j += 1

        gap = nextGap(gap)


if __name__ == "__main__":

    X = [1, 4, 7, 8, 10]
    Y = [2, 3, 9]

    merge(X, Y)

    print("X:", X)
    print("Y:", Y)