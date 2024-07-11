import win32com.client
def shoutout(names):
    speak = win32com.client.Dispatch("SAPI.SpVoice")
    for name in names:
        speak.Speak("Shoutout to " + name.upper())

names_list = ["Nirupam","Vaibhav","Nishad","Amit"]
shoutout(names_list)