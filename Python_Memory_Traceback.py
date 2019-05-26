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
# Get the traceback of a memory block.
# 
# Code to display the traceback of the biggest memory block:
# 

import tracemalloc

# Store 25 frames

tracemalloc.start(25)

# ... run your application ...

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('traceback')

# pick the biggest memory block

stat = top_stats[0]

print("%s memory blocks: %.1f KiB" % (stat.count, stat.size / 1024))

for line in stat.traceback.format():
    print(line)
