import pickle
import matplotlib.pyplot as plt

with open('dump.pickle', 'rb') as f:
    fig = pickle.loads(f.read())

print(repr(fig))
fig.Figure.show()