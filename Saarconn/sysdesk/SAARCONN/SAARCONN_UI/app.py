from flask import Flask, request, jsonify, render_template
import os
import subprocess
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'xlsx', 'xls', 'sdp'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Max file size: 16 MB

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')  # This renders the HTML page

@app.route('/uploadExcelFile', methods=['POST'])
def upload_excel_file():
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'}), 400
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Call Python script with the uploaded file path
        result = subprocess.run(['python', '05-12.py', file_path], capture_output=True, text=True)
        
        return jsonify({'message': f"File uploaded and processed: {result.stdout}"}), 200
    return jsonify({'message': 'Invalid file format'}), 400

@app.route('/uploadExcelAndSdpFiles', methods=['POST'])
def upload_excel_and_sdp_files():
    if 'excel_file' not in request.files or 'sdp_file' not in request.files:
        return jsonify({'message': 'Missing files'}), 400

    excel_file = request.files['excel_file']
    sdp_file = request.files['sdp_file']

    if excel_file and allowed_file(excel_file.filename) and sdp_file and allowed_file(sdp_file.filename):
        excel_filename = secure_filename(excel_file.filename)
        sdp_filename = secure_filename(sdp_file.filename)

        excel_file_path = os.path.join(app.config['UPLOAD_FOLDER'], excel_filename)
        sdp_file_path = os.path.join(app.config['UPLOAD_FOLDER'], sdp_filename)

        excel_file.save(excel_file_path)
        sdp_file.save(sdp_file_path)

        # Call Python script with both file paths
        result = subprocess.run(['python', 'edit_old_project.py', excel_file_path, sdp_file_path], capture_output=True, text=True)

        return jsonify({'message': f"Files uploaded and processed: {result.stdout}"}), 200
    return jsonify({'message': 'Invalid file format'}), 400

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER) 
    app.run(debug=True)
