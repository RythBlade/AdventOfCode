
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

countOfValidPasswords = 0

print('Parsing and counting valid passwords')
for line in passwordFile:
    # split the line into password and policy
     splitLine = line.split(':', 1) # there should only be a single colon character on each line, which separates the password from the policy
     policyString = splitLine[0].strip()
     password = splitLine[1].strip()
     policy = passwordPolicy.parsePasswordPolicyFromString(policyString)

     if policy.isPasswordValid(password) == True:
        countOfValidPasswords += 1

print('Parse complete. There are, ' + str(countOfValidPasswords) + ', valid passwords')

print('Application complete. Time taken (s): ' + str(applicationTimer.elapsedTime()))