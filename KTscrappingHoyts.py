from bs4 import BeautifulSoup
import requests

url = "http://www.cinehoyts.cl"
# Realizamos la petición a la web

req = requests.get(url)
statusCode = req.status_code
print(statusCode)
if statusCode == 200:
    html = BeautifulSoup(req.text, "html.parser")
    #print(html.prettify().encode('UTF-8'))
    lista_pelis = html.find('div', {'class': 'sellos'})
    for pel in lista_pelis:
        titulo = pel.find('h1')
        print(titulo)
    print('------------')
    # for entrada in entradas:
    # print(str(entrada.text).encode('UTF-8'))
    #     print(type(entrada))
    #     tables = entrada.find_all('table')
    #     for table in tables:
    # print(str(table.text).encode('UTF-8'))
    #         links = table.find_all('a')
    #         for link in links:
    #             title = str(link.text).encode('UTF-8')
    #             if title and len(title) > 4:
    #                 print(str(link.text).encode('UTF-8'))
    #                 print('1111111111111111111111111SB')
    #         spans = table.find_all('span')
    #         for span in spans:
    #             print(str(span.text).encode('UTF-8'))
    #             print('----------------')
    # print(len(entradas))
