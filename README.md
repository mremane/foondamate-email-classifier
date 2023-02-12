# foondamate-email-classifier
Email classifier for foondamate ML Challenge 🚀

Uses a RandomForestClassifier to classify e-mails between two labels -  _“Student has shared”_ or _“Student wants to know if can share”_

### Requirements.txt
File is available with all required libraries for import

### Unit tests
You may run tests with command ```python -m unittest```

### Import function

Our email classifier is exposed as a python librray so all you have to do is import it into your code.

```
from classifier.classifier import Classifier
classifier = Classifier('model.pkl')
```
Please consult _demo.ipynb_ notebook for an example.

### Model creation

Documented process of model creation can be found on _ml-e2e.ipynb_ notebook.

### ToDo
- Automate python unit tests (CI)
- Fix .gitignore
