## AI Assistant

**Purpose:**
This Python program serves as a basic speech-to-text AI assistant. It utilizes Google's Web Speech API for speech recognition and the Gemini-1.5-Flash generative AI model for text generation.
I also built show my GF I can somewhat code.

**Dependencies:**

- `speech_recognition`
- `pyttsx3`
- `time`
- `google.generativeai`
- `os`
- `dotenv`

**Setup:**

1. **Create a Google Cloud Platform project** and enable the **Web Speech API** and **Generative AI API**.
2. **Obtain an API key** for your project.
3. **Create a `.env` file** in your project directory and add the API key as `GOOGLE_API_KEY`.

**Usage:**

1. **Run the Python script.**
2. **Speak into your microphone** when prompted.
3. **The assistant will process your speech and respond** using the Gemini-1.5-Flash model.

**Key Features:**

- **Speech recognition:** Uses Google's Web Speech API to convert spoken words into text.
- **Text-to-speech:** Converts text responses into spoken words using `pyttsx3`.
- **AI-powered responses:** Leverages the Gemini-1.5-Flash model to generate contextually relevant responses.
- **Conversation history:** Maintains a simple conversation history to provide context for responses.

**Limitations:**

- **Speech recognition accuracy:** May vary depending on factors like background noise and microphone quality.
- **AI model limitations:** The Gemini-1.5-Flash model's capabilities are limited and may not always provide perfect responses.

**Future enhancements:**

- **Improved speech recognition:** Explore alternative speech recognition engines or techniques.
- **Enhanced AI model:** Consider using more advanced AI models with greater capabilities.
- **Natural language understanding:** Implement techniques to better understand the user's intent.
- **Integration with other services:** Connect the assistant to other services like calendars, email, or smart home devices.
