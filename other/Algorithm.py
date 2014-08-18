#!/usr/bin/env python
# coding:utf-8
# Author:Eular
import math
from math import factorial as f
from numpy import *

def binarySearch(a,k):
    st,ed=0,len(a)-1
    while st<ed:
        mid=st+((ed-st)>>1)
        if k<=a[mid]: ed=mid
        else: st=mid+1
    if k==a[st]: return st
    return -1

#Euler's Totient function,φ(n)
def Phi(L):
    phi = range(L+1)
    for n in xrange(2, L+1):
        if phi[n] == n:
            for k in xrange(n, L+1, n):
                phi[k] = phi[k] / n * (n-1)
    return phi

def phi(n):
    if is_prime(n): return n-1
    if n%2==0 and n/2%2!=0: return phi(n/2)
    t=prime_factors(n)
    f=lambda x,y:x*y
    return n*reduce(f,[i-1 for i in t])/reduce(f,t)

def phi_hash(n):
    a={}
    for p in gen_primes():
        if p>n: break
        a[p]=p-1
    for i in itertools.combinations([j for j in a],2):
        t=i[0]*i[1]
        if t>n: break
        a[t]=(i[0]-1)*(i[1]-1)
    for j in xrange(4,n+1):
        if j not in a:
            t=prime_factors(n)
            f=lambda x,y:x*y
            b=n*reduce(f,[i-1 for i in t])/reduce(f,t)
            a[j]=b
            if j%2==1 and 2*j<=n: a[2*j]=b
    return a

def i_add_f(i,f):
    return [f[0]+i*f[1],f[1]]

def anti_Continued_Fractions(arr):
    if len(arr)==1: return [arr[0],1]
    return i_add_f(arr[0],anti_Continued_Fractions(arr[1:])[::-1])

def sqrt_Continued_Fractions(num):
    a0=int(math.sqrt(num))
    r=[[0,1,a0]]
    while 1:
        p=r[-1][2]*r[-1][1]-r[-1][0]
        q=(num-p**2)/r[-1][1]
        a=(a0+p)/q
        if [p,q,a] in r:
            k=len(r)-r.index([p,q,a])
            break
        r.append([p,q,a])
    return [[i[2] for i in r],k]

#最大公约数 gcd
def hcf(a,b):
    if b==0: return a
    return hcf(b,a%b)

def Continued_Fractions(a,b):
    r=[]
    t=gcb(a,b)
    a/=t
    b/=t
    while 1:
        r.append(a/b)
        if b==1: break
        a,b=b,a%b
    return r

def Combinator(n,r):
	return f(n)/(f(r)*f(n-r))

def Fibonacci():
	a=[1,1]
	while True:
		a.append(sum(a))
		yield a.pop(0)

def is_palindrome(num):
	if num==int(str(num)[::-1]): return True
	return False

def is_leap_yeay(year):
	if year%400==0: return True
	if year%4==0 and year%100!=0: return True
	return False

def divisors_sum(num):
	divisors=[1]
	for i in xrange(2,num/2+1):
		if num%i==0: divisors.append(i)
	return sum(divisors)

def is_perfect_number(num):
	if num==divisors_sum(num): return True
	return False

def m_divide_n(m,n):
	while m%n!=0:
		if m/n==0:
			yield (0,m)
			m*=10
		else:
			yield (m/n,m%n)
			m=m%n*10
	yield (m/n,0)

def factor_numbers(num):
    n=1
    for x in xrange(2,int(math.sqrt(num))):
        if num%x==0:
            n+=1
    return n*2

def most(arr):
    return max(map(lambda x:(arr.count(x),x),arr))[1]

###############
# Triangular  #
# Square      #
# pentagonal  #
# hexagonal   #
# ...         #
###############
def t(n):
	return n*(n+1)/2

def s(n):
    return n*n

def p(n):
	return n*(3*n-1)/2

def h(n):
	return n*(2*n-1)

def hept(n):
    return n*(5*n-3)/2

def o(n):
    return n*(3*n-2)

def is_triangular(num):
	if (math.sqrt(1+8*num)-1)%2==0: return True
	return False

def is_square(num):
    a=int(math.sqrt(num))
    if num==1 or a**2==num: return True
    return False

def is_pentagonal(num):
	if (1+math.sqrt(1+24*num))%6==0: return True
	return False

def is_hexagonal(num):
	if (1+math.sqrt(1+8*num))%4==0: return True
	return False

def is_heptagonal(num):
    if (3+math.sqrt(9+40*num))%10==0: return True
    return False

def is_octagonal(num):
    if (2+math.sqrt(4+12*num))%6==0: return True
    return False

