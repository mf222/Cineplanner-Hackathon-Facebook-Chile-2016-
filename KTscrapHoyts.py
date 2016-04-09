from bs4 import BeautifulSoup
import requests

lista_peliculas = []
url = 'http://www.cinehoyts.cl/cartelera/'

req = requests.get(url)
statusCode = req.status_code
if statusCode == 200:
    html = BeautifulSoup(req.text, "html.parser")

    print(html.prettify().encode('UTF-8'))
    nombres = html.find('section', {'class':'listaCarteleraHorario'})
    #print(str(nombres.text).encode('UTF-8'))
    complejos = nombres.find_all('div')
    #print(complejos)
    for complejo in complejos:
        articulos = complejo.find_all('articles')
        for artic in articulos:
            div = artic.find('div')
            header = div.find('header')
            casi = header.find('h3')
            #print(len(casi))
            #print(casi.text.encode('ISO-8859-1'))
    # print('--------------------------')
