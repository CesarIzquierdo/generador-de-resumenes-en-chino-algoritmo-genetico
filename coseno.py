import numpy as np
import random 
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from stop_words import get_stop_words
from tkinter import *
import tkinter.filedialog
from tkinter.simpledialog import *
from tkinter import *

stop_words = get_stop_words('spanish')

#se abre el documento para sacar la cantidad de 
# oraciones
i = 0
nombre_de_la_lista = []
with open("./Noticias/Noticias segmentadas/contenido/noticia 3 segmentada.txt" , encoding="utf8") as archivo:
    for linea in archivo:       
    	#incrementa y cuenta el numero de oraciones que son los genes
    	##el i va a servir para crear la n cantidad de oraciones pero en documentos 
        i= i+1
lista= [i]


nombre_de_la_lista = [i]


array = np.random.randint(i, size=(i, i)) 
print(array) 
j = 0
with open("./Noticias/Noticias segmentadas/contenido/noticia 3 segmentada.txt" , encoding="utf8") as archivo:
    for linea in archivo:
        nombre_de_la_lista[j] =  linea       	    


######
#cantidad de genes
######


def ruleta(data):

	rango1 = []
	rango2 = []
	rango3 = []
	rango4 = []
	n2 = 0
	for n2 in nombre_de_la_lista:
		nombre_de_la_lista[0]

	seleccion_azar2 = random.choice(data)


	return seleccion_azar2



def elitista(data):
	temp = 0
	for n in data:
		if n > temp:
			temp = n

	return temp
poblacion_inicial = [] 

nombre_de_la_lista = [i]
vector = array.copy()


flujo = 0
for x in range(0, len(array)):	
	print ("##### Ruleta: #####  \n")
	poblacion_inicial.append(random.randint(0, i))  
 
	for n in range(0,len(array)):
		
		p1 =  ruleta(poblacion_inicial)
		p2 =  ruleta(poblacion_inicial)
		p3 =  ruleta(poblacion_inicial)
		p4 =  ruleta(poblacion_inicial)
		p5 =  ruleta(poblacion_inicial)
		p6 =  ruleta(poblacion_inicial)
		p7 =  ruleta(poblacion_inicial)
		p8 =  ruleta(poblacion_inicial)

		if p1 == p2:
			p2 =  ruleta(poblacion_inicial)

		if p1 == p3:
			p3 =  ruleta(poblacion_inicial)

		if p2 == p1:
			p1 =  ruleta(poblacion_inicial)

		if p2 == p3:
			p3 =  ruleta(poblacion_inicial)

		if p3 == p2:
			p2 =  ruleta(poblacion_inicial)

		if p3 == p1:
			p1 =  ruleta(poblacion_inicial)

		if array[x][n] == p1 or array[x][n] == p2 or array[x][n] == p3 or array[x][n] == p4 or array[x][n] == p5 or array[x][n] == p6 or array[x][n] == p7 or array[x][n] == p8:
			vector[x][n]=1
		else:
			if array[x][n] != p1 or array[x][n] != p2 or array[x][n] != p3 or array[x][n] != p4 or array[x][n] != p5 or array[x][n] != p6 or array[x][n] != p7 or array[x][n] != p8:
				vector[x][n]=0


		print("El elemento elegido por ruleta es", p1, p2, p3, p4, p5, p6, p7, p8)	


		yi2 = n
		s2 = str(yi2).zfill(5)

		f = open ('comparacion/holamundo'+s2+'.txt','w'  , encoding="utf8")
		i = 0
		nombre_de_la_lista = []
		with open("./Noticias/Noticias segmentadas/contenido/noticia 3 segmentada.txt" , encoding="utf8") as archivo:
		    for linea in archivo:       
		  
		       	if i == p1 or  i == p2  or i == p3 or i == p4 or i == p5 or i == p6 or i == p7 or i == p8:
		       		f.write(linea)       		
			

		       	i= i+1

		f.close()
	

datos2 = [i]
k =0
with open("comparacion/holamundo00001.txt" , encoding="utf8") as archivo2:
	    for linea2 in archivo2:       	  	          	
	    	datos2[k] = linea2