###############
#    prime    #
###############
def gen_primes():
    D={}
    q=2
    while True:
        if q not in D:
            yield q
            D[q*q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p+q,[]).append(p)
            del D[q]
        q+=1

def primes_lessthan_max(max):
    prime=[2]
    m=3
    while prime[-1]<max:
        i=0
        while prime[i]**2<=m:
            if m%prime[i]==0:
                m+=2
                i=1
            else:i+=1
        prime.append(m)
        m+=2
    prime.pop()
    return prime

def primes_until_n(n):
    prime=[2]
    m=3
    while len(prime)<n:
        i=0
        while prime[i]**2<=m:
            if m%prime[i]==0:
                m+=2
                i=1
            else:i+=1
        prime.append(m)
        m+=2
    return prime

def prime_factors(num):
    factors=[]
    half=num/2
    for p in gen_primes():
        if p>half: break
        if num%p==0: factors.append(p)
    return factors

def get_prime_factors(num):
    factors=[]
    for p in gen_primes():
        i,a=num,0
        if p>num:
            break
        while i%p==0:
            i/=p
            a+=1
        if a!=0:
            factors.append((p,a))
    return factors

def prime_factor_numbers(num):
    n=0
    for p in gen_primes():
        if p>num/2: break
        if num%p==0: n+=1
    return n

def is_prime2(num):
    if num<=0: return False
    for p in gen_primes():
        if p>math.sqrt(num): break
        if num%p==0: return False
    return True

def is_prime(num):
    if num==2: return True
	if num%2==0 or num<=0: return False
	for i in xrange(3,int(math.sqrt(num))+1,2):
		if num%i==0: return False
	return True

###############
#    Sort     #
###############
def BubbleSort(a):
    # method 1
    for n in xrange(len(a)-1,0,-1):
        for i in xrange(0,n):
            if a[i]>a[i+1]:a[i],a[i+1]=a[i+1],a[i]
    return a

def SelectionSort(a):
    # method 1
    '''
    for n in xrange(len(a),0,-1):
        k=0
        for i in xrange(1,n):
            if a[k]<a[i]:k=i
        a[k],a[n-1]=a[n-1],a[k]
    '''
    # method 2 reversed
    for n in xrange(0,len(a)-1):
        k=n
        for i in xrange(n,len(a)):
            if a[k]>a[i]:k=i
        a[k],a[n]=a[n],a[k]
    return a

def InsertionSort(a):
    # method 1
    '''
    for n in xrange(1,len(a)):
        t,i=a[n],n-1
        while a[i]>t and i>=0:a[i+1],i=a[i],i-1
        a[i+1]=t
    return a
    '''
    # method 2
    if len(a)==1:return a
    b=InsertionSort(a[1:])
    for i in xrange(0,len(b)):
        if a[0]<=b[i]:
            return b[:i]+[a[0]]+b[i:]
    return b+[a[0]]


def ShellSort(a):
    l,k=len(a),len(a)/2
    while k>0:
        for i in xrange(k,l):
            t,j=a[i],i-k
            while a[j]>t and j>=0:a[j+k],j=a[j],j-k
            a[j+k]=t
        k=k/2
    return a

def CombSort(a):
    k=l=len(a)
    while k>1:
        k=int(k/1.3)
        for i in xrange(l-k):
            if a[i]>a[i+k]: a[i],a[i+k]=a[i+k],a[i]
    return a

def HeapSort(a):
    def shift_down(arr,root,e):
        while 1:
            child=2*root+1
            if child>e:break
            if child+1<=e and arr[child]<arr[child+1]:child+=1
            if arr[root]<arr[child]:
                arr[root],arr[child],root=arr[child],arr[root],child
            else:break
    for r in xrange((len(a)-2)/2,-1,-1):shift_down(a,r,len(a)-1)
    for e in xrange(len(a)-1,0,-1):
        a[0],a[e]=a[e],a[0]
        shift_down(a,0,e-1)
    return a

def QuickSort(a,left,right):
    k=a[right]
    l,r=left,right
    if l==r:return
    while 1:
        while (a[l]>=k) and (r>l):l+=1
        while (a[r]<=k) and (r>l):r-=1
        a[l],a[r]=a[r],a[l]
        if l>=r:break
    a[r],a[right]=a[right],a[r]
    if left<l:QuickSort(a,left,l-1)
    QuickSort(a,r,right)
    return a

def MergeSort(a):
    def merge(a1,a2):
        a12=[]
        while a1 and a2:
            if a1[0]<a2[0]:a12.append(a1.pop(0))
            else:a12.append(a2.pop(0))
        return a12+a1+a2
    def m_sort(arr):
        if len(arr)==1:return arr
        m=len(arr)/2
        return merge(m_sort(arr[:m]),m_sort(arr[m:]))
    return m_sort(a)

def CountingSort(a):
    pass

