
__weight=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
__validate=['1','0','X','9','8','7','6','5','4','3','2']

def getValidateCode(idNum):
    sum=0
    if len(idNum) != 17:
        raise Exception("Not a Validate Number")
    idLs = list(idNum)
    for index in range(len(idNum)):
        sum = sum + __weight[index]*int(idLs[index])
    mode =sum % 11
    return __validate[mode]
