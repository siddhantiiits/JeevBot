import pickle

# Create a variable
myvar = {}

# Open a file and use dump()
with open('file.pkl', 'wb') as file:
    # A new file will be created
    pickle.dump(myvar, file)
    print("Dumped")


