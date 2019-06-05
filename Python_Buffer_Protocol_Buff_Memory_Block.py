# Python Buffer Protocol
# Certain objects available in Python wrap access to an underlying memory array or buffer.
# Such objects include the built-in bytes and bytearray, and some extension types like array.array.
# Third-party libraries may define their own types for special purposes, such as image processing or numeric analysis.
# While each of these types have their own semantics, they share the common characteristic of being backed by a possibly large memory buffer.
# It is then desirable, in some situations, to access that buffer directly and without intermediate copying.
#
# Python provides such a facility at the C level in the form of the buffer protocol. This protocol has two sides:
# > on the producer side, a type can export a “buffer interface” which allows objects of that type to expose information about their underlying buffer.
#    This interface is described in the section Buffer Object Structures;
# > on the consumer side, several means are available to obtain a pointer to the raw underlying data of an object (for example a method parameter).
# 
# Simple objects such as bytes and bytearray expose their underlying buffer in byte-oriented form. Other forms are possible; for example, the elements
# exposed by an array.array can be multi-byte values.
# 
# An example consumer of the buffer interface is the write() method of file objects: any object that can export a series of bytes through the buffer
# interface can be written to a file. While write() only needs read-only access to the internal contents of the object passed to it, other methods such as
# readinto() need write access to the contents of their argument.
# The buffer interface allows objects to selectively allow or reject exporting of read-write and read-only buffers.
# 
# There are two ways for a consumer of the buffer interface to acquire a buffer over a target object:
# > call PyObject_GetBuffer() with the right parameters;
# > call PyArg_ParseTuple() (or one of its siblings) with one of the y*, w* or s* format codes.
# 
# In both cases, PyBuffer_Release() must be called when the buffer isn’t needed anymore. Failure to do so could lead to various issues such as resource
# leaks.
#
# Buffer structure:
# 
# Buffer structures (or simply “buffers”) are useful as a way to expose the binary data from another object to the Python programmer. 
# They can also be used as a zero-copy slicing mechanism. Using their ability to reference a block of memory, it is possible to expose any data to the Python
# programmer quite easily. The memory could be a large, constant array in a C extension, it could be a raw block of memory for manipulation before passing
# to an operating system library, or it could be used to pass around structured data in its native, in-memory format.
# Contrary to most data types exposed by the Python interpreter, buffers are not PyObject pointers but rather simple C structures.
# This allows them to be created and copied very simply. When a generic wrapper around a buffer is needed, a memoryview object can be created.
#

#
# NumPy-style: shape and strides.
# The logical structure of NumPy-style arrays is defined by itemsize, ndim, shape and strides.
# If ndim == 0, the memory location pointed to by buf is interpreted as a scalar of size itemsize.
# In that case, both shape and strides are NULL.
# If strides is NULL, the array is interpreted as a standard n-dimensional C-array. Otherwise, the consumer must access an n-dimensional array as follows:
# 

# ptr = (char *)buf + indices[0] * strides[0] + ... + indices[n-1] * strides[n-1] item = *((typeof(item) *)ptr);

#
# 'buf' can point to any location within the actual memory block.
# An exporter can check the validity of a buffer with this function:
# 

def verify_structure(memlen, itemsize, ndim, shape, strides, offset):
    """Verify that the parameters represent a valid array within
       the bounds of the allocated memory:
           char *mem: start of the physical memory block
           memlen: length of the physical memory block
           offset: (char *)buf - mem
    """

    if offset % itemsize:
        return False

    if offset < 0 or offset+itemsize > memlen:
        return False

    if any(v % itemsize for v in strides):
        return False

    if ndim <= 0:
        return ndim == 0 and not shape and not strides

    if 0 in shape:
        return True

    imin = sum(strides[j]*(shape[j]-1) for j in range(ndim)
               if strides[j] <= 0)

    imax = sum(strides[j]*(shape[j]-1) for j in range(ndim)
               if strides[j] > 0)

    return 0 <= offset+imin and offset+imax+itemsize <= memlen
