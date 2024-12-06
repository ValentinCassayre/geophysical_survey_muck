import numpy as np
import pandas as pd
import os

gnss = pd.read_csv('data/gnss_sismique_p.csv')
gnss['geophone'] = gnss['Name'].map(lambda e: int(e.split('.')[-1]))
gnss = gnss.set_index('geophone')
gnss = gnss.sort_index()

df = pd.read_csv('data/pointage.csv')

x_geophs = df['REC_X'].unique()
x_geophs.sort()
x_shots = df['SRC_X'].unique()
x_shots.sort()
ng = len(df['REC_X'].unique())
ns = len(df['SRC_X'].unique())
dx = 1.5
offset = .75

profil = df[['REC_X', 'REC_ELEV']].drop_duplicates(subset=['REC_X']).values # positions x, z des géophones
profil = profil[profil[:, 0].argsort()]

x = np.concatenate((x_geophs, x_shots))
x.sort()
y_geophs = profil[:, 1]

y = np.interp(x, x_geophs, y_geophs) # interpolation de l'altitude des capteurs (mesurées) pour estimer celle des sources
xy = np.array((x, y)).T # positions de tous les capteurs et receveurs