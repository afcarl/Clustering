from norm import *
from Silhouette import *
import pandas as pd

#------------------------------- IMPORT CSV + MODIFICHE DATASET -------------------------------#

#Importiamo il csv e lo trasformiamo in una matrice
data = pd.read_csv("candy_1.csv", sep = ",", header=None)
data = data.as_matrix()
#Creiamo la matrice x
X = data[:, 0:data.shape[1]-1]
#------------------------------------ NORMALIZAZZIONE FEATURE ---------------------------------#

#------------------------------------- ZSCORE -----------------------------------#


mu, sigma = muSigma(X)
X = zScore(X, mu, sigma)

#--------------------------------------------------------------------------------#


#------------------------------------ MINMAX ------------------------------------#

# min, diff, max = minmax(X)
# X = Min_Max(X, min, diff)

#--------------------------------------------------------------------------------#


#-------------------------------- FEATURE SCALING -------------------------------#

# min, diff, max = minmax(X)
# X = Feat_Scaling(X, max)

#--------------------------------------------------------------------------------#
silouette(X)

