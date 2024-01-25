import tkinter as tk
import speech_recognition as sr
# Create the main application window
window = tk.Tk()
window.title("Speech Recognition")
window.geometry("400x200")
# Create a label to display the recognized speech
label = tk.Label(window, text="Recognized Speech:")
label.pack()
# Function to process the recorded audio and perform speech recognition
def recognize_speech():
    # Record audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        # Perform speech recognition on the recorded audio
        recognized_text = r.recognize_google(audio)
        label.config(text="Recognized Speech: " + recognized_text)
    except sr.UnknownValueError:
        label.config(text="Could not understand audio")
    except sr.RequestError as e:
        label.config(text="Could not request results; {0}".format(e))
# Create a button to start speech recognition
button = tk.Button(window, text="Start", command=recognize_speech)
button.pack()
window.mainloop()
