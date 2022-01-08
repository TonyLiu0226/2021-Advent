from typing import Counter

#DAY 1 ONLY CONTAINS PART 2 CODE
def day1():
    try:
        numbers = []
        with open('t.txt', 'r') as f:

            nums = f.read().splitlines()
            for n in nums:
                numbers.append(int(n))
        

        count = 0
        j = 1
        k = j + 1
        i = j - 1
        g = len(numbers)
        st = []

        while k < g:
            print(k)
            s = numbers[i] + numbers[j] + numbers[k]
            st.append(s)
            i+=1
            j+=1
            k+=1
        
       
        for x in range(1998):
            if (st[x-1] < st[x]):
                count+=1


        print("The depth increased: " + str(count) + " times")

    except Exception as f:
        print(f)



def migrate(counter):
    next_shift = Counter()

    for x in counter:
        if x == 0:
            next_shift[6] += counter[0]
            next_shift[8] += counter[0]

        else:
            next_shift[x - 1] += counter[x]

    return next_shift

def day2():
    keys = []
    num = []
    distance = 0
    depth = 0
    with open('w.txt', 'r') as f:

        strings = f.read().splitlines()
        for s in strings:
            k = s.split()
            keys.append(k[0])
            num.append(int(k[1]))

        
    for i in range (0, len(keys)):
        if keys[i] == "forward":
            distance += num[i]
        elif keys[i] == "down":
            depth += num[i]
        elif keys[i] == "up":
            depth -= num[i]
        else:
            print("Invalid input")

    print("depth is: " + str(depth))
    print("distance is: "+ str(distance))   

def day2part2():
    keys = []
    num = []
    distance = 0
    depth = 0
    aim = 0
    with open('w.txt', 'r') as f:

        strings = f.read().splitlines()
        for s in strings:
            k = s.split()
            keys.append(k[0])
            num.append(int(k[1]))

    print(keys)
    print(num)
        
    for i in range (0, len(keys)):
        if keys[i] == "forward":
            distance += num[i]
            depth += (num[i] * aim)
        elif keys[i] == "down":
            aim += num[i]
        elif keys[i] == "up":
            aim -= num[i]
        else:
            print("Invalid input")

    print("depth is: " + str(depth))
    print("distance is: "+ str(distance))   

#both part 1 and part 2, modify num_days values as needed

def day3():
    g = [] #main matrix that stores the big array of values
    number = []
    ep = []
    gamma = 0
    epsilon = 0
    original = []
    oxyRating = []
    CO2Rating = []

    with open('l.txt', 'r') as f:

        nums = f.read().splitlines()
        for n in nums:
            s = []
            original.append(n)

            for i in n:
                s.append(int(i))

            g.append(s)

    #temporary arrays to be used in part 2 calculations
    for num in original:
        oxyRating.append(num)
        CO2Rating.append(num)

    for j in range (0, len(g[0])):
        numOnes = 0
        numZeros = 0

        for i in range (0, len(g)):
            if g[i][j] == 1:
                numOnes+=1
            else:
                numZeros+=1

        if numOnes > numZeros:
            number.append(1)
            ep.append(0)

        elif numZeros > numOnes:
            number.append(0)
            ep.append(1)
        
        else:
            print("Something went wrong")

    print(number)
    print(ep)
    #convert number and ep from binary to decimal
    gamma = binaryToDecimalNumber(number)
    epsilon = binaryToDecimalNumber(ep)

    print("Answer is: " +str(gamma*epsilon))

    #part2
    removeEntries(number, oxyRating)
    removeEntries(ep, CO2Rating)

    print(CO2Rating)
    print(oxyRating)
    x = int(oxyRating[0])
    y = int(CO2Rating[0])
    print(x)
    print(y)

def binaryToDecimalNumber(array):
    value = 0
    i = len(array) - 1
    power = 0
    while i > -1:
        value += (array[i] * (pow(2, power)))
        power+=1
        i-=1

    return value

def removeEntries(keys, array):
    count = 0
    for i in keys:
        print(len(array))
        toRemove = []
        #keep only values in original that matches the number
        for n in array:
            if (len(array) == 1):
                break 
            else:
                if (int(n[count]) != i):
                    toRemove.append(n)

        #need a special case for if toRemove is the size of the array
            #in this case, we retain the last entry in toRemove
        if (len(toRemove) != len(array)):       
            for entry in toRemove:
                array.remove(entry)

        count=count+1

