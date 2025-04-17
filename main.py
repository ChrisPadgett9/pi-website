from flask import Flask, request, jsonify, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run_command():
    try:
        command = request.json.get('command')
        if not command:
            return jsonify({'error': 'No command provided'}), 400

        # Execute the command securely
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return jsonify({
            'stdout': result.stdout,
            'stderr': result.stderr,
            'returncode': result.returncode
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337)