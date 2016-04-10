#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function

import sys

import requests
from bs4 import BeautifulSoup

import os
import psycopg2
from urllib.parse import urlparse

###### Conexión con la base de datos


conn = psycopg2.connect(
    database="d3o89blriss3f6",
    user="nccnbdlyxeplyg",
    password="LzPNgd2NfUZSDBxU3MbEkFiqYx",
    host="ec2-23-21-249-224.compute-1.amazonaws.com",
    port="5432"
)

cur = conn.cursor()
"""

cur.execute("SELECT * FROM Pelicula;")

a = cur.fetchone()
print(a)
"""

###### Scraping javascript
###### Inicio scraping

url = "http://800.cl/ResultadoPeliculas.asp?blnPeli=1&opPE=3"
# Realizamos la petición a la web
req = requests.get(url)

html = BeautifulSoup(req.text, "html.parser")
entradas = html.find_all('tr')
informacion = []
informacion.append([])
index = 0




for i,entrada in enumerate(entradas):
    entries = entrada.find_all('td')
    isLink = True

    for j,entry in enumerate(entries):
      data = entry.text
      if(data != ""):
          #print("TODA LA INFO: " + data)
          #print("Index: " + str(index))
          informacion[index].append(data.splitlines()[2]) #Agrega la cosa al principio de la lista
          #print("NOMBRE DE UNA PELICULA: " + data.splitlines()[2] + "\n")      #Estos son los nombres de las peliculas
          index = index + 1
          informacion.append([])
      alink =  entry.find('a')
      link = ""
      
      if alink != None and isLink:
        link = alink.get('href')
        isLink = False

        url_peli = "http://www.800.cl"+link
        req2 = requests.get(url_peli)
        html2 = BeautifulSoup(req2.text, "html.parser")
        html2 = BeautifulSoup(req2.text, "html.parser")

        results = html2.find_all('div', {'class':'CajaSombraCont'})
        time = html2.find('div',{'class':'FichaAntigua'}).getText().split(',')
        minutes = time[len(time)-1].split('.')
        duracion = minutes[0]
        if(duracion[0]!='('):
          numero_duracion = duracion.split('m')[0].split(' ')[1]
          #print(duracion)
          #print(numero_duracion)
          if numero_duracion!=None:
              informacion[index].append(numero_duracion)
          else:
              informacion[index].append(-1)
          #print('no info')
        else:
            informacion[index].append(-1)
        descripcion = html2.find('div', {'id':'TextoDetalladoLargo'})
        if descripcion !=None:
          #print(descripcion.getText().split('-')[0])
          informacion[index].append(descripcion.getText().split('-')[0])
        for result in results:
          #print("NOMBRE DE UN CINE: " + str(result.text)[5:].splitlines()[0])
          #print("DIRECCION DE UN CINE: " + str(result.text)[5:].splitlines()[1][:-6].lstrip())
          #print(str(result.text)[5:].split('\n\n\n\n\n\n\n\n\n\n\n'))
            asda = str(result.text)[5:].split('\n\n\n\n\n\n\n\n\n\n\n')
            for nn in asda:
               horarios = nn.splitlines()[2]
               #print(horarios)
               aux_count = 0
               doblada = False
               if horarios[0]=='D':
                   doblada = True
               digitos_sub = ""
               digitos_dob = ""
               while(aux_count < (len(horarios))):
                    if horarios[aux_count].isdigit():
                        if doblada:
                            digitos_dob=digitos_dob + horarios[aux_count]
                        else:
                            digitos_sub=digitos_sub + horarios[aux_count]
                    elif horarios[aux_count]=="s" or horarios[aux_count]=="S":
                        if ((horarios[aux_count]+horarios[aux_count+1])=="su") or ((horarios[aux_count]+horarios[aux_count+1])=="Su"):
                            doblada = False
                    aux_count+=1
               #print(digitos_dob)
               #print(digitos_sub)

               
               informacion[index].append({'sucursal': nn[0:].splitlines()[0], 'direccion':nn[5:].splitlines()[1][:-6].lstrip(), 'horario_sub':digitos_sub,'horario_dob':digitos_dob})
print("........................ O: \n")
for info in informacion:
    data = ""
    if(len(info)>0):
        """
        data = "('"+str(info[len(info)-1])+"',"+str(info[0])+",'"+str(info[1])+"', 'subtitulada');"
        query1="INSERT INTO Pelicula VALUES"+str(data)
        print(query1)
        cur.execute(query1)
        conn.commit()
        
        pos = 2
        while(pos<len(info)-1):
            data1 = "('"+str(info[len(info)-1])+"','"+str(info[pos]['horario_dob'])+"','"+str(info[pos]['sucursal'])+"', 'doblada');"
            data2 = "('"+str(info[len(info)-1])+"','"+str(info[pos]['horario_sub'])+"','"+str(info[pos]['sucursal'])+"', 'subtitulada');"
            query21="INSERT INTO Horarios VALUES"+str(data1)
            query22="INSERT INTO Horarios VALUES"+str(data2)
            print(query21)
            print(query22)
            pos+=1
            cur.execute(query21)
            cur.execute(query22)
        conn.commit()
    
        """
        pos = 2
        while(pos<len(info)-1):
            data = "('"+str(info[pos]['sucursal'])+"',' ','"+ str(info[pos]['direccion'])+"');"
            query ="INSERT INTO Sucursales VALUES"+str(data)
            cur.execute(query)
            pos+=1
        conn.commit()
            
    #for j,entry in enumerate(entries):
    #    data = entry.find('div')
    #    if data != None:
    #        data.getText()
        
    #    print(data)

    #link =  entrada.find('div',{'class':'contenido'}).find('a').get('href')
    #print(link)
    
    #req2 = requests.get(link)
    #html2=BeautifulSoup(req2.text, "html.parser")
    #entries = html2.find_all('div',{'class':'contenedor-info-galeria-pequena'})

    
    #for j,entry in enumerate(entries):
    #    data = entry.find('div')
    #    if data != None:
    #        data.getText()
        
    #    print(data)
        
    #render = Render(link)
    #print("Pase")
    #result = render.frame.toHtml()

    #print(result)

    #data_peli = request.find('div',{'class':'contenedor-info-galeria-pequena'}).find('p').getText()

    #l = entrada.find('div',{'class':'informacion'}).find('p',{'class':'titulo'})
    #h = entrada.find('div',{'class':'informacion'}).find('p',{'class':'texto'})
    #if l!=None and h!=None:
    #    lugar = l.getText()
    #    horarios = h.getText()
    #    print(lugar, horarios)
    #else:
    #    print("esta no tiene info para hoy")
    



cur.close()
conn.close()