def RadixSort(a):
    pass

def BucketSort(a,p,q):
    k,b=(q-p)/10,[[],[],[],[],[],[],[],[],[],[],[]]
    for i in a:
        t=i/k
        b[t].append(i)
        for j in xrange(len(b[t])-1,0,-1):
            if b[t][j]<b[t][j-1]: b[t][j],b[t][j-1]=b[t][j-1],b[t][j]
    return reduce(lambda x,y:x+y,b)

##################
#  Coin Problem  #
##################
def Coin(arr):
    target=arr[-1]
    ways=(target+1)*[0]
    ways[0]=1
    for i in arr:
        for j in xrange(i,target+1):
            ways[j]+=ways[j-i]
    return ways

##################
#    Dijkstra    #
##################
def neighbor(u):
    i,j=u
    v=[(i-1,j),(i,j+1),(i+1,j),(i,j-1)]
    return v

def dijkstra(graph,start,end):
    dist={}
    Q={}
    for g in graph: Q[g]=float('inf')
    Q[start]=graph[start]
    
    while 1:
        u=min(Q,key=Q.get)
        dist[u]=Q[u]
        del Q[u]
        if u==end: break

        for v in neighbor(u):
            if v in Q:
                tmp=dist[u]+graph[v]
                if Q[v]>tmp: Q[v]=tmp

    return dist

##################
# k-近邻算法(knn) #
##################
from numpy import *

def autoNorm(dataSet):
    mins=dataSet.min(axis=0)
    maxs=dataSet.max(axis=0)
    ranges=maxs-mins
    m=dataSet.shape[0]
    normDataSet=(dataSet-tile(mins,(m,1)))*1./tile(ranges,(m,1))
    return normDataSet,mins,ranges

def knn(inputX,dataSet,labels,k):
    m=dataSet.shape[0]
    diffM=tile(inputX,(m,1))-dataSet
    distances=(diffM**2).sum(axis=1)**0.5
    sortedIndex=distances.argsort(axis=0)
    result={}
    for i in range(k):
        label=labels[sortedIndex[i]]
        result[label]=result.get(label,0)+1
    return sorted(result.iteritems(),key=lambda x:x[1],reverse=True)[0][0]

def createDataSet():
    group=array([[9,400],[200,5],[100,77],[40,300]])
    labels=['A','B','C','A']
    return group,labels

def simpleTest():
    group,labels=createDataSet()
    print knn(array([199,4]),group,labels,1)

def dataClassTest():
    Ratio=0.1
    error=0.0
    dataM,dataL=file2matrix('data.txt')
    normMat,mins,ranges=autoNorm(dataM)

    testNum=int(normData.shape[0]*Ratio)
    for i in xrange(testNum):
        r=knn(normData[i],normData[testNum:],dataL[testNum:],3)
        if r!=dataL[i]: error+=1
    print 'Error Rate is',error/testNum


################
# Solve Sudoku #
################
'''
sudoku data structure:  nd_array((9,9))
'''
def easy_solve(sudoku):
    rest=0
    change=0
    for i in range(9):
        for j in range(9):
            if sudoku[i,j]==0:
                row=set(sudoku[i])
                col=set(sudoku[:,j])
                grid=set(sudoku[i/3*3:i/3*3+3,j/3*3:j/3*3+3].flatten())
                chooise=set(range(10)) - (row | col | grid)
                if len(chooise)==1:
                    sudoku[i,j]=list(chooise)[0]
                    change+=1
                else:
                    rest+=1
    if change==0 and rest>0:
        return 'Cant solve this one'
    elif rest==0:
        return sudoku
    else:
        return easy_solve(sudoku)

def check_solve(sudoku_solved):
    if all([len(set(i))==9 for i in sudoku.T]) and all([len(set(i))==9 for i in sudoku]) and int(sum(sudoku))==405:
        return True
    return False

def grid_chooise(sudoku):
    chooise_hash={}
    for i in range(9):
        for j in range(9):
            if sudoku[i,j]==0:
                row=set(sudoku[i])
                col=set(sudoku[:,j])
                grid=set(sudoku[i/3*3:i/3*3+3,j/3*3:j/3*3+3].flatten())
                chooise=list(set(range(10)) - (row | col | grid))
                chooise_hash[i,j]=chooise
    return sorted(chooise_hash.items(),lambda x,y:cmp(len(x[1]),len(y[1])))

'''
shortest code, but slow
data structure: string
'''
from sys import exit
def r(a):
    i=a.find('0')
    ~i or exit(a)
    [m in [(i-j)%9*(i/9^j/9)*(i/27^j/27|i%9/3^j%9/3) or a[j] for j in range(81)] or r(a[:i]+m+a[i+1:]) for m in '123456789']