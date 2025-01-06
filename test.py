import time
import multiprocessing
from multiprocessing import Pool
import numpy as np

def empty_loop(chunk_size):
    # Using numpy's fast array operations instead of Python loop
    np.zeros(chunk_size)

if __name__ == '__main__':
    iterations = 10000000000
    num_cores = multiprocessing.cpu_count()
    chunk_size = iterations // num_cores

    start_time = time.time()
    
    # Using Pool context manager for better resource management
    with Pool(num_cores) as pool:
        # Using imap instead of map for better memory efficiency
        list(pool.imap(empty_loop, [chunk_size] * num_cores, chunksize=1000))
    
    end_time = time.time()
    duration = end_time - start_time
    
    print(f"Duration in m. sec: {duration * 1000}")  # Convert to milliseconds