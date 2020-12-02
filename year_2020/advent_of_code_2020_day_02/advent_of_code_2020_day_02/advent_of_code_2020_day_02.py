
import passwordPolicy

from Timer import Timer

passwordFile = []
passwordFileName = "password_input.txt"

def readPasswordFile(filename):
    # read in the file contents - each value is an int on an individual line
    with open(filename) as file:
        lines = file.readlines()
        return lines

print('Starting application')
applicationTimer = Timer()

print('Reading password file')
passwordFile = readPasswordFile(passwordFileName)
print('Password file read')

countOfValidPasswordsPart1 = 0
countOfValidPasswordsPart2 = 0

print('Parsing and counting valid passwords')
for line in passwordFile:
    # split the line into password and policy
     splitLine = line.split(':', 1) # there should only be a single colon character on each line, which separates the password from the policy
     policyString = splitLine[0].strip()
     password = splitLine[1].strip()
     policy = passwordPolicy.parsePasswordPolicyFromString(policyString)

     if policy.isPasswordValidPart1(password) == True:
        countOfValidPasswordsPart1 += 1
        
     if policy.isPasswordValidPart2(password) == True:
        countOfValidPasswordsPart2 += 1

print('Parse complete.')
print('Part 1: There are, ' + str(countOfValidPasswordsPart1) + ', valid passwords')
print('Part 2: There are, ' + str(countOfValidPasswordsPart2) + ', valid passwords')

print('Application complete. Time taken (s): ' + str(applicationTimer.elapsedTime()))