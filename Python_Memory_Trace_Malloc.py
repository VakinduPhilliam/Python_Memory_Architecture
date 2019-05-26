# Python Memory Allocation, Partitioning and Mapping
# tracemalloc — Trace memory allocations
# The tracemalloc module is a debug tool to trace memory blocks allocated by Python. It provides the following information:
# > Traceback where an object was allocated
# > Statistics on allocated memory blocks per filename and per line number: total size, number and average size of allocated memory blocks
# > Compute the differences between two snapshots to detect memory leaks
# To trace most memory blocks allocated by Python, the module should be started as early as possible by setting the PYTHONTRACEMALLOC environment
# variable to 1, or by using -X tracemalloc command line option. The tracemalloc.start() function can be called at runtime to start tracing Python
# memory allocations.
# traceback. 
# Traceback where the memory block was allocated, Traceback instance.
# 
# Traceback
# class tracemalloc.Traceback 
# Sequence of Frame instances sorted from the oldest frame to the most recent frame.
#
# format(limit=None, most_recent_first=False). 
# Format the traceback as a list of lines with newlines. Use the linecache module to retrieve lines from the source code.
# If limit is set, format the limit most recent frames if limit is positive. Otherwise, format the abs(limit) oldest frames.
# If most_recent_first is True, the order of the formatted frames is reversed, returning the most recent frame first instead of last.
# 
# Similar to the traceback.format_tb() function, except that format() does not include newlines.
# 
# Example:
# 

print("Traceback (most recent call first):")

for line in traceback:
    print(line)
