# from flask import Flask, render_template, request
# import pandas as pd
# import pickle
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.linear_model import LogisticRegression

# app = Flask(__name__)

# # ==============================
# # Train model (run once)
# # ==============================
# df = pd.read_csv("final_polished_student_legal_dataset.csv")

# def train_model():
    

    

#     X = df["question"]
#     y = df["category"]   # CHANGE HERE

#     vectorizer = TfidfVectorizer()
#     X_vec = vectorizer.fit_transform(X)

#     model = LogisticRegression(max_iter=1000)
#     model.fit(X_vec, y)

#     pickle.dump(model, open("model.pkl", "wb"))
#     pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

# # Uncomment below line only first time
# train_model()

# # ==============================
# # Load model
# # ==============================
# model = pickle.load(open("model.pkl", "rb"))
# vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# # ==============================
# # Routes
# # ==============================
# @app.route("/", methods=["GET", "POST"])
# def home():
#     response = ""

#     if request.method == "POST":
#         user_input = request.form["question"]

#         vec = vectorizer.transform([user_input])
#         predicted_category = model.predict(vec)[0]

#         # t best matching answer from dataset
#         filtered = df[df["category"] == predicted_category]

#         if not filtered.empty:
#             response = filtered.iloc[0]["answer"]
#         else:
#             response = "No proper legal advice found."

#     return render_template("index.html", response=response)


# if __name__ == "__main__":
#     app.run(debug=True)
# ==============================
# Student Legal Advisor AI (Advanced Version)
# ==============================

# from flask import Flask, render_template, request
# import pandas as pd
# import pickle
# import numpy as np
# import re
# from sklearn.metrics.pairwise import cosine_similarity

# app = Flask(__name__)

# # ==============================
# # LOAD DATASET
# # ==============================
# df = pd.read_csv("final_polished_student_legal_dataset.csv")

# # ==============================
# # LOAD MODEL & VECTORIZER
# # ==============================
# model = pickle.load(open("model.pkl", "rb"))
# vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# ==============================
# HOME ROUTE
# ==============================
# @app.route("/", methods=["GET", "POST"])
# def home():
#     response = ""
#     user_input = ""

#     if request.method == "POST":
#         user_input = request.form["question"]

#         # 🔹 Clean input
#         cleaned_input = user_input.lower()
#         cleaned_input = re.sub(r"[^a-zA-Z0-9 ]", "", cleaned_input)

#         # 🔹 Convert input to vector
#         input_vec = vectorizer.transform([cleaned_input])

#         # 🔹 Convert dataset questions
#         all_vec = vectorizer.transform(df["question"])

#         # 🔹 Compute similarity
#         similarity = cosine_similarity(input_vec, all_vec)

#         # 🔹 Get best match
#         best_index = np.argmax(similarity)
#         confidence = similarity[0][best_index]

#         # 🔹 Response logic
#         if confidence > 0.3:
#             answer = df.iloc[best_index]["answer"]
#             category = df.iloc[best_index]["category"]

#             response = f"[{category}] {answer} (Confidence: {round(confidence*100,2)}%)"
#         else:
#             response = "Sorry, I couldn't understand your legal issue clearly. Please rephrase your question."

#     return render_template("index.html", response=response, user_input=user_input)


# # ==============================
# # RUN APP
# # ==============================
# if __name__ == "__main__":
#     app.run(debug=True)

# # ==============================
# # Student Legal Advisor AI (Final Version)
# # ==============================

# from flask import Flask, render_template, request
# import pandas as pd
# import pickle
# import numpy as np
# import re
# from sklearn.metrics.pairwise import cosine_similarity

# app = Flask(__name__)

# # ==============================
# # LOAD DATASET
# # ==============================
# df = pd.read_csv("final_polished_student_legal_dataset.csv")

# # ==============================
# # LOAD MODEL & VECTORIZER
# # ==============================
# model = pickle.load(open("model.pkl", "rb"))
# vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# # ==============================
# # HOME ROUTE
# # ==============================
# @app.route("/", methods=["GET", "POST"])
# def home():
    
#     global model, vectorizer   # ✅ ADD THIS LINE
#     response = ""
#     user_input = ""

#     if request.method == "POST":

#         # ==============================
#         # 🧠 HANDLE QUESTION
#         # ==============================
#         if request.form.get("form_type") == "question":
#             user_input = request.form["question"]

#             # 🔹 Clean input
#             cleaned_input = user_input.lower()
#             cleaned_input = re.sub(r"[^a-zA-Z0-9 ]", "", cleaned_input)

#             # 🔹 Vectorize input
#             input_vec = vectorizer.transform([cleaned_input])

#             # 🔹 Vectorize dataset
#             all_vec = vectorizer.transform(df["question"])

#             # 🔹 Compute similarity
#             similarity = cosine_similarity(input_vec, all_vec)

#             # 🔹 Best match
#             best_index = np.argmax(similarity)
#             confidence = similarity[0][best_index]

#             # 🔹 Response logic
#             if confidence > 0.3:
#                 answer = df.iloc[best_index]["answer"]
#                 category = df.iloc[best_index]["category"]

#                 response = f"[{category}] {answer} (Confidence: {round(confidence*100,2)}%)"
#             else:
#                 response = "Sorry, I couldn't understand your legal issue clearly. Please rephrase your question."

#     #     # ==============================
#     #     # 👍 👎 HANDLE FEEDBACK
#     #     # ==============================
#     #     elif request.form.get("form_type") == "feedback":
#     #         fb = request.form["feedback"]
#     #         q = request.form["feedback_question"]
#     #         a = request.form["feedback_answer"]

