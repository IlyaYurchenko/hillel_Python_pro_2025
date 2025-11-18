import multiprocessing as mp

def collatz_holds(n: int) -> bool:
    original = n
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        if n < 1:
            return False
    return True

def worker(task_queue, result_queue):
    while True:
        try:
            start, end = task_queue.get_nowait()
        except:
            break

        passed = 0
        for number in range(start, end):
            if collatz_holds(number):
                passed += 1

        result_queue.put((start, end, passed))

def main():
    task_queue = mp.Queue()
    result_queue = mp.Queue()

    chunk_size = 10000
    max_number = 1_000_000

    for start in range(1, max_number + 1, chunk_size):
        end = min(start + chunk_size, max_number + 1)
        task_queue.put((start, end))

    workers = []
    num_workers = mp.cpu_count()

    for _ in range(num_workers):
        process = mp.Process(target=worker, args=(task_queue, result_queue))
        process.start()
        workers.append(process)

    total_checked = 0
    total_passed = 0

    while any(process.is_alive() for process in workers) or not result_queue.empty():
        try:
            start, end, passed = result_queue.get(timeout=1)
            total_checked += (end - start)
            total_passed += passed
            print(f"Checked {start}-{end}, passed={passed}")
        except:
            pass

    print("Total checked:", total_checked)
    print("Total passed:", total_passed)

if __name__ == "__main__":
    main()
