# Assignment 2 Highrollers Program Slicer
# Jessica Leishman
  
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
        #check if the line prior is not the first line in the program
        if (index-1) >= 0:

            # check if the line prior is an if, elif, or else. If it is, need to add it
            if "else" in lines[index-1]:
                slices.insert(index, lines[index-1])
            elif "if" in lines[index-1] and variable not in lines[index-1]:
                slices.insert(index, lines[index-1])
            elif "elif" in lines[index-1] and variable not in lines[index-1]:
                slices.insert(index, lines[index-1])

        #if if/elif is in the line as well as the variable, include the next line as well if variable not in it
        if "if" in line or "elif" in line:
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
    lineLen = len(slices)
    print("Program slice on variable:  " + variable + "\n")
    for i in range(lineLen):
        print(end=slices[i])
    print()
  