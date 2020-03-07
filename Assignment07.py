# ------------------------------------------------- #
# Title: Pickling - dumping and unloading
# Description: My made up script demonstrating  Python pickling functionality
# ChangeLog:
# dstrop, 3.6.20, file created
# ------------------------------------------------- #

import pickle, shelve

# The three lists that I plan to pickle
print('Want to know the best artists of the 80s, 90s and 00s')
the_80s = ['Guns and Roses', 'Def Leopard', 'Bon Jovi']
the_90s = ['Nirvana', 'Pearl Jam', 'The Smashing Pumpkins']
the_00s = ['Britney Spears', 'Blink 182', 'Green Day']

try:
    num = float(input('Press any number to begin: '))
except:
    print("that's not a number!")

# Open the new binary file to write to, use the wb to write to binary
f = open('c:\_Pythonclass\Assignment07\ bestbands.dat', 'wb')


# Next use the pickle.dump() function, this requires the data to pickle and file to store in

pickle.dump(the_80s, f)
pickle.dump(the_90s, f)
pickle.dump(the_00s, f)
f.close() # proper practice to close the file

# Retrieve and unpickle the three lists with pickle.load()

print('Obviously the best are:')
f = open('c:\_Pythonclass\Assignment07\ bestbands.dat', 'rb')
the_80s = pickle.load(f)
the_90s = pickle.load(f)
the_00s = pickle.load(f)

print(the_80s)
print(the_90s)
print(the_00s)
f.close()
