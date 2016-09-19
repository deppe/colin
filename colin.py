#!/usr/local/bin/python

def exponential_search(X,key):
    bound = 1

    try:
        while X[bound] < key:
            bound *=2
    except IndexError as e:
        pass

    return binary_search(X,bound/2,bound,key)
        

def binary_search(X,start,end,key):
    print start,end
    if end < start:
        return None
    mid = start + (end-start)/2

    try:
        val = X[mid] #val == inf
    except IndexError as e:
        val = None

    if val  == key:
        return mid
    elif val < key:
        return binary_search(X,mid+1,end,key)
    elif val > key or val is None:
        return binary_search(X,start,mid-1,key)


    #try:
    #    if X[mid] == key:
    #        return mid
    #    elif X[mid] > key:
    #        return binary_search(X,start,mid-1,key)
    #    elif X[mid] < key:
    #    return binary_search(X,mid+1,end,key)
    #except IndexError as e:
    #    return binary_search(X,start,mid-1,key)




def main():
    X = [0,1,2,3,4,6,7,8,9]
    index = exponential_search(X,5)
    print index

if __name__ == "__main__":
    main()

