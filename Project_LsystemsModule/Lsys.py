
class Lsystem ():
    def __init__(self,args,commands,rules,module = ""):

        self.mod =""
        self.commands = commands
        
        if module:
            self.mod = __import__(module)
            
                      
        self.arguments = args
        self.rules = rules

       
        
    def execute_cmd_Lstring(self,iter_number,start_string,print_cmd = 0):
        
        commands = dict ()
        if self.mod:
           for key in self.commands:
                if self.commands[key]:
                    commands[key] = "self.mod" + "." + self.commands[key]
                else:
                    commands[key] = ""

                
        self.__make_string (iter_number,start_string)
        arguments = self.arguments
        for char in self.start_string:
            if print_cmd:        
                print (char)
                print (commands[char])
            if commands[char]:
                eval (commands[char])
            
            

    def print_Lstring (self,iter_number,start_string):

        print (self.__make_string (iter_number,start_string))
        
            
    def __make_string (self,iter_number,start_string):

        self.iter = iter_number
        self.start_string = start_string

        new_string = ""

        for j in range (self.iter):
    
            for char in self.start_string:
               
                if char in self.rules:
                    new_string = new_string + self.rules[char]
            
                else:
                    new_string = new_string + char
    
            self.start_string = new_string
            new_string = ""
        
        return self.start_string
        

        
        
