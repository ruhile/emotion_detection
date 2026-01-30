"""
Flask server for Emotion Detection application.
Handles user input, emotion analysis, and error handling.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def home():
    """
    Render the home page.
    """
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET", "POST"])
def emotion_detector_route():
    """
    Handle emotion detection requests.
    """
    text_to_analyze = (
        request.args.get("textToAnalyze")
        or request.form.get("text")
    )

    response = emotion_detector(text_to_analyze)

    # Handle None or invalid responses safely
    if not response or response.get("dominant_emotion") is None:
        return "Invalid text! Please try again!"

    result = (
        "For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

    return result


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
