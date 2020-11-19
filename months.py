#CSci 127 Teaching Staff
#October 2017
#A program that uses functions to print out months.
#Modified by:  ADD YOUR NAME HERE

def monthString(monthNum):
     """
     Takes as input a number, monthNum, and
     returns the corresponding month name as a string.
     Example: monthString(1) returns "January".
     Assumes that input is an integer ranging from 1 to 12
     """
     
     monthString = ""

   #validate input for number between 1 and 12 only and keep looping for wrong input
    while monthNum not in range(1,13):
        print("\nThis is not a valid month. Please enter a number between 1 and 12: ")
        monthNum=int(input())
    
    #list containing all the months
    ls=["January","Febuary","March","April","May","June","July","August","September","October","November","December"]

     return(monthString)



def main():
     n = int(input('Enter the number of the month: '))
     mString = monthString(n)
     print('The month is', mString)



#Allow script to be run directly:
if __name__ == "__main__":
     main()
                   
