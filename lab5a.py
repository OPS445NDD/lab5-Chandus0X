#!/usr/bin/env python3

def read_file_string(file_name):
    f = open('data.txt', 'r')
    read_data = f.read()
    f.close()
    return read_data
def read_file_list(file_name):
    f=open('data.txt', 'r')   
    new_list=[]
    for line in f:
        new_list.append(line.strip())



    f.close()
    return (new_list)
if __name__=='__main__':
    file_name='data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
