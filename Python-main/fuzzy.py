def union(A,B):

      u = {}

      for i in A:

            if i in B:
                  u[i]=max(A[i],B[i])
            else:
                  u[i]=A[i]
      for i in B:
            if i not in A:
                  u[i]=B[i]
      return(u)
      
def intersection(A,B):
      inter = {}
      for i in A:
            if i in B:
                  inter[i]=min(A[i],B[i])
            else:
                  inter[i]=A[i]
      for i in B:
            if i not in A:
                  inter[i]=B[i]
      return(inter)
def difference(A,B):
      comp_b = complement(B)
      diff = intersection(A,comp_b) #A-B = A intersection B' return(diff)

def complement(A):
      comp_a={}
      for i in A:
            comp_a[i] = round((1-A[i]),1)
      return(comp_a)



def morgan(A,B):
      #case 1
      p = intersection(A,B)
      p_bar = complement(p)
      comp_a = complement(A)

#p -> A intersection B
      #p_bar -> (A intersection B)bar
      comp_b = complement(B)
      q = union(comp_a,comp_b)
      if(p_bar == q):
            print("(A n B)' = ",p_bar)
            print(" A' u B' = ",q)
            print("Thus, (A n B)' = A' u B'")
            print("Law 1 proved")



#case 2
      p = union(A,B)
      p_bar = complement(p)
      comp_a = complement(A)
      comp_b = complement(B)
      q = intersection(comp_a,comp_b)
      if(p_bar == q):
            print("\n(A u B)' = ",p_bar)
            print(" A' n B' = ",q)
            print("Thus, (A u B)' = A' n B'")
            print("Law 2 proved")
      print("\nHence De Morgan's Law is proved")

#p -> A intersection B

#p_bar -> (A intersection B)bar
a=[]
n=input("Enter the elements of set A = ")
a=n.split(',')
print("Enter the membership value for each element")
mem_a = {}
for i in a:
      print(i,"= ",end='')
      mem_a[i] = float(input())
print("A = ",mem_a)
b=[]
n=input("\nEnter the elements of set B = ")
b=n.split(',')
print("Enter the membership value for each element")
mem_b = {}
for i in b:
      print(i,"= ",end='')
      mem_b[i] = float(input())

print("B = ",mem_b)
print("\n1.Union\n2.Intersection\n3.Difference\n4.Complement\n5.De Morgan's Law\n6.Exit")

n=int(input("Enter your choice = "))

while(n < 6):

      if(n == 1):
            u = union(mem_a,mem_b)
            print("Union = ",u)
      
      elif(n == 2):
            inter = intersection(mem_a,mem_b)
            print("Intersection = ",inter)
      elif(n == 3):
            diff = difference(mem_a,mem_b)
            print("Difference = ",diff)
      elif(n == 4):
            comp_a = complement(mem_a)
            comp_b = complement(mem_b)
            print("A's complement = ",comp_a)
            print("B's complement = ",comp_b)
      else:
            morgan(mem_a,mem_b)
      print("\n1.Union\n2.Intersection\n3.Difference\n4.Complement\n5.De Morgan's Law\n6.Exit")
      n=int(input("Enter your choice = "))