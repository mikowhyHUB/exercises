'''Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.'''

class Myclass:    
    def get_string(self):
        self.word = input('Type some shit: ')
        
    def print_string(self):
        print(self.word)
obj = Myclass()
obj.get_string()
obj.print_string()

