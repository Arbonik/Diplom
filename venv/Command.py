from fuzzywuzzy import fuzz

class CommandHolder:
    def __init__(self, comm, ch = None):
        self.lastWeight : int
        self.commandHolder = ch
        self.commands = comm
    def cost(self, string : str):
        if self.commandHolder is None:
            print("i be here")
            return self.bestOfMyCommands(string)

        if type(self.commandHolder) is CommandHolder:
            print("Print succec")
            if self.commandHolder.cost(string) > self.bestOfMyCommands(string):
                print("hold better")
                return self.commandHolder.cost(string)
            else:
                print("mycomm better")
                return self.bestOfMyCommands(string)

        if type(self.commandHolder) == list:
            bestOf = instance_empty_Command()
            for c in self.commandHolder:
                temp = c.cost(string)
                if temp > bestOf:
                    bestOf = temp
            return bestOf

    def bestOfMyCommands(self, string):
        if type(self.commands) is list:
            bestOf = 0;
            for c in self.commands:
                if bestOf < c.answerCount(string):
                    bestOf = c.lastWeight
                    ret = c
            return ret
        if type(self.commands) is Command:
            b = self.commands.answerCount(string)
            print(b)
            return self.commands

    def display(self):
        print(self.commands)

class Command:

    def __init__(self, keyList, answList : str):
        self.keys = keyList
        self.answer = answList
        self.lastWeight = 0

    def answerCount(self, string : str):
        result = 0
        if type(self.keys) is list:
            print("list of keys")
            for key in self.keys:
                self.lastWeight = fuzz.ratio(string, key)
                if self.lastWeight > result:
                    result = self.lastWeight
                self.lastWeight = result
            return self.lastWeight
        else:
            self.lastWeight = fuzz.ratio(string.lower(), self.keys)
            return self.lastWeight

    def __lt__(self, other):
        return self.lastWeight < other.lastWeight

    def __gt__(self, other):
        return self.lastWeight > other.lastWeight

def instance_empty_Command():
    ret = Command("","")
    ret.lastWeight = 0
    return ret