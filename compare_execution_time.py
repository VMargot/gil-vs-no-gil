import time
import threading
import multiprocessing


N = 10**6
NUM_THREADS = 4
NUM_PROCESSES = 4
NUM_ITERATIONS = 100


# CPU-bound task
def is_prime(n: int) -> bool:
    """ Check if a number is prime.
    args:
        n (int): The number to check."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def count_primes(start: int, end: int) -> int:
    """ Count the number of prime numbers in the range [start, end).
    args:
        start (int): The start of the range.
        end (int): The end of the range."""
    count = 0
    for i in range(start, end):
        if is_prime(i):
            count += 1
    return count


def single_threaded(n: int) -> int:
    return count_primes(0, n)


def multi_threaded(n: int, num_threads: int = 4) -> int:
    """ Count the number of prime numbers in the range [0, n) using multiple threads.
    args:
        n (int): The upper limit of the range.
        num_threads (int): The number of threads to use."""
    threads = []
    results = [0] * num_threads
    step = n // num_threads

    def worker(idx, s, e):
        results[idx] = count_primes(s, e)

    for i in range(num_threads):
        s = i * step
        e = (i + 1) * step if i < num_threads - 1 else n
        thread = threading.Thread(target=worker, args=(i, s, e))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return sum(results)


def multi_processing(n: int, num_processes: int = 4) -> int:
    """ Count the number of prime numbers in the range [0, n) using multiple processes.
    args:
        n (int): The upper limit of the range.
        num_processes (int): The number of processes to use."""
    pool = multiprocessing.Pool(processes=num_processes)
    step = n // num_processes
    tasks = [(i * step, (i + 1) * step if i < num_processes - 1 else n) for i in range(num_processes)]
    results = pool.starmap(count_primes, tasks)
    pool.close()
    pool.join()
    return sum(results)


if __name__ == "__main__":
    # Single-threaded
    t1 = time.time()
    for _ in range(NUM_ITERATIONS):
        single_result = single_threaded(N)
    t2 = time.time()
    print(f"Single-threaded: {single_result} primes found in {(t2 - t1) / NUM_ITERATIONS:.4f} seconds")

    # Multi-threaded
    t3 = time.time()
    for _ in range(NUM_ITERATIONS):
        multi_thread_result = multi_threaded(N, NUM_THREADS)
    t4 = time.time()
    print(f"Multi-threaded: {multi_thread_result} primes found in {(t4 - t3) / NUM_ITERATIONS:.4f} seconds")

    # Multi-processing
    t5 = time.time()
    for _ in range(NUM_ITERATIONS):
        multi_process_result = multi_processing(N, NUM_PROCESSES)
    t6 = time.time()
    print(f"Multi-processing: {multi_process_result} primes found in {(t6 - t5) / NUM_ITERATIONS:.4f} seconds")
