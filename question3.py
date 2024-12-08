def find_min_of_max_subarrays(k, n, array):
    subarrays = [array[i:i + k] for i in range(n - k + 1)]
    return min(map(max, subarrays))

def main():
    k = int(input("Enter the value of k (length of subarray): "))
    n = int(input("Enter the total number of elements in the array: "))
    array = [int(input(f"Enter element {i+1}: ")) for i in range(n)]
    
    result = find_min_of_max_subarrays(k, n, array)
    
    print(f"The minimum of the maximums of all subarrays of length {k} is: {result}")

if __name__ == "__main__":
    main()
