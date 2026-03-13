from keras.preprocessing import sequence
from keras.models import load_model
from prediict import *
import random
from keras.preprocessing.text import Tokenizer
import numpy as np
def testing(data):
    try:
        tokenizer = Tokenizer(num_words=500, split=' ')
        twt = tokenizer.texts_to_sequences(data)
        ## = sequence.pad_sequences(data, maxlen=500)
        X_train = sequence.pad_sequences(twt, maxlen=28, dtype='int32', value=0)
        model = load_model('sentiment.h5')
        pred=model.predict(X_train)[0]
        print(np.argmax(pred))
        result=prediction(data)
        return(result)
    except Exception as e:
        result=prediction(data)
        return result
a=input("Enter data:\n")
print(testing(a))
