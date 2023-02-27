from flask import Flask, request, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def Web4Sight():
    return render_template('Web4Sight.html')

@app.route('/get_city',methods=['POST', 'GET'])
def get_city():
    output = request.form.to_dict()
    print(output)
    name = output["city"]
    return name

@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['resume']
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)
    return uploaded_file.filename

@app.route('/outputs', methods=['POST'])
def upload_output(filename):
    uploaded_file = request.files['resume']
    if uploaded_file.filename != '':
        uploaded_file.save(filename)
    return uploaded_file.filename

@app.route('/run_script', methods=['POST'])
def run_script():
    city = get_city()
    path = upload_file()
    results = subprocess.run(['python', 'LinkedIn6.py',path,city], capture_output=True,text=True)#,stdout=subprocess.PIPE
    if results.returncode == 0:
        return 'Script executed successfully!'
    else:
        return 'Nothing was found! Try another search'

@app.route('/post',methods=['POST','GET'])
def post():
    file=request
    return file




if __name__ == '__main__':
    app.run(debug=True)