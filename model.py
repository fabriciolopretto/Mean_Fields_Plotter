# -*- coding: utf-8 -*-
"""
Lee el archivo de Datos y arma las variables a graficar.
"""

# Se importan las librerias necesarias
import pandas as pd
import netCDF4 as nc
import numpy as np
from netCDF4 import Dataset
import os

# Se definen variables globales
global longitude, latitude, time, level, z, q, t, u, v



def diferencia_paralelo_lon(lon_ini, lon_fin, dlon, lat):
    """
    Calcula la longitud del arco ssobre la superficie
    terrete, a lo largo de un paralelo.
    """
    # Radio de la Tierra en metros
    radio_tierra = 6371000

    # Convertir longitudes de grados a radianes
    lon_ini_rad = np.radians(lon_ini)
    lon_fin_rad = np.radians(lon_fin)

    # Convertir la latitud de grados a radianes
    lat_rad = np.radians(lat)

    # Calcular la diferencia de longitud en radianes
    diff_lon_rad = np.abs(lon_fin_rad - lon_ini_rad)

    # Calcular la longitud de arco a lo largo del paralelo
    # La longitud de arco varía con la latitud
    longitud_arco = radio_tierra * np.cos(lat_rad) * diff_lon_rad

    return longitud_arco

def lectura():

  # Se define la ruta al archivo de datos
  ruta = os.path.dirname((os.path.abspath(__file__)))
  ruta_datos = ruta + '/datos_enero.nc'

  # Lectura de archivos NetCDF
  ds = nc.Dataset(ruta_datos, 'r')

  # Lectura de variables de Geo-referenciacion
  longitude = ds.variables['longitude'][:]
  latitude = ds.variables['latitude'][:]
  level = ds.variables['level'][:]

  # Lectura de variable Temporal
  time = ds.variables['time'][:]

  # Lectura de variables meteorologicas
  z = ds.variables['z'][:]
  q = ds.variables['q'][:]
  t = ds.variables['t'][:]
  u = ds.variables['u'][:]
  v = ds.variables['v'][:]

  # Cierra los archivos NetCDF
  ds.close()

  return longitude, latitude, time, level, z, q, t, u, v


def calculos(longitude, latitude, time, level, z, q, t, u, v):
  """
  Calcula el campo medio de las variables dadas,
  además define la intensidad del viento media
  a partir de las variables provistas, como también
  la advección y convergencia de humedad específica
  en 850 hPa y los espesores de la capa 1000 500 hPa.
  """
  # Calculo de campos medios
  z_med = (1/(len(time)))*np.sum(z, axis=0)
  q_med = (1/(len(time)))*np.sum(q, axis=0)
  t_med = (1/(len(time)))*np.sum(t, axis=0)
  u_med = (1/(len(time)))*np.sum(u, axis=0)
  v_med = (1/(len(time)))*np.sum(v, axis=0)
  i_med = np.sqrt(u_med**2+v_med**2)

  # Modificacion campos medios
  z_med_mod = 0.1*z_med   # [mgp]
  q_med_mod = 0.001*q_med   # [g/Kg]
  t_med_mod = t_med - 273 # [°C]
  u_med_mod = 1.94*u_med  # [kt]
  v_med_mod = 1.94*v_med  # [kt]
  i_med_mod = 1.94*i_med  # [kt]

  # Calculo de Adveccion de humedad especifica
  adv_q_med_850 = np.zeros((len(latitude),len(longitude)))  # [g/Kg*s]

  delta_y = 27819.45 # [m]
  dlon = 0.25        # [° grados]

  for i in range(len(latitude)-1):
    lat = latitude[i]
    for j in range(len(longitude)-1):
      lon_ini = longitude[j-1]
      lon_fin = longitude[j+1]
      delta_x = diferencia_paralelo_lon(lon_ini, lon_fin, dlon, lat)
      if i!=0 and j!=0:
        adv_q_med_850[i][j] = -u_med[1][i][j]*((q_med_mod[1][i][j+1]-q_med_mod[1][i][j-1])/(delta_x))-v_med[1][i][j]*((q_med_mod[1][i-1][j]-q_med_mod[1][i+1][j])/(delta_y))

  adv_q_med_850 = (10**10)*adv_q_med_850

  # Calculo de Convergencia de humedad especifica
  conv_q_med_850 = np.zeros((len(latitude),len(longitude)))  # [g/Kg*s]

  delta_y = 27819.45 # [m]
  dlon = 0.25        # [° grados]

  for i in range(len(latitude)-1):
    lat = latitude[i]
    for j in range(len(longitude)-1):
      lon_ini = longitude[j-1]
      lon_fin = longitude[j+1]
      delta_x = diferencia_paralelo_lon(lon_ini, lon_fin, dlon, lat)
      if i!=0 and j!=0:
        conv_q_med_850[i][j] = ((q_med_mod[1][i][j+1]*u_med[1][i][j+1]-q_med_mod[1][i][j-1]*u_med[1][i][j-1])/(delta_x))+((q_med_mod[1][i-1][j]*v_med[1][i-1][j]-q_med_mod[1][i+1][j]*v_med[1][i+1][j])/(delta_y))

  conv_q_med_850 = (10**9)*conv_q_med_850

  # Calculo de Espesores de la capa 1000/500 hPa
  esp_1000_500 = np.zeros((len(latitude),len(longitude)))  # [m]

  R = 287.05 # [m**2/s**2*K]
  g = 9.8        # [m/s**2]
  C = np.log(2)

  for i in range(len(latitude)-1):
    for j in range(len(longitude)-1):
      esp_1000_500[i][j] = 0.5*(t_med[0][i][j]+t_med[2][i][j])*R*C*(1/g)
  
  # Devuelve las variables medias
  return z_med_mod, q_med_mod, t_med_mod, u_med_mod, v_med_mod, i_med_mod, adv_q_med_850, conv_q_med_850, esp_1000_500
