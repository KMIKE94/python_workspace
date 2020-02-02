from flask import Flask
import webscraper

app = Flask(__name__)

@app.route("/thejournal")
def theJournalStories():
    return webscraper.getResults('http://thejournal.ie')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)