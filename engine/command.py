import pyttsx3
import speech_recognition as sr
import eel
import time
def speak(text):
    text = str(text)
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 174)
    eel.DisplayMessage(text)
    engine.say(text)
    eel.receiverText(text)
    engine.runAndWait()


def takecommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('listening....')
        eel.DisplayMessage('listening....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        
        audio = r.listen(source, 10, 6)

    try:
        print('recognizing')
        eel.DisplayMessage('recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
        eel.DisplayMessage(query)
        time.sleep(2)
       
    except Exception as e:
        return ""
    
    return query.lower()

@eel.expose
def allCommands(message=1):

    if message == 1:
        query = takecommand()
        print(query)
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)
    try:
        # Open applications or websites
        if "open" in query:
            from engine.features import openCommand
            openCommand(query)
        
        # YouTube playback
        elif "on youtube" in query:
            from engine.features import PlayYoutube
            PlayYoutube(query)
        
        # Contact-related commands (messages, calls)
        elif "send message" in query or "phone call" in query or "video call" in query:
            from engine.features import findContact, whatsApp, makeCall, sendMessage
            contact_no, name = findContact(query)
            if(contact_no != 0):
                speak("Which mode you want to use whatsapp or mobile")
                preferance = takecommand()
                print(preferance)

                if "mobile" in preferance:
                    if "send message" in query or "send sms" in query: 
                        speak("what message to send")
                        message = takecommand()
                        sendMessage(message, contact_no, name)
                    elif "phone call" in query:
                        makeCall(name, contact_no)
                    else:
                        speak("please try again")
                elif "whatsapp" in preferance:
                    message = ""
                    if "send message" in query:
                        message = 'message'
                        speak("what message to send")
                        query = takecommand()
                                        
                    elif "phone call" in query:
                        message = 'call'
                    else:
                        message = 'video call'
                                        
                    whatsApp(contact_no, query, message, name)
        
        # Weather information
        elif "weather" in query:
            from engine.api_integrations import get_weather
            # Extract city name from query
            city = query.replace("weather", "").replace("in", "").replace("what's the", "").replace("what is the", "").strip()
            if not city:
                speak("Which city would you like to know the weather for?")
                city = takecommand()
            
            weather_info = get_weather(city)
            speak(weather_info)
        
        # News headlines
        elif "news" in query:
            from engine.api_integrations import get_news
            category = "general"
            
            # Check for specific news categories
            categories = ["business", "entertainment", "health", "science", "sports", "technology"]
            for cat in categories:
                if cat in query:
                    category = cat
                    break
            
            news = get_news(category=category)
            speak(news)
        
        # Jokes
        elif "joke" in query or "make me laugh" in query:
            from engine.api_integrations import get_joke
            joke = get_joke()
            speak(joke)
        
        # Inspirational quotes
        elif "quote" in query or "inspiration" in query:
            from engine.api_integrations import get_quote
            quote = get_quote()
            speak(quote)
        
        # Word definitions
        elif "define" in query or "meaning of" in query or "definition of" in query:
            from engine.api_integrations import get_definition
            # Extract the word to define
            word = ""
            if "define" in query:
                word = query.replace("define", "").strip()
            elif "meaning of" in query:
                word = query.replace("meaning of", "").strip()
            elif "definition of" in query:
                word = query.replace("definition of", "").strip()
            
            if word:
                definition = get_definition(word)
                speak(definition)
            else:
                speak("What word would you like me to define?")
        
        # Default: use chatbot for general queries
        else:
            from engine.features import chatBot
            chatBot(query)
    except Exception as e:
        print(f"Error processing command: {e}")
        speak("I'm sorry, I encountered an error while processing your request.")
    
    eel.ShowHood()