import numpy as np
import pandas as pd
import os

gnss = pd.read_csv('data/gnss_sismique_s.csv')
gnss['geophone'] = gnss['Name'].map(lambda e: int(e.split('.')[-1]))
gnss = gnss.set_index('geophone')
gnss = gnss.sort_index()

files_pointage = [f for f in os.listdir('data/pointage') if f.endswith('txt')]

dx = 4
offset = 2
ng = len(gnss['A'].values)
ns = len(files_pointage)
x_geophs = np.arange(ng)*dx # géophones espacés de 4m
x_shots = np.arange(ns)*dx + offset # sources espacées de 4m entre 2 géophones
x = np.concatenate((x_geophs, x_shots))
x.sort()
y_geophs = gnss['A'].values
y = np.interp(x, x_geophs, y_geophs) # interpolation de l'altitude des capteurs (mesurées) pour estimer celle des sources
y_shots = y[0:-1:2]