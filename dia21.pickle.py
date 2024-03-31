import pickle

data_to_save = {
    'name': 'Keanu Reeves',
    'age': 59,
    'city': 'Los Angeles'
}
with open('dia21.data.pkl', 'wb') as file:
    pickle.dump(data_to_save, file)   # serialize 

with open('dia21.data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)   # deserialize

print("Loaded data:", loaded_data)