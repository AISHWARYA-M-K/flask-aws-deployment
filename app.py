from flask import Flask, render_template, jsonify
import platform
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html',
                         title='Flask on AWS EC2!',
                         message='Your Flask app is running successfully!',
                         python_version=platform.python_version(),
                         current_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

@app.route('/about')
def about():
    return jsonify({
        'app_name': 'Flask AWS Demo',
        'version': '1.0.0',
        'environment': 'Ubuntu 24.10',
        'python_version': platform.python_version(),
        'server_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