print(vector)

#for x in range(0, len(array)):	
	#contador de documentos
	
		
#	for n in range(0,len(array)):
#		yi2 = x
#		s2 = str(yi2).zfill(5)
#		f = open ('comparacion/holamundo'+s2+'.txt','w'  , encoding="utf8")
#		g = 0
#		nombre_de_la_lista = []
#		with open("./Noticias/Noticias segmentadas/contenido/noticia 3 segmentada.txt" , encoding="utf8") as archivo: 
#			for linea in archivo:		
##				if linea == ' ':
#					print("hola")
#
#				if vector[x][n] == 1:
#					f.write(linea)
#					
##					print(f)
##				else:
#					print("no")	
#					f.close()
#				g = g + 1		
								
	    	
#		f.close()
#		flujo = flujo + 1


#print("ii",g)
#print("flujo",flujo)
#datos2 = [g]
#k =0
#with open("comparacion/holamundo00001.txt" , encoding="utf8") as archivo2:
#	    for linea2 in archivo2:       	  	          	
#	    	datos2[k] = linea2
	       

vectorizer = CountVectorizer()

#print("datos2",datos2)

print("datos de prueba\n" )

x=vectorizer.fit_transform(datos2)

print("\n")
print("\n")
print("\n")

print("get feature names")
print(vectorizer.get_feature_names)

print("vocabulario")
print(vectorizer.vocabulary_)


tfid = TfidfVectorizer().fit_transform(datos2)
print(tfid)

print(cosine_similarity(tfid[0:10], tfid).flatten())
""" Elitismo """

""" Cruza multi punto aleatorio """

""" mutacion """



"""

filename=""
labele=""

def xz():
    filename=tkinter.filedialog.askopenfilename()
    if filename != '':
         lb.config(text='El archivo que seleccionó es'+filename)
         labele = filename
         print(labele)
    else:
         lb.config(text='No seleccionaste ningún archivo')

def ruleta(event):
      s = 'El valor de la ruleta' + str(var.get())
      lb.config(text=s)

def eli(event):
      s = 'El valor elitimo' + str(var.get())
      lb.config(text=s)

def cruza(event):
      s = 'El valor de la cruza multi punto aleatorio' + str(var.get())
      lb.config(text=s)


def mutacion(event):
      s = 'El valor de la inversion' + str(var.get())
      lb.config(text=s)

root = Tk()
root.geometry('800x800')
root.title('Generador automatico de resumenes en chino ')

lb = Label(root,text='')
lb.pack()

btn=Button(root,text='Aparece el cuadro de diálogo de selección de archivos',command=xz)
btn.pack()

varRul=DoubleVar()
sclRul = Scale(root,orient=HORIZONTAL,length=400,from_=1.0,to=25.0,label='Arrastre el control de la ruleta',tickinterval=1,resolution=1.00,variable=varRul)
sclRul.bind('<ButtonRelease-1>',ruleta)
sclRul.pack()

varEli=DoubleVar()
sclEli = Scale(root,orient=HORIZONTAL,length=400,from_=1.0,to=25.0,label='Arrastre el control del elitismo',tickinterval=1,resolution=1.00,variable=varEli)
sclEli.bind('<ButtonRelease-1>',eli)
sclEli.pack()

varCru=DoubleVar()
sclCru = Scale(root,orient=HORIZONTAL,length=400,from_=1.0,to=25.0,label='Arrastre el control de la cruza',tickinterval=1,resolution=1.00,variable=varCru)
sclCru.bind('<ButtonRelease-1>',cruza)
sclCru.pack()

varMuta=DoubleVar()
sclMuta = Scale(root,orient=HORIZONTAL,length=400,from_=1.0,to=25.0,label='Arrastre el control de la mutacion',tickinterval=1,resolution=1.00,variable=varMuta)
sclMuta.bind('<ButtonRelease-1>',mutacion)
sclMuta.pack()

lb = Label(root,text='')
lb.pack()

btn=Button(root,text='Iniciar algoritmo')
btn.pack()
print()
root.mainloop()"""
