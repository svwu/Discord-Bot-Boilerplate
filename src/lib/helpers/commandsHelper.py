import os.path

class CommandsHelper:

    def readCommandText(commandName):

        filePath = "/app/src/command_text/" + commandName + ".txt"
        commandText = ""

        if(os.path.exists(filePath))
            commandFile = open(filePath, "r")
            commandText = commandFile.read()

        return commandText