import Preprocessor as P
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report, confusion_matrix


class SVMClassification:
    def __init__(self, path, param_grid=None):
        p = P.Preprocessor(path)
        features, labels = p.preprocess()
        self.features = features
        self.labels = labels
        if param_grid is None:
            self.param_grid = {'C': [1e2, 1e3, 1e4,], 'gamma': [0.0001, 0.001, 0.005, 0.01], 'kernel': ['linear', 'rbf']}
        elif type(param_grid) == type(dict()):
            self.param_grid = param_grid
        else:
            raise ValueError(f'Parameter grid must be a dictionary, received {type(param_grid)} instead.')

    
    def train_and_test(self):
        X_train, X_test, y_train, y_test = train_test_split(self.features, self.labels, test_size=0.30, random_state=1)
        model = GridSearchCV(SVC(class_weight='balanced'), self.param_grid, cv=5)
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        print(confusion_matrix(y_test, y_pred))

    
    def train_and_get_model(self):
        """
            Uses all of the data for training the model
        """
        model = GridSearchCV(SVC(class_weight='balanced'), self.param_grid, cv=5)
        model.fit(self.features, self.labels)

        return model
