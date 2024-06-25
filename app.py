from flask import Flask, request, jsonify
from recommeder_function import build_chart  # Import your module containing the build_chart function

app = Flask(__name__)

@app.route('/recommendations', methods=['GET'])
def get_recommendations():
    # Extract parameters from the request query string
    genre = request.args.get('genre')
    low_time = request.args.get('low_time')
    high_time = request.args.get('high_time')
    low_year = request.args.get('low_year')
    high_year = request.args.get('high_year')
    
    # Call the build_chart function with the provided parameters
    recommendations = build_chart(genre, low_time, high_time, low_year, high_year)
    
    # Convert the DataFrame to JSON and return as the API response
    return  jsonify({'recommendations':recommendations})

if __name__ == '__main__':
    app.run(debug=True)
