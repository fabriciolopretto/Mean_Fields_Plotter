"""
Este archivo es el CONTROLADOR de la aplicacion.

Se importan funciones y clases desde "modelo.py" y "vista.py".
Se ejecutan en orden funciones de estos modulos y objetos
de diferentes clases.
"""

# Se importan las librerias necesarias.
from model import lectura, calculos
from view import graficado_campo_500, graficado_campo_Adv_850, graficado_campo_Conv_850, graficado_campo_Esp_1000_500

# Se declaran los objetos.
if __name__ == "__main__":    
    longitude, latitude, time, level, z, q, t, u, v = lectura()
    z_med_mod, q_med_mod, t_med_mod, u_med_mod, v_med_mod, i_med_mod, adv_q_med_850, conv_q_med_850, esp_1000_500 = calculos(longitude, latitude, time, level, z, q, t, u, v)
    graficado_campo_500(longitude, latitude, z_med_mod, q_med_mod, t_med_mod, u_med_mod, v_med_mod, i_med_mod, adv_q_med_850, conv_q_med_850, esp_1000_500)
    graficado_campo_Adv_850(longitude, latitude, z_med_mod, q_med_mod, t_med_mod, u_med_mod, v_med_mod, i_med_mod, adv_q_med_850, conv_q_med_850, esp_1000_500)
    graficado_campo_Conv_850(longitude, latitude, z_med_mod, q_med_mod, t_med_mod, u_med_mod, v_med_mod, i_med_mod, adv_q_med_850, conv_q_med_850, esp_1000_500)
    graficado_campo_Esp_1000_500(longitude, latitude, z_med_mod, q_med_mod, t_med_mod, u_med_mod, v_med_mod, i_med_mod, adv_q_med_850, conv_q_med_850, esp_1000_500)
