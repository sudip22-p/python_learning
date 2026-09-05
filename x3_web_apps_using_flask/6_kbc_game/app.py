from flask import Flask, render_template, session, redirect, url_for, request
from questions import questions, prizes
import random

app = Flask(__name__)
app.secret_key = "kbc_game_secret_key"


# ------------------------
# Utility Functions
# ------------------------
def get_current_question():
    index = session.get("current_qn", 0)
    order = session.get("question_order")
    if order is None or not isinstance(order, list) or len(order) != len(questions):
        # If order is corrupted, restart the game
        return None
    if index < len(order):
        return questions[order[index]]
    return {}


def use_50_50(options, answer_en):
    correct = next(opt for opt in options if opt["en"] == answer_en)
    others = [opt for opt in options if opt["en"] != answer_en]
    removed = random.sample(others, 2)
    reduced = [correct] + [opt for opt in others if opt not in removed][
        :1
    ]  # Keep 1 wrong
    random.shuffle(reduced)
    return reduced


# ------------------------
# Routes
# ------------------------
@app.route("/")
def index():
    session["current_qn"] = 0
    session["score"] = 0
    session["lifelines"] = {"fifty_fifty": True, "audience": True, "friend": True}
    indices = list(range(len(questions)))
    random.shuffle(indices)
    session["question_order"] = indices
    return redirect(url_for("question"))


@app.route("/question")
def question():
    qn = get_current_question()
    current_index = session.get("current_qn", 0)
    order = session.get("question_order")
    # If session is corrupted (no order), reset. If just out of questions, go to result.
    if order is None or not isinstance(order, list) or len(order) != len(questions):
        return redirect(url_for("index"))
    if current_index >= len(order):
        return redirect(url_for("result"))
    if not qn:
        return redirect(url_for("result"))

    options = qn["options"]
    lifelines = session.get("lifelines")
    if lifelines is None:
        lifelines = {"fifty_fifty": False, "audience": False, "friend": False}
    used = session.get("used_lifeline")
    # Defensive: clamp current_index to valid range
    if current_index < 0:
        current_index = 0
    if current_index >= len(prizes):
        current_index = len(prizes) - 1

    if used == "50-50" and lifelines.get("fifty_fifty") == False and qn is not None and options:
        options = use_50_50(options, qn["answer_en"])

    show_audience_poll = used == "audience" and lifelines.get("audience") == False
    audience_poll_data = list(zip(options, qn["audience_poll"])) if show_audience_poll and "audience_poll" in qn else []

    return render_template(
        "question.html",
        question=qn,
        options=options,
        lifelines=lifelines,
        prizes=prizes,
        current_index=current_index,
        total=len(questions),
        show_audience_poll=show_audience_poll,
        audience_poll_data=audience_poll_data,
        used_lifeline=used
    )


@app.route("/answer", methods=["POST"])
def answer():
    selected = request.form["selected"]
    qn = get_current_question()
    if not qn:
        # If question order is corrupted, restart the game
        return redirect(url_for("index"))
    session["used_lifeline"] = None
    session["selected_answer"] = selected
    session["was_correct"] = selected == qn["answer_en"]
    session["last_qn"] = session.get("current_qn", 0)
    # Do not update score or current_qn here
    return redirect(url_for("feedback"))


@app.route("/lifeline/<type>")
def lifeline(type):
    # Ensure lifelines are initialized
    if "lifelines" not in session:
        session["lifelines"] = {"fifty_fifty": True, "audience": True, "friend": True}
    
    if type in session["lifelines"] and session["lifelines"][type]:
        session["lifelines"][type] = False
        if type == "fifty_fifty":
            session["used_lifeline"] = "50-50"
        elif type == "audience":
            session["used_lifeline"] = "audience"
        elif type == "friend":
            session["used_lifeline"] = "friend"
        else:
            session["used_lifeline"] = None
    return redirect(url_for("question"))


@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    last_index = session.get("last_qn", 0)
    order = session.get("question_order")
    # If session is corrupted (no order), reset. If just out of questions, go to result.
    if order is None or not isinstance(order, list) or len(order) != len(questions):
        return redirect(url_for("index"))
    if last_index >= len(order):
        return redirect(url_for("result"))
    qn = questions[order[last_index]]
    selected = session.get("selected_answer")
    was_correct = session.get("was_correct")
    lifelines = session.get("lifelines")
    if lifelines is None:
        lifelines = {"fifty_fifty": False, "audience": False, "friend": False}
    current_index = last_index
    if current_index < 0:
        current_index = 0
    if current_index >= len(prizes):
        current_index = len(prizes) - 1
    prizes_list = globals()["prizes"]
    if request.method == "POST":
        if "take_money" in request.form:
            return redirect(url_for("result"))
        elif "next_question" in request.form:
            if was_correct:
                session["score"] += 1
            session["current_qn"] = last_index + 1
            session.pop("selected_answer", None)
            session.pop("was_correct", None)
            session.pop("last_qn", None)
            session["used_lifeline"] = None
            return redirect(url_for("question"))
        elif not was_correct:
            return redirect(url_for("wrong"))
    return render_template(
        "feedback.html",
        question=qn,
        options=qn["options"],
        selected=selected,
        was_correct=was_correct,
        lifelines=lifelines,
        prizes=prizes_list,
        current_index=current_index,
        total=len(prizes_list)
    )


@app.route("/wrong")
def wrong():
    return render_template("wrong.html")


@app.route("/result")
def result():
    score = session.get("score", 0)
    if score > 0:
        prize = prizes[score-1]
    else:
        prize = "Rs. 0"
    return render_template("result.html", prize=prize, score=score, total=len(questions))


@app.route("/walkaway", methods=["POST"])
def walkaway():
    # Only allow walk away if the user hasn't answered the current question yet
    current_index = session.get("current_qn", 0)
    # If the user already answered, don't allow walk away
    if session.get("selected_answer") is not None:
        return redirect(url_for("result"))
    session["score"] = current_index
    # Clear selected_answer to prevent double walk away
    session["selected_answer"] = None
    return redirect(url_for("result"))


if __name__ == "__main__":
    app.run(debug=True)
