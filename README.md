# Python_Memory_Partition
These scripts are written to demonstrate the process of Python Memory Allocation, Partitioning and Mapping. 
The Python ‘tracemalloc’ module is used to trace memory allocations. 
The tracemalloc module is a debug tool to trace memory blocks allocated by Python.  
It provides the following information: > Traceback where an object was allocated.  > Statistics on allocated memory blocks per filename and per line number: total size, number and average size of allocated memory blocks.  > Compute the differences between two snapshots to detect memory leaks. 
To trace most memory blocks allocated by Python, the module should be started as early as possible by setting the PYTHONTRACEMALLOC environment variable to 1, or by using -X tracemalloc command line option.  
The tracemalloc.start() function can be called at runtime to start tracing Python memory allocations. 
Compiled and presented by Vakindu Philliam.
