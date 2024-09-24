from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    try:
        with open('/app/flag.txt', 'r') as file:
            flag_content = file.read()
        return flag_content
    except FileNotFoundError:
        return "EQST{Test_Flag}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
