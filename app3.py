import os
import uuid
import pandas as pd
from flask import Flask, render_template, request, Response, send_from_directory, jsonify
import PyPDF2

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'basuck' and password == 'Basu#@2103':
            return "welcome"
        else: 
            return "wrong credentials"
        
@app.route('/file_upload', methods=['POST'])
def file_upload():
    file = request.files['file']

    if file.content_type == 'text/plain':
        return file.read().decode()
    
    elif file.content_type in (
        'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        'application/vnd.ms-excel'
    ):
        df = pd.read_excel(file)
        return df.to_html()
    
    elif file.content_type == 'application/pdf':
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() or ""   # extract text page by page
        return f"<pre>{text}</pre>"

    else:
        return "Unsupported file type"

@app.route('/convert_csv', methods=['POST'])
def convert_csv():
    file= request.files['file']
 
    df= pd.read_excel(file)
    response= Response(
        df.to_csv(), 
        mimetype='text/csv',
        headers={
            'Content-Disposition': 'attachment; filename=result.csv'
        }
    )
    return response

@app.route('/convert_csv_two', methods=['POST'])
def convert_csv_two():
    file= request.files['file']
    df= pd.read_excel(file)

    if not os.path.exists('temp'):
        os.makedirs('temp')
    filename= f'{uuid.uuid4()}.csv'
    df.to_csv(os.path.join('temp', filename))

    return render_template('download.html', filename= filename)

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory('temp', filename, download_name= 'result.csv')

@app.route('/handle_post', methods=['POST'])
def handle_post():
    data = request.get_json()
    greeting = data.get('greeting')
    name = data.get('name')

    # Write to file
    with open('file.txt', 'w') as f:
        f.write(f'{greeting}, {name}')

    return jsonify({'message': 'Successfully written'})


# main  
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)




# stoppen at json part of 
