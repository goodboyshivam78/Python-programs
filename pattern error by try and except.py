import time, sys

inc = 1
inc_s = True

while True:
    print(" " * inc , end="")
    print("*******")
    time.sleep(0.2)
    try:
        if inc_s ==True:
            inc += 1
            if inc==6:
                inc_s = False
        else:
            inc -= 1
            if inc == 1:
                inc_s = True

    except KeyboardInterrupt:
        sys.exit()
            
        
