
from flask import Flask, request, render_template
from sklearn.feature_extraction.text import CountVectorizer
import joblib
import re


# Declare a Flask app
app = Flask(__name__)

# Main function here
# ------------------

@app.route('/', methods=['GET', 'POST'])
def main():
    
    # If a form is submitted
    if request.method == "POST":
        
        # Unpickle classifier
        clf = joblib.load("clf.pkl")
        
        # Get values through input bars
        text = request.form.get("text_input")
        vector = joblib.load('vectorizer.pickle')

        #Removes the punctuation from the real_df data frame.
        #Process text

        text = re.sub(r'[^\w\s]','',text)
        #Removes the numerals from the real_df data frame.
        text = text.replace('\d+','')
        #Removes the quotation marks from the real_df data frame.
        text = re.sub(r'\"', '', text)
        #Lower case for all text.
        text= text.lower()

        t = vector.transform([text])


        # Get prediction
        prediction = clf.predict_proba(t)[0]
        
    else:
        prediction = ""
        
    return render_template("website.html", output = prediction)


# Running the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug = True)
