import tkinter as tk
from tkinter import messagebox
import pygame
import time
import threading

# Lista de canciones con sus rutas locales
songs = [
    {"title": "Canción 1", "file": "song1.mp3"},
    {"title": "Canción 2", "file": "song2.mp3"},
    {"title": "Canción 3", "file": "song3.mp3"}
]

current_index = 0
liked_songs = []

# Inicializa pygame para manejar el audio
pygame.mixer.init()

# Función para reproducir un fragmento de la canción
def play_snippet(song_file):
    def play():
        pygame.mixer.music.load(song_file)
        pygame.mixer.music.play()
        time.sleep(10)  # Reproduce solo 10 segundos
        pygame.mixer.music.stop()
    threading.Thread(target=play).start()

# Función para manejar "Me gusta"
def like_song():
    global current_index
    liked_songs.append(songs[current_index]["title"])
    next_song()

# Función para manejar "No me gusta"
def dislike_song():
    next_song()

# Función para avanzar a la siguiente canción
def next_song():
    global current_index
    current_index += 1
    if current_index < len(songs):
        update_ui()
    else:
        end_program()

# Actualiza la interfaz con la nueva canción
def update_ui():
    song_label.config(text=f"Reproduciendo: {songs[current_index]['title']}")
    play_snippet(songs[current_index]["file"])

# Finaliza el programa y muestra las canciones guardadas
def end_program():
    pygame.mixer.music.stop()
    messagebox.showinfo("Fin", f"Canciones que te gustaron:\n{', '.join(liked_songs)}")
    root.destroy()

# Configuración de la interfaz
root = tk.Tk()
root.title("Music Swipe")
root.geometry("400x200")

song_label = tk.Label(root, text="Haz clic en 'Empezar' para reproducir música", font=("Arial", 14))
song_label.pack(pady=20)

like_button = tk.Button(root, text="👍 Me gusta", font=("Arial", 12), command=like_song)
like_button.pack(side="left", padx=20)

dislike_button = tk.Button(root, text="👎 No me gusta", font=("Arial", 12), command=dislike_song)
dislike_button.pack(side="right", padx=20)

start_button = tk.Button(root, text="Empezar", font=("Arial", 12), command=update_ui)
start_button.pack(pady=20)

root.mainloop()