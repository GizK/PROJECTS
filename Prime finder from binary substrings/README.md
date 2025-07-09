# Prime finder from binary substrings
- This project is a binary substring prime checker built using Python. It extracts all valid integer values from substrings of a given binary string, converts them to decimal, and uses trial division to test for 
  primality. It returns a summary of all primes found that are less than a user-defined limit N.
- Accepts binary input strings from the user, extracts substrings, converts them to decimal, and ignores values ≥ N, skips substrings starting with leading 0s, efficiently checks for primes using an optimized trial 
  division method, memorises previously checked numbers to avoid redundant computation. Displays: Total number of primes found, the first 3 and last 3 primes (if more than 6), tracks and displays execution runtime for 
  performance benchmarking.
- What I learnt: 
1. Efficient Primality Testing
   I implemented a 6k ± 1 optimization in trial division to reduce the number of unnecessary checks.
2. Substring Generation and Bit Manipulation
   I practiced generating substrings using bit-shifting techniques and converting binary segments directly to decimal integers.
3. Set and Dictionary Usage for Speed
   I used set() to store unique primes and a dict to memorize previous results, reducing runtime significantly on larger inputs.
4. Performance Profiling
   I used Python’s time module to measure execution time, helping me evaluate the scalability and efficiency of the algorithm.
5. Edge Case Handling
   I handled: Leading zeros, duplicates, substrings out of bounds, large binary inputs with careful performance considerations
- Self-reflection: This project challenged me to combine bitwise logic, performance tuning, and algorithmic problem solving. The rapid growth in runtime with large binary strings emphasized the importance of 
  optimization and caching. I also gained experience in profiling and improving algorithms based on real-time test cases. It was rewarding to see how subtle changes like skipping known composites or caching previous 
  results could lead to substantial improvements in performance. This project pushed my understanding of both low-level binary manipulation and high-level performance analysis.
