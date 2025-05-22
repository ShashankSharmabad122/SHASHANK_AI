# SHASHANK - Personal Voice Assistant

SHASHANK is a Python-based personal voice assistant with face authentication that can perform various tasks through voice commands or text input. It features a modern UI with animations and provides functionality like opening applications, playing YouTube videos, sending messages, making calls, and more.

## Features

- **Face Authentication**: Secure access with facial recognition
- **Voice Commands**: Control your computer with natural language
- **Text Input**: Type commands when voice isn't practical
- **Application Control**: Open applications and websites
- **YouTube Integration**: Play videos directly from voice commands
- **WhatsApp Integration**: Send messages, make calls, and video calls
- **Mobile Device Control**: Connect to Android devices for calls and SMS
- **AI Chatbot**: Get answers to questions using HugChat integration
- **Weather Information**: Get current weather conditions for any city
- **News Headlines**: Stay updated with the latest news in various categories
- **Jokes and Quotes**: Get random jokes and inspirational quotes
- **Dictionary**: Look up word definitions

## Prerequisites

- Python 3.8+
- Windows OS (some features are Windows-specific)
- Chrome browser
- Android device (for mobile features)
- ADB (Android Debug Bridge) for mobile device control
- Webcam (for face authentication)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/shashank.git
   cd shashank
   ```

2. Create a virtual environment:
   ```
   python -m venv envshashank
   ```

3. Activate the virtual environment:
   ```
   # On Windows
   envshashank\Scripts\activate
   ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

5. Set up face authentication:
   - Run the sample collection script to create your face profile:
     ```
     python engine/auth/sample.py
     ```
   - Follow the prompts to capture your face samples
   - Run the trainer to create your face recognition model:
     ```
     python engine/auth/trainer.py
     ```

6. Set up HugChat for AI responses:
   - Create a HugChat account
   - Save your cookies to `engine/cookies.json`

7. Set up API keys for external services:
   - Open `engine/api_config.py`
   - Register for free API keys:
     - OpenWeatherMap: https://openweathermap.org/api
     - NewsAPI: https://newsapi.org/
   - Replace the placeholder API keys with your actual keys

8. Set up the database:
   - The system will create a SQLite database (`shashank.db`) automatically
   - You can add your contacts and application shortcuts to the database

## Usage

1. Start SHASHANK:
   ```
   python run.py
   ```

2. Complete face authentication when prompted

3. Interact with SHASHANK using:
   - Voice commands (click the microphone button or press Win+J)
   - Text input (type in the chat box)

### Voice Commands

- **Open applications**: "SHASHANK, open Chrome"
- **Play YouTube videos**: "SHASHANK, play [song name] on YouTube"
- **Send messages**: "SHASHANK, send message to [contact name]"
- **Make calls**: "SHASHANK, phone call to [contact name]"
- **Video calls**: "SHASHANK, video call to [contact name]"
- **Weather information**: "SHASHANK, what's the weather in New York"
- **News updates**: "SHASHANK, tell me the latest news" or "SHASHANK, tell me the sports news"
- **Entertainment**: "SHASHANK, tell me a joke" or "SHASHANK, give me an inspirational quote"
- **Dictionary**: "SHASHANK, define happiness" or "SHASHANK, what is the meaning of serendipity"
- **General questions**: Ask anything, and the AI will respond

## Mobile Device Integration

To use mobile device features:

1. Connect your Android device to the same WiFi network as your computer
2. Enable USB debugging on your Android device
3. Connect your device via USB once to authorize the connection
4. Run the `device.bat` script to establish a wireless ADB connection
5. Now you can use mobile features like calls and SMS

## Database Configuration

The system uses SQLite to store:

1. **System Commands**: Applications that can be opened
   ```sql
   INSERT INTO sys_command VALUES (null, 'app_name', 'C:\path\to\application.exe');
   ```

2. **Web Commands**: Websites that can be opened
   ```sql
   INSERT INTO web_command VALUES (null, 'website_name', 'https://website.com');
   ```

3. **Contacts**: People you can message or call
   ```sql
   INSERT INTO contacts VALUES (null, 'contact_name', 'phone_number', 'email');
   ```

## Customization

- Change the assistant name in `engine/config.py`
- Modify UI elements in the HTML/CSS files
- Add new commands by extending the `allCommands` function in `engine/command.py`

## Troubleshooting

- **Face Authentication Issues**: Make sure you have good lighting and your face is clearly visible
- **Voice Recognition Problems**: Check your microphone settings and speak clearly
- **Mobile Connection Issues**: Run `device.bat` again to reconnect to your device
- **Application Not Opening**: Verify the path in the database is correct

## Project Structure

- `main.py`: Main application entry point
- `run.py`: Process management for the application
- `engine/`: Core functionality modules
  - `features.py`: Main features implementation
  - `command.py`: Command processing
  - `helper.py`: Utility functions
  - `db.py`: Database operations
  - `config.py`: Configuration settings
  - `api_config.py`: API keys and configuration
  - `api_integrations.py`: External API connections for weather, news, etc.
  - `auth/`: Face authentication modules
- `www/`: Web interface files
  - `index.html`: Main UI
  - `style.css`: Styling
  - `script.js`: Animation and UI behavior
  - `controller.js`: Interface between Python and JavaScript
  - `main.js`: Main JavaScript functionality
- `shashank.db`: SQLite database for storing commands and contacts

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Copyright

© 2025 SHASHANK SHARMA. All rights reserved.

## Acknowledgments

- Thanks to all the open-source libraries that made this project possible
- Special thanks to the contributors and testers
