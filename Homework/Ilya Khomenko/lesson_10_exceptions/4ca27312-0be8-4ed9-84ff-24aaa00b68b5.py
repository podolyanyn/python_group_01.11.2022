def oops():
     ob=IndexError
     raise ob

def anotherfunc():
    try:
        oops()
    except :
        print("Error caught")


def ex2():
     try:
          a = input('Vvedit chyslo: ')
          b = input('Vvedit chyslo: ')
          print((int(a)**2)//int(b))
     except:
          if a!=int or b!=int:  
               raise ValueError 
          if b==0:
               raise ZeroDivisionError 

ex2()

