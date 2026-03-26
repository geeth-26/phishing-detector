from flask import Flask, render_template, request
import pickle
from feature_extraction import extract_features

app = Flask(__name__)

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    url = request.form['url'].lower()

    # ✅ 1. TRUSTED WEBSITES (TOP PRIORITY)
    trusted_sites = ["google.com", "youtube.com", "facebook.com", "amazon.com"]

    if any(site in url for site in trusted_sites):
        result = "Legitimate Website ✅ (Trusted)"
        color = "limegreen"
        return render_template('index.html', prediction_text=result, color=color)

    # ✅ 2. RULE-BASED DETECTION
    suspicious_keywords = ["login", "secure", "bank", "update", "free"]

    if "@" in url:
        result = "Phishing Website ❌ (Detected '@')"
        color = "red"
        return render_template('index.html', prediction_text=result, color=color)

    if any(word in url for word in suspicious_keywords):
        result = "Phishing Website ❌ (Suspicious keywords)"
        color = "red"
        return render_template('index.html', prediction_text=result, color=color)

    if url.count(".") > 3:
        result = "Phishing Website ❌ (Too many subdomains)"
        color = "red"
        return render_template('index.html', prediction_text=result, color=color)

    # ✅ 3. MACHINE LEARNING
    features = extract_features(url)

    prediction = model.predict([features])[0]
    prob = model.predict_proba([features])[0]
    confidence = round(max(prob) * 100, 2)

    if prediction == 1:
        result = f"Legitimate Website ✅ ({confidence}%)"
        color = "limegreen"
    else:
        result = f"Phishing Website ❌ ({confidence}%)"
        color = "red"

    return render_template('index.html', prediction_text=result, color=color)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)