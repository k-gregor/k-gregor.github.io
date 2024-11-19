import numpy as np

array = np.random.randint(0, 101, size=(100000, 10000))

memory_usage_in_bytes = array.nbytes / (1024 ** 2)

array_int8 = array.astype(np.int8)
converted_memory_usage_in_bytes = array_int8.nbytes / (1024 ** 2)

print(f'{memory_usage_in_bytes:.2f}, {converted_memory_usage_in_bytes:.2f}')
