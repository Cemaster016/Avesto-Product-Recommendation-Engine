# from flask import Flask, request, jsonify
#from Avesto import build_chart

#app = Flask(__name__)

#@app.route('/result', methods=['GET'])
#def build_chart_api():
 #   categories = request.args.get('categories')
  #  result = build_chart(categories)
   # return jsonify([result]) 


#if __name__ == '__main__':
 #   app.run(debug=True)
  #  
from flask import Flask, request, jsonify
from Avesto import build_chart

app = Flask(__name__)

@app.route('/result', methods=['GET'])
def build_chart_api():
    categories = request.args.getlist('categories')  # Get list of categories from the request
    result = build_chart(*categories)  # Pass categories as individual arguments
    return jsonify(result)  # Return the result as a JSON array

if __name__ == '__main__':
    app.run(debug=True)
