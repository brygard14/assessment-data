log_file = open("um-server-01.txt")
#above line assigns the accessed data in the txt file to a the variable called log_file


def sales_reports(log_file):
#above line defines the function called sales_reports, passing in an argument of the variable we created for the txt file containing the data
    for line in log_file:
    #above line is a for loop that will cause this function to iterate through the lines of data in the txt file
        line = line.rstrip()
        #above line will remove the '/n' (new line character) at the end of the lines of data in the txt file when printing
        day = line[0:3]
        #above line will check the first 3 characters of the string/line of the txt file (which in this case, indicates the day) and assign it to a variable called "day"
        if day == "Mon":
            print(line)
        #the 2 lines of code above set the condition that if the first 3 characters of the string matches the day (for example "Mon"), it will print that entire line

sales_reports(log_file)
#the above line runs the function for the txt file, passing in the variable we set it to at the top of this code
