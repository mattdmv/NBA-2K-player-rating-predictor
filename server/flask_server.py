from flask import Flask, request, jsonify
import utility
 
app = Flask(__name__)

@app.route('/predict_player_rating', methods=['GET', 'POST'])
def predict_player_rating():
    player_name = request.form['player_name']

    response = jsonify({
        'predicted_value': utility.main_pipeline(player_name), 
        'player_stats': utility.transform_player_stats(player_name)
        })

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__=="__main__":
    print("Starting FastAPI Server for NBA2K player rating prediction!")
    app.run()
 