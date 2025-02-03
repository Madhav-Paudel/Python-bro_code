# example of keyword arguments
def key_value(**kargs):
    for key,value in kargs.items():
        print(f"{key}:{value}")
    print(" ")


key_value(street= "457",
          town=   "bansgadhi",
          postal= "123546"

          )