#     #         # Save feedback
#     #         with open("feedback.csv", "a", encoding="utf-8") as f:
#     #             f.write(f"{q},{a},{fb}\n")

#     #         response = "Thank you for your feedback!"

#     # return render_template("index.html", response=response, user_input=user_input)
#     # Improved feedback learning algorithm
#     # ==============================
# # 👍 👎 HANDLE FEEDBACK (AUTO LEARNING)
# # ==============================
#         elif request.form.get("form_type") == "feedback":
#             fb = request.form["feedback"]
#             q = request.form["feedback_question"]
#             a = request.form["feedback_answer"]

#         # Save feedback log
#             with open("feedback.csv", "a", encoding="utf-8") as f:
#                 f.write(f"{q},{a},{fb}\n")

#     # ==============================
#     # ✅ IF FEEDBACK IS GOOD → LEARN
#     # ==============================
#             if fb == "good":
#         # Load dataset
#                 df = pd.read_csv("final_polished_student_legal_dataset.csv")

#         # Add new learned entry
#                 new_row = {
#                     "question": q,
#                     "category": "User Learned",
#                     "law": "Feedback",
#                     "answer": a,
#                     "severity": "Medium",
#                     "action": "Learned"
#                 }

#                 df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

#         # Save updated dataset
#                 df.to_csv("final_polished_student_legal_dataset.csv", index=False)

#         # ==============================
#         # 🔁 RETRAIN MODEL
#         # ==============================
#                 from sklearn.feature_extraction.text import TfidfVectorizer
#                 from sklearn.linear_model import LogisticRegression

#                 X = df["question"]
#                 y = df["answer"]

#                 vectorizer = TfidfVectorizer()
#                 X_vec = vectorizer.fit_transform(X)

#                 model = LogisticRegression(max_iter=1000)
#                 model.fit(X_vec, y)

#         # Save updated model
#                 pickle.dump(model, open("model.pkl", "wb"))
#                 pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

#                 response = "👍 Thanks! I learned from this and improved."
    
#     # ==============================
#     # ❌ BAD FEEDBACK
#     # ==============================
#             else:
#                 response = "👎 Thanks! I will try to improve this answer."
#     return render_template("index.html", response=response, user_input=user_input)
# # ==============================
# # RUN APP
# # ==============================
# if __name__ == "__main__":
#     app.run(debug=True)

# ==============================
# Student Legal Advisor AI (Final Improved Version)
# ==============================

from flask import Flask, render_template, request
import pandas as pd
import pickle
import numpy as np
import re
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

# ==============================
# LOAD DATASET
# ==============================
df = pd.read_csv("final_polished_student_legal_dataset.csv")

# ==============================
# LOAD MODEL & VECTORIZER
# ==============================
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# ==============================
# HOME ROUTE
# ==============================
@app.route("/", methods=["GET", "POST"])
def home():
    global model, vectorizer, df   # ✅ important

    response = ""
    user_input = ""

    if request.method == "POST":

        form_type = request.form.get("form_type")

        # ==============================
        # 🧠 HANDLE QUESTION
        # ==============================
        if form_type == "question":
            user_input = request.form["question"]

            # Clean input
            cleaned_input = user_input.lower()
            cleaned_input = re.sub(r"[^a-zA-Z0-9 ]", "", cleaned_input)

            # Vectorize
            input_vec = vectorizer.transform([cleaned_input])
            all_vec = vectorizer.transform(df["question"])

            # Similarity
            similarity = cosine_similarity(input_vec, all_vec)

            best_index = np.argmax(similarity)
            confidence = similarity[0][best_index]

            if confidence > 0.3:
                answer = df.iloc[best_index]["answer"]
                category = df.iloc[best_index]["category"]

                response = f"[{category}] {answer} (Confidence: {round(confidence*100,2)}%)"
            else:
                response = "Sorry, I couldn't understand your legal issue clearly. Please rephrase your question."

        # ==============================
        # 👍 👎 HANDLE FEEDBACK
        # ==============================
        elif form_type == "feedback":

            fb = request.form["feedback"]
            q = request.form["feedback_question"]
            a = request.form["feedback_answer"]

            # Save feedback log
            with open("feedback.csv", "a", encoding="utf-8") as f:
                f.write(f"{q},{a},{fb}\n")

            # ==============================
            # ✅ GOOD FEEDBACK → LEARN
            # ==============================
            if fb == "good":

                # Avoid duplicate learning
                if q not in df["question"].values:

                    new_row = {
                        "question": q,
                        "category": "User Learned",
                        "law": "Feedback",
                        "answer": a,
                        "severity": "Medium",
                        "action": "Learned"
                    }

                    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

                    # Save dataset
                    df.to_csv("final_polished_student_legal_dataset.csv", index=False)

                    # 🔁 Retrain model
                    X = df["question"]
                    y = df["answer"]

                    vectorizer = TfidfVectorizer()
                    X_vec = vectorizer.fit_transform(X)

                    model = LogisticRegression(max_iter=1000)
                    model.fit(X_vec, y)

                    # Save updated model
                    pickle.dump(model, open("model.pkl", "wb"))
                    pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

                    response = "👍 Thanks! I learned from this and improved."

                else:
                    response = "👍 Already learned this!"

            # ==============================
            # ❌ BAD FEEDBACK
            # ==============================
            else:
                response = "👎 Thanks! I will try to improve this answer."

    return render_template("index.html", response=response, user_input=user_input)


# ==============================
# RUN APP
# ==============================
if __name__ == "__main__":
    app.run(debug=True)