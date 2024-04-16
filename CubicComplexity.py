def cubic_search(arr, target):
    """
    Perform a cubic complexity search to find the target in the given array.
    
    Parameters:
        arr (list): The list of numbers to search through.
        target (int): The number to search for.
    
    Returns:
        int: The index of the target if found, otherwise -1.
    """
    n = len(arr)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if arr[i] + arr[j] + arr[k] == target:
                    return i, j, k  # Returning indices if found
    return -1  # Target not found

# Example usage:
arr = [1, 2, 3, 4, 5]
target = 10
result = cubic_search(arr, target)
if result != -1:
    print(f"Target {target} found at indices: {result}")
else:
    print(f"Target {target} not found in the array.")
