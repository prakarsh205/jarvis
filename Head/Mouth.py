import pyttsx3
def speak(text):
    engine = pyttsx3.init()
    pitch = 180
    rate = 180
    volume = 3
    voice_id = engine.getProperty("voices")
    if voice_id:
        voices = engine.getProperty('voices')
        try:
            engine.setProperty('voice', voices[0].id)
        except IndexError:
            print("Voice ID not found. Using the default voice.")


    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)
    engine.setProperty('pitch', pitch)


    print(text)
    engine.say(text)
    engine.runAndWait()





# animation message
# import asyncio
# import threading
# import os
# import edge_tts  # pip install edge-tts
# import pygame  # pip install pygame
# import sys
# import time
#
# VOICE = "en-AU-WilliamNeural"
# BUFFER_SIZE = 1024
#
#
# def print_animated_message(message):
#     for char in message:
#         sys.stdout.write(char)
#         sys.stdout.flush()
#         time.sleep(0.095)  # Adjust the sleep duration for the animation speed
#     print()
#
#
# def remove_file(file_path):
#     max_attempts = 3
#     attempts = 0
#     while attempts < max_attempts:
#         try:
#             with open(file_path, "wb"):
#                 pass
#             os.remove(file_path)
#             break
#         except Exception as e:
#             print(f"Error removing file: {e}")
#             attempts += 1
#
#
# async def amain(TEXT, output_file) -> None:
#     try:
#         communicate = edge_tts.Communicate(TEXT, VOICE)
#         await communicate.save(output_file)
#         thread = threading.Thread(target=play_audio, args=(output_file,))
#         thread.start()
#         thread.join()
#     except Exception as e:
#         print(f"error: {e}")
#     finally:
#         remove_file(output_file)
#
#
# def play_audio(file_path):
#     try:
#         pygame.init()
#         pygame.mixer.init()
#         sound = pygame.mixer.Sound(file_path)
#         sound.play()
#
#         while pygame.mixer.get_busy():
#             pygame.time.Clock().tick(10)
#
#         pygame.quit()
#
#     except Exception as e:
#         print(f"Error during audio playback: {e}")
#
#
# def speak1(TEXT, output_file=None):
#     if output_file is None:
#         output_file = os.path.join(os.getcwd(), "speak.mp3")
#     asyncio.run(amain(TEXT, output_file))
#
#
# def speak(text):
#     t1 = threading.Thread(target=speak1, args=(text,))
#     t2 = threading.Thread(target=print_animated_message, args=(text,))
#     t1.start()
#     t2.start()
#     t1.join()
#     t2.join()


# import asyncio
# import threading
# import os
# import edge_tts
# import pygame
#
# VOICE = "en-AU-WilliamNeural"
# BUFFER_SIZE = 1024
#
# def remove_file(file_path):
#     max_attempts = 3
#     attempts = 0
#     while attempts < max_attempts:
#         try:
#             with open(file_path, 'wb'):
#                 pass  # Try to close the file handle
#             os.remove(file_path)
#             break  # If successful, break out of the loop
#         except Exception as e:
#             print(f"Error removing file: {e}")
#             attempts += 1
#
# async def amain(TEXT, output_file) -> None:
#     try:
#         # Main function
#         communicate = edge_tts.Communicate(TEXT, VOICE)
#         await communicate.save(output_file)
#
#         # Use threading to run audio playback in a separate thread
#         thread = threading.Thread(target=play_audio, args=(output_file,))
#         thread.start()
#         thread.join()  # Wait for the audio playback thread to finish
#
#     except Exception as e:
#         print(f"Error: {e}")
#
#     finally:
#         remove_file(output_file)
#
# def play_audio(file_path):
#     try:
#         # Initialize pygame
#         pygame.init()
#
#         # Open the audio file
#         pygame.mixer.init()
#         sound = pygame.mixer.Sound(file_path)
#
#         # Play the audio
#         sound.play()
#
#         # Wait for the audio to finish playing
#         while pygame.mixer.get_busy():
#             pygame.time.Clock().tick(10)
#
#         # Quit pygame
#         pygame.quit()
#
#     except Exception as e:
#         print(f"Error during audio playback: {e}")
#
# def speak(TEXT, output_file=None):
#     if output_file is None:
#         output_file = f"{os.getcwd()}/speak.mp3"
#     asyncio.run(amain(TEXT, output_file))
#
#
