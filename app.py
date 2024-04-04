from flask import Flask, render_template, request, redirect, url_for
import plotly.graph_objects as go
import numpy as np
# from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__) 
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
# app.config['SQLALCHEMY_TRACK _MODIFICATIONS'] = False
# db = SQLAlchemy (app)


# class Database(db.Model):
#     sno = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(200), nullable=False)
#     desc = db.Column(db.String(500), nullable=False)
#     date_created = db.Column(db.DateTime, default=datetime.utcnow)
def plot(csvfile):
        np.random.seed(42)
        x = np.random.normal(loc=0, scale=1, size=100)
        y = np.random.normal(loc=0, scale=1, size=100)
        # Create a scatter plot figure using Plotly
        fig = go.Figure()
        # Add a scatter trace to the figure
        fig.add_trace(go.Scatter(x=x, y=y, mode='markers'))
        # Update layout and axis labels
        fig.update_layout(
            title='Scatter Plot',
            xaxis_title='X',
            yaxis_title='Y'
        )
        # Convert the plot to JSON
        plot_html=fig.to_html(full_html=False)
        return plot_html

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/csvfile', methods=['GET', 'POST'])
def csvfile():
    return render_template('csvfile.html')


@app.route('/input', methods=['GET', 'POST'])
def input():
    csvfile=None
    if request.method=="POST":
        csvfile=request.form["csvfile"]
        return render_template("csvfile.html",csvfile=csvfile)
        # if 'csvfile' in request.form:
        #     return redirect(url_for('analysis',csvfile=csvfile))
        # else:
        #     return redirect(url_for('prediction'))

# this mesaage is added
@app.route('/analysis', methods=['GET', 'POST'])
def analysis():
    if request.method=="POST":
        csvfile = request.args.get('csvfile')
        plot_html=plot(csvfile)
    return render_template('Analysis.html',plot_html=plot_html)



@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method=="POST":
        return render_template('Prediction.html')



@app.route('/dataentry', methods=['GET', 'POST'])
def dataentry():
    if request.method=="POST":
        return render_template('Prediction.html')



if __name__ == '__main__':
    app.run(debug=True) 