import random
def main():

    C = (CreateRandomList(10))
    D = C.copy()
    D.sort()
    BubbleSort(C)

    if D != C:
        print("Error in bubble sort")
    else:
        print( f"Copy of Random list then sorted {D}" )
        print(f"bubble sort {C}")

    E = (CreateRandomList(10))
    B = E.copy()
    B.sort()
    ShakerSort(E)

    if B != E:
         print("Error in Shaker sort")
    else:
         print(f"Copy of Random list then sorted {B}")
         print(f"Shaker sort list {E}")

    G = (CreateRandomList(10))
    H = G.copy()
    H.sort()
    CountingSort(G)
    if H != G:
        print("Error in Counting sort")
    else:
        print(f"Copy of Random list then sorted {H}")
        print(f"Counting sort {G}")

def CreateRandomList(A):
# create a list with A number of integers so 0-9 as the index.
    b = []
    for i in range(A):
            b.append(random.randrange(0, A))
    return b

def BubbleSort(A):
        is_Sorted = False
        while is_Sorted == False:
            is_Sorted = True
            for i in range(len(A) - 1):
                if A[i] > A[i + 1]:
                    A[i], A[i + 1] = A[i + 1], A[i]
                    is_Sorted = False

def ShakerSort(A):
    is_Sorted = False
    while is_Sorted == False:
        is_Sorted = True
        for i in range(len(A) - 1):
              if A[i] > A[i + 1]:
                   A[i], A[i + 1] = A[i + 1], A[i]
                   is_Sorted = False
        for i in range(len(A) -2, -1, -1):
             if A[i] > A[i + 1]:
                  A[i], A[i + 1] = A[i + 1], A[i]
                  is_Sorted = False

def CountingSort(A):
    # print (A) 
    f = [0] * len(A)
    # print(f)

    for x in A:
        f[x] = f[x] + 1 # finds the iteration of the given number and adds one to it.
    # print(f)

    K = 0 # initialize k first to be zero so it does not throw errors
    for i in range(len(f)): 
         v = i # v is the value you are on
         count = f[i] # count is how many there are of that value
         for j in range(count): # this loop will only do anything if the count is bigger than 0
            # print(j, end=" ")
            A[K] = v #A[K] starts at zero goes up
            K += 1 # # we use k to iterate up becuase if we use j it will be an error out of the range
main()