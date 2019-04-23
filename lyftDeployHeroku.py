from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route('/test', methods = ['POST'])
def lyft():
    if request.method == 'POST':
        data = request.get_json()
        output = ""
        if data is not None:
            for enum, character in enumerate(list(data['string_to_cut'])):
                if enum%3 == 2:
                    output += character
        return jsonify({"return_string": output})

with app.test_client() as lyftCase:
    resp = lyftCase.post('/test', json={
        'string_to_cut': 'iamyourlyftdriver'
    })
    if resp.data.decode('utf-8') == '{"return_string":"muydv"}\n':
        print('Test Success:', resp.data.decode('utf-8'))
    else:
        print('Test Failed')

if __name__ == '__main__':
    app.run()
