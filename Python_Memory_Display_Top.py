# Python Memory Allocation, Partitioning and Mapping
# tracemalloc — Trace memory allocations
# The tracemalloc module is a debug tool to trace memory blocks allocated by Python. It provides the following information:
# > Traceback where an object was allocated
# > Statistics on allocated memory blocks per filename and per line number: total size, number and average size of allocated memory blocks
# > Compute the differences between two snapshots to detect memory leaks
# To trace most memory blocks allocated by Python, the module should be started as early as possible by setting the PYTHONTRACEMALLOC environment
# variable to 1, or by using -X tracemalloc command line option. The tracemalloc.start() function can be called at runtime to start tracing Python
# memory allocations.
# Pretty top.
# Code to display the 10 lines allocating the most memory with a pretty output, ignoring <frozen importlib._bootstrap> and <unknown> files:
 
import linecache
import os
import tracemalloc

def display_top(snapshot, key_type='lineno', limit=10):

    snapshot = snapshot.filter_traces((
        tracemalloc.Filter(False, "<frozen importlib._bootstrap>"),
        tracemalloc.Filter(False, "<unknown>"),
    ))

    top_stats = snapshot.statistics(key_type)

    print("Top %s lines" % limit)

    for index, stat in enumerate(top_stats[:limit], 1):
        frame = stat.traceback[0]

        # replace "/path/to/module/file.py" with "module/file.py"

        filename = os.sep.join(frame.filename.split(os.sep)[-2:])

        print("#%s: %s:%s: %.1f KiB"
              % (index, filename, frame.lineno, stat.size / 1024))

        line = linecache.getline(frame.filename, frame.lineno).strip()

        if line:
            print('    %s' % line)

    other = top_stats[limit:]

    if other:
        size = sum(stat.size for stat in other)

        print("%s other: %.1f KiB" % (len(other), size / 1024))
    total = sum(stat.size for stat in top_stats)

    print("Total allocated size: %.1f KiB" % (total / 1024))

tracemalloc.start()

# ... run your application ...

snapshot = tracemalloc.take_snapshot()

display_top(snapshot)
