def meetUser():
    userName = input( "What's your name: " )
    print( "Hey", userName, "Nice name!" )
    userLocation = input("So " + userName + ", where are you from?: ")
    print( "Ah", userName, userLocation, "is a beautiful place" )

numberOfGuestsAsAString = input( "How many guest are you expecting: " )
numberOfGuestsAsAnInt = int( numberOfGuestsAsAString )

for currentUser in range( numberOfGuestsAsAnInt ):
    print("User number:", currentUser + 1)
    meetUser()
    print() # Line break