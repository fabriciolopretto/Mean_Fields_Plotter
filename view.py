# -*- coding: utf-8 -*-
"""
Este script permite graficar los campos medios
de altura geopotencial e intensidad de viento en 500 hPa.
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.colors import TwoSlopeNorm, LinearSegmentedColormap
from matplotlib.colors import ListedColormap
import os

# Se define la ruta al archivo de datos
ruta = os.path.dirname((os.path.abspath(__file__)))
ruta_figuras = ruta + '\Figuras'

# Latitudes y longitudes deseadas
lat_min, lat_max = -60, -20
lon_min, lon_max = -80, -50

def graficado_campo_500(longitude, latitude, z_med_mod, q_med_mod, t_med_mod, u_med_mod, v_med_mod, i_med_mod, adv_q_med_850, conv_q_med_850, esp_1000_500):
  """
  Genera y guarda el campo de altura geopotencial e intensidad de viento en 500 hPa.
  """
  # Crear el mapa usando Basemap
  fig, ax = plt.subplots(figsize=(12, 8))
  m = Basemap(projection='merc', llcrnrlat=lat_min, urcrnrlat=lat_max,
              llcrnrlon=lon_min, urcrnrlon=lon_max, resolution='l', ax=ax) # resolution = [low: l, intermediate: i, high: h, full: f]

  # Crear una malla de latitudes y longitudes
  lon_grid, lat_grid = np.meshgrid(longitude, latitude)
  x, y = m(lon_grid, lat_grid)

  # Graficar los datos de temperatura en el mapa
  contour = m.contourf(x, y, i_med_mod[0,:,:], levels=np.linspace(30, 80, 6), cmap='Greens')

  # Agregar la barra de color
  cbar = m.colorbar(contour, location='right', pad='10%')
  cbar.set_label('Intensidad de Viento [kt]', fontsize=10)

  # Agregar características del mapa
  m.drawcoastlines()
  m.drawcountries()
  m.drawstates()
  m.drawparallels(np.arange(lat_min, lat_max, 10), labels=[1,0,0,0])
  m.drawmeridians(np.arange(lon_min, lon_max, 10), labels=[0,0,0,1])

  # Agregar las isolíneas de z_med_mod
  contour = m.contour(x, y, z_med_mod[0,:,:], colors='black')

  # Añadir etiquetas
  plt.clabel(contour, inline=True, fontsize=8)

  # Mostrar el gráfico
  plt.title('Campo de Alt. Geop. 500 hPa [lineas] \n e Int. de Viento [somb.] Medias', fontsize=11)
  plt.savefig(ruta_figuras + '\Alt_Geop_500_Int_V.png', bbox_inches='tight')

  
def graficado_campo_Adv_850(longitude, latitude, z_med_mod, q_med_mod, t_med_mod, u_med_mod, v_med_mod, i_med_mod, adv_q_med_850, conv_q_med_850, esp_1000_500):
  """
  Genera y guarda el campo de altura geopotencial y Advección
  de humedad específica en 850 hPa.
  """
  # Crear el mapa usando Basemap
  fig, ax = plt.subplots(figsize=(12, 8))
  m = Basemap(projection='merc', llcrnrlat=lat_min, urcrnrlat=lat_max,
              llcrnrlon=lon_min, urcrnrlon=lon_max, resolution='l', ax=ax) # resolution = [low: l, intermediate: i, high: h, full: f]

  # Crear una malla de latitudes y longitudes
  lon_grid, lat_grid = np.meshgrid(longitude, latitude)
  x, y = m(lon_grid, lat_grid)

  # Define tus intervalos y colores correspondientes
  colores = ['lightskyblue', 'lightblue', 'white', 'white', 'red', 'brown']  # Colores para cada intervalo

  levels = [-1.2, -0.8, -0.4, 0, 0.4, 0.8, 1.2]

  # Crea el cmap personalizado
  cmap = ListedColormap(colores)

  # Graficar los datos de temperatura en el mapa
  contour = m.contourf(x, y, adv_q_med_850, cmap=cmap, levels=levels)

  # Agregar la barra de color
  cbar = m.colorbar(contour, location='right', pad='10%')
  cbar.set_label('Advección de humedad específica en 850 hPa [g/kg*s] 1e-10', fontsize=10)

  # Agregar características del mapa
  m.drawcoastlines()
  m.drawcountries()
  m.drawstates()
  m.drawparallels(np.arange(lat_min, lat_max, 10), labels=[1,0,0,0])
  m.drawmeridians(np.arange(lon_min, lon_max, 10), labels=[0,0,0,1])

  # Agregar las isolíneas de z_med_mod
  contour = m.contour(x, y, z_med_mod[1,:,:], colors='black')

  # Añadir etiquetas
  plt.clabel(contour, inline=True, fontsize=8)

  # Mostrar el gráfico
  plt.title('Campo de Alt. Geop. 850 hPa [lineas] \n y Adv. hum. esp. [somb.] Medias', fontsize=11)
  plt.savefig(ruta_figuras + '\Alt_Geop_850_Adv_q.png', bbox_inches='tight')


def graficado_campo_Conv_850(longitude, latitude, z_med_mod, q_med_mod, t_med_mod, u_med_mod, v_med_mod, i_med_mod, adv_q_med_850, conv_q_med_850, esp_1000_500):
  """
  Genera y guarda el campo de altura geopotencial y Convergencia
  de humedad específica en 850 hPa.
  """
  # Crear el mapa usando Basemap
  fig, ax = plt.subplots(figsize=(12, 8))
  m = Basemap(projection='merc', llcrnrlat=lat_min, urcrnrlat=lat_max,
              llcrnrlon=lon_min, urcrnrlon=lon_max, resolution='l', ax=ax) # resolution = [low: l, intermediate: i, high: h, full: f]

  # Crear una malla de latitudes y longitudes
  lon_grid, lat_grid = np.meshgrid(longitude, latitude)
  x, y = m(lon_grid, lat_grid)

  # Define tus intervalos y colores correspondientes
  colores = ['orangered', 'orange', 'white', 'white', 'springgreen', 'seagreen']  # Colores para cada intervalo

  levels = [-0.9, -0.6, -0.3, 0, 0.3, 0.6, 0.9]

  # Crea el cmap personalizado
  cmap = ListedColormap(colores)

  # Graficar los datos de temperatura en el mapa
  contour = m.contourf(x, y, conv_q_med_850, cmap=cmap, levels=levels)

  # Agregar la barra de color
  cbar = m.colorbar(contour, location='right', pad='10%')
  cbar.set_label('Convergencia de humedad específica en 850 hPa [g/kg*s] 1e-9', fontsize=10)

  # Agregar características del mapa
  m.drawcoastlines()
  m.drawcountries()
  m.drawstates()
  m.drawparallels(np.arange(lat_min, lat_max, 10), labels=[1,0,0,0])
  m.drawmeridians(np.arange(lon_min, lon_max, 10), labels=[0,0,0,1])

  # Agregar las isolíneas de z_med_mod
  contour = m.contour(x, y, z_med_mod[1,:,:], colors='black')

  # Añadir etiquetas
  plt.clabel(contour, inline=True, fontsize=8)

  # Mostrar el gráfico
  plt.title('Campo de Alt. Geop. 850 hPa [lineas] \n y Conv. hum. esp. [somb.] Medias', fontsize=11)
  plt.savefig(ruta_figuras + '\Alt_Geop_850_Conv_q.png', bbox_inches='tight')


def graficado_campo_Esp_1000_500(longitude, latitude, z_med_mod, q_med_mod, t_med_mod, u_med_mod, v_med_mod, i_med_mod, adv_q_med_850, conv_q_med_850, esp_1000_500):
  """
  Genera y guarda el campo de Altura geopotencial en 1000 hPa
  y el campo de espesores de la capa 1000/500 hPa.
  """
  # Crear el mapa usando Basemap
  fig, ax = plt.subplots(figsize=(12, 8))
  m = Basemap(projection='merc', llcrnrlat=lat_min+0.5, urcrnrlat=lat_max-0.5,
              llcrnrlon=lon_min+0.5, urcrnrlon=lon_max-0.5, resolution='l', ax=ax) # resolution = [low: l, intermediate: i, high: h, full: f]

  # Crear una malla de latitudes y longitudes
  lon_grid, lat_grid = np.meshgrid(longitude, latitude)
  x, y = m(lon_grid, lat_grid)

  # Agregar características del mapa
  m.drawcoastlines()
  m.drawcountries()
  m.drawstates()
  m.drawparallels(np.arange(lat_min, lat_max, 10), labels=[1,0,0,0])
  m.drawmeridians(np.arange(lon_min, lon_max, 10), labels=[0,0,0,1])

  # Agregar las isolíneas de z_med_mod
  contour = m.contour(x, y, z_med_mod[2,:,:], colors='black')

  # Agregar etiquetas a las líneas de contorno
  plt.clabel(contour, inline=True, fontsize=8)

  # Añadir etiquetas
  plt.clabel(contour, inline=True, fontsize=8)

  # Agregar las isolíneas de esp_1000_500 con niveles específicos
  intervalos_esp = np.arange(5220, 5761, 60)
  contour = m.contour(x, y, esp_1000_500, levels=intervalos_esp, colors='skyblue', linestyles='dotted')

  # Graficar contorno para las isolíneas específicas en rojo
  contour_red = m.contour(x, y, esp_1000_500, levels=[5700], colors='red')

  # Agregar etiquetas a las líneas de contorno rojos
  plt.clabel(contour_red, inline=True, fontsize=8, fmt='%1.0f')

  # Graficar contorno para las isolíneas específicas en verde
  contour_green = m.contour(x, y, esp_1000_500, levels=[5580], colors='green')

  # Agregar etiquetas a las líneas de contorno rojos
  plt.clabel(contour_green, inline=True, fontsize=8, fmt='%1.0f')

  # Graficar contorno para las isolíneas específicas en azul
  contour_blue = m.contour(x, y, esp_1000_500, levels=[5400], colors='blue')

  # Agregar etiquetas a las líneas de contorno azules
  plt.clabel(contour_blue, inline=True, fontsize=8, fmt='%1.0f')

  # Graficar contorno para las isolíneas específicas en amarillo
  contour_yellow = m.contour(x, y, esp_1000_500, levels=[5280], colors='yellow')

  # Agregar etiquetas a las líneas de contorno amarillas
  plt.clabel(contour_yellow, inline=True, fontsize=8, fmt='%1.0f')

  # Mostrar el gráfico
  plt.title('Campo de Alt. Geop. 1000 hPa [lineas] \n y Esp. 1000/500 hPa [color lineas] Medias', fontsize=11)
  plt.savefig(ruta_figuras + '\Alt_Geop_1000_Esp_1000500.png', bbox_inches='tight')
