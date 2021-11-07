from googlesearch import search
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

outputs = []
def searchgoogle(query):
  for i in search(query, tld='co.in', lang='en', num=5, start=0, stop=5, pause=2):
    outputs.append(i)


@app.route('/', methods=['POST'])
def searching():
  query = request.form['text']
  f = open("searchhistory.txt", "a")
  f.write(query+"\n")
  f.close()
  searchgoogle(query)

  output0 = outputs[0]
  output1 = outputs[1]
  output2 = outputs[2]
  output3 = outputs[3]
  output4 = outputs[4]

  outputs.clear()

  return render_template('index.html', output0=output0, output1=output1, output2=output2, output3=output3, output4=output4)

app.run(host='0.0.0.0', port=8080)
