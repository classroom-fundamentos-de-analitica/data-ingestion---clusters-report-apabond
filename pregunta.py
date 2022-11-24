"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re

def ingest_data():
    
    dictionary = {}
    contador = 0
    df = pd.DataFrame()
    
    with open('./clusters_report.txt') as data:
        for line in data:
            line = re.sub(r"\s+", " ", line)
            if len(line)>1 and contador > 3:
                if line.split()[0].isnumeric() == True:
                    try: 
                        dictionary['principales_palabras_clave'] = ' '.join(dictionary['principales_palabras_clave'])
                        df = df.append(dictionary, ignore_index=True)
                        
                    except: pass
                    dictionary = {'cluster': int(line.split()[0]),
                                'cantidad_de_palabras_clave': int(line.split()[1]),
                                'porcentaje_de_palabras_clave': float(line.split()[2].replace(',','.')),
                                'principales_palabras_clave': line.split()[4:]}
                    
                else: 
                    dictonary['principales_palabras_clave'].append(' '.join(line.split()))
                    
            contador += 1
            
    dictionary['principales_palabras_clave'] = ' '.join(dictionary['principales_palabras_clave'])
    df = df.append(dictionary, ignore_index=True)
    df['principales_palabras_clave'] = df['principales_palabras_clave'].str.rstrip('\.')
    
    
    return df
