from Arbre import*
import unittest
class Tests(unittest.TestCase):
    def setUp(self):
        self.n =Noeud()
        self.a=Arbre(4,2)
        self.a.racine = self.n
        self.a.insertion(self.a.racine, 10)
        self.a.insertion(self.a.racine, 20)
        self.a.insertion(self.a.racine, 30)
        self.a.insertion(self.a.racine, 12)
        self.a.insertion(self.a.racine, 25)
        self.a.insertion(self.a.racine, 14)
        self.a.insertion(self.a.racine, 40)
        self.a.insertion(self.a.racine, 35)
        self.a.insertion(self.a.racine, 13)
        self.a.insertion(self.a.racine, 32)
        self.a.insertion(self.a.racine, 28)




    def test1(self):
       self.assertTrue(self.a.recherche(self.a.racine,30))
       self.assertTrue(self.a.recherche(self.a.racine, 12))
       self.assertTrue(self.a.recherche(self.a.racine, 28))
       self.assertTrue(self.a.recherche(self.a.racine, 35))
    def test2(self):
        self.assertFalse(self.a.recherche(self.a.racine, 26))
        self.assertFalse(self.a.recherche(self.a.racine, 80))
    def testInsertion(self):

        self.assertEqual(self.a.racine.cles,[30])
        self.assertEqual(self.a.racine.fils[0].cles, [13,20])
        self.assertEqual(self.a.racine.fils[1].cles, [35])
        self.assertEqual(self.a.racine.fils[0].fils[0].cles, [10,12])
        self.assertEqual(self.a.racine.fils[0].fils[1].cles, [14])
        self.assertEqual(self.a.racine.fils[0].fils[2].cles, [25,28])
        self.assertEqual(self.a.racine.fils[1].fils[0].cles, [32])
        self.assertEqual(self.a.racine.fils[1].fils[1].cles, [40])
if __name__ == "__main__":
    test = Tests()
    test.setUp()
    test.test1()
    test.test2()
    test.testInsertion()