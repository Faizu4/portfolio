from flask import Flask, send_from_directory
import os  # add this

app = Flask(__name__)

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    # Change this line:
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)
