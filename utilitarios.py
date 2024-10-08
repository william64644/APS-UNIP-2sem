import math
from collections import Counter

arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

arr2 = [0]*len(arr)
offset = 3

# Time: O(n)
# Space: O(2n)
def shiftArray(arr, offset):
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
bit_string = "010010"
print(min_entropy(bit_string))  # Outputs the min-entropy




def calculate_entropy(s):
    # Calculate frequency of each character
    frequency = Counter(s)
    total_chars = len(s)
    
    # Calculate Shannon entropy
    shannon_entropy = -sum((count / total_chars) * math.log2(count / total_chars) for count in frequency.values())
    
    # Calculate pattern complexity
    runs = 0
    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            runs += 1
    runs += 1  # Count the first run
    
    # Incorporate pattern complexity into entropy
    pattern_complexity = runs / total_chars
    adjusted_entropy = shannon_entropy * (1 + pattern_complexity)
    
    return adjusted_entropy