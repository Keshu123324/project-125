from flask import Flask,jsonify,request
from classifier import get_prediction

app=Flask(__name__)

@app.route("/pred-alphabet")
def pred_data(): 
    image=request.files.get("alphabet")
    prediction=get_prediction(image)
    return jsonify({
        "prediction": prediction
    }),200

if(__name__=="__main__"):
    app.run()
