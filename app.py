from flask import Flask,redirect,render_template,request
import pickle
import pandas as pd
app=Flask(__name__)


# code
model=pickle.load(open('svc_model.pkl','rb'))
output='Your result will be showed here'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method=='POST':
        clump_thickness=request.form["clump_thickness"]
        size_uniformity=request.form['size_uniformity']
        shape_uniformity=request.form['shape_uniformity']
        marginal_adhesion=request.form['marginal_adhesion']
        epithelial_size=request.form['epithelial_size']
        bare_nucleoli=request.form['bare_nucleoli']
        bland_chromatin=request.form['bland_chromatin']
        normal_nucleoli=request.form['normal_nucleoli']
        mitoses=1

        
        result=model.predict(pd.DataFrame([[float(clump_thickness),
        float(size_uniformity),
        float(shape_uniformity),
        float(marginal_adhesion),
        float(epithelial_size),
        float(bare_nucleoli),
        float(bland_chromatin),
        float(normal_nucleoli),
        float(mitoses)
        ]]))[0]

        if int(result)==2:
            output='The Cell is Benign'
        else:
            output='The Cell is Malignant'    
        return render_template('index.html',prediction=output)
    return render_template('index.html') 

         
if __name__=='__main__':
    app.run(debug=True)
