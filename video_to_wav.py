import os
import speech_recognition as sr
command2mp3 = 'ffmpeg -i sample_video_neso.mp4 sample_audio_neso.mp3'
command2wav = 'ffmpeg -i sample_audio_neso.mp3 sample_audio_neso.wav'
os.system(command2mp3)
os.system(command2wav)
