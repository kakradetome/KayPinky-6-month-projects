def greet( firstName, lastName ):
    print( f"Hello, {firstName} {lastName}" )

def returnName():
    return "randomName"

greet ( returnName() )