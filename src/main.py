import SVMClassification as s
import pickle
import os
import time

classifier = s.SVMClassification()
classifier.train_and_test()

train = input("Press 0 to exit, 1 to train model with all data")

try:
    if int(train) == 0:
        exit(0)
    elif int(train) == 1:
        model = classifier.train_and_get_model()
        model_path = os.path.abspath('../model')

        if not os.path.isdir(model_path):
            os.mkdir(model_path)

        my_time = time.localtime()
        extension = 'sav'
        file_name = f'SVM-{my_time.tm_mday}-{my_time.tm_mon}-{my_time.tm_year}-{my_time.tm_hour}-{my_time.tm_min}-{my_time.tm_sec}.{extension}'

        with open(os.path.join(model_path, file_name), 'wb') as pickle_out_model:
            pickle.dump(model, pickle_out_model, 0)
except ValueError:
    print('Invalid input')
    exit(-1)
