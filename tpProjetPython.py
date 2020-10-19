# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 15:36:05 2020

@author: braud
"""

import pandas as df

fichier = df.read_csv('D:/Utilisateur/Bureau/projetPython_data/20180110_RES_FichesInstallations.csv', delimiter=";", usecols=[0, 2, 4], dtype={0:str, 2:str, 4:str })

print(fichier.head())