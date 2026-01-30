"""
Emotion detection module using Watson NLP.
"""


def emotion_detector(text_to_analyze):
    """
    Analyze text and return detected emotions.
    """
    if not text_to_analyze or text_to_analyze.strip() == "":
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    # existing API logic continues...
