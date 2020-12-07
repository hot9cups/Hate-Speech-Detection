from flask import Flask, render_template, request
import pickle


app = Flask(__name__, template_folder='templates')
model = pickle.load(open("model.pkl", 'rb'))
cv = pickle.load(open('count_vect', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET','POST'])
def predict():
    message = request.form.get('text')
    data = [message]
    vect = cv.transform(data).toarray()
    pred = model.predict(vect)
    return render_template('result.html', prediction = pred, msg = message)


if __name__ == '__main__':
    import warnings
    warnings.warn("use 'python -m nltk', not 'python -m nltk.downloader'",         DeprecationWarning)
    app.run(port=5000, debug=True)