def day4():
    call_order = [63,23,2,65,55,94,38,20,22,39,5,98,9,60,80,45,99,68,12,3,6,34,64,10,70,69,95,96,83,81,32,30,42,73,52,48,92,28,37,35,54,7,
    50,21,74,36,91,97,13,71,86,53,46,58,76,77,14,88,78,1,33,51,89,26,27,31,82,44,61,62,75,66,11,93,49,43,85,0,87,40,24,29,15,59,16,67,19,72,57,
    41,8,79,56,4,18,17,84,90,47,25]

    booleanBoard = []
    boards = []
    boardlines = []
    with open ('i1.txt', 'r') as f:
        strings = f.read().splitlines()
        for s in strings:
            k = s.split()
            boardline = []
            for i in k:
                boardline.append(int(i))
            boardlines.append(boardline)

        x = 0
        y = len(boardlines)
        
        #add every 5 lines into a board, then add the board into boards
        while x < y:
            board = []
            for s in range (x, x+5):
                board.append(boardlines[s])

            boards.append(board)
            x+=6
        print(boards)

    #creates a boolean board for each board
    for b in boards:
        b = []
        for i in range(5):
            s = [False, False, False, False, False]
            b.append(s)

        booleanBoard.append(b)

    for c in call_order:
        print("checking " + str(c))
        checkNum(c, boards, booleanBoard)

        winners = checkBingo(booleanBoard)
        if (len(winners) != 0):
            print("The size of the array is: " + str(len(boards)))
            for i in winners:

                print("Wincondiion is: " + str(i))
                winner = boards[i]

                if (len(boards) != 1):
                    del boards[i]
                    del booleanBoard [i]
                    continue
                else:
                    print("winner declared")
                    sum = 0
                    #find falses
                    tCheck = booleanBoard[i]
                    for i in range(len(tCheck)):
                        for j in range(len(tCheck[0])):
                            if (tCheck[i][j] == False):
                                sum += winner[i][j]

                    score = sum * c
                    print("score is:" + str(score))
                    break
                
def checkNum(num, board, booleanBoard):
    print(num)
    count = 0
    for b in board:
        toCheck = booleanBoard[count]
        #iterate through all the boards and checks if the value exists
        for i in range (len(b)):
            for j in range (len(b[0])):
                if (b[i][j] == num):
                    toCheck[i][j] = True

            
        count = count+1

def checkBingo(booleanBoard):

    winners = []
    count = 0
    for c in booleanBoard:
        #rows
        if (c[0][0] == True & c[0][1] == True & c[0][2] == True & c[0][3] == True & c[0][4] == True):
            winners.append(count)
        elif (c[1][0] == True & c[1][1] == True & c[1][2] == True & c[1][3] == True & c[1][4] == True):
            winners.append(count)
        elif (c[2][0] == True & c[2][1] == True & c[2][2] == True & c[2][3] == True & c[2][4] == True):
            winners.append(count)
        elif (c[3][0] == True & c[3][1] == True & c[3][2] == True & c[3][3] == True & c[3][4] == True):
            winners.append(count)
        elif (c[4][0] == True & c[4][1] == True & c[4][2] == True & c[4][3] == True & c[4][4] == True):
            winners.append(count)
        
        #columns
        elif (c[0][0] == True & c[1][0] == True & c[2][0] == True & c[3][0] == True & c[4][0] == True):
            winners.append(count)
        elif (c[0][1] == True & c[1][1] == True & c[2][1] == True & c[3][1] == True & c[4][1] == True):
            winners.append(count)
        elif (c[0][2] == True & c[1][2] == True & c[2][2] == True & c[3][2] == True & c[4][2] == True):
            winners.append(count)
        elif (c[0][3] == True & c[1][3] == True & c[2][3] == True & c[3][3] == True & c[4][3] == True):
            winners.append(count)
        elif (c[0][4] == True & c[1][4] == True & c[2][4] == True & c[3][4] == True & c[4][4] == True):
            winners.append(count)
        else:
            count = count + 1
        
    return winners


