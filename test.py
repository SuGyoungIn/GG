a=[1,0,1,1]
b=[0,1,0,0]

print(sum([a[i]*b[i] for i in range(len(a))])/((sum([a[i]**2 for i in range(len(a))])**0.5)*(sum([b[i]**2 for i in range(len(a))])**0.5)))