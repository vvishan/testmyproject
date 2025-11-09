import pickle
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier()
model.fit([[0, 1], [1, 0]], [0, 1])

with open("model.pkl","wb") as f:
    pickle.dump(model,f)