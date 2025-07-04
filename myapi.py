# myapi.py

from textblob import TextBlob
import spacy

class API:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def sentiment_analysis(self, text):
        blob = TextBlob(text)
        return {
            "sentiment": {
                "polarity": blob.sentiment.polarity,
                "subjectivity": blob.sentiment.subjectivity
            }
        }

    def named_entity_recognition(self, text):
        doc = self.nlp(text)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        return {"entities": entities}

    def emotion_detection(self, text):
        # Simple keyword-based dummy logic
        text = text.lower()
        emotion_scores = {
            "joy": sum([text.count(word) for word in ['happy', 'joy', 'excited', 'great', 'pleased']]),
            "sadness": sum([text.count(word) for word in ['sad', 'unhappy', 'cry', 'depressed', 'down']]),
            "anger": sum([text.count(word) for word in ['angry', 'mad', 'furious', 'hate']]),
            "fear": sum([text.count(word) for word in ['scared', 'afraid', 'fear', 'terrified']])
        }

        total = sum(emotion_scores.values()) or 1
        normalized = {emotion: score / total for emotion, score in emotion_scores.items()}
        return {"emotion": normalized}
