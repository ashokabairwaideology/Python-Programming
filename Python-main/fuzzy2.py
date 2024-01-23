class FzSets:

      def __init__(self):
            self.A = dict()
            self.B = dict()
            self.complement_A = dict()
            self.complement_B = dict()
            self.union_AB = dict()
            self.intersection_AB = dict()
            self.differenceAB = dict()
            self.differenceBA = dict()
            self.change_union = False
            self.change_intersection = False
            self.change_complement = False

      def __init__(self,A,nA,B,nB):
            self.A = A
            self.B = B
            self.Aname = nA
            self.Bname = nB
            self.complement_A = dict()
            self.complement_B = dict()
            self.union_AB = dict()
            self.intersection_AB = dict()
            self.differenceAB = dict()
            self.differenceBA = dict()
            self.change_union = False
            self.change_intersection = False
            self.change_complement = False


      def unionOp(self):
            if self.change_union:
                  print('Result of UNION operation :',self.union_AB)
            else:
	#unionSet = set(self.A.keys()).union(self.B.keys())
                  sa = set(self.A.keys())
                  sb = set(self.B.keys())
                  intersectionSet = set(self.A.keys()).intersection(self.B.keys())
                  for i in intersectionSet:
                        self.union_AB[i] = max(self.A[i],self.B[i])
                        for i in sa-intersectionSet:
                              self.union_AB[i] = self.A[i]
                              for i in sb-intersectionSet:
                                    self.union_AB[i] = self.B[i]
                                    print('Result of UNION operation :',self.union_AB)
	

def intersectionOp(self):
	if self.change_intersection:
		print('Result of INTERSECTION operation :\n\t\t',self.intersection_AB)
	else:
	
	#unionSet = set(self.A.keys()).union(self.B.keys())
	sa = set(self.A.keys())
	sb = set(self.B.keys())
	intersectionSet = set(self.A.keys()).intersection(self.B.keys())

	for i in intersectionSet:
		self.intersection_AB[i] = min(self.A[i],self.B[i])
	for i in sa-intersectionSet:
		self.intersection_AB[i] = 0.0
	for i in sb-intersectionSet:
		self.intersection_AB[i] = 0.0
	
	print('Result of INTERSECTION operation :\n\t\t',self.intersection_AB)
	self.change_intersection = True

def complementOp(self):
	if self.change_complement:
	print('Result of COMPLEMENT on ',self.Aname,' operation :',self.complement_A)
	print('Result of COMPLEMENT on ',self.Bname,' operation :',self.complement_B)
	else:
	
	for i in self.A:
		self.complement_A[i] = 1 - A[i]
	for i in self.B:
		self.complement_B[i] = 1 - B[i]

	print('Result of COMPLEMENT on ',self.Aname,' operation :',self.complement_A)
	print('Result of COMPLEMENT on ',self.Aname,' operation :',self.complement_B)

	self.change_complement = True

def __oneMinustwo(self,L,R):
	minus_d = dict()
	Rcomp = dict()
	for i in R:
	Rcomp[i] = 1 - R[i]
	sa = set(L.keys())
	sb = set(R.keys())
	intersectionSet = sa.intersection(sb) # min( A , complement(B) )

	# l - r OR a - b
	for i in intersectionSet:
	minus_d[i] = min(L[i],Rcomp[i])
	for i in sa-intersectionSet:
	minus_d[i] = 0.0
	for i in sb-intersectionSet:
	minus_d[i] = 0.0

	return minus_d
	
def AminusB(self):
	self.differenceAB = self.__oneMinustwo(self.A,self.B)
	print('Result of DIFFERENCE ',self.Aname,' | ',self.Bname,' operation :\n\t\t',self.differenceAB)

def BminusA(self):
	self.differenceBA = self.__oneMinustwo(self.B,self.A)
	print('Result of DIFFERENCE ',self.Bname,' | ',self.Aname,' operation :\n\t\t',self.differenceBA)

def change_Setz(self,A,B):
	self.A = A
	self.B = B

	print('\nSet ',self.Aname,' :',self.A)
	print('Set ',self.Bname,' :',self.B,end='')

	self.change_union = True
	self.change_intersection = True
	self.change_complement = True
	print('\t\t\t Cache Reset')

def displaySets(self):
	print('\nSet ',self.Aname,' :',self.A)
	print('Set ',self.Bname,' :' ,self.B)
