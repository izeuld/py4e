# The file handle does not contain the data for the file, it is quite easy to construct a for loop to read through and count each of the lines in a file. Because the for loop reads the data one line at a time, it can efficiently read and count the lines in very large files without running out of main memory to store the data. This program can count the lines in any size file using very little memory since each line is read, counted, and then discarded.
fhand = open('../text/mbox-short.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)

# If you know the file is relatively small compared to the size of your main memory, you can read the whole file into one string using the read method on the file handle.
fhand = open('mbox-short.txt')
inp = fhand.read()
