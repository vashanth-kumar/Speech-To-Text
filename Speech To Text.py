# import speech_recognition as sr
# recognizer = sr.Recognizer()
# with sr.Microphone() as source:
#     print("Speak something...")
#     audio = recognizer.listen(source)
#
#     try:
#         text = recognizer.recognize_google(audio)
#         print(f"You said: {text}")
#     except sr.UnknownValueError:
#         print("Sorry, could not understand the audio.")
#     except sr.RequestError as e:
#         print(f"Could not request results; {e}")

import tkinter as tk
import speech_recognition as sr


def recognize_speech():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        output_text.config(state=tk.NORMAL)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, text)
        output_text.config(state=tk.DISABLED)
    except sr.UnknownValueError:
        output_text.config(state=tk.NORMAL)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Sorry, could not understand the audio.")
        output_text.config(state=tk.DISABLED)
    except sr.RequestError as e:
        output_text.config(state=tk.NORMAL)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, f"Error: {e}")
        output_text.config(state=tk.DISABLED)


# Create the main window
root = tk.Tk()
root.title("Speech to Text Converter")

# Create UI elements
label = tk.Label(root, text="Click 'Recognize' and speak...")
label.pack()

output_text = tk.Text(root, height=10, width=50, state=tk.DISABLED)
output_text.pack()

recognize_button = tk.Button(root, text="Recognize", command=recognize_speech)
recognize_button.pack()

# Start the GUI main loop
root.mainloop()
