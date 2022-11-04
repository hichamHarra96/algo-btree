from Noeud import *
from dicho import *
from tree_printer import*
from random import randint
class Arbre:
    def __init__ (self,u,l):
        self.size=None
        self.U=u
        self.L=l
        self.racine=None
    """   
    def recherche(self,noeud,e):
        res=False
        if noeud.feuille:
            res=recherchDicho(e,noeud.cles)
        elif recherchDicho(e,noeud.cles):
            res= True
        else:
             for f in noeud.fils:
                res=self.recherche(f,e)
                    
        return res
    """
    
    
    
    
    
    def recherche(self,noeud,e):
        """
        recherche element e dans noeud
        :param noeud: le noeud ou on cherche (si dans l arbre noeud est racine)
        :param e: element a chercher
        :return: Bool True si e est dans l arbre False sinon 
        """
        if noeud.feuille:
            res=recherchDicho(e,noeud.cles)
        elif recherchDicho(e,noeud.cles):
            res= True
        else:
            i=0
            ind=-1
            while(i< len(noeud.cles) and ind==-1):
                if(e<noeud.cles[i]):
                    ind=i
                i+=1
            if (ind == -1):
                ind =len(noeud.cles)
            res=self.recherche(noeud.fils[ind],e)
              
        return res
    
    
    def recherche_feuille(self,noeud,e):
        """
        recherche la feuille ou on doit inserer e l arbre de racine noeud
        :param noeud: le noeud ou on cherche (si dans l arbre noeud est racine)
        :param e: elemnt a inserer
        :return: Noeud ou on, doit inserer  
        """
        res=noeud
        if noeud.feuille:
            res=noeud
        elif recherchDicho(e,noeud.cles):
            res= noeud
        else:
            i=0
            ind=-1
            while(i< len(noeud.cles) and ind==-1):
                if(e<noeud.cles[i]):
                    ind=i
                i+=1
            if (ind == -1):
                ind =len(noeud.cles)
            
            if(noeud.fils[ind]!=None):
                res=self.recherche_feuille(noeud.fils[ind],e)
        return res
    def insertion(self,noeud,e):
        """
        insere e dans l arbre de racine noeud
        :param noeud: racine de l arbre 
        :param e: elemnt a inserer
        """
        feuille=self.recherche_feuille(noeud,e)
        self.insertion_dans_feuille(feuille,e)
        
    def insertion_dans_feuille(self,noeud,e):
        """
        insere e dans noeud (initialement la feuille)
        :param noeud: le noeud ou on insere
        :param e: elemnt a inserer
        """
        feuille=noeud
        if(len(feuille.cles)<self.U-1): ## place dans la feuille
            feuille.cles.append(e)
            feuille.cles.sort()                                      
        elif(feuille==self.racine):
            newRacine=Noeud()
            newRacine.feuille=False
            self.racine=newRacine
            feuille.cles.append(e)
            feuille.cles.sort()
            
            
            ind=len(feuille.cles)//2
            elt=feuille.cles[ind]
            print(feuille.cles)
            feuille.cles.remove(elt)
            print(feuille.cles)
            print('a')
            
            n1=Noeud()
            n2=Noeud()
            n1.feuille=feuille.feuille
            n1.feuille=feuille.feuille
            n1.parent=newRacine
            n2.parent=newRacine
            ind=len(feuille.fils)//2
            print("a252")
            print(len(feuille.fils))
            n1.fils=feuille.fils[0:ind+1]
            n2.fils=feuille.fils[ind+1:len(feuille.fils)]
            for f in n1.fils:
                f.parent=n1
            for f in n2.fils:
                f.parent=n2
            ind=len(feuille.cles)//2 
            n1.cles=feuille.cles[0:ind+1] 
            n2.cles=feuille.cles[ind+1:len(feuille.cles)]
            newRacine.fils.append(n1)
            newRacine.fils.append(n2)
            newRacine.cles.append(elt) 
            newRacine.cles.sort()
            print(n1.cles)
            print(n2.cles)
        
        else:
            feuille.cles.append(e)
            feuille.cles.sort()
            
            ind=len(feuille.cles)//2
            elt=feuille.cles[ind]                
            feuille.cles.remove(elt)
            #ind=len(feuille.cles)//2 
            n1=Noeud()
            n2=Noeud()
            n1.feuille=feuille.feuille
            n1.feuille=feuille.feuille
            n1.parent=feuille.parent
            n2.parent=feuille.parent
            
            if(len(feuille.fils)>0):
                n1.fils=feuille.fils[0:ind+1]
                n2.fils=feuille.fils[ind+1:len(feuille.fils)]
            for f in n1.fils:
                f.parent=n1
            for f in n2.fils:
                f.parent=n2
            
            n1.cles=feuille.cles[0:ind]
            n2.cles=feuille.cles[ind:len(feuille.cles)]
            
            index_feuille=feuille.parent.fils.index(feuille)
            feuille.parent.fils[index_feuille]=n1
            feuille.parent.fils.insert(index_feuille+1,n2)
            self.insertion_dans_feuille(feuille.parent,elt)
            
    

    

if __name__ == "__main__":
    n =Noeud()
    a=Arbre(4,2)
    #n.cles=[]
   
    
    a.racine=n
    #res= a.recherche(a.noeud,11)
    #print(res)
    
    #res1=a.recherche_feuille(a.noeud,4)
    #print(res1.cles)
    #print("aaaa")
   # a.ins(a.noeud,3)
   # print(len(n4.fils))
    a.insertion(a.racine,10)
    a.insertion(a.racine,20)
    a.insertion(a.racine,30)
    a.insertion(a.racine,12)
    a.insertion(a.racine,25)
    a.insertion(a.racine,14)
    a.insertion(a.racine,40)
    a.insertion(a.racine,35)
    a.insertion(a.racine,13)
    a.insertion(a.racine,32)
    a.insertion(a.racine,28)
    a.insertion(a.racine,29)
    
    #for i in range(0,500):
        #a.insertion(a.racine,10000)
    
    
    #a.ins(a.noeud,18)
    res= a.recherche(a.racine,103)
    print(res)
    res1=a.recherche_feuille(a.racine,26)
    print(res1.cles)
    
        
    