import time
def fibbo(m):
    if m == 0 or m == 1 :
        return 1
    else:
        return fibbo(m-1)+fibbo(m-2)
start = time.time()
print(fibbo(37))
print(time.time()-start)
#This process is time consuming and when calculate higher order fibbonacci then higher time consuming, so for this problem we use memoization