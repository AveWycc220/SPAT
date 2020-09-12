from flask import Flask, render_template, redirect, url_for
import os

DATA_DIR = os.path.join( os.path.dirname( __file__ ))
app = Flask(__name__, template_folder='')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<int:N>')
def show_post(N):
    os.system(f'python src/plots.py {N}')
    return redirect(url_for('index'))

if __name__ == '__main__':
   app.run()