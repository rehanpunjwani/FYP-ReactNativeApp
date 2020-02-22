from itertools import combinations, permutations

# b = input ('Books: ')
# L = input ('Librys: ')
# d = input ('Days: ')

scores = [1,2,3,6,5,4]
i = 0

fo = open('a_example.txt')
data = fo.readline()
data2 = data.split(' ')
#data2 = data2.rstrip('')
b=int(data2[0])
L=int(data2[1])
d = int(data2[2].rstrip())
print('Line ',data2)

scores=fo.readline()
scores = scores.split(' ')
print('Line ',scores)
scores = list(map(int, scores))
print(scores)

m = []
l=fo.readline()
l=l.split(' ')
l=list(map(int, l))


l_1 = fo.readline()
l_1=l_1.split(' ')
l_1=list(map(int, l_1))
m.append(l)
m.append(l_1)
print(m)


l_1 = [5,2,2]
b_l_1 = [0,1,2,3,4]
l_2 = [4,3,1]
b_l_2 = [3,2,5,0]
l = [[5,2,2],[4,3,1]]
b = [[0,1,2,3,4],[3,2,5,0]]
c_max =[]
for i in range(0,L):
    l1 = list(xrange(L))
    perm_l = list(permutations(l1))
    sum_l = []
    print(perm_l)
    for i in perm_l:
        print(i)
        c_max=[]
        for j in i:
            print(j)
            dl = d- l[j][1]
            r = l[j][2]
            temp = b[j]
            r1 = r + dl
            # print(r1)
            r2 = min(r1,len(temp))
            comb = list(combinations(temp,r2))
            sum_1 = [0]*len(comb)
            
            x=0
            for k in comb:
                sum_x = 0
                for u in k:
                    sum_x = sum_x + scores[u]    
                sum_1[x] = sum_x
                x+=1
            print('Vlue of Sum_1: ',sum_1)
            m=sum_1.index(max(sum_1))   
            print('Vlue of m: ',m)
            print('Vlue of Comb[0]: ',type(comb[m]))
            c_max.append(list(comb[m]))
            print('C_MAX',type(c_max))
        uni = set(c_max[len(c_max)-2]) | set(c_max[len(c_max)-1])    
        sum_s = 0
        for v in uni:
            sum_s =sum_s + scores[v]
        sum_l.append(sum_s) 

print(sum_1)
res= sum_l
print('Result: ',res)





