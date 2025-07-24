
"""Flask app: Sentiment (exercise1) & Drug (exercise2)
Expect artefacts_ex1/vectorizer.pkl + model.pkl
        artefacts_ex2/model.pkl
The script searches first in the current directory, then one level up.
"""
from flask import Flask, render_template, request
import joblib, numpy as np, os, sys, pathlib

app = Flask(__name__)

def find_artifact(path_parts):
    # try current dir then parent
    here = pathlib.Path(__file__).resolve().parent
    candidate = here.joinpath(*path_parts)
    if candidate.exists():
        return candidate
    parent_candidate = here.parent.joinpath(*path_parts)
    return parent_candidate if parent_candidate.exists() else None

# -------- load artefacts safely ---------
vec_path   = find_artifact(['artefacts_ex1', 'vectorizer.pkl'])
model1_path = find_artifact(['artefacts_ex1', 'model.pkl'])
model2_path = find_artifact(['artefacts_ex2', 'model.pkl'])

if not (vec_path and model1_path and model2_path):
    missing = [p for p, n in [('artefacts_ex1/vectorizer', vec_path),
                              ('artefacts_ex1/model', model1_path),
                              ('artefacts_ex2/model', model2_path)] if n is None]
    sys.exit(f"[ERROR] Missing artefacts: {', '.join(missing)}.\n"
             "Run exercise1.ipynb & exercise2.ipynb with the dump cells to generate them.")

vec_ex1  = joblib.load(vec_path)
model_ex1 = joblib.load(model1_path)
model_ex2 = joblib.load(model2_path)

sex_map  = {'F': 0, 'M': 1}
bp_map   = {'LOW': 0, 'NORMAL': 1, 'HIGH': 2}
chol_map = {'NORMAL': 0, 'HIGH': 1}
drug_map = {1:'drugA', 2:'drugB', 3:'drugC', 4:'drugX', 5:'DrugY'}

# ---------- helper ----------
def predict_sentiment(text):
    X = vec_ex1.transform([text])
    return 'positive' if model_ex1.predict(X)[0]==1 else 'negative'

def predict_drug(age, sex, bp, chol, na_to_k):
    row = [
        float(age), float(na_to_k),
        1 - sex_map[sex], sex_map[sex],
        1 if bp=='HIGH' else 0,
        1 if bp=='LOW' else 0,
        1 if bp=='NORMAL' else 0,
        1 if chol=='HIGH' else 0,
        1 if chol=='NORMAL' else 0
    ]
    pred = model_ex2.predict(np.array([row]))[0]
    return drug_map.get(pred, str(pred))

# ---------- routes ----------
@app.route('/', methods=['GET', 'POST'])
def home():
    sent_res = drug_res = None
    if request.method == 'POST':
        if request.form.get('text'):
            sent_res = predict_sentiment(request.form['text'])
        if request.form.get('age'):
            drug_res = predict_drug(request.form['age'],
                                    request.form['sex'],
                                    request.form['bp'],
                                    request.form['chol'],
                                    request.form['na_to_k'])
    return render_template('index.html', sent_res=sent_res, drug_res=drug_res)

if __name__ == '__main__':
    app.run(debug=True)
