from flask import Flask, request, jsonify
from indexer import Indexer

app = Flask(__name__)
indexer = Indexer('output.json')
indexer.load_data()

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/search')
def search():
    query = request.args.get('q', '')
    results = indexer.search(query)
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=False, port=8080, host="0.0.0.0")
