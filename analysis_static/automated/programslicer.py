# Python Program to Print Lines
# Containing Given String in File
  
# entering try block

f = open("highrollers.txt", "r")

variable = input("Enter the variable to parse for: ")

# reading file content line by line.
lines = f.readlines()

slices = []
index = 0

# looping through each line in the file
for line in lines:

    if "def" in line: #trying to add breakpoints between slice printout for function differences
        line = "\n" + line

    if variable in line:
        #if if/elif/else is in the line as well as the variable, include the next line as well if variable not in it
        if "if" in line or "elif" in line or "else" in line:
            slices.insert(index, line)

            #add next line to slices (it wont be auto included and skipped in next pass, really only works for return values)
            if variable not in lines[index+1]:
                lines[index+1] = lines[index+1] + "\n"
                slices.insert((index+1), lines[index+1])

        else: #insert the line normally
            slices.insert(index, line)

    index += 1 #used to keep track of position in lines array in case of backtracking

# closing file after reading
f.close()

# if length of slices list 0, variable not in the program
if len(slices)==0:
    print("\nCould not slice on variable: " + variable )
else:

    # displaying the lines 
    # containing given string
    lineLen = len(slices)
    print("\n Program slice on variable:  " + variable + "\n")
    for i in range(lineLen):
        print(end=slices[i])
    print()
  