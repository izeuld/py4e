# The file handle does not contain the data for the file, it is quite easy to construct a for loop to read through and count each of the lines in a file. Because the for loop reads the data one line at a time, it can efficiently read and count the lines in very large files without running out of main memory to store the data. This program can count the lines in any size file using very little memory since each line is read, counted, and then discarded.
fhand = open('../text/mbox-short.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)

# If you know the file is relatively small compared to the size of your main memory, you can read the whole file into one string using the read method on the file handle.
fhand = open('mbox-short.txt')
inp = fhand.read()

# the newline character is a single character, separating the characters in the file into lines.
stuff = 'A1\nA2'
print(stuff)
len(stuff)

# To write a file, you have to open it with mode "w" as a second parameter. If the file already exists, opening it in write mode clears out the old data and starts fresh, so be careful! If the file doesn't exist, a new one is created.
fout = open('mbox-short2.txt', 'w')
print(fout)
# The file object keeps track of where it is, so if you call write again, it adds the new data to the end. To manage the ends of lines as we write to the file, explicitly insert the newline character when ending a line.
line2 = 'the emblem of our land.\n'
fout.write(line2)
# When you are done writing, close the file to make sure that the last bit of data is physically written to the disk.
fout.close()
