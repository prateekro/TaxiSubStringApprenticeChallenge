from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/test', methods = ['POST'])
def lyft():
    if request.method == 'POST':
        data = request.get_json()
        output = ""
        if data is not None:
            for enum, i in enumerate(list(data['string_to_cut'])):
                if enum%3 == 2:
                    output += i
            return '%s' % output
        else:
            return ""

with app.test_client() as lyftCase:
    resp = lyftCase.post('/test', json={
        'string_to_cut': 'iamyourlyftdriver'
    })
    if resp.data.decode('utf-8') == 'muydv':
        print('Test Success:', resp.data.decode('utf-8'))

if __name__ == '__main__':
    app.run()
