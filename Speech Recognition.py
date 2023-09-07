#!/usr/bin/env python
# coding: utf-8

# # SPEECH RECOGNITION

# In[2]:


pip install SpeechRecognition


# In[3]:


pip install PyAudio


# In[2]:


import speech_recognition as sr
recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something:")
    audio = recognizer.listen(source, timeout=5)
try:
    text = recognizer.recognize_google(audio)
    print(f"You said: {text}")
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print(f"Could not request results from Google Web Speech API; {e}")


# # TEXT TRANSLATION 

# In[3]:


pip install googletrans==4.0.0-rc1


# In[2]:


from googletrans import Translator
translator=Translator()
text_to_translate=input("enter text:")
detected_language=translator.detect(text_to_translate).lang
target_language=input("enter language:")
translated_text=translator.translate(text_to_translate,src=detected_language,dest=target_language)
ans=translated_text.text
print(translated_text.text)


# # AUDIO TRANSLATION

# In[5]:


import speech_recognition as sr
from googletrans import Translator
recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak something...")
    audio = recognizer.listen(source)
try:
    text = recognizer.recognize_google(audio)
    print("You said: " + text)
    translator=Translator()
    detected_language=translator.detect(text).lang
    target_language=input("enter language:")
    translated_text=translator.translate(text,src=detected_language,dest=target_language)
    ans=translated_text.text
    print(translated_text.text)
except sr.UnknownValueError:
    print("Sorry, I couldn't understand what you said.")
except sr.RequestError as e:
    print("Error: {0}".format(e))


# In[ ]:




