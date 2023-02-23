#importar paquetes
from bs4 import BeautifulSoup
import urllib.request

url = 'https://www3.gobiernodecanarias.org/medusa/edublog/ieselrincon/'
ourURL=urllib.request.urlopen(url)

soup=BeautifulSoup(ourURL,'html.parser')

#ver dentro del soup de forma mas limpia
#print(soup.prettify())
#posts5225 y 5214
post = soup.find('article',id='post-5225') #sacamos el post
head = post.header
h = head.h1
ht = h.get_text()
print(ht) #sacamos del post la etiqueta head y de esta el h1 y lo mostramos
div = post.div #sacamos el div del articulo en cuestion

for x in div:
	#p = div.contents[x]
	style = div.style
	if(x == style):
		break;
	else:
		p = x.get_text()
		print(p)
		pass

"""
sacamos parrafos uno a uno
p1 = div.contents[1] #el primer parrafo del p(el texto son los impares)
p1t = p1.get_text()
print(p1t)
"""

"""
recorremos todo el articulo y sacamos todo, en verdad saca el primer p nada mas
activity=[] #lista vacia donde guardar las categorias
for i in soup.find_all('article', {'id':'post-5225'}):
	soup.div
	per_activity=i.find('p') #extraer la categoria
	print(per_activity)
	activity.append(per_activity)

len(activity)
"""
