# create a list as below
output=[[1,2,3],[4,5,6],[7,5,3,2,3,[2,[3]]]]
a=[1,2,3]
b=[4,5,6]
c=[7,5,3,2,3]
d=[2]
e=[3]

# use these lists to create another list which will look like the list output in line 2
#output=[[1,2,3],[4,5,6],[7,5,3,2,3,[2,[3]]]]
a=[1,2,3]
b=[4,5,6]
c=[7,5,3,2,3]
d=[2]
e=[3]
list=[]
print(list)

# use append method to do this.
list.append(a)
list.append(b)
d.append(e)
c.append(d)
list.append(c)
