
from flask import Flask,render_template,request
import pickle
import numpy as np
import pandas as pd

model=pickle.load(open('model.pkl','rb'))


app=Flask(__name__)
@app.route('/')
def home():
    return render_template('debetes.html')

@app.route('/predict',methods=["POST"])
def predict():
    item=[x for x in request.form.values()]
    data=[]

    data.append(int(item[0]))
    if item[1] == 'Male' :
        data.append(1)
    else:
        data.append(0)
    if item[2]=='Yes':
        data.append(1)
    else:
        data.append(0)
    if item[3]=='Yes':    
        data.append(1)
    else:
        data.append(0)
    if item[4]=='Yes':    
        data.append(1)
    else:
        data.append(0)
    if item[5]=='Yes':    
        data.append(1)
    else:
        data.append(0)
    if item[6]=='Yes':    
        data.append(1)
    else:
        data.append(0)
    if item[7]=='Yes':    
        data.append(1)
    else:
        data.append(0)
    if item[8]=='Yes':    
        data.append(1)
    else:
        data.append(0)
    if item[9]=='Yes':    
        data.append(1)
    else:
        data.append(0)
    if item[10]=='Yes':    
        data.append(1)
    else:
        data.append(0)
    if item[11]=='Yes':    
        data.append(1)
    else:
        data.append(0)
    if item[12]=='Yes':    
        data.append(1)
    else:
        data.append(0)
    if item[13]=='Yes':    
        data.append(1)
    else:
        data.append(0)
    if item[14]=='Yes':    
        data.append(1)
    else:
        data.append(0)
    if item[15]=='Yes':    
        data.append(1)
    else:
        data.append(0)
    pred=model.predict([data])
    if pred==1:
        final="Positive"
    else:
        final= "Negative"

    return render_template('debetes.html',prediction_text='Diabetes result - {}'.format(final))

if __name__=="__main__":   
    app.run(debug=True)
    
