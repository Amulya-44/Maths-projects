# 🔢 Sieve of Eratosthenes (Prime Number Generator)

A highly optimized C++ implementation of the ancient Greek algorithm used to find all prime numbers up to a specified limit $n$. This project demonstrates efficient memory usage, algorithmic optimization, and the foundational mathematics that power modern cryptography.

---

## 🧠 The Mathematics & Overview

The **Sieve of Eratosthenes** is an ancient, highly efficient mathematical algorithm for finding all prime numbers up to any given limit. Instead of checking every single number to see if it has divisors (which is computationally expensive), the sieve works by **process of elimination**.

### How it Works:
1. Create a boolean array representing numbers from $0$ to $n$, initially marking all numbers as `true` (prime).
2. Set $0$ and $1$ to `false` since they are not prime.
3. Start at the first prime number, $2$. Mark all of its multiples ($4, 6, 8, 10...$) as `false`.
4. Move to the next unmarked number, $3$. Mark all of its multiples ($6, 9, 12...$) as `false`.
5. Repeat this process only up to $\sqrt{n}$. Any composite number less than $n$ must have a prime factor less than or equal to $\sqrt{n}$.
6. The numbers that remain marked as `true` are your prime numbers.

---

## ⚡ Performance Breakdown: Trial Division vs. Optimized Sieve

To appreciate why this implementation is effective, we can compare it to the standard "brute-force" approach (Trial Division).

### Complexity Comparison Table

| Approach | Time Complexity | Space Complexity | Efficiency Note |
| :--- | :--- | :--- | :--- |
| **Brute Force (Trial Division)** | $\mathcal{O}(n \sqrt{n})$ | $\mathcal{O}(1)$ | Iterates and checks every single number individually. Incredibly slow for large values of $n$. |
| **Optimized Sieve (This Code)** | $\mathcal{O}(n \log(\log n))$ | $\mathcal{O}(n)$ | Eliminates composite numbers in bulk. The $\sqrt{n}$ outer loop and $p^2$ inner loop bypass unnecessary redundant checks. |

### Code Optimization Highlights in This Project:
* **The $\sqrt{n}$ Boundary:** The outer loop terminates early at `sqrt(num)`. If a number has a factor, its corresponding factor must have already been checked.
* **The $p^2$ Inner Loop Starting Point:** Instead of starting the elimination loop at $2p$ or $3p$, the inner loop starts directly at $p \times p$. This avoids redundant work, as smaller multiples (like $2p$ or $3p$) will have already been crossed out by smaller primes ($2$ and $3$).

---

## 🌐 Real-World Applications

Prime numbers aren't just theoretical puzzle pieces; they are foundational to modern software engineering:

* **Public-Key Cryptography (RSA):** Secure internet communication, SSL/TLS certificates, and SSH keys rely on the difficulty of factoring giant numbers built from massive prime pairs.
* **Hash Tables & Hashing Functions:** Many hash functions use prime numbers for table sizing or multiplier keys because they minimize data collisions, ensuring even distribution.
* **Random Number Generation:** Advanced pseudorandom number generators (PRNGs) utilize prime number characteristics to achieve longer periods of unpredictability.

---

## 🛠️ How to Run the Project

### Prerequisites
Make sure you have a C++ compiler installed (e.g., `g++` via GCC or Clang).
