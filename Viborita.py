import turtle
import time
import random

posponer = 0.1
#marcador
puntaje=0
puntaje_alto=0




#Configuracion de la ventana
wn= turtle.Screen()
wn.title("Juego de viborita")
wn.bgcolor("black")
wn.setup(width=600,height=600)
wn.tracer(0)

#Cabeza serpiente
cabeza=turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction="stop"
cabeza.color("white")

#Comida
comida=turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.penup()
comida.goto(0,100)
comida.color("red")

#cuerpo serviente
segmento = []

#Texto
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Puntaje: 0   Puntaje Alto: 0", align = "center",font=("Courier",24,"normal"))


#Funciones
def arriba():
	cabeza.direction = "up"

def abajo():
	cabeza.direction = "down"

def izquierda():
	cabeza.direction = "left"

def derecha():
	cabeza.direction = "right"


def mov():
	if cabeza.direction == "up":
		y = cabeza.ycor()
		cabeza.sety(y+20)

	if cabeza.direction == "down":
		y = cabeza.ycor()
		cabeza.sety(y-20)

	if cabeza.direction == "left":
		x = cabeza.xcor()
		cabeza.setx(x-20)

	if cabeza.direction == "right":
		x = cabeza.xcor()
		cabeza.setx(x+20)

#Teclado
wn.listen()
wn.onkeypress(arriba,"Up")
wn.onkeypress(abajo,"Down")
wn.onkeypress(izquierda,"Left")
wn.onkeypress(derecha,"Right")

while True:
	wn.update()
	#Colisiones bordes
	if cabeza.xcor()>280 or cabeza.xcor()< -290 or cabeza.ycor()>290 or cabeza.ycor()< -290:
		time.sleep(1)
		cabeza.goto(0,0)
		cabeza.direction = "stop"

	#Esconder segmento
		for SEGMENTO in segmento:
			SEGMENTO.goto(1000,1000)
			time.sleep(1)
			cabeza.goto(0,0)
			cabeza.direction="stop"



	#Limpiar lista de segmento
		segmento.clear()

	#Resetear marcador
		puntaje = 0
		texto.clear()
		texto.write("Puntaje: {}   Puntaje Alto: {}".format(puntaje,puntaje_alto), align = "center",font=("Courier",22,"normal"))

	#Colisiones comida
	if cabeza.distance(comida) < 20:
		x = random.randint(-280,280)
		y = random.randint(-280,280)
		comida.goto(x,y)

		nuevo_segmento=turtle.Turtle()
		nuevo_segmento.speed(0)
		nuevo_segmento.shape("square")
		nuevo_segmento.penup()
		nuevo_segmento.color("yellow")
		segmento.append(nuevo_segmento)

		#Aumentar marcador
		puntaje+=10

		if puntaje > puntaje_alto:
			puntaje_alto = puntaje
			texto.clear()
			texto.write("Puntaje: {}   Puntaje Alto: {}".format(puntaje,puntaje_alto), align = "center",font=("Courier",22,"normal"))


	#Mover el cuerpo de la serpiente
	totalSeg=len(segmento)
	for index in range(totalSeg -1,0,-1):
		x = segmento[index -1].xcor()
		y = segmento[index -1].ycor()
		segmento[index].goto(x,y)

	if totalSeg > 0:
		x=cabeza.xcor()
		y=cabeza.ycor()
		segmento[0].goto(x,y)

	mov()
	#Colisiones cuerpo
	for SEGMENTO in segmento:
		if SEGMENTO.distance(cabeza)<20:
			time.sleep(1)
			cabeza.goto(0,0)
			cabeza.direction = "stop"
	
			#esconder segmentos
			for SEGMENTO in segmento:
				SEGMENTO.goto(1000,1000)

			#Limpiar los elementos de la lista
			segmento.clear()

			#Resetear marcador
			puntaje = 0
			texto.clear()
			texto.write("Puntaje: {}   Puntaje Alto: {}".format(puntaje,puntaje_alto), align = "center",font=("Courier",22,"normal"))

	time.sleep(posponer)