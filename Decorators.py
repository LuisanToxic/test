from datetime import datetime


def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args,**kwargs)
        print(datetime.now() - start)
        return result
    return wrapper

#@timeit
def prog(chis):
    for i in range(1000, 10000):
        vrem = i
        strok = []
        des = 1
        good = []
        for j in range(1, 5):
            strok.append(vrem % (10 * des) // des)
            des *= 10
        for j in range(3):
            good.append(int(strok[j]) + int(strok[j + 1]))
        good.pop(good.index(min(good)))
        otv = int(str(min(good)) + str(max(good)))
        if otv == chis:
            return i

#@timeit
def two(n):
    #start = datetime.now()
    l = [x for x in range(n) if x % 2==0]
    #print(datetime.now() - start)
    return l


l1 = timeit(prog)
#l2 = two(10000)
#print(l1)
#print(12)
#print(two())

#print(type(l1), l1.__name__)
a=l1(10)

