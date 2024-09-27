arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

arr2 = [0]*len(arr)
offset = 3

# Time: O(n)
# Space: O(2n)
def shiftArray(arr, offset)
    arr2 = [0]*len(arr)
    for i, num in enumerate(arr):
        pos = (i+offset) % len(arr)
        arr2[pos] = num
    return arr2

print(arr)
print(arr2)


def min_entropy(bit_string):
    probabilities = {}
    for bit in bit_string:
        if bit in probabilities:
            probabilities[bit] += 1
        else:
            probabilities[bit] = 1
    
    # Normalize counts to probabilities
    length = len(bit_string)
    max_prob = max(probabilities[bit] / length for bit in probabilities)

    # Calculate min-entropy
    import math
    return -math.log2(max_prob)

# Example usage:
bit_string = "11001100"
print(min_entropy(bit_string))  # Outputs the min-entropy
