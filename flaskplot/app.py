from flask import Flask, render_template, request,redirect
from werkzeug.utils import secure_filename
import os
import plotly
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import chart_studio.plotly as py
import numpy as np
import pandas as pd
import json

app = Flask (__name__)
app.config['UPLOAD_FOLDER'] = './static'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/pyplot', methods=['POST'])
def pyplot():
    request.method == 'POST'
    myFile = request.files['fileku']
    fn = secure_filename(myFile.filename)

    df = pd.read_csv(fn)
    x = np.array(list(df['x']))
    y = np.array(list(df['y']))
    plot = go.Scatter(x = x,y = y)

    plot = [plot]
    plotJSON = json.dumps(plot, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('plot.html', x=plotJSON)

@app.route('/matplotlib', methods=['POST'])
def matplotlib():
    request.method == 'POST'
    myFile = request.files['fileku']
    fn = secure_filename(myFile.filename)

    df = pd.read_csv(fn)
    x = np.array(list(df['x']))
    y = np.array(list(df['y']))

    plt.plot(x,y, linestyle='-',marker='o', color='red')
    plt.title('Matplotlib Grafik Plotting', fontdict={'fontsize':30})
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.savefig('./static/graph.png')
    return render_template('visual2.html')

if __name__ == '__main__':
    app.run(debug=True)