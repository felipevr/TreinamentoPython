#!/usr/bin/python

filename = "myfile.txt"

with open( filename ) as f:

    # file read can happen here

    print( "file exists")

    print(f.readlines())

with open( filename, "w") as f:

    print("file write happening here")

    f.write("write something here ")
