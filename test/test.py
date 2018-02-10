import time


def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


start = time.time()
li = [x for x in range(100000) if isPrime(x)]
end = time.time()

print(end - start)
