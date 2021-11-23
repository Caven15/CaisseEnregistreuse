#!/bin/python3
#print("<=---------------------------=>")
print("Lancement...")
print("Version 1.0 ")
#---------------------------------------------------------------------------------------
# Definition des Variables et affectation de valeur de départ :
#<=---------------------------=>

Somme = 0
NB_user = 0
SommeAchat = 0
NombreClient = 0
ArticleTotal = 0
NombreArticle = 0
TotalArticle_J = 0
SommeJournaliere = 0

Caisse = True
Confirmation = True

Cloture = ""
Anulation = "y"
NouvelleSession = "y"

#---------------------------------------------------------------------------------------
# initialisation de la liste de prix et affectations de valeur :
#<=---------------------------=>

ListePrix =[None ,0.95, 4.99, 5.81,17.52, 6.49,10.25, 1.19, 2.36, 14.05, 16, 2.99, 6.75, 6.45, 78.12, 4.55, 4.95, 6.96, 1.70, 6.96,  5.9]

#---------------------------------------------------------------------------------------
# Definition des fonctions :
#<=---------------------------=>
# Fonction qui ajouter un article au panier du compte client

def AjoutPanier (Total,Liste,Val_User) :                        
  TailleListe = len(Liste)
  i = 0
  while (i < Val_User) :
    i += 1
    if (Val_User == i) :
      Total = Total + Liste[i]
  return float(Total) 
  
#<=---------------------------=>
# Fonction qui nous préviens ou permet d'acceder a la fermeture du compte journalier

def AvertissementCloture(Val,Reponse) :                         
  print("<=---------------------------=>")
  Reponse = input("Attention vous aller fermer le chiffre d'affaire journalier voulez vous vraimment continuer ? (y) pour oui / (n) pour non")
  if (Reponse == "y") :
    Val = False
  else :
    Val = True
  return bool(Val)

#<=---------------------------=>
# fonction pour le calcul de la monnaie (possible amélioration calcul tva)

def CalculMonnaie(Prix,Recu) :                                  
  Recu = float(Recu) - float(Prix)
  return float(Recu)

#<=---------------------------=>
# procédure qui détermine si la somme donner par le client est suffisante

def CalculNegatif(recu,A_payer) :                              
  while (float(recu) < float(A_payer)) :
    print("<=---------------------------=>")
    recu = float(input("Le montant donner est inférieur au montant d'achat veuillez entrer une somme suffisante !"))

#<=---------------------------=>
# procédure qui donne les statistique de la journée pour le magasin

def Statistiques(Total_J,Nombre_J,Total_ArticleJ) :             
  print("<=---------------------------=>")
  print("--- => Cloture Journalière <= ---")
  print("Nous avons accueillis : " , Nombre_J , " Client(s)")
  print("le magasin a gagner : " , Total_J , " €")
  print("Le magasin a écouler : " , TotalArticle_J , " article(s)")

#<=---------------------------=>
# fonction qui vérifie si la variables est de type str

def Verificationstr(NB_user) :                                  
  # not permet d'inverser lle retour de valeur de la fonction .isdigit()
  while ( not NB_user.isdigit()) :                  
    print("<=---------------------------=>")
    NB_user = input("Erreur, les caractère alphanumérique sont invalide. Veuillez entrer un nombre valide !")
  return str(NB_user)
  
#<=---------------------------=>
# fonction qui vérifie si la variables est de type float                                      

def Verificationfloat(NB_user) : # pour la férification des valeur entré j'ai ici diviser la fonction en 3 fonction pour appliquer chaque cas en fonction de mon besoin
  while (float(NB_user) - round(float(NB_user)) != 0) :
    print("<=---------------------------=>")
    NB_user = input("Erreur, les nombre a virgules sont incorrect. Veuillez entrer un nombre valide !")
  return int(NB_user)
  
#<=---------------------------=>
# fonction qui vérifie si la variables est comprise dans la valeur du tableau

def VerificationListe(VAl_Liste,NB_user) :                      
  TailleTableau = len(VAl_Liste)
  i = 0
  while (int(NB_user) >= int(TailleTableau)) :
    print("<=---------------------------=>")
    NB_user = input("Erreur, article introuvable... Veuillez saisir un Numéro d'article")
  return int(NB_user)
  
#<=---------------------------=>
# fonction qui vérifie si les options de réponse attendue par le programme sont bien valide

def VerificationReponse(Reponse) :                              
  while (Reponse != "y" and Reponse != "n") :
    print("<=---------------------------=>")
    Reponse = input("Erreur, Veuillez encoder une réponse valide ( y => oui / n => non )")
  return str(Reponse)

