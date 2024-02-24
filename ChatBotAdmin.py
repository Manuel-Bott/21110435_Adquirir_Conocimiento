# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 01:35:03 2024

@author: JMnau
"""
import os
import time

class ChatBot:
    def __init__(self):
        self.questions = {
            "1": {"question": "¿Cuál es tu nombre?", "answer": "Mi nombre es ChatBot."},
            "2": {"question": "¿Como me llego a mi casa?", "answer": "Dirigete a la estacion rumbo al este, y pregunatale a un policia."},
            "3": {"question": "¿Cuál es tu función?", "answer": "Estoy aquí para ayudarte con cualquier pregunta que tengas."},
            "4": {"question": "¿Puedo reportar un crimen?", "answer": "Sin duda!. Presiona el boton de S.O.S. y reportalo por favor."}
        }

    def ask_question(self, question_number):
        if question_number in self.questions:
            return self.questions[question_number]["question"]
        else:
            return "Lo siento, no tengo respuesta para esa pregunta."

    def ask_answer(self, question_number):
     if question_number in self.questions:
         return self.questions[question_number]["answer"]
     else:
         return "----\n"

    def add_question(self, question, answer):
        new_question_number = str(len(self.questions) + 1)
        self.questions[new_question_number] = {"question": question, "answer": answer}
        return f"Pregunta añadida con éxito con el número {new_question_number}."

    def get_answer(self, question_number):
        if question_number in self.questions:
            return self.questions[question_number]["answer"]
        else:
            return "Lo siento, no tengo respuesta para esa pregunta.\n\n"

    def show_questions(self):
        print("\n\nLista de preguntas y respuestas:")
        for question_number, question_info in self.questions.items():
            print(f"{question_number}. Pregunta: {question_info['question']}")
            print(f"   Respuesta: {question_info['answer']}")

def limpiar_consola_con_delay():
    # Esperar 3 segundos
    time.sleep(3)
    
    # Limpiar la consola
    if os.name == 'nt':
        _ = os.system('cls')
    

# Llamar a la función para limpiar la consola con un retraso de 3 segundos

def main():
    chatbot = ChatBot()

    while True:
        print("1. Ver una pregunta.")
        print("2. Agregar una pregunta.")
        print("3. Mostrar lista de preguntas y respuestas.")
        print("4. Salir.")
        choice = input("¿Qué te gustaría hacer? ")

        if choice == "1":
            question_number = input("Por favor ingresa el número de la pregunta: ")
            print("\nPregunta: " + chatbot.ask_question(question_number))
            #print("\n")
            print("Respuesta: " +chatbot.ask_answer(question_number)+"\n\n")
        elif choice == "2":
            question = input("Por favor ingresa la nueva pregunta: ")
            answer = input("Por favor ingresa la respuesta a la nueva pregunta: ")
            print(chatbot.add_question(question, answer))
        elif choice == "3":
            chatbot.show_questions()
            print(" \n\n---------------------------------------------------------------------\n\n")
        elif choice == "4":
            print("Gracias por usar el ChatBot. ¡Hasta luego!")
            limpiar_consola_con_delay()
            break
        else:
            print("Selección no válida. Por favor, elige nuevamente.\n\n")


if __name__ == "__main__":
    main()
    
    