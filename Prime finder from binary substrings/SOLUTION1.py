import math

import time


def sieve_of_eratosthenes(N):
    sieve = [True] * N

    sieve[0:2] = [False, False]

    for i in range(2, int(math.sqrt(N)) + 1):

        if sieve[i]:

            for j in range(i * i, N, i):
                sieve[j] = False

    return {i for i, is_prime in enumerate(sieve) if is_prime}


def find_primes_sieve(binary_str, N):
    use_sieve = N <= 10 ** 7

    primes = sieve_of_eratosthenes(N) if use_sieve else set()

    found_primes = set()

    max_length = len(bin(N - 1)) - 2  # Max binary length for numbers less than N

    for i in range(len(binary_str)):

        if binary_str[i] == '0' and len(binary_str) - i > 1:
            continue

        num = 0

        for j in range(i, min(i + max_length, len(binary_str))):

            num = (num << 1) | (1 if binary_str[j] == '1' else 0)

            if num >= N:
                break

            if num >= 2 and ((use_sieve and num in primes) or (not use_sieve and is_prime(num))):
                found_primes.add(num)

    primes_sorted = sorted(found_primes)

    if len(primes_sorted) < 6:

        return f"{len(primes_sorted)}: {', '.join(map(str, primes_sorted))}"



    else:

        return f"{len(primes_sorted)}: {', '.join(map(str, primes_sorted[:3] + primes_sorted[-3:]))}"


def is_prime(n):
    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(n)) + 1, 2):

        if n % i == 0:
            return False

    return True


# User Input and Execution


binary_input = input("Enter the binary string: ").strip()

N = int(input("Enter the limit (N): "))

# Sieve Solution


start_time = time.time()

result_sieve = find_primes_sieve(binary_input, N)

end_time = time.time()

runtime_sieve = end_time - start_time

# Displaying Results


print("\n Sieve of Eratosthenes Solution ")

print(f"Output: {result_sieve}")

print(f"Runtime: {runtime_sieve:.5f} seconds")

# The test case results were done via the IDE Google colab - Gizem

# Test case 1: Output: 15: 2, 3, 5, 269, 2153, 17231 - Runtime: 0.14525 seconds

# Test case 2: Output: 28: 2, 3, 5, 10729, 17231, 85837 - Runtime: 0.16639 seconds

# Test case 3: Output: 7: 3, 7, 31, 8191, 131071, 524287 - Runtime: 0.25586 seconds

# Test case 4: Output: 44: 2, 3, 5, 5571347, 41577089, 55398449 - Runtime: 0.00124 seconds

# Test case 5: Output: 52: 2, 3, 5, 84087683, 3920234023, 5625434161 - Runtime: 0.00938 seconds

# Test case 6: Output: 64: 2, 3, 5, 2724796139969, 5841981288761, 45810224399911 - Runtime: 0.56194 seconds

# Test case 7: Output: 71: 2, 3, 5, 45810224399911, 7435453988964809, 18946016916092977 - Runtime: 12.74939 seconds

# Test case 8: Output: 76: 2, 3, 5, 45810224399911, 7435453988964809, 18946016916092977 - Runtime: 17.54148 seconds

# Test case 9: Output: 81: 2, 3, 5, 7435453988964809, 18946016916092977, 378518838354150661 - Runtime: 46.81164 seconds

# Test case 10: Output: 89: 2, 3, 5, 7435453988964809, 18946016916092977, 378518838354150661 - Runtime: 59.71938 seconds 