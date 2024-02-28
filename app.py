from flask import Flask, render_template, request, send_file
import subprocess
import os
import pandas as pd
import matplotlib.pyplot as plt
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads'
ALLOWED_EXTENSIONS = {'csv'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    result = None
    if request.method == 'POST':
        selected_options = request.form.getlist('analysisType')
        uploaded_file = request.files['fileUpload']
        if uploaded_file and allowed_file(uploaded_file.filename):
            filename = secure_filename(uploaded_file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            uploaded_file.save(file_path)
            results = []
            for option in selected_options:
                if option == 'Average Tree Height':
                    subprocess.run(['python', 'pyscripts/average_height.py', file_path])
                    results.append('Tree_height.png') 
                elif option == 'Average Tree Width':
                    subprocess.run(['python', 'pyscripts/average_width.py', file_path])
                    results.append('Tree_width.png')
                elif option == 'Diversity Map':
                    subprocess.run(['python', 'pyscripts/distribution_map.py', file_path])
                    results.append('diversity_map.png')
                    results.append('diversity.html')
                elif option == 'Distribution of Trees':
                    subprocess.run(['python', 'pyscripts/pie_diversity.py', file_path])
                    results.append('Distribution.png')
                elif option == 'Heat Map':
                    subprocess.run(['python', 'pyscripts/heatmap_carbonseq.py', file_path])
                    results.append('carbon_seq_gabgal.png')
                    results.append('carbon_seq_gabgal.html')
                elif option == 'Summary Table':
                    subprocess.run(['python', 'pyscripts/summary_table.py', file_path])
                    results.append('summary_table.png')
            return render_template('upload.html', results=results)
    return render_template('upload.html', result=result)

# @app.route('/download/<filename>')
# def download_file(filename):
#     path = f'pyscripts/{filename}'
#     if os.path.exists(path):
#         return send_file(path, as_attachment=True)
#     return "File not found", 404
@app.route('/download/<analysisType>/<filename>')
def download_file(analysisType, filename):
    directory = './pyscripts'  # Specify the directory where the result files are stored
    path = os.path.join(directory, filename)
    if os.path.exists(path):
        return send_file(path, as_attachment=True)
    return "File not found", 404

if __name__ == '__main__':
    app.run(debug=True)


#Popup window before the upload option which include a preview csv file