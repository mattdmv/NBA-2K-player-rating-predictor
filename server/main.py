from fastapi import FastAPI, jsonify
import uvicorn
import utility

app = FastAPI()

@app.post('/predict_player_rating')
async def predict_player_rating():
    pts = float(request.form['pts'])
    reb = float(request.form['reb'])
    ast = float(request.form['ast'])
    stl = float(request.form['stl'])
    blk = float(request.form['blk'])
    three_p = float(request.form['three_p'])
    plus_minus = float(request.form['plus_minus'])
    gp = int(request.form['gp'])

    response = jsonify({
        'estimated_rating':utility.get_estimated_rating(pts, reb, ast, stl, blk, three_p, plus_minus, gp)})
        response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__=="__main__":
    print("Starting FastAPI Server for NBA2K player rating prediction!")
    utility.load_saved_artifacts()
    uvicorn.run(app, host='localhost', port=8000)

