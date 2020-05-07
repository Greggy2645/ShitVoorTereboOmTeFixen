import math
from termcolor import colored
#menu, zal altijd in een loop zijn
foutgegaan = -1
zucht = ""
def keuze():
        #idee van terebo
    global zucht
    startding = str(input('Type \'shower\' to calculate.\n Type exit to stop.' + zucht + '\n'))
    if startding == 'shower':
        shower()
    elif startding == 'exit':
        exit()
    else:
        print(colored('your fucking retarded', 'red'))
        global foutgegaan
        foutgegaan += int(1)
        if foutgegaan > 3:
            zucht = " zucht..."
            #geeft erro: [pyflakes] local variable 'zucht' is assigned to but never used. was geen global var :)
        keuze()

#shower dingetje
def shower():
    kmperliter = 2
    literperminute = 7.9
    showertime = int(input('How long have you showered in minutes?\n'))
    total = showertime * literperminute
    total = math.floor(total)
    walktime = total * kmperliter
    hours = walktime / 6
    hours = math.floor(hours)
    print('You have used ' + str(total) + ' liters of water.')
    print('An african child has to walk ' + str(walktime) +
          'km for this amount of water.')
    print('That takes the child about ' + str(hours) + ' hours.\n')
    if showertime > 10:
        print('how the fuck did you shower over 10 mins tho')
    keuze()

#eerste start menu
keuze()

