import one
print("TOP LEVEL IN TWO.PY")

one.func()

if __name__ == "__main__":
    print('ONE IS ON THE TOP LEVEL')
else:
    print('One is being imported')