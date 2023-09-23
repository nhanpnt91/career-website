from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,000,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary':  'Rs. 15,000,000'
  }
]

@app.route('/')
def hello_me():
  return render_template('home.html', jobs=JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)