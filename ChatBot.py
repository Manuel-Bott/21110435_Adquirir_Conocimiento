# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 00:25:25 2024

@author: JMnau
"""
import os
import time
import random
 
Bienvenida = "¡Hola! Soy un chatbot. ¿En qué puedo ayudarte hoy? \n 1- ¿Cuál es tu nombre?  \n 2- ¿Cómo estás?  \n 3- ¿Qué puedes hacer? "
Salir =  "\n 12- Salir"

# Definir las preguntas y respuestas precargadas
preguntas = [
   "0",
    "1",
    "2",
    "3"
]

respuestas = [
    "Mi nombre es Chatbot.",
    "Estoy bien, gracias por preguntar.",
    "Puedo responder preguntas y ayudarte con problemas de programación, entre otras cosas."
]

def responder_pregunta(pregunta):
    # Buscar la pregunta en la lista preguntas
    if pregunta in preguntas:
        # Encontrar el índice de la pregunta
        index = preguntas.index(pregunta)
        # Devolver la respuesta correspondiente
        return respuestas[index]
    else:
        # Si la pregunta no está en la lista, devolver una respuesta genérica
        return "Lo siento, no entiendo esa pregunta."




def limpiar_consola_con_delay():
    # Esperar 3 segundos
    time.sleep(3)
    
    # Limpiar la consola
    # Para Windows
    if os.name == 'nt':
        _ = os.system('cls')
    

# Llamar a la función para limpiar la consola con un retraso de 3 segundos



# Función principal del chatbot
def chat():
    print(Bienvenida + Salir)
    while True:
        entrada_usuario = input("Usuario: ")
        # Salir del bucle si el usuario escribe "salir"
        if entrada_usuario.lower() == "12":
            print("¡Hasta luego!")
            limpiar_consola_con_delay()
            break
        # Elegir una respuesta aleatoria si el usuario no hace una pregunta específica
        if "?" not in entrada_usuario:
            print("Chatbot: " + random.choice(respuestas))
        else:
            # Responder a la pregunta del usuario
            print("Chatbot: " + responder_pregunta(entrada_usuario))
            print (responder_pregunta(entrada_usuario)) 

# Iniciar el chatbot
if __name__ == "__main__":
    chat()