import sys

if len(sys.argv) != 2:
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    sys.exit(1)

if not (1 <= n <= 100):
    sys.exit(1)

primes = []
num = 2
while len(primes) < n:
    is_prime = True
    if num < 2:
        is_prime = False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

    if is_prime:
        primes.append(num)

    num += 1

print(" ".join(map(str, primes)))

     
