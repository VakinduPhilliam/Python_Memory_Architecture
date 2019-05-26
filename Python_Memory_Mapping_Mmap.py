# Python Memory Mapping.
# mmap — Memory-mapped file support.
# Memory-mapped file objects behave like both bytearray and like file objects.
# You can use mmap objects in most places where bytearray are expected; for example, you can use the re module to search through
# a memory-mapped file.
# You can also change a single byte by doing obj[index] = 97, or change a subsequence by assigning to a slice: obj[i1:i2] = b'...'.
# You can also read and write data starting at the current file position, and seek() through the file to different positions.
# class mmap.mmap(fileno, length, flags=MAP_SHARED, prot=PROT_WRITE|PROT_READ, access=ACCESS_DEFAULT[, offset]).
# (Unix version) Maps length bytes from the file specified by the file descriptor fileno, and returns a mmap object.
# If length is 0, the maximum length of the map will be the current size of the file when mmap is called.
# ALLOCATIONGRANULARITY which is equal to PAGESIZE on Unix systems.
# To ensure validity of the created memory mapping the file specified by the descriptor fileno is internally automatically synchronized
# with physical backing store on Mac OS X and OpenVMS.
# 
# This example shows a simple way of using mmap:
# 

import mmap

# write a simple example file

with open("hello.txt", "wb") as f:
    f.write(b"Hello Python!\n")

with open("hello.txt", "r+b") as f:

    # memory-map the file, size 0 means whole file

    mm = mmap.mmap(f.fileno(), 0)

    # read content via standard file methods

    print(mm.readline())  # prints b"Hello Python!\n"

    # read content via slice notation

    print(mm[:5])  # prints b"Hello"

    # update content using slice notation;
    # note that new content must have same size

    mm[6:] = b" world!\n"

    # ... and read again using standard file methods

    mm.seek(0)

    print(mm.readline())  # prints b"Hello  world!\n"

    # close the map

    mm.close()

#
# 
# mmap can also be used as a context manager in a with statement:
#
# 

import mmap

with mmap.mmap(-1, 13) as mm:
    mm.write(b"Hello world!")
 
#
#
# Context manager support.
#
# 
# The next example demonstrates how to create an anonymous map and exchange data between the parent and child processes:
# 
#

import mmap
import os

mm = mmap.mmap(-1, 13)
mm.write(b"Hello world!")

pid = os.fork()

if pid == 0:  # In a child process
    mm.seek(0)

    print(mm.readline())

    mm.close()

#
# 
# Memory-mapped file objects support the following methods:
#
#