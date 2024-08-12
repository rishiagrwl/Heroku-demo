from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get form data
        cgpa = request.form['cgpa']
        iq = request.form['iq']
        profile_score = request.form['profile_score']
        # Add more features as needed

        # Convert form data to the format your model expects (e.g., list, array, etc.)
        data = [[float(cgpa), float(iq), float(profile_score)]]  # Example with two features
        prediction = model.predict(data)[0]  # Get the prediction

        return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0', port=8080)