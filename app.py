import speech_recognition as sr
import pyttsx3
import time
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize recognizer, text-to-speech engine, and AI client
recognizer = sr.Recognizer()
engine = pyttsx3.init()
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

# Initialize conversation history
messages = [
    {
        "role": "assistant",
        "content": "Hi! How can I help you today?",
    }
]


def speak(text):
    """Function to convert text to speech"""
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()


def get_ai_response(user_input):
    """Function to get AI response from Claude"""
    try:
        # Add user message to conversation history
        messages.append({"role": "user", "content": user_input})
        prompt = (
            "You a helpful and friendly AI assistant. "
            "Keep responses concise and conversational. "
            f"User says: {user_input}"
        )

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:
        print(f"Error getting AI response: {str(e)}")
        return "I apologize, but I encountered an error while processing your request. Please try again."


def recognize_speech():
    """Function to capture audio and recognize speech"""
    with sr.Microphone() as source:
        speak("Adjusting for ambient noise. Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        speak("I'm listening. Please speak now...")
        try:
            # Capture audio
            audio = recognizer.listen(source, timeout=20, phrase_time_limit=100)

            # Use Google's Web Speech API to recognize speech
            print("Processing your speech...")
            text = recognizer.recognize_google(audio)

            # Get AI response
            ai_response = get_ai_response(text)

            # Speak the AI response
            speak(ai_response)

            return text

        except sr.WaitTimeoutError:
            speak("Sorry, I didn't hear anything. Please try again.")
        except sr.UnknownValueError:
            speak("Sorry, I couldn't understand what you said. Please try again.")
        except sr.RequestError:
            speak("Sorry, there was an error with the speech recognition service.")
        return None


def main():
    # Speak initial greeting from messages history
    speak(messages[0]["content"])

    while True:
        text = recognize_speech()

        # Check if user wants to exit
        if text and any(
            phrase in text.lower() for phrase in ["exit", "quit", "goodbye", "bye"]
        ):
            speak("Goodbye! Have a great day!")
            break

        # Small pause between iterations
        time.sleep(1)


if __name__ == "__main__":
    main()
