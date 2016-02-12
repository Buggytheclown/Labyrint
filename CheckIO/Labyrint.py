lab = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
       [1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
       [1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
       [1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
       [1, 0, 0, 0, 1, 1, 1, 0, 1, 1],
       [1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
       [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
       [1, 0, 0, 1, 1, 1, 1, 0, 1, 1],
       [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


class At():

    def __init__(self, i, j, end_path):
        self.i=i
        self.j=j
        self.stuck=[]
        self.ncroad=[]  #croad in use
        self.end_path=end_path

    def croad (self, i, j):
        return {(i, j+1):lab[i] [j+1],
                (i+1, j):lab[i+1][j],
                (i, j-1):lab[i] [j-1],
                (i-1, j):lab[i-1][j]}

    def step (self, i, j, k):
        lab[i][j] = k
        self.i = i
        self.j = j

    def watch (self): #for testing
        for j in lab:
            for i in j:
                if i!=-1:
                    print ('  {}'.format(i), end='')
                else:
                    print (' {}'.format(i), end='')
            print(end='\n')
        print()


    def path(self): #path till cross-road, croad in stuck
        print('!!!PATH!!! on', self.i, self.j)
        while list(self.croad(self.i,self.j).values()).count(0) == 1:
            for i in self.croad(self.i,self.j).keys():
                if self.croad(self.i,self.j)[i]==0:
                    print ('step -1', i)   ###
                    self.step(*i,-1)
                    break

        if list(self.croad(self.i,self.j).values()).count(0) > 1: #reached croad
            self.stuck.append((self.i, self.j))

        elif list(self.croad(self.i,self.j).values()).count(1) == 3: #reached dend
            if (self.i, self.j) == (self.end_path):                  #reached END
                    print('Hyyyray END!!!')
                    lab[self.i][self.j]='!!!'
                    self.watch()
            else:
                self.dend()
        self.watch()


    def dend(self):
        print('!!!DEND!!! on', self.i, self.j)
        while list(self.croad(self.i, self.j).values()).count(1) ==3:
            lab[self.i][self.j] = 1
            print ('1step +1', self.i, self.j)   ###
            for i in self.croad(self.i, self.j).keys():
                if self.croad(self.i, self.j)[i] == -1:
                    at.step(*i, -1)
                    print ('2step -1', self.i, self.j)
                    break
        self.watch()

at=At(1, 1, (8, 8))
lab[1][1]=-1
at.path()
while at.stuck:
    at.ncroad=at.stuck.pop()
    while list(at.croad(*at.ncroad).values()).count(0) != 0:  #checked all ways from atm crossroad
        at.i, at.j = at.ncroad
        for i in at.croad(at.i,at.j).keys():
            if at.croad(at.i,at.j)[i] == 0:
                at.step(*i, -1)
                at.path()
                at.i, at.j = at.ncroad
'''
#################
class AtUPD(At):
    def __init__(self, i, j, end_path):
        At.__init__(self, i, j, end_path)
        self.walked=[]

    def stepUPD (self, i, j):
        ab=(i-self.i, j-self.j)
        nswe = ('N', 'S', 'W', 'E')
        direction = (-1, 0), (1,0), (0,-1),(0, 1)
        Dnswe = dict(zip(direction, nswe))
        self.walked.append(Dnswe[ab])
        self.i=i
        self.j=j


atu = AtUPD(1,1, (8,8))

while list(at.croad(atu.i,atu.j).values()).count(-1) == 1:  #добавить в AtUPD,
            for i in atu.croad(atu.i,atu.j).keys():
                if atu.croad(atu.i,atu.j)[i]==-1:
                    atu.stepUPD(*i) # mark way, crossraods
                    break

if list(self.croad(self.i,self.j).values()).count(0) > 1: #reached croad
            self.stuck.append((self.i, self.j))
'''
