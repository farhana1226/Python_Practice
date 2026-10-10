
#Hashing: Prestoring values into some datastructure like List/Dictionary/Set and the fetching it.

n=[5,9,9,2,4,4,5,5,6,4,3,1,1,2,6]
m=[45,4,58,111,53,20,9,1,2]
hash_={}
for i in range(len(m)):
    for j in range(len(n)):
        if [m[i]] in n[j]:
            hash_[hash_[m[i]]] += 1
        else:
            hash_[m[i]] = 1
print(hash_)
