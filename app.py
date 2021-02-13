from flask import Flask
from flask import render_template, Response, request
import time, os
from time import sleep

app = Flask(__name__)

def get_message():
    s = time.ctime(time.time())
    return s

def get_file_content(filename):
    path = os.path.join('files', filename + '.txt')
    if os.path.exists(path):
        f = open(path, 'r')
        content = f.read()
        f.close()
        return content
    return f'File {filename}.txt not found!'

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/other')
def other():
    x = sum([x for x in range(100000)])
    return render_template('test.html', value = x)

@app.route('/stream_with_args')
def stream_with_value():
    file_name = request.args.get('file_name')
    def eventStream():
        while True:
            sleep(0.1)
            yield 'data: {}\n\n'.format(get_file_content(file_name))
    return Response(eventStream(), mimetype="text/event-stream")

@app.route('/stream')
def stream():
    def eventStream():
        while True:
            sleep(0.1)
            yield 'data: {}\n\n'.format(get_message())
    return Response(eventStream(), mimetype="text/event-stream")

if __name__ == '__main__':
    app.run(port=5000, debug=True)