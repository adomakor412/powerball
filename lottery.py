# Choose the lottery numbers
# lottery.py by Ronald Adomako July 7, 2016
import timeit
start_time = timeit.default_timer()

from itertools import combinations

class lotteryDatabase:
    #Generate pool of possible numbers
    '''
    pool = []
    for first in range(1,70):
        for second in range (first+1,70):
            for third in range(second+1,70):
                for fourth in range(third+1,70):
                    for fifth in range(fourth+1,70):
                        draw=[first, second, third, fourth, fifth]
                        pool.append(draw)
    '''
    def __init__(self):       
        self.histBallCount = [0]*69
        self.histDraw = []       
        self.pool = list(combinations(list(range(1,70)),5))
        #len('self.pool') > len('lotteryDatabase.pool')
        self.optPool = []
         
    def genHistDraw(self, draws):       
        for line in draws:
            line = line.strip()
            date, *nums = line.split() #python 3
            for i in range(5):
                ball = int(nums[i])
                self.histBallCount[ball-1]+=1
        elapsed = timeit.default_timer() - start_time
        print(elapsed, 'seconds?')        
        return self.histBallCount

    def pickDrawing(self):
        minDraws = []
        for i in range(69):
            if i==0:
                minDraws[i] = i+1
            elif self.histBallCount[i-1] < self.histBallCount[i]:
                minDraws.insert(i, i+1)
            else:
                #handle repeated or tied values
                maxDrawValues = self.histBallCount[minDraws[-1]] 
                indexMaxDrawValues = self.histBallCount.index(maxDrawValues)
                minDraws.insert(indexMaxDrawValues,i+1)  

def main():
    lottery = lotteryDatabase()
    tally = open('powerball.txt','r')
    tallyList = lottery.genHistDraw(tally)
    print (lottery.histBallCount)
    draws = open('tickets.txt','r')
'''
if __name__ == 'main':
'''
main()#indent when using command line


    #history = input(lottery.txt)
    #work out length of time to finish running
    #work out writing file to check algorithm (! in shell)


