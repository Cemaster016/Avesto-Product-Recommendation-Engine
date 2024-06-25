# Avesto Recommendation System

## Overview
This recommendation system was developed for Avesto, an organization that deals with selling stocks and other investment products. The system utilizes knowledge-based (average weighted method) and content-based recommendation techniques to provide personalized investment recommendations to users.

## Features
- **Knowledge-Based Recommendation**: The system uses the average weighted method to recommend investments based on the user's past interactions and preferences. It calculates the average weight of each investment product based on the user's ratings or interactions and recommends products with higher average weights.
  
- **Content-Based Recommendation**: The system also utilizes content-based recommendation techniques to recommend investment products similar to those the user has previously shown interest in. It analyzes the features of each investment product (e.g., risk level, return rate, industry sector) and recommends products with similar features to those the user has liked or interacted with.

## Technologies Used
- **Python**: Used for implementing the recommendation algorithms and the backend logic.
- **Pandas**: Used for data manipulation and analysis.
- **Flask**: Used for creating a web interface for users to interact with the recommendation system.
- **SQL Server**: Used for storing user and investment product data.

## Usage
1. Clone the repository: git clone https://github.com/Cemaster016/Avesto-Product-Recommendation-Engine.git
2. Install the required libraries: pip install -r requirements.txt
3. Run the Flask app: app.py
4. Access the web interface in your browser at http://localhost:5000

## Future Improvements
- **Enhanced Recommendation Algorithms**: Implement more advanced recommendation algorithms such as collaborative filtering to improve recommendation accuracy.
- **User Profiling**: Develop user profiling techniques to better understand user preferences and improve recommendation quality.
- **Integration with External Data Sources**: Integrate external data sources such as financial news and market trends to provide more context-aware recommendations.

## Credits
- Developed by Adeniyi Olaolu Peter
- Inspired by the needs of Avesto organization
