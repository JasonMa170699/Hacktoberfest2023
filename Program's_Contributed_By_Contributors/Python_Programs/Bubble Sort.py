# Python3 program for Bubble Sort Algorithm Implementation
def bubble_sort(arr):
    # Get the length of the array
    n = len(arr)

    # Traverse through all elements in the array
    for i in range(n):
        # The inner loop iterates through the unsorted part of the array
        for j in range(0, n - i - 1):
            # Swap the elements if the current element is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Driver code
if __name__ == "__main":
    # Example to test the above code
    arr = [2, 1, 10, 23]

    # Call the bubble_sort function to sort the array
    bubble_sort(arr)

    print("Sorted array is:")
    for element in arr:
        print(element)
