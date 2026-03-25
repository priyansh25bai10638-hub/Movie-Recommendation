live demo: https://movie-recommendation-e2zkflu8ewuns2dd3fxoaw.streamlit.app/
# Movie-Recommendation
# 🎬 Movie Recommender System

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An interactive movie recommendation application built with **Streamlit** that helps users discover their next favorite film. Say goodbye to decision fatigue - let our algorithm find the perfect movie based on your preferences!

## ✨ Features

- **Multi-criteria Filtering**: Search movies by:
  - Multiple genres (select one or more)
  - Minimum IMDb rating (0.0 to 10.0)
  - Production studio
  - Specific director
- **Smart Matching**: Finds movies matching ALL selected criteria
- **Random Selection**: When multiple movies match, picks one randomly for you
- **Rich Movie Database**: 100+ carefully curated critically acclaimed films
- **Beautiful UI**: Clean, intuitive interface with detailed movie information
- **Real-time Feedback**: Instant recommendations with balloon celebration! 🎈

## 🎯 How It Works

1. **Select your preferences** using the sidebar filters
2. **Click "Get Recommendation"**
3. The system filters the database based on ALL your criteria
4. If matches are found, a random movie is displayed with:
   - Title
   - IMDb rating
   - Production studio
   - Director
   - Full synopsis

## 🛠️ Tech Stack

- **Frontend/UI**: Streamlit
- **Language**: Python 3.7+
- **Data Storage**: Python dictionary (easily expandable)
- **Logic**: Custom filtering algorithm with set operations
- **Randomization**: Python's random module for unbiased picks

## 📊 Database Overview

The movie database includes critically acclaimed films across categories:

### Top Tier (9.0+)
- The Shawshank Redemption (9.3)
- The Godfather (9.2)
- The Dark Knight (9.0)
- Schindler's List (9.0)
- And more classics...

### High Tier (8.5-8.9)
- Pulp Fiction (8.9)
- Inception (8.8)
- The Matrix (8.7)
- Interstellar (8.7)
- And many more...

### Great Tier (8.0-8.4)
- Parasite (8.5)
- La La Land (8.0)
- The Incredibles (8.0)
- Whiplash (8.5)
- And numerous others...

### Diverse Categories
- **Genres**: Drama, Action, Crime, Comedy, Sci-Fi, Animation, Horror, Thriller, and more
- **Studios**: Warner Bros., Paramount, Universal, Pixar, Studio Ghibli, etc.
- **Directors**: Nolan, Spielberg, Tarantino, Scorsese, Miyazaki, and many legends
- **International**: Films from US, UK, Japan, Italy, France, Germany, South Korea, Brazil

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/movie-recommender.git
cd movie-recommender
2. pip install streamlit
3. streamlit run app.py
4. http://localhost:8501
