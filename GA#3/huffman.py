# Basil Alzamil
# CS325 - GA#3
# Fall 2016
import string 
import sys
from itertools import chain

def main():
    #Reading from a input.txt
    fname = "input.txt"
    fd = open(fname, 'r')
    line = fd.readline()
    line = line.split('\n')
    line = line[0] 

    print line
    #(A) Simple Encoding
    print "\nSample Encode"
    simple_arr = SimpleEncode(line)
    print simple_arr
    print "Size of file =", getSimpleSize(simple_arr)
    

#   (B) Run-Length Encoding
    print "\nRun-Length Encoding"
    my_arr = RunLength(line)
    my_bit_arr = RunLengthToBits(my_arr)
    print "Run-Length:", my_arr
    print "Run-Length in Binary:", my_bit_arr
    print "size of file =", getRLSize(my_bit_arr)

    
#   (C) Huffman Code
    
    
    
    
    
    
#Converts lower case letters to bits a to z, form 00000 to 11001, respectively.
def SimpleEncode(word):
    length = len(word)
    bit_arr = [None] * (length)
    for i in range(0, length):
        bit_arr[i] = EncodeChar(word[i])
    return bit_arr
        


def EncodeChar(char):   
    decimal = ord(char) - 97
    bits = format(decimal, 'b').zfill(5)
    return bits



def getSimpleSize(arr):
    count = 0
    length = len(arr)
    for i in range(0, length):
        count += len(arr[i])
    return count
        


def RunLength(word):
    i = 0
    count = 1
    array = []
    length = len(word)

    for i in range(0,length):
        if word[i] != word[i-1]:
            if (i-1) >= 0:
                entry = (word[i-1], count)
                array.append(entry)
            count = 1
        else: #else if the character is repeated, keep counting
            count += 1

    entry = (word[i], count) #adding the last entry
    array.append(entry)
    return array
    


def RunLengthToBits(rn_array):
    length = len(rn_array)
    bit_arr = [[0 for j in range(2)] for i in range(length)]

    for i in range(0, length): 
        bit_arr[i][0] = EncodeChar(rn_array[i][0]) #converting lower case chars to bits
        bit_arr[i][1] = format(rn_array[i][1], 'b').zfill(19) #converting n from decimal to binary
    return bit_arr



def getRLSize(arr):
    count = 0
    length = len(arr)
    for i in range(0, length):
        count += len(arr[i][0])
        count += len(arr[i][1])
    return count
    
    

if __name__ == '__main__':
  main()





# TESTING
#    for i in range(ord('a'), ord('z')+1):
#        print chr(i), SimpleEncode(chr(i))

#Useful
#    my_bit_arr = list(chain(*my_bit_arr)) #converts list of tuples to list
