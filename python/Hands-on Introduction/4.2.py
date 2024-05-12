import csv
from flask import Flask, jsonify, request

if __name__ == '__main__':
    app = Flask(__name__)

    with open('laureates.csv', 'r', ) as csvfile:
        reader = csv.DictReader(csvfile)
        laureates = list(reader)


    @app.route('/')
    def index():
        return f"We have {len(laureates)} laureates"


    @app.route('/laureates')
    def get_all_laureates():
        return jsonify(laureates)


    @app.route('/laureates/<name>')
    def get_laureate_by_name(name):
        for laureate in laureates:
            if laureate['name'] == name:
                return jsonify(laureate)
        return "Not found"


    @app.route('/laureates/search/<partial_name>')
    def search_laureate(partial_name):
        search_results = []
        for laureate in laureates:
            if partial_name in laureate['name'] or partial_name in laureate['surname']:
                print(laureate['name'], laureate['surname'])
                search_results.append(laureate)
        if len(search_results) > 0:
            return jsonify(search_results)
        return "Not found"


    app.run(debug=True)
