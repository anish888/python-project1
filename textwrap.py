#import the module textwrap for wrapping the text
import textwrap
#function for defining the wrapping of text
def wrap(string,width):
    return textwrap.fill(string,width)
if __name__=='__main__':
    #taking the input from the user
    string,width=input(" enter the string yoy want to wrap"),int(input("enter the width of the string"))
    #calling function
    result=wrap(string,width)
    #printing the result
    print(result)

