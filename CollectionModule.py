import collections

from numpy import equal


#counter:
#its output will be  a  dictionary :shows how many times each word  repeated
# c=collections.Counter("dfdsfdsewtytiouiuudfsd  ")
# print(c)


# list1=[23,45,56,78,78,5,8,1,23,45,45,78,78,89,89,45,89]
# d=collections.Counter(list1)

# counter most_common:those ones which repeated More
# brings a list
# list1=[23,45,56,78,78,5,8,1,23,45,45,78,78,89,89,45,89]
# d=collections.Counter(list1).most_common(3)
# print(d)




# dic1={}
# dic1["red"]=200
# print(dic1["red"])




# dic1={}
# dic1["red"]=200
# print(dic1["red"])



# dic1={"a":"Andy","b":"Sandy","c":"Rose"}
# print(dic1)


# dic2={"c":"Andy","a":"Sandy","b":"Rose"}
# print(dic2)


# Checks the contents equal Or Not:
# print(dic1==dic2)



#Orderdict: Arrange  two  dictionries :if the itmes should be the same
# dic1={"a":"Andy","b":"Sandy","c":"Rose"}
# dic1["a"]="Andy"
# dic1["c"]="Rose"
# dic1["b"]="Sandy"

# for k,v in dic1.items():
#     print(f"{k} :{v}")
# print()

# dic2={"c":"Andy","a":"Sandy","b":"Rose"}
# dic1["a"]="Andy"
# dic1["b"]="Sandy"
# dic1["c"]="Rose"

# for k,v in dic2.items():
#     print(f"{k} :{v}")
# print()
# print(dic1==dic2)

#ChainMap:

# d1={"Jack":100, " Donald":200,"Daniel":500}
# d2={"erd":10, " blue":20,"green":50}
# d3={100:True,300:False}

# d4=collections.ChainMap(d1,d2,d3)
# print(d4)


#NamedTuple: for creating a  new  Construction:a datatype like 
#dictionary 

# Person=collections.namedtuple("Person", "name age avg children")
# print(type(Person))
# person1=Person("Andy",20,20,["Nina","David"])
# person2=Person("Andy",10,50,["Rose","Philip"])

# print(person1)
# print(person2)
# print(person1.name)
# print(person1.age)
# print(person1.avg)
# print(person1.children)
# person1.children.append("sara")
# print(person1)




# Person=collections.namedtuple("Person", "name age avg children")
# person1=Person("Andy",20,20,["Nina","David"])
# person2=Person("Andy",10,50,["Rose","Philip"])

#to have  an Iterable :
#_make  helps to Open a  person into a list:
# for item in Person._make(person1):
#     print(item)


#or
# print(Person._make(person1))

#_asdict: make a dic 
# print(person1._asdict())


#field:gives  Tuples:drags its fields
# print(person1._fields)


#deque:to make a queue :make lists to be able to put at first or end or from end to first
# dq1=collections.deque([1,2,3,4])
# print(dq1)
# dq1.append(5)
# print(dq1)
# print()
# dq1.appendleft(6)
# print(dq1)

# dq1.pop() # take one from the last item
# print(dq1)
# dq1.popleft()
# print(dq1)


#UserList UserString:
# list1=[12,23,45,89,78]
# list1.remove(78)
# print(list1)



class MyList(collections.UserList):
    def remove(self):
        raise RuntimeError(" Delete Not Allowed")


# list1=MyList([12,23,45,89,78])
# print(list1)
# list1.remove(78)
# print(list1)

# list1=MyList([12,23,45,89,78])
# print(list1)
#     try:
#       print(x)
#     except:
#       print('An exception occurred')
#        print(x)
      
# list1.remove(78)
# print(list1)

# Add a  new function To ReMove a Letter or  sth
class MyString(collections.UserString):
     def remove(self,s):
         self.data=self.data.replace(s, "")
    
str1=MyString("Max")    
# str1="Maxim Jokar"    
str1.remove("ax")
print(str1)
























































