# Chapter 21 - Virtual Environments & PIP

## Learn Python fast with some content ideas

Learning Python is a great choice, especially given your interest in web development, mobile app development, and software engineering. Here are some excellent resources to get you started:

**1. LearnPython.org:** This interactive Python tutorial offers free lessons for beginners. It covers topics like variables, loops, functions, and more. You can even get certified after completing the [`tutorials[1]`](https://www.learnpython.org/).

**2. Python Official Documentation:** The official Python documentation provides comprehensive information about the language. Start with the Python Tutorial for beginners and explore further as you gain [`confidence[2]`](https://stackoverflow.com/questions/70577/best-online-resource-to-learn-python).

**3. freeCodeCamp’s Python Courses:**
**- [`Full Course for Beginners`](https://www.freecodecamp.org/news/learn-python-free-python-courses-for-beginners/):** This YouTube course covers programming basics, including lists, conditionals, strings, and small projects like a calculator and a guessing game.
**- [`The Ultimate Python Beginner’s Handbook`](https://www.freecodecamp.org/news/the-python-guide-for-beginners/)** Dive deeper into Python concepts and explore its growing popularity [`3`](https://www.freecodecamp.org/news/learn-python-free-python-courses-for-beginners/) and [`4`](https://www.freecodecamp.org/news/the-python-guide-for-beginners/).

**REMEMBER:** practice coding regularly, work on small projects, and explore real-world examples.

## What is Virtual Environments in Python?

A virtual environment in Python is an isolated environment that allows you to manage dependencies for a specific project without affecting other projects or the global Python installation. It ensures that each project can have its own dependencies, regardless of what dependencies every other project has.

### Key Benefits:

1. **Dependency Management**: Different projects can have different versions of the same package without conflict.
2. **Isolation**: Keeps your global Python environment clean and free from project-specific dependencies.
3. **Reproducibility**: Makes it easier to reproduce the environment on different machines, ensuring consistency.

### How to Create and Activate a Virtual Environment:

1. **Create a Virtual Environment**:

   ```sh
   python -m venv .venv
   ```

   This creates a virtual environment in a directory named [`.venv`].

2. **Activate the Virtual Environment**:

   - On Windows:
     ```sh
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source .venv/bin/activate
     ```

3. **Deactivate the Virtual Environment**:
   ```sh
   deactivate
   ```

### Example:

```sh
# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
.venv\Scripts\activate  # On Windows
# source .venv/bin/activate  # On macOS/Linux

# Install packages
pip install requests

# Deactivate the virtual environment
deactivate
```

Using virtual environments is a best practice for Python development, ensuring that your projects remain clean, isolated, and manageable.

## Create Virtual Environment

py -m venv .venv
source .venv/Scripts/activate
py -m pip show requests
py -m pip install -U pip
python.exe -m pip install --upgrade pip
py -m pip install python-dotenv
py -m pip freeze > requirements.txt

https://home.openweathermap.org/api_keys
login into your account
copy API_KEY
Then, go to API
Then, see Current Weather Data
click on API doc button
API Call
https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
Then, on the right hand side, click on Units of measurement

pypi.org

To activate a virtual environment in Python on a Windows machine, you can use the following command in your terminal:

```sh
.venv\Scripts\activate
```

If you are using PowerShell, the command would be:

```sh
.venv\Scripts\Activate.ps1
```

Make sure to replace [`.venv`] with the name of your virtual environment directory if it is different.

## How can I create a class in Python?

To run the provided Python code, follow these steps:

1. **Ensure you have the required packages installed**:
   Open a terminal and run:

   ```sh
   pip install requests python-dotenv
   ```

2. **Create a `.env` file**:
   In the same directory as your `weather.py` file, create a `.env` file and add your OpenWeatherMap API key:

   ```
   API_KEY=your_openweathermap_api_key
   ```

3. **Run the script**:
   In the terminal, navigate to the directory containing your [`weather.py`] file and run:
   ```sh
   python weather.py
   ```

This will execute the script, prompt you to enter a city name, and then display the current weather conditions for that city.

To get the rain data from the OpenWeatherMap API, you need to check if the `"rain"` key exists in the [`weather_data`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fd%3A%2FlearnPython%2FLesson21%2Fweather.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A22%2C%22character%22%3A4%7D%5D 'weather.py') dictionary. The rain data is usually nested under the `"rain"` key and contains information about the volume of rain for the last 1 or 3 hours.

Here’s how you can modify your code to include the rain data:

```python
import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

def get_current_weather():
    print(f"\n*** Get Current Weather Conditions ***\n")

    city = input("\nPlease enter a city name:\n")

    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

    # print(request_url)

    weather_data = requests.get(request_url).json()

    print(weather_data)

    print(f'\nCurrent weather for {weather_data["name"]}:')
    print(f'\nThe temp is {weather_data["main"]["temp"]:.1f}°')
    print(f'The humidity is {weather_data["main"]["humidity"]}%')
    print(f'The wind speed is {weather_data["wind"]["speed"]}km/h')
    print(
        f'\n{weather_data["weather"][0]["description"].capitalize()} and feels like {weather_data["main"]["feels_like"]:.1f}°\n')

    print(
        f'The high today is {weather_data["main"]["temp_max"]:.1f}° and the low is {weather_data["main"]["temp_min"]:.1f}°\n')

    # Check for rain data
    if "rain" in weather_data:
        rain_1h = weather_data["rain"].get("1h", 0)
        rain_3h = weather_data["rain"].get("3h", 0)
        print(f'Rain volume for the last 1 hour: {rain_1h} mm')
        print(f'Rain volume for the last 3 hours: {rain_3h} mm')
    else:
        print('No rain data available.')

if __name__ == "__main__":
    get_current_weather()
```

This code checks if the `"rain"` key exists in the `weather_data` dictionary and prints the rain volume for the last 1 hour and 3 hours if available. If there is no rain data, it prints a message indicating that no rain data is available.

To loop the weather query with a `while` loop, you can wrap the main logic of the [`get_current_weather`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fd%3A%2FlearnPython%2FLesson21%2Fweather.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A13%2C%22character%22%3A4%7D%5D 'weather.py') function inside a `while` loop. You can also provide an option for the user to exit the loop.

Here’s how you can modify your code:

```python
import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

def get_current_weather():
    while True:
        print(f"\n*** Get Current Weather Conditions ***\n")

        city = input("\nPlease enter a city name (or type 'exit' to quit):\n")

        if city.lower() == 'exit':
            print("\nExiting the weather application. Goodbye!\n")
            break

        request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

        # print(request_url)

        weather_data = requests.get(request_url).json()

        print(weather_data)

        print(f'\nCurrent weather for {weather_data["name"]}:')
        print(f'\nThe temp is {weather_data["main"]["temp"]:.1f}°')
        print(f'The humidity is {weather_data["main"]["humidity"]}%')
        print(f'The wind speed is {weather_data["wind"]["speed"]}km/h')
        print(
            f'\n{weather_data["weather"][0]["description"].capitalize()} and feels like {weather_data["main"]["feels_like"]:.1f}°\n')

        print(
            f'The high today is {weather_data["main"]["temp_max"]:.1f}° and the low is {weather_data["main"]["temp_min"]:.1f}°\n')

        # Check for rain data
        if "rain" in weather_data:
            rain_1h = weather_data["rain"].get("1h", 0)
            rain_3h = weather_data["rain"].get("3h", 0)
            print(f'Rain volume for the last 1 hour: {rain_1h} mm')
            print(f'Rain volume for the last 3 hours: {rain_3h} mm')
        else:
            print('No rain data available.')

        print(f'\n\n*** End of Current Weather Conditions ***\n\n')

if __name__ == "__main__":
    get_current_weather()
```

In this modification:

1. The main logic of `get_current_weather` is wrapped inside a `while True` loop.
2. The user is prompted to enter a city name or type 'exit' to quit the loop.
3. If the user types 'exit', the loop breaks and the program exits.
4. The weather data is fetched and displayed as before.
