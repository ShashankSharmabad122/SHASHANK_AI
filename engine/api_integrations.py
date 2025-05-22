import requests
import json
from datetime import datetime
from engine.api_config import OPENWEATHER_API_KEY, NEWS_API_KEY

def get_weather(city):
    """
    Get current weather information for a specified city
    
    Args:
        city (str): Name of the city to get weather for
        
    Returns:
        str: Formatted weather information or error message
    """
    try:
        # Make API request
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_API_KEY}&units=metric"
        response = requests.get(url)
        
        # Check if request was successful
        if response.status_code == 200:
            data = response.json()
            
            # Extract relevant information
            weather_desc = data['weather'][0]['description']
            temp = data['main']['temp']
            feels_like = data['main']['feels_like']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            
            # Format the response
            weather_info = (
                f"Current weather in {city}: {weather_desc}. "
                f"Temperature is {temp}°C, feels like {feels_like}°C. "
                f"Humidity is {humidity}% with wind speed of {wind_speed} meters per second."
            )
            
            return weather_info
        else:
            return f"Sorry, I couldn't find weather information for {city}. Please try another city."
    
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return "Sorry, I encountered an error while fetching weather information. Please try again later."

# News API uses the key imported from api_config.py

def get_news(category="general", country="us", count=5):
    """
    Get latest news headlines
    
    Args:
        category (str): News category (business, entertainment, general, health, science, sports, technology)
        country (str): 2-letter country code (us, gb, in, etc.)
        count (int): Number of news items to return
        
    Returns:
        str: Formatted news headlines or error message
    """
    try:
        # Make API request
        url = f"https://newsapi.org/v2/top-headlines?country={country}&category={category}&apiKey={NEWS_API_KEY}"
        response = requests.get(url)
        
        # Check if request was successful
        if response.status_code == 200:
            data = response.json()
            
            if data['totalResults'] > 0:
                # Format the response
                news_text = f"Here are the top {min(count, len(data['articles']))} {category} news headlines:\n"
                
                for i, article in enumerate(data['articles'][:count]):
                    news_text += f"{i+1}. {article['title']}"
                    if article['description']:
                        news_text += f" - {article['description']}"
                    news_text += "\n"
                
                return news_text
            else:
                return f"Sorry, I couldn't find any {category} news for {country}."
        else:
            return "Sorry, I encountered an error while fetching news. Please try again later."
    
    except Exception as e:
        print(f"Error fetching news data: {e}")
        return "Sorry, I encountered an error while fetching news information. Please try again later."

# Joke API - Free, no API key required
def get_joke():
    """
    Get a random joke
    
    Returns:
        str: A joke or error message
    """
    try:
        # Make API request
        url = "https://official-joke-api.appspot.com/random_joke"
        response = requests.get(url)
        
        # Check if request was successful
        if response.status_code == 200:
            data = response.json()
            
            # Format the joke
            joke = f"{data['setup']} {data['punchline']}"
            return joke
        else:
            return "Sorry, I couldn't fetch a joke right now. Please try again later."
    
    except Exception as e:
        print(f"Error fetching joke: {e}")
        return "Sorry, I encountered an error while fetching a joke. Please try again later."

# Quote API - Free, no API key required
def get_quote():
    """
    Get a random inspirational quote
    
    Returns:
        str: A quote or error message
    """
    try:
        # Make API request
        url = "https://api.quotable.io/random"
        response = requests.get(url)
        
        # Check if request was successful
        if response.status_code == 200:
            data = response.json()
            
            # Format the quote
            quote = f'"{data["content"]}" - {data["author"]}'
            return quote
        else:
            return "Sorry, I couldn't fetch a quote right now. Please try again later."
    
    except Exception as e:
        print(f"Error fetching quote: {e}")
        return "Sorry, I encountered an error while fetching a quote. Please try again later."

# Dictionary API - Free, no API key required
def get_definition(word):
    """
    Get the definition of a word
    
    Args:
        word (str): The word to define
        
    Returns:
        str: Word definition or error message
    """
    try:
        # Make API request
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        response = requests.get(url)
        
        # Check if request was successful
        if response.status_code == 200:
            data = response.json()
            
            if data and len(data) > 0:
                # Format the definition
                result = f"Definition of {word}:\n"
                
                for meaning in data[0]['meanings'][:2]:  # Limit to first 2 meanings
                    part_of_speech = meaning['partOfSpeech']
                    result += f"\nAs a {part_of_speech}:\n"
                    
                    for definition in meaning['definitions'][:2]:  # Limit to first 2 definitions per part of speech
                        result += f"- {definition['definition']}\n"
                        
                        if 'example' in definition and definition['example']:
                            result += f"  Example: {definition['example']}\n"
                
                return result
            else:
                return f"Sorry, I couldn't find a definition for {word}."
        else:
            return f"Sorry, I couldn't find a definition for {word}."
    
    except Exception as e:
        print(f"Error fetching definition: {e}")
        return f"Sorry, I encountered an error while fetching the definition of {word}."