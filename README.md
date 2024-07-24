# Weather-WebApp
A forecast weather application which gives the accurate weather condition of any city made with the use of one of the prominent python library 'Tkinter' .
# Weather App

This is a Weather App built using Python and Tkinter. It provides current weather information for any city in the world by fetching data from the OpenWeatherMap API.

## Features

- Display current weather conditions including temperature, wind speed, humidity, description, and pressure.
- Fetch and display the current local time of the queried city.
- User-friendly interface with search functionality.
- Error handling for invalid city names and API request failures.

## Prerequisites

- Python 3.x
- Required Python libraries:
  - tkinter
  - geopy
  - timezonefinder
  - requests
  - pytz
  - Pillow (PIL)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/weather-app.git
    cd weather-app
    ```

2. Install the required libraries:
    ```sh
    pip install -r requirements.txt
    ```

3. Ensure you have an API key from OpenWeatherMap. Replace `YOUR_API_KEY` in the code with your actual API key:
    ```python
    api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY"
    ```

## Usage

1. Run the application:
    ```sh
    python weather_app.py
    ```

2. Enter the city name in the search box and click the search icon to retrieve the weather data.

## Code Overview

### Functionality

- **load_image(path, widget_class=Label, **kwargs)**: Function to load and place an image on the Tkinter window.
- **getWeather()**: Function to fetch weather data from OpenWeatherMap API, and update the Tkinter window with the fetched data.

### UI Elements

- **Search Box**: Text field for entering the city name.
- **Search Icon**: Button to initiate the weather data retrieval.
- **Logo**: App logo displayed on the UI.
- **Bottom Box**: Frame containing the weather information.
- **Time**: Displays the current local time of the queried city.
- **Weather Details**: Labels displaying wind speed, humidity, description, and pressure.

