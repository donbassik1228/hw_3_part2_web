
from multiprocessing import Pool, cpu_count
import time

def factorize_async(num):
    divisors = [1]
    for i in range(2, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def factorize_parallel(numbers):
    with Pool(cpu_count()) as pool:
        results = pool.map(factorize_async, numbers)
    return results

if __name__ == '__main__':
    numbers_to_factorize = [1000000, 500000, 750000]

    start_time = time.time()
    result_parallel = factorize_parallel(numbers_to_factorize)
    end_time = time.time()

    print("Parallel Factorize Results:", result_parallel)
    print("Parallel Execution Time:", round(end_time - start_time, 4), "seconds")