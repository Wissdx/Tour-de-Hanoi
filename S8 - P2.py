#coding:utf-8
from tkinter import *
import pygame
import random

pygame.mixer.init()

sons = ["bois1.wav","bois2.wav","bois3.wav","bois4.wav","bois5.wav"] # Liste de sons qui seront joués au déplacement des disques

deplacements = 0

def deplace(disque,x,y):
    global deplacements
    pygame.mixer.music.load(random.choice(sons)) # Charge un son au hasard dans la liste sons
    pygame.mixer.music.play() # Joue un des sons séléctionnés quand le disque est déplacé ->
    Canevas.move(disque,x,y) # Déplace le disque aux coordonnées x et y
    deplacements+=1 # Incrémente le nombre de déplacements
    Canevas.delete(fenetre,"deplacement") # Supprime l'ancien texte contenant le nombre de déplacement
    Canevas.create_text(width/2, height/10, text="Nombre de déplacements : " + str(deplacements), fill="black", font="Impact 24", tag="deplacement") # Affiche le nombre de déplacement

def jouerTroisDisques():
    global deplacements
    pygame.mixer.music.load("game_start.wav")
    pygame.mixer.music.play()
    # Mise en place de la situation 1
    petit_disque = Canevas.create_polygon(width*1/4-50, 650, width*1/4+50, 650,width=35, outline="#F4A31F",tag="disque") # Création du petit disque
    moyen_disque = Canevas.create_polygon(width*1/4-125, 690, width*1/4+125, 690,width=35, outline="#F4A31F",tag="disque") # Création du moyen disque
    grand_disque = Canevas.create_polygon(width*1/4-200, 730, width*1/4+200, 730,outline="#F4A31F", width=35, tag="disque") # Création du grand disque
    
    Canevas.after(1000,deplace,petit_disque,width*2/4,80) # Situation 2
    Canevas.after(2000,deplace,moyen_disque,width*1/4,40) # Situation 3
    Canevas.after(3000,deplace,petit_disque,-width*1/4,-40) # Situation 4
    Canevas.after(4000,deplace,grand_disque,width*2/4,0) # Situation 5
    Canevas.after(5000,deplace,petit_disque,-width*1/4,40) # Situation 6
    Canevas.after(6000,deplace,moyen_disque,width*1/4,-40) # Situation 7
    Canevas.after(7000,deplace,petit_disque,width*2/4,-80) # Situation 8
    Canevas.after(11000,Canevas.delete,fenetre,"disque")
    deplacements = 0

width = 1920 # Longueur du Canevas
height = 1080 # Hauteur du Canevas

fenetre = Tk()
fenetre.title("S8 P2 - Les tours d'Hanoï")
fenetre.attributes('-fullscreen', True) # Lance la fenetre en plein écran

Canevas = Canvas(fenetre,bg="grey",width=width,height=height, bd=0, highlightthickness=1, highlightbackground="black")
Canevas.pack(padx=0,pady=0)

close_window = Button(Canevas,text="X",
    font=("Comic Sans MS", 14, "bold"),
    fg="red",bg="grey",bd=0,padx=0,pady=0,command=fenetre.destroy) # Création d'un bouton qui permet de fermer la fenetre

Canevas.create_window(1920,1, anchor=NE ,window=close_window) # Affiche le bouton qui ferme la fenetre
Canevas.create_text(width/50, height/50, text="DERGHAL Wissem - TGLE NSI Edouard BRANLY", fill="black", font="Impact 18", anchor="nw")# Affichage du nom et prénom en texte

Canevas.create_rectangle(width/10, 750, width*9/10, 760, fill="#1F76F4", outline="#1F76F4") # Création de la base des tours
Canevas.create_rectangle(width*1/4+3,200,width*1/4-3,750,fill="#1F76F4",outline="#1F76F4") # Création de la Tour 1
Canevas.create_rectangle(width*2/4+3,200,width*2/4-3,750,fill="#1F76F4",outline="#1F76F4") # Création de la Tour 2
Canevas.create_rectangle(width*3/4+3,200,width*3/4-3,750,fill="#1F76F4",outline="#1F76F4") # Création de la Tour 3



play3 = Button(Canevas, text="Jouer avec trois disques", font=("Comic Sans MS", 18, "italic"), fg="orange", bg="grey", command=jouerTroisDisques)
Canevas.create_window(width/8,height/2, window=play3)

fenetre.mainloop()