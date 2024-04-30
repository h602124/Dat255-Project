import os
import pygame

def speak(text):
    voice = 'en-US-JennyNeural'
    data = f'python -m edge_tts --voice "{voice}" --text "{text}" --write-media "data.mp3"'
    os.system(data)

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("data.mp3")

    try:
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        print(e)
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()
