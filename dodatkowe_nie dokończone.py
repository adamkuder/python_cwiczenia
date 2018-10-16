# IS17, AiP, Projekt 1
#### Imię i nazwisko: Adam Kuder
# Współpraca - Brak 
# Kopia tego pliku - Wykład i reszte sam
# Czas pracy nad zadaniem: 2godz nad ascend_gradient 3 godz nad divide_and_command razem 5 godz
# pozniej juz mi sie nie chcialo dodawwac komentarzy po angielsku 

class Peak(object):
    """find peak 2d"""
    
    def __init__(self, L):
        self._L = L[:]
        self._n = len(self._L)
        self._m = len(self._L[0])

    def get_dim(self):
        """zwraca rozmiary tablicy"""
        return (self._n, self._m)

    def get_val(self, loc):
        """zwraca wartosc na pozycji loc"""
        return self._L[loc[0]][loc[1]]

    def next_element(self, loc):
        """zwraca lokalizacje kolejnego elem"""
        if loc[1] < self._m - 1:
            return loc[0], loc[1] + 1
        else:
            if loc[0] < self._n - 1:
                return loc[0] + 1, 0
            else:
                return -1
        
    def exhaustive(self, start=(0,0)):
        """przeszukiwanie wyczerpujace"""
        loc = start[:]

        found = False
        while not found:
            left = top = right = bottom = None
            pos = self.get_val(loc)
            if loc[0] == 0:
                top = pos
            if loc[0] == self._n - 1:
                bottom = pos
            if loc[1] == 0:
                left = pos
            if loc[1] == self._m - 1:
                right = pos
            
            if left == None:
                left = self.get_val((loc[0], loc[1]-1))
            if right == None:
                right = self.get_val((loc[0], loc[1]+1))
            if top == None:
                top = self.get_val((loc[0]-1, loc[1]))
            if bottom == None:
                bottom = self.get_val((loc[0]+1, loc[1]))

            #print pos, ":", left, top, right, bottom
            if pos >= left and pos >= top and pos >= right and pos >= bottom:
                found = True
            else:
                buf = self.next_element(loc)
                if buf == -1:
                    found = True
                else:
                    loc = buf[:]
        return loc
    
    #NIE WIDZIE ROZNICY POMIIEDZY Z TYM Z WYKLADU KOPIUJ WKLEJ :( 
    def brute_force(self, start=(0,0)):
        loc = start[:]
        pos = self.get_val(loc)
        found = False
        while not found:
            left = top = right = bottom = None
            if loc[0] == 0:
                top = pos
            if loc[0] == self._n - 1:
                bottom = pos
            if loc[1] == 0:
                left = pos
            if loc[1] == self._m - 1:
                right = pos
            if left == None:
                left = self.get_val((loc[0], loc[1]-1))
            if right == None:
                right = self.get_val((loc[0], loc[1]+1))
            if top == None:
                top = self.get_val((loc[0]-1, loc[1]))
            if bottom == None:
                bottom = self.get_val((loc[0]+1, loc[1]))
            if pos >= left and pos >= top and pos >= right and pos >= bottom:
                found = True
            else:
                buf = self.next_element(loc)
                if buf == -1:
                    found = True
                else:
                    loc = buf[:]
        return loc
    
    def ascend_gradient(self, start=(1,1)):
        loc= (self._n//2,self._m//2)
        found = False
        while not found:
            pos = self.get_val(loc)

            #to the end off loop, condition
            finishdirectionleft=False
            finishdirectionright=False
            finishdirectiontop=False
            finishdirectionbottom=False
            
            """'4 while loop' LEFT-->TOP-->RIGHT-->BOTTOM"""
           
            """if pos less element chceck, replace"""
            """if not end loop"""
            while not finishdirectionleft:
                if loc[1]-1==-1: # if out of range
                    finishdirectionleft=True
                elif pos < self.get_val((loc[0], loc[1]-1)):
                    loc=(loc[0], loc[1]-1)
                    pos = self.get_val(loc)
                else:
                    finishdirectionleft=True
                    
                    
            while not finishdirectiontop:
                if loc[0]+1==-1: # if out of range
                    finishdirectiontop=True
                elif pos < self.get_val((loc[0]-1, loc[1])):
                    loc=(loc[0]-1, loc[1])
                    pos = self.get_val(loc)
                else:
                    finishdirectiontop=True
                    

            while not finishdirectionright:
                if loc[1]+1>=len(self._L[0]): # if out of range
                    finishdirectionright=True
                elif pos < self.get_val((loc[0], loc[1]+1)):
                    loc=(loc[0], loc[1]+1)
                    pos = self.get_val(loc)
                else:
                    finishdirectionright=True


                    

            while not finishdirectionbottom:
                if loc[0]+1>=len(self._L): # if out of range
                    finishdirectionbottom=True
                elif pos < self.get_val((loc[0]+1, loc[1])): 
                    loc=(loc[0]+1, loc[1])
                    pos = self.get_val(loc)
                else:
                    finishdirectionbottom=True
            
            
            #final check, no need chceck down becouse we chceck last in loop... copy paste :)             
            left = top = right = None
            if loc[0] == 0:
                top = pos
            if loc[1] == 0:
                left = pos
            if loc[1] == self._m - 1:
                right = pos
            
            if left == None:
                left = self.get_val((loc[0], loc[1]-1))
            if right == None:
                right = self.get_val((loc[0], loc[1]+1))
            if top == None:
                top = self.get_val((loc[0]-1, loc[1]))

            #print pos, ":", left, top, right, bottom
            if pos >= left and pos >= top and pos >= right:
                found = True
        
        return loc
    
    
    #FUNCTION MAX NEED IN DIVIDE AND COMMAND
    def index_max_element_row(self,loc):
        k=0
        z=0
        a=self.get_val((loc[0],loc[1]))
        end=False 
        while not end:
            if loc[0]+z+1>=len(self._L):
                end=True
            elif a<= self.get_val((loc[0]+z+1,loc[1])):
                a=self.get_val((loc[0]+z+1,loc[1]))
                k=z+1
            z+=1
        return k
    
    def divide_and_command(self):
        a=False
        b=False
        restrictleft=1
        restrictright=0
        loc= (0,self._m//2)
        k = self.index_max_element_row(loc)
        #print(k)
        finish=False
        while not finish:
            loc=(k,loc[1])
            #print(loc)
            pos= self.get_val((loc[0],loc[1]))
            #print (pos)
            if loc[1]<len(self._L[0])-1:#jesli nie przekracza maxa
                if pos < self.get_val((loc[0],loc[1]+1)):# sprawdzaj czy element jest mniejszy od prawego
                    restrictright=loc[1]+2
                    #print("rr=",restrictright)
                    row=restrictright
                else:
                    a=True
            else: #zabezpieczenie jak jest przy prawej stronie
                a=True
            if loc[1]-1>=-1:#jesli nie przekaracza minimum
                if  pos < self.get_val((loc[0],loc[1]-1)):# sprawdzaj czy element jest mniejszy od lewego
                    restrictleft=loc[1]-1
                    #print("rl=",restrictleft)
                    row=restrictleft
                else:
                    b=True
            else: #zabezpieczenie jak jest przy lewej stronie
                b=True
            #if restrictright>restrictleft:
            #    return loc
            if a==True and b==True:
                return loc
            #print("heh")
            #if restrictright>0:
            #    row=restrictright#//2+self._m//2-1
            #if restrictleft>=0:
            #    print("daje")
            #    row=restrictleft
            if restrictleft==0:#jak jestśmy przy lewej krawedzi
                loc=(0,restrictleft)
                k=self.index_max_element_row(loc)
                return (loc[0]+k,loc[1])
            if restrictright>=len(self._L[0]):
                loc=(0,restrictright-1)
                k=self.index_max_element_row(loc)
                return (loc[0]+k,loc[1])
            loc=(0,row)
            k=self.index_max_element_row(loc)
            a=False
            b=False
        return loc




    def greedy_ascent(self, start=(0,0)):
        """..."""
        pass

    def divide_and_conquer(self, scol="mid"):
        """..."""
        pass


A = [[1,   2,  3,  4],
     [14, 15, 16,  5],
     [13, 18, 17,  6],
     [12,  9,  3,  7],
     [11, 10,  9,  8]]

p = Peak(A)
#print("loc (2, 1)", p.exhaustive())

B = [[1,2,3,4,5],
     [5,6,7,8,9]]
C = [[2,3,1],
    [9,5,5],
    [5,9,5],
    [2,1,1],
    [1,3,3],
    [2,2,123121],
    [4,55,8],
    [7,5,4],
    [8,9,9],
    [4,85,96],
    [11,8,98],
    [1486,850,123]]

pB = Peak(B)
pC = Peak(C)
print(p.ascend_gradient())
print(pB.ascend_gradient())
print(pC.ascend_gradient())

print(p.divide_and_command())
print(pB.divide_and_command())
print(pC.divide_and_command())
