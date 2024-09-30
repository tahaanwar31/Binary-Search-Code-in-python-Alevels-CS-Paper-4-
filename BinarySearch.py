Data=[1,2,3,4,5,6,7,8,9,10]
def BinarySearch():
    global Data
    UpperBound=len(Data)-1
    LowerBound=0
    Found=False
    NotInList=False
    ValueToSearch = int(input("Please enter the number you want to search in the array: "))
    while Found==False and NotInList==False:
        MidPoint=(LowerBound+UpperBound)//2
        if ValueToSearch==Data[MidPoint]:
            Found=True
            print("This number was found on:",MidPoint," index in the array")
        elif ValueToSearch>Data[MidPoint]:
            LowerBound=MidPoint+1
        else:
            UpperBound=MidPoint-1
        if LowerBound>UpperBound:
            NotInList=True
            print("Number not found in the array")
BinarySearch()


