import pickle
from warnings import filterwarnings

import numpy as np
from typing import List


filterwarnings("ignore")

MODEL_FILE = "pickled_model_hw2.pkl"
MODEL_FILE = "pickled_model.pkl"
model = pickle.load(open(MODEL_FILE, "rb"))


def predict(numbers: List[int]):
    """Использует сохраненную модель, возвращает её предсказание"""
    x = np.array(numbers).reshape(1, -1)
    return int(model.predict(x))
