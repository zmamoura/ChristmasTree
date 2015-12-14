i=0 
j=0 
while i<10:
    print((" " *(10-i)) + ("*" * (i*2 + 1)))
    if i>=9:
      while j<4:
        print((" " * 8) + ("*" * 5))
        j=j+1
    i=i+1 