from Command import CommandHolder, Command, instance_empty_Command

class HolderBuilder:
    facultHolder: CommandHolder()
    commands = None

    def addCommands(self, comm):
        self.commands = comm
        return self

    def addHolder(self, direct):
        if direct is not None:
            self.facultHolder.commandHolder = dir
        return self

    def build(self):
        return self.facultHolder
