import joblib

class Classifier:
    def __init__(self, path):
        self._path = path
        self._model = joblib.load(self._path)
    
    def classify(self, sentence):
        if sentence is None:
            raise TypeError('Text parameter cannot be null.')
        if not sentence:
            raise ValueError('Cannot convert empty string.')
        prediction = self._model.predict([sentence]).tolist().pop()
        return 'Student has shared.' if prediction==1 else 'Student wants to know if can share.'