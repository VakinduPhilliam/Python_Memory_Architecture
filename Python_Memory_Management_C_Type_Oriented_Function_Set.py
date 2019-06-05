# Python Memory Management
# Memory management in Python involves a private heap containing all Python objects and data structures.
# The management of this private heap is ensured internally by the Python memory manager.
# The Python memory manager has different components which deal with various dynamic storage management aspects, like sharing, segmentation, preallocation
# or caching.
# At the lowest level, a raw memory allocator ensures that there is enough room in the private heap for storing all Python-related data by interacting with 
# the memory manager of the operating system. On top of the raw memory allocator, several object-specific allocators operate on the same heap and implement
# distinct memory management policies adapted to the peculiarities of every object type.
# For example, integer objects are managed differently within the heap than strings, tuples or dictionaries because integers imply different storage
# requirements and speed/space tradeoffs. 
# The Python memory manager thus delegates some of the work to the object-specific allocators, but ensures that the latter operate within the bounds of the
# private heap.
# 
# It is important to understand that the management of the Python heap is performed by the interpreter itself and that the user has no control over it, even
# if they regularly manipulate object pointers to memory blocks inside that heap.
# The allocation of heap space for Python objects and other internal buffers is performed on demand by the Python memory manager through the Python/C API
# functions listed in this document.
# To avoid memory corruption, extension writers should never try to operate on Python objects with the functions exported by the C library: malloc(),
# calloc(), realloc() and free().
# This will result in mixed calls between the C allocator and the Python memory manager with fatal consequences, because they implement different algorithms
# and operate on different heaps.
# However, one may safely allocate and release memory blocks with the C library allocator for individual purposes.
#


#
# tracemalloc C Example:
# 
# This example is written so that the I/O buffer is allocated from the Python heap by using the type-oriented function set:
# 

#
# PyObject *res;
#
# char *buf = PyMem_New(char, BUFSIZ); /* for I/O */
#
# if (buf == NULL)
#    return PyErr_NoMemory();
#
# /* ...Do some I/O operation involving buf... */
#
# res = PyBytes_FromString(buf);
#
# PyMem_Del(buf); /* allocated with PyMem_New */
#
# return res;
#
