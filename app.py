from flask import Flask , request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model_pkl','rb'))

@app.route('/')
def home():
    return render_template('recommandation.html')

@app.route('/fill',methods = ['POST','GET'])
def fill():
     if request.method == "POST":
          var = request.form['fromGroupExampleInput9']
     def predict(title):
         song_id = data[data.Title == title]['Index'].values[0]
         scores = list(enumerate([song_id]))
         sorted_scores = sorted(scores,key=lambda x:x[1],reverse = True)
         sorted_scores = sorted_scores[1:]
         j = 0
         k = []
         for item in sorted_scores:
             song_title = data[data.Index == item[0]]['Title'].values[0]
             #q=(j+1,song_title)
             q = (song_title)
             k.append(q)
             j = j+1
             if j > 6:
                 break;
         return k
     data = predict(var)
     return render_template('recommandation.html')

if __name__ == "__main__":
    app.run(debug = True)