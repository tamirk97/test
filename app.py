from module1 import add,minus,bigger,mult
from module2 import hello,howareyou
from icecream import ic
import pickle

def main():
    ic(hello())
    ic(howareyou())
    ic(add(4,5))
    ic(minus(4,5))
    ic(mult(4,5))
    ic(bigger(5,5))
    ic(restored_data)
   

# Create a Python object
data = {'name': 'John', 'age': 30, 'city': 'New York'}

# Serialize the object to a byte stream
with open('data.pickle', 'wb') as f:
    pickle.dump(data, f)

# Deserialize the byte stream back into a Python object
with open('data.pickle', 'rb') as f:
    restored_data = pickle.load(f)


    
    

if __name__ == "__main__":
    main()
