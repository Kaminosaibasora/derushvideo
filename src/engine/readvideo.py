from moviepy.editor import VideoFileClip

# Chemin vers la vidéo
chemin_video = "../file_in/videotest.mp4"

# Charger la vidéo
video = VideoFileClip(chemin_video)

# Définir les instants de début et de fin de la partie à découper (en secondes)
debut = 1  # Début de la partie à découper
fin = 3.5  # Fin de la partie à découper

# Découper la partie de la vidéo
video_decoupee = video.subclip(debut, fin)

# Chemin vers la vidéo découpée
chemin_video_decoupee = "../file_out/videotest_2.mp4"

# Enregistrer la vidéo découpée
video_decoupee.write_videofile(chemin_video_decoupee)

# Lire la vidéo avec le son
video = VideoFileClip(chemin_video_decoupee)
video.preview()