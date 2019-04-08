import time
while True:
    FILE = open("Stunden.dll", "r")
    Stunden = float(FILE.read())
    FILE.close()
    Stunden += 0.000278
    FILE = open("Stunden.dll", "w")
    FILE.write(str(Stunden))
    FILE.close()
    time.sleep(1)