import pyttsx3
import speech_recognition as sr
import openai


# Set up OpenAI API credentials
openai.api_key = ("Chat-Gpt API")

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Initialize speech recognizer
r = sr.Recognizer()

# Set the voice for the assistant
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# Define a function to speak the given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define a function to recognize speech input
def recognize_speech():
    with sr.Microphone() as source:
        print('Listening...')
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print('You said:', text)
            return text
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
        except sr.RequestError:
            print('Sorry, my speech service is down.')

# Define a function to generate text using OpenAI API
def generate_text(prompt):
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=prompt,
      max_tokens=1024,
      n=1,
      stop=None,
      temperature=0.7,
    )

    return response.choices[0].text

# Main program loop
while True:
    speak('How can I help you?')
    text = recognize_speech()

    if 'hello' :
        speak('Hello! How are you?')
    elif 'what is your name' in text.lower():
        speak('My name is Voice Assistant.')
    elif 'open' in text.lower():
        speak('What would you like to ask?')
        prompt = recognize_speech()
        response = generate_text(prompt)
        speak(response)
    elif 'exit' in text.lower():
        speak('goodbye!')
        break
    else:
        speak("Sorry, I didn't understand that.")
