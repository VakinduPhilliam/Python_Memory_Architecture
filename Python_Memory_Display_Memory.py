# Python Memory Allocation, Partitioning and Mapping
# tracemalloc — Trace memory allocations
# The tracemalloc module is a debug tool to trace memory blocks allocated by Python. It provides the following information:
# > Traceback where an object was allocated
# > Statistics on allocated memory blocks per filename and per line number: total size, number and average size of allocated memory blocks
# > Compute the differences between two snapshots to detect memory leaks
# To trace most memory blocks allocated by Python, the module should be started as early as possible by setting the PYTHONTRACEMALLOC environment
# variable to 1, or by using -X tracemalloc command line option. The tracemalloc.start() function can be called at runtime to start tracing Python
# memory allocations.
#
# Display the 10 files allocating the most memory:
# 

import tracemalloc

tracemalloc.start()

# ... run your application ...

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

print("[ Top 10 ]")

for stat in top_stats[:10]:
    print(stat)
