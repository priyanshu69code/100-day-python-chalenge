import pickle

with open('pri', 'rb') as f:
    my_list = pickle.load(f)

print(my_list.score)
print(my_list.life)
