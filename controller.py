from inflammation.compute_data import analyse_data
from inflammation.models import CSVDataSource, JSONDataSource

directory = input("CSV Directory:")
try:
    data_source = JSONDataSource(directory)
    loaded_data = data_source.load_data()
except:
    print("No JSONs")
try:
    data_source = CSVDataSource(directory)
    loaded_data = data_source.load_data()
except:
    print("No CSVs")

# print(loaded_data)
data = analyse_data(data_source)
print(data)
