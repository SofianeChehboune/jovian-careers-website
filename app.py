from flask import Flask, render_template, jsonify

app= Flask(__name__)
JOBS=[
  {
    'id':1,
    'title':'Data analyst',
    'location':'Boumerdes, Algerie',
    'salary' : 'Rs. 50 000,00 DZD'
  },
    {
    'id':2,
    'title':'computer scientist',
    'location':'Boumerdes, Algerie',
    'salary' : 'Rs. 50 000,00 DZD'
  },
    {
    'id':3,
    'title':'Frontend Enginner',
    'location':'Remote'
  },
    {
    'id':4,
    'title':'Backend Enginner',
    'location':'Tipaza, Algerie',
    'salary' : 'Rs. 70 000,00 DZD'
  },
]
@app.route("/")
def hello_world():
  return render_template('home.html',
                         jobs=JOBS,
                         company_name= 'jovian')
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
                         
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)