def day6():
    num_days = 100000
    init_state = [3,5,1,5,3,2,1,3,4,2,5,1,3,3,2,5,1,3,1,5,5,1,1,1,2,4,1,4,5,2,1,2,4,3,1,2,3,4,3,4,4,5,1,1,1,1,5,5,3,4,4,4,5,3,4,1,4,3,3,2,1,
1,3,3,3,2,1,3,5,2,3,4,2,5,4,5,4,4,2,2,3,3,3,3,5,4,2,3,1,2,1,1,2,2,5,1,1,4,1,5,3,2,1,4,1,5,1,4,5,2,1,1,1,4,5,4,2,4,5,4,2,4,4,1,1,2,2,1,1,2,
3,3,2,5,2,1,1,2,1,1,1,3,2,3,1,5,4,5,3,3,2,1,1,1,3,5,1,1,4,4,5,4,3,3,3,3,2,4,5,2,1,1,1,4,2,4,2,2,5,5,5,4,1,1,5,1,5,2,1,3,3,2,5,2,1,2,4,3,3,
1,5,4,1,1,1,4,2,5,5,4,4,3,4,3,1,5,5,2,5,4,2,3,4,1,1,4,4,3,4,1,3,4,1,1,4,3,2,2,5,3,1,4,4,4,1,3,4,3,1,5,3,3,5,5,4,4,1,2,4,2,2,3,1,1,4,5,3,1,1,1,
1,3,5,4,1,1,2,1,1,2,1,2,3,1,1,3,2,2,5,5,1,5,5,1,4,4,3,5,4,4]

    try:
        i = 0 #after 0 days
        c = Counter(init_state)
        print(c)
        
        #find value after 256 days
        while (i < num_days):
            c = migrate(c)
            i+=1
            
        sum = 0

        for x in c:
            sum +=c[x]
        
        print("sum is: " + str(sum))

    except Exception as e:
        print(e)

def day7():

    fuelCosts = []
    input = [1101,1,29,67,1102,0,1,65,1008,65,35,66,1005,66,28,1,67,65,20,4,0,1001,65,1,65,1106,0,8,99,35,67,101,99,105,32,110,39,101,115,116,32,112,97,115,32,
    117,110,101,32,105,110,116,99,111,100,101,32,112,114,111,103,114,97,109,10,602,216,979,1851,549,9,38,931,28,9,303,933,1262,265,81,291,1447,737,379,456,1236,
    604,393,438,260,242,421,549,390,372,366,717,927,94,146,603,557,676,1729,4,1027,26,671,213,286,948,142,97,1087,210,72,949,947,1251,414,968,1300,42,814,1036,610,214,
    1536,210,108,545,375,1248,647,233,406,1502,433,243,13,836,815,73,525,129,323,912,671,270,635,501,110,128,113,147,534,894,883,318,205,453,264,259,1039,759,439,918,1647,
    493,1,422,503,583,1591,254,267,1213,604,145,242,795,278,181,12,236,1122,1002,235,965,73,228,755,562,91,4,205,1669,25,297,744,36,861,19,875,878,118,147,397,171,199,1286,72,
    942,200,991,8,496,631,214,668,79,1582,426,240,146,1153,88,1582,204,1254,527,19,358,444,944,84,1573,466,532,118,285,293,126,43,1348,837,326,154,412,153,861,1378,138,730,484,157,42,
    17,43,553,468,1668,16,301,612,65,293,383,95,260,1219,13,29,322,1043,1303,43,1147,1505,816,836,43,339,825,703,371,289,290,1060,492,661,667,818,178,114,1042,
    244,383,127,280,500,291,141,2,806,911,252,282,38,348,155,84,138,563,11,304,1216,1312,560,266,328,1570,1330,136,292,25,414,75,1172,387,291,279,12,405,169,661,102,
    24,66,1149,83,161,120,310,1041,686,149,328,345,1143,190,111,155,183,1210,619,40,431,9,470,731,453,1195,415,641,393,81,234,157,42,911,1365,292,163,388,204,1160,971,13,980,
    535,285,1504,454,461,518,242,974,798,93,80,720,234,378,1355,351,160,228,407,494,1650,629,621,965,686,341,273,252,66,189,526,15,273,389,1033,126,89,731,1254,1109,83,1660,682,700,
    712,140,105,929,62,623,476,918,15,568,406,346,720,402,1421,468,702,1090,159,794,14,59,863,393,540,1367,785,824,1016,857,488,515,539,109,12,53,371,13,483,930,112,666,30,664,768,699,
    1247,449,6,132,61,688,356,46,42,375,1320,606,62,14,233,161,497,150,1084,517,7,128,379,412,264,826,962,101,909,9,1624,77,307,485,106,103,4,1239,173,711,1533,99,762,100,382,876,26,305,
    218,27,41,1126,11,477,60,1187,201,541,102,571,227,60,118,1561,269,388,233,828,382,195,186,199,1552,444,605,22,78,159,386,1076,813,160,355,860,675,1139,437,71,1605,1,450,163,125,1245,
    778,10,375,348,18,174,223,367,342,697,257,317,454,242,99,1243,876,719,641,1097,538,444,280,33,99,0,492,194,458,983,42,651,454,1171,621,198,1152,31,410,3,247,977,338,220,830,580,1021,1238,
    401,536,124,1605,1461,1785,644,837,492,473,1073,1166,78,565,1018,155,156,948,942,368,1140,893,1059,501,46,383,752,373,236,1138,1279,450,104,502,229,783,241,186,46,919,514,371,18,578,428,
    1205,317,945,71,741,125,1155,680,1081,436,525,1396,171,942,225,403,564,365,372,167,599,955,1442,1672,258,717,922,219,1044,216,224,417,149,510,332,236,533,28,391,39,857,842,601,1216,151,538,
    900,481,39,363,400,78,1006,384,957,626,1503,269,429,259,755,1140,537,45,1,243,194,815,346,376,304,1167,423,822,166,282,20,200,133,892,140,1073,639,409,1644,105,828,881,1155,41,1590,647,449,89,
    845,554,411,260,837,237,377,154,49,36,687,62,230,14,11,26,853,497,48,130,17,1817,131,433,106,414,1034,146,977,565,670,581,999,4,164,706,58,212,554,101,64,123,219,154,28,531,626,64,782,505,364,
    281,1084,1414,27,226,736,507,837,142,434,319,409,819,48,23,820,454,1080,567,783,201,53,1153,404,187,814,28,898,309,380,295,437,366,1226,861,100,550,119,8,233,1452,30,753,381,365,683,474,227,
    155,1795,1093,208,159,121,1547,942,194,139,325,838,901,597,805,486,1499,597,405,1042,41,222,740,478,884,165,62,547,15,20,309,454,132,5,136,972,45,65,267,463,581,244,51,981,1120,75,410,1310,991,
    607,1801,950,913,98,769,81,322,19,459,1210,617,48,1163,1243,332,92,1713,120,269,20,246,323,1365,80,1165,1344,236,750,269,62,375,143,163,1444,172,789,521,105,369,1,40,341,625,674,1073,1376,108,
    391,277,122,181,134,78,1058,103,300,30,848,708,59,93,204,263,32,951,1884,23,488,258,1156,838,72,310,29,209,908,39,119,119,352,70,139,3,884,86,57,541,1553,5,105,710,29,335,1197,1152,144,696,685,
    948,563]

    #find largest element in the array, and smallest element in the array
    Max = max(input)
    Min = min(input)

    #part 1
    for i in range (Min, Max +  1):
        fuel = 0
        #iterate through all array by calculating difference between the array value at the position with i
        for k in input:
            fuel += abs(k - i)  

        fuelCosts.append(fuel)
    
    print(min(fuelCosts))

    part2 = []
    #part 2
    for i in range (Min, Max + 1):
        fuel = 0
        for k in input:
            w = abs(k - i)
            fuel += sum(0, w)

        part2.append(fuel)

    print(min(part2))


def sum(startNum, endNum):
    
    k = 0
    for i in range (startNum, endNum + 1):
        k+=i

    return k


def day8():
    count = 0
    arr1 = []
    arr2 = []
    arr3 = []

    with open ('g.txt', 'r') as g:
        nums = g.read().splitlines()
        for n in nums:
            arr1.append(n)
        

    for x in arr1:
        y = x.split('|')
        arr3.append(y[0])
        arr2.append(y[1])

    for val in arr2:
        h = val.split()

        for i in h:

            if len(i) == 2:
                count+=1
                continue
            if len(i) == 3:
                count+=1
                continue
            if len(i) == 4:
                count+=1
                continue
            if len(i) == 7:
                count +=1
                continue

    print(count)

def day9():
    input = []
    num_lowpoints = 0
    risk = 0
    lowindex = []
    
    with open ('k.txt', 'r') as f:
        nums = f.read().splitlines()
        for n in nums:
            
            #iterate each number, add it to temp list
            temp = []
            for element in n:
                temp.append(int(element))
            
            input.append(temp)
            

        #input is a 2d array

    rows = len(input)    
    cols = len(input[0])
    print(rows)
    print(cols)

    for i in range (0, rows):
        for j in range (0, cols):

            #graph for each iteration
            graph = {}
            #variable to track travelled stat
            travelled = False
            #make a new graph for each entry
            ID = str(i) + str(j)
            print("id is: " +ID)
            value = input[i][j]

            if value != 9:
                graph
            
            #top left corner
            if (i == 0 and j == 0):
                right = input[i][j+1]
                down = input[i+1][j]
                if (right > value and down > value):
                    num_lowpoints += 1
                    lowindex.append(value)

            #bottom right corner
            elif (i == rows-1 and j == rows-1):
                left = input[i][j-1]
                up = input[i-1][j]
                if (left > value and up > value):
                    num_lowpoints += 1
                    lowindex.append(value)
            
            #bottom left corner
            elif (i == rows-1 and j == 0):
                
                right = input[i][j+1]
                up = input[i-1][j]
                if (right > value and up > value):
                    num_lowpoints += 1
                    lowindex.append(value)

            #top right corner
            elif (i == 0 and j == rows-1):
                
                left = input[i][j-1]
                down = input[i+1][j]
                if (left > value and down > value):
                    num_lowpoints += 1
                    lowindex.append(value)
            
            #top edge
            elif (i == 0):
                
                right = input[i][j+1]
                down = input[i+1][j]
                left = input[i][j-1]
                if (left > value and right > value and down > value):
                    num_lowpoints += 1
                    lowindex.append(value)
            
            #left edge
            elif (j == 0):
                
                right = input[i][j+1]
                down = input[i+1][j]
                up = input[i-1][j]
                if (right > value and up > value and down > value):
                    num_lowpoints += 1
                    lowindex.append(value)
            
            #bottom edge
            elif (i == rows-1):
                
                right = input[i][j+1]
                up = input[i-1][j]
                left = input[i][j-1]
                if (left > value and right > value and up > value):
                    num_lowpoints += 1
                    lowindex.append(value)
            
            #right edge
            elif (j == rows-1):
                
                up = input[i-1][j]
                down = input[i+1][j]
                left = input[i][j-1]
                if (left > value and up > value and down > value):
                    num_lowpoints += 1
                    lowindex.append(value)

            #middle
            else:
                
                up = input[i-1][j]
                down = input[i+1][j]
                left = input[i][j-1]
                right = input[i][j+1]
                if (left > value and right > value and down > value and up > value):
                    num_lowpoints += 1
                    lowindex.append(value)
            
    #sums up the number of lowpoints
    print(num_lowpoints)

    for x in lowindex:
        risk += (x+1)

    print(risk)

def day11():
    h = []
    flashes = 0
    allFlashed = 0
    with open('kt.txt', 'r') as f:

        nums = f.read().splitlines()
        for n in nums:
            g = []
            print(n)
            for i in range(len(n)):
                g.append(int(n[i]))
            h.append(g)

    print(h)

    #calculate the state of the board after n number of steps
    for steps in range(1000):
        #creates a boolean matrix to keep track of flashes
        flashed = [[False for c in range(len(h[0]))] for r in range(len(h))]
        print(flashed)

        #increases each energy level by 1
        for i in range (len(h)):
            for j in range (len(h[0])):
                h[i][j] += 1

        print(h)
        #iterates through the array, any octopus with size 9 flashes
        for i in range (len(h)):
            for j in range (len(h[0])):
                if (flashed[i][j] == False):
                    if (h[i][j] > 9):
                        flash(h, flashed, i, j)
        
        #sets anything that is flashed to 0
        for i in range (len(flashed)):
            for j in range(len(flashed[0])):
                if flashed[i][j] == True:
                    h[i][j] = 0
                    flashes=flashes+1
        
        #checks to see if all octupuses flash
        isAllFlashed = True
        for i in range (len(flashed)):
            for j in range(len(flashed[0])):
                if flashed[i][j] == False:
                    isAllFlashed = False
                    break
                
        if isAllFlashed == True:
            allFlashed = steps + 1
            print("The step where all the octopuses flash is: " + str(allFlashed))
            break


        print("After step " + str(steps))
        print(h)
        print("Flashes: " +str(flashes))

def flash(array, flashed, i, j):
    #sets flashed to true
    flashed[i][j] = True
    #for every neighbor, increase by 1. If the result is >9, call flash on neighbor
    for i1 in range (i-1, i+2):
        for j1 in range (j-1, j+2):
            print (str(i1) +" " + str(j1))
            if i1 < 0 or j1 < 0 or i1 >= len(array) or j1 >= len(array[0]):
                print("out of range")
                continue
            else:
                if flashed[i1][j1] == False:
                    array[i1][j1] += 1
                    if (array[i1][j1] > 9):
                        flash(array, flashed, i1, j1)

def day15():
    h = []
    
    with open('kt.txt', 'r') as f:

        nums = f.read().splitlines()
        for n in nums:
            g = []
            print(n)
            for i in range(len(n)):
                g.append(int(n[i]))
            h.append(g)

    print(h)

#replace this method call with that of the day you wish to run
day15()

