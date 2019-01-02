# Linear search test file

TestData = [5, 7, 10, 12, 15]

#linear search function
#inputs params
# @find number you wish to search
# @testData sample Data set to search in
# @returns, index in the dataSet and flag boolean to indicate search result
def searchLinear(find, testData):
    i = 0
    found=False
    while i < len(testData):
        if testData[i] == find:
            i += 1
            found = True
            break
        i += 1

    return i,found

#Get input from user to find the data
while True:
    try:
        searchData= int(input("\nPlease enter the Number your wish to find: "))
        break
    except:
        print("That's not a valid option!")

#Start search
print("Search {0} in test data {1}..".format(searchData, TestData))
index, sres = searchLinear(searchData, TestData)

#print search results.
if sres:
    print("\t Found \'{0}\' at position \'{1}\' in the TestData Set".format(searchData, index))
else:
    print("\t \'{0}\' is NOT found in the TestData Set".format(searchData))