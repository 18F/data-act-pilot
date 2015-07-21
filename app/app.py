from flask import Flask, request, url_for, render_template 
import os

app = Flask(__name__)

ALLOWED_EXTENSIONS = ['csv']

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        file = request.files['file']
        filename = None
        if file and allowed_file(file.filename):
            filename = file.filename
            # process file

        return render_template('home.html', upload_filename=filename)

    return render_template('home.html')

if __name__ == "__main__":
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
