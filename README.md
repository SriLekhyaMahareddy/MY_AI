# MY_AI
## Project Description

MY_AI is an AI assistant that performs a variety of tasks based on voice commands. It can tell the current date and time, search Wikipedia, take screenshots, open YouTube, open a browser, send WhatsApp messages, remember and recall information, send emails, play songs, and even shut down or restart your system. Additionally, it can respond to general inquiries using responses from ChatGPT.

## Installation Instructions

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/MY_AI.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd MY_AI
    ```

3. **Create and activate a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Setup additional dependencies:**

    Ensure you have all necessary software and libraries installed, such as:
    - Python 3.x
    - pyttsx3
    - SpeechRecognition
    - Wikipedia
    - pyscreeze
    - requests
    - pywhatkit
    - smtplib

6. **Update Authorization Token:**

    Replace the placeholder `Authorization` token in the code with your actual token.

## Here the files 'data.txt' stores data that has to be remembered by my_ai ,song.py file is imported into my_ai,image.png stores the picture we took screenshot of.

## Usage Instructions

1. **Run the main script:**

    ```bash
    python first.py
    ```

2. **Interact with the AI assistant:**

    The AI assistant will listen for your commands and perform the tasks as per your instructions. Some example commands include:
    - "What time is it?"
    - "Tell me today's date."
    - "Search Wikipedia for Python programming."
    - "Take a screenshot."
    - "Open YouTube and search for lo-fi music."
    - "Open the browser and search for latest news."
    - "Send a WhatsApp message."
    - "Remember that I have a meeting at 5 PM."
    - "Do I have anything to know?"
    - "Send an email."
    - "Play a song."
    - "Shutdown the system."
    - "Restart the system."

3. **Custom Commands:**

    You can ask the AI assistant any question or give any command, and it will respond using ChatGPT.

## Features

- **Date and Time**: Tells the current date and time.
- **Wikipedia Search**: Searches Wikipedia and reads a summary.
- **Screenshot**: Takes a screenshot and saves it.
- **YouTube Search**: Opens YouTube and searches for the provided query.
- **Browser Search**: Opens the browser and searches for the provided query.
- **WhatsApp Message**: Sends a WhatsApp message instantly.
- **Memory**: Remembers information and recalls it later.
- **Email**: Sends an email to the specified recipient.
- **Music Playback**: Plays, pauses, and stops songs.
- **System Control**: Shuts down or restarts the system.
- **ChatGPT Responses**: Provides responses to general inquiries using ChatGPT.

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or issues, feel free to open an issue on GitHub or contact me directly at 21pa1a0597@vishnu.edu.in.

---

This README template should give a clear overview of your project, how to install and use it, and how others can contribute. Feel free to customize any part of it as needed.
