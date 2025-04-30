import math 
import time 
 
def is_prime(n): 
    if n < 2: 
        return False 
    if n in {2, 3}: 
        return True 
    if n % 2 == 0 or n % 3 == 0: 
        return False 
    for i in range(5, int(math.sqrt(n)) + 1, 6): 
        if n % i == 0 or n % (i + 2) == 0: 
            return False 
    return True 
 
 
def find_primes_trial(binary_str, N): 
    found_primes = set() 
    checked_numbers = {}  # memorising numbers 
    max_length = len(bin(N - 1)) - 2 
 
    for i in range(len(binary_str)): 
        if binary_str[i] == '0' and i + 1 < len(binary_str): 
            continue  # Skip substrings starting with 0 
 
        num = 0 
        for j in range(i, min(i + max_length, len(binary_str))): 
            num = (num << 1) | int(binary_str[j]) 
 
            if num >= N: 
                break  # Stop checking numbers greater than N 
 
            if num in checked_numbers: 
                if checked_numbers[num]: 
                    found_primes.add(num) 
                continue 
 
            if num >= 2 and is_prime(num): 
                found_primes.add(num) 
                checked_numbers[num] = True 
            else: 
                checked_numbers[num] = False 
 
    primes_sorted = sorted(found_primes) 
    if len(primes_sorted) < 6: 
        return f"{len(primes_sorted)}: {', '.join(map(str, primes_sorted))}" 
    else: 
        return f"{len(primes_sorted)}: {', '.join(map(str, primes_sorted[:3] + primes_sorted[-3:]))}" 
 
 
def main(): 
    while True: 
        binary_input = input("Enter the binary string (or type 'exit' to quit): ").strip() 
        if binary_input.lower() == 'exit': 
            break 
 
        N = int(input("Enter the limit (N): ")) 
 
        start_time = time.time() 
        result_trial = find_primes_trial(binary_input, N) 
        end_time = time.time() 
        runtime_trial = end_time - start_time 
 
        print("\nTrial Division Solution") 
        print(f"Output: {result_trial}") 
        print(f"Runtime: {runtime_trial:.5f} seconds\n") 
 
 
if __name__ == "__main__": 
    main()

# The test case results were done via the IDE Google colab FOR THE OPTIMISED SOLUTION 2 - Gizem

# Test case 1: Output: 15: 2, 3, 5, 269, 2153, 17231 - Runtime: 0.00009 seconds

# Test case 2: Output: 28: 2, 3, 5, 10729, 17231, 85837 - Runtime: 0.00018 seconds

# Test case 3: Output: 7: 3, 7, 31, 8191, 131071, 524287 - Runtime: 0.00028 seconds

# Test case 4: Output: 44: 2, 3, 5, 5571347, 41577089, 55398449 - Runtime: 0.00091 seconds

# Test case 5: Output: 52: 2, 3, 5, 84087683, 3920234023, 5625434161 - Runtime: 0.00635 seconds

# Test case 6: Output: 64: 2, 3, 5, 2724796139969, 5841981288761, 45810224399911 - Runtime: 0.37514 seconds

# Test case 7: Output: 71: 2, 3, 5, 45810224399911, 7435453988964809, 18946016916092977 - Runtime: 8.73149 seconds

# Test case 8: Output: 76: 2, 3, 5, 45810224399911, 7435453988964809, 18946016916092977 - Runtime: 12.08159 seconds

# Test case 9: Output: 81: 2, 3, 5, 7435453988964809, 18946016916092977, 378518838354150661 - Runtime: 32.11066 seconds

# Test case 10: Output: 89: 2, 3, 5, 7435453988964809, 18946016916092977, 378518838354150661 - Runtime: 40.33269 seconds