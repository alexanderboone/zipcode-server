import os
from flask import Flask

app = Flask(__name__)

with open('zipcodes-lat-long.txt') as f:
    zipcodes = {}
    for line in f.readlines():
        data = line.strip().split(',')
        zipcodes[data[0].strip()] = data[1:]

@app.route('/<zipcode>/')
def get_coordinates(zipcode):
    return str(zipcodes[zipcode])

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)