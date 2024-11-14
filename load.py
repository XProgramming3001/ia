
# from os import path
# from pocketsphinx import pocketsphinx, get_model_path



# # Chemin vers le modèle de langue PocketSphinx
# model_path = get_model_path()


# class SpeechRecognizer:
#     def __init__(self, grammar_file, language="fr-FR"):
#         self.grammar_file = grammar_file
#         self.language = language
#         # Configuration de PocketSphinx
#         config = pocketsphinx.Config(lm=None, jsgf=None)
        
        
#         config.set_string('-hmm', path.join(model_path,'fr-FR/accoustic-model/cmusphinx-fr'))  # Remplacez par votre modèle acoustique
#         config.set_string('-lm', path.join(model_path,'fr-FR/fr-small.lm.bin'))  # Remplacez par votre modèle de langage
#         config.set_string('-dict', path.join(model_path,'fr-FR/fr.dict'))
        
#          # Remplacez par votre dictionnaire de prononciation
        
#         self.decoder = pocketsphinx.Decoder(config)
        
        
       
        
    

    
#     def recognize_speech(self, audio_data):
#         self.decoder.start_utt()
#         while True:
#             buf = audio_data.read(1024)
#             if buf:
#                 self.decoder.process_raw(buf, False, False)
#             else:
#                 break
#         self.decoder.end_utt()
#         hypothesis = self.decoder.hyp()
#         recognized_phrase = hypothesis.hypstr
#         return recognized_phrase

# recognizer = SpeechRecognizer(grammar_file='C:/Users/XProgramming/Desktop/ia/grammar.jsgf')


# audio_file_path = 'menu.wav'
# audio_data = open(audio_file_path, 'rb')

# recognized_phrase = recognizer.recognize_speech(audio_data)
# print("you said: " + recognized_phrase) 

from pocketsphinx import pocketsphinx, get_model_path
import speech_recognition as sr



r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source)



print(r.recognize_sphinx(audio, language="fr-FR", grammar="grammar.jsgf"))
