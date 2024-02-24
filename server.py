from flask import Flask, request, jsonify
from indexer import Indexer
import time

app = Flask(__name__)
indexer = Indexer('output.json')
indexer.load_data()

@app.route('/')
def index():
    return app.send_static_file('index.html')

# @app.route('/search')
# def search():
#     query = request.args.get('q', '')
#     results = indexer.search(query)
#     return jsonify(results)


@app.route('/search')
def search():
    query = request.args.get('q', '')
    start_time = time.time()
    results = indexer.search(query)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return jsonify({'results': results, 'elapsed_time': elapsed_time})

if __name__ == "__main__":
    app.run(debug=False, port=8080, host="0.0.0.0")
