from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def homepage():
	return """
	<h1>Hello! </h1>
	<p> Use <a href="https://github.com/prateekro/LyftApprenticeChallenge">https://github.com/prateekro/LyftApprenticeChallenge</a> to learn more about the API usage</p>
	<h2>Welcome to the Taxi</h2>
	<img src="http://loremflickr.com/600/400/yellowtaxi">
    """
	
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
    return 'None'

with app.test_client() as lyftCase:
    resp = lyftCase.post('/test', json={
        'string_to_cut': 'iamyourlyftdriver'
    })
    if resp.data.decode('utf-8') == '{"return_string":"muydv"}\n':
        print('Test Success:', resp.data.decode('utf-8'))
    else:
        print('Test Failed')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
