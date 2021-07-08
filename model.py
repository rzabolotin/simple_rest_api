import pickle

import numpy as np
from typing import List

MODEL_FILE = r"models/hw1 (1).pkl"
model = pickle.load(open(MODEL_FILE, "rb"))


def predict(numbers: List[int]):
    """Использует сохраненную модель, возвращает её предсказание"""
    x = np.array(numbers).reshape(1, -1)
    return model.predict(x)[0]