#---------------------------------------------------------------------------------------
# programme principale :
#<=---------------------------=>

while (str(NouvelleSession) == "y") :                           # boucle qui lance une nouvelle session tant que l'utilisateur le demande                                                
  print("<=---------------------------=>")
  print("--- => Logiciel Caisse Magasin <= ---")
  
  while (bool(Caisse) == True) :                                # boucle qui modifie le nombre de client tant que l'utilisateur le demande
    NombreClient = NombreClient + 1
    print("<=---------------------------=>")
    print("Compte client nr : " , NombreClient)
    Confirmation = True
    
    while (bool(Confirmation) == True) :                        # boucle qui encode un nouvel article tant que l'utilisateur le demande                         
      print("<=---------------------------=>")
      NewArticle = str(input("Voulez vous scanner un nouvelle article ?  ( y => oui / n => non )"))
      NewArticle = VerificationReponse(NewArticle)
      
      if (str(NewArticle) == "y") :                             # si la réponse est oui => procédure d'encodage
        Confirmation = True
        NBuser = input("Veuillez entrer un numéro d'article ")
        NBuser = Verificationstr(NBuser)
        NBuser = Verificationfloat(NBuser)
        NBuser = VerificationListe(ListePrix,NBuser)
        Somme = Somme + AjoutPanier(SommeAchat,ListePrix,NBuser)
        NombreArticle = NombreArticle + 1
        ArticleTotal = ArticleTotal + NombreArticle
        print("<=---------------------------=>")
        print("Montant actuel : " , Somme , " €")
        print("article actuel : " , NombreArticle , " unité(s)")
        Anulation = str(input("Voulez vous valider l'article ?  ( y => oui / n => non )"))
        Anulation = VerificationReponse(Anulation)
        
        if (Anulation == "y") :                                 # validation du choix de l'utilisateur
          print("<=---------------------------=>")
          print("article " , NombreArticle , " valider")
          
        else :                                                  # si l'utilisateur c'est tromper il a la posibilité de déduire l'article du panier
          print("<=---------------------------=>")
          Somme = Somme - AjoutPanier(SommeAchat,ListePrix,NBuser)
          NombreArticle = NombreArticle - 1
          print("Le dernier article a bien été retirer")
          
      else :                                                    # si l'utilisateur n'a plus d'article a encodé il est redirigé vers le processus de payement
        Confirmation = False
        
    if (int(Somme) > 0) :                                       # si la somme est suffisante on procède au payement
      print("<=---------------------------=>")
      SommeJournaliere = Somme + SommeJournaliere
      print("Fin de compte client nr : " , NombreClient)
      print("Total a payer : " , Somme , " €")
      print("Article total : " , NombreArticle)
      ArgentClient = input("Veuillez encoder le montant donner par le client")
      ArgentClient = Verificationstr(ArgentClient)
      CalculNegatif(ArgentClient,Somme)
      CalculMonnaie(ArgentClient,Somme)
      Reste = CalculMonnaie(Somme,ArgentClient)
      print("<=---------------------------=>")
      print("Vous devez rendre : " , Reste , " €")
      Cloture = str(input("passer au client suivant ?  ( y => oui / n => non )"))
      Cloture = VerificationReponse(Cloture)
      NombreArticle = 0
      Somme = 0
      
      if (str(Cloture) == "y") :                                # demande a l'utilisateur si il veux passer au client suivant
        Confirmation = True
      else :                                                    # sinon redirection vers la cloture de la recette de la journée
        Confirmation = False
        Caisse = AvertissementCloture(Caisse,Cloture)           
        
    else :                                                    
      NombreClient = NombreClient - 1
      Caisse = AvertissementCloture(Caisse,Cloture)            
      
  Statistiques(SommeJournaliere,NombreClient,ArticleTotal)      # calcul des statistique de la journée en cours
  print("<=---------------------------=>")
  NouvelleSession = str(input("Voulez vous démarer une nouvelle journée ?  ( y => oui / n => non )"))   # proposition de démarage de nouvelle session
  NouvelleSession = VerificationReponse(NouvelleSession)
      
  if (str(NouvelleSession) == "y") :                            # si l'utilisateur le veux il peut relancer une nouvelle session
    Caisse = True
    Confirmation = True
print("<=---------------------------=>")                        # fin de programme 
print("--- => Fin de Programme <= ---")
print("          Au revoir !         ")
print("<=---------------------------=>")
