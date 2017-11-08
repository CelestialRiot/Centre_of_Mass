import matplotlib.pyplot as plt

plt.ylabel('Weight')
plt.xlabel('Distance')
inpt = input('An Array:\n')
distance = []
weight = []
top = []
bottom = []
ALL = []
average = 0

z = 0
for i in range(0,len(inpt)):
	weight.append(float(inpt[i]))
	distance.append(z)
	z += 1

if len(weight)%2 == 0:
	for i in range(0,len(distance),2):
		p1,p2,p3 = weight[i]*distance[i] , weight[i+1]*distance[i+1] , weight[i]+weight[i+1]
		ALL.append((p1+p2)/p3)
	for i in range(0,len(ALL)):
		average += ALL[i]
	average /= len(ALL)
else:
	for i in range(0,len(distance)-1,2):
		p1,p2,p3 = weight[i]*distance[i] , weight[i+1]*distance[i+1] , weight[i]+weight[i+1]
		top.append(p1+p2)
		bottom.append(p3)
	for i in range(0,len(top)):
		extra_top = 0
		extra_bottom = 0
		extra_top += top[i]
		extra_bottom += bottom[i]
	average += ((extra_top + weight[-1]*distance[-1])/2)/((extra_bottom + weight[-1])/2)
	average /= len(top)

print(average)
plt.axvline(x=average)
plt.plot(distance,weight)
plt.show()