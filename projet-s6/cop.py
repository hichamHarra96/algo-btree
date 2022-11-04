                                    
        elif(feuille==self.racine):
            newRacine=Noeud()
            newRacine.feuille=False
            self.racine=newRacine
            feuille.cles.append(e)
            feuille.cles.sort()
           
            n1=Noeud()
            n2=Noeud()
            n1.feuille=feuille.feuille
            n1.feuille=feuille.feuille
            n1.parent=newRacine
            n2.parent=newRacine
            ind=len(feuille.fils)//2
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
    
        
    