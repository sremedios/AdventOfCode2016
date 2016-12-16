puzzleInput = '00101000101111010'
diskSize = 272

resultData = puzzleInput

while len(resultData) <= diskSize:
    b = []
    # reverse order of data in resultData and store in b
    for i in range(len(resultData)):
        b.append(resultData[-1-i])
        # flip bits
        b[i] = '0' if b[i] == '1' else '1'
    # append to resultData
    resultData = resultData + '0' + ''.join(b)

# truncate down to diskSize
resultData = ''.join(list(resultData)[:diskSize])

# calculate checksum
checkSum = [] 

# initial checksum calc
for x in range(0,len(resultData),2):
    if resultData[x] == resultData[x+1]:
        checkSum.append('1')
    else:
        checkSum.append('0')


# if checksum is not odd, repeat checksum on itself
while len(checkSum)%2 == 0:
    temp = []
    for x in range(0,len(checkSum),2):
        if checkSum[x] == checkSum[x+1]:
            temp.append('1')
        else:
            temp.append('0')
    checkSum = temp
    
print(''.join(checkSum))
