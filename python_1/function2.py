amount = 1.2
print(f"{amount:,.0%}")

# countries = ["Japan", "France", "Germany", "Brazil", "Egypt"]
# greetings = ["こんにちは", "Bonjour", "Hallo", "Olá", "مرحبا"]

# # Start of my program
# def main():
#     userWantsToTryAgain = True

#     while userWantsToTryAgain:

#         # Ask for user information
#         userName = input( "What's your name: " )
#         userLocation = input( "Where are you from: " )

#         # Compare l....
#         if userLocation in countries:
#             for currentCountryIndex in range( len( countries ) ):
#                 if userLocation == countries[ currentCountryIndex ]:
#                     print( greetings[ currentCountryIndex ], userName )
#         else:
#             print( "Sorry", userName + ".", userLocation, "is not supported yet. Try again later" )
        
#         userResponse = input( "Again? y/n: " )

#         if userResponse == "y":
#             userWantsToTryAgain = True
#         else:
#             userWantsToTryAgain = False

# main()