# 🌤 Weather Forecasting App

A simple and user-friendly weather forecasting application that displays real-time weather data based on the user's city input. The app is built using Python and supports both **Console** and **Graphical User Interface (GUI)** modes.

## 📌 Features

- Real-time weather information by city name  
- Displays:
  - Temperature
  - Humidity
  - Atmospheric pressure
  - Wind speed
  - Weather description
  - Current local time
  - Timezone info
- Built with an intuitive GUI using **Tkinter**
- API-powered via **OpenWeatherMap**

## 📁 Project Structure

- `weather.py`: Handles API requests and data processing  
- `weathergui.py`: GUI implementation using `tkinter`  
- `demo.py`: Console-based version

## 🛠 Technologies & Libraries Used

- **Tkinter** – GUI framework for desktop apps  
- **Geopy** – For geocoding (address to coordinates)  
- **Timezonefinder** – Finds timezone from coordinates  
- **Requests** – Sends HTTP requests to the API  
- **Datetime** – Handles date and time  
- **Pytz** – Timezone calculations  
- **OpenWeatherMap API** – Provides weather data  

## 🚀 How to Run

### 1. Install Dependencies

```bash
pip install tkinter geopy timezonefinder requests pytz
```

### 2. Console Version

```bash
python demo.py
```

Enter your city name when prompted.

### 3. GUI Version

```bash
python weathergui.py
```

Enter your city name in the search bar of the GUI.

## 🔗 UI Design

UI originally created in Figma and converted into a `tkinter` interface.  
**[Link to UI Design]** (Replace with your actual link)

## 📡 Requirements

- Python 3.x
- Internet connection (app won't work offline)
- API key from [OpenWeatherMap](https://openweathermap.org/api)

