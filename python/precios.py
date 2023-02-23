#importar paquetes
from bs4 import BeautifulSoup
import urllib3

http = urllib3.PoolManager()

url = 'https://www.mediamarkt.es/es/category/port%C3%A1tiles-gaming-158.html'
response = http.request('GET', url)
soup = BeautifulSoup(response.data, features= "html.parser")

#print(soup)

#StyledBox-sc-1vld6r2-0 ESTA CLASE ES DONDE ESTAN TODOS LOS ITEM |||| tyledListItem-sc-7l2z3t-0 Y ESTA CLASE LA TIENEN TODOS LOS PORTATILES
#item1 = soup.find('div',{"class":"StyledHeadingWrapper-cwyxax-0"}).get_text() #con esto ya sacamos el nombre
#div = soup.find('div',{"class":"StyledBox-sc-1vld6r2-0"})

entradas = soup.find_all('div',{'class':'StyledListItem-sc-7l2z3t-0'}) #div de todos los portatiles listados, dentro esta toda la info de cada portatil
#print(len(entradas))

precio2 = soup.find_all('div',{"class":"StyledUnbrandedPriceDisplayWrapper-sc-1n9i68m-0"}) #saca todos los precios
#ScreenreaderTextSpan-sc-11hj9ix-0  ||||| StyledUnbrandedPriceDisplayWrapper-sc-1n9i68m-0 ||||| BaseTypo-sc-1jga2g7-0<-- PRECIOS CLASES
for x in entradas:
    nombre = x.find('div',{"class":"StyledHeadingWrapper-cwyxax-0"}).get_text() #sacamos el nombre
    #precio = x.find_all('div',{"class":"StyledStrikePriceWrapper-jah2p3-5"}) #saca todos los precios
    precioOfertado = x.find('span',{"class":"ScreenreaderTextSpan-sc-11hj9ix-0"}).get_text() #saca todos los precios

    print(nombre ,':', precioOfertado ,"€")
    #print(precio)