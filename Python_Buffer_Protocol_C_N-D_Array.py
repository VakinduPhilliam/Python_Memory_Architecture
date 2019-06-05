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
# PIL-style: shape, strides and suboffsets
# In addition to the regular items, PIL-style arrays can contain pointers that must be followed in order to get to the next element in a dimension.
# For example, the regular three-dimensional C-array char v[2][2][3] can also be viewed as an array of 2 pointers to 2 two-dimensional arrays: char
# (*v[2])[2][3].
# In suboffsets representation, those two pointers can be embedded at the start of buf, pointing to two char x[2][3] arrays that can be located anywhere in
# memory.
# 

#
# Here is a function that returns a pointer to the element in an N-D array pointed to by an N-dimensional index when there are both non-NULL strides and
# suboffsets:
# 

#
# void *get_item_pointer(int ndim, void *buf, Py_ssize_t *strides,
#                       Py_ssize_t *suboffsets, Py_ssize_t *indices) {
#
#    char *pointer = (char*)buf;
#    int i;
#
#    for (i = 0; i < ndim; i++) {
#
#        pointer += strides[i] * indices[i];
#
#        if (suboffsets[i] >=0 ) {
#
#            pointer = *((char**)pointer) + suboffsets[i];
#
#        }
#    }
#
#    return (void*)pointer;
# }
#