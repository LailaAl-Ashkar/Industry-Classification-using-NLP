#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


# In[7]:


app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


# In[8]:


@app.route('/')
def home():
    return render_template('index.html')


# In[9]:


@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    X = [str(x) for x in request.form.values()]
    prediction = model.predict(X)

    return render_template('index.html', prediction_text='Industry: {}'.format(prediction))


# In[10]:


@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([list(data.values())])

    return jsonify(prediction)


# In[11]:


if __name__ == "__main__":
    app.run(debug=True)

