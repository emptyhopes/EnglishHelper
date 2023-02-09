from Modules.Utils import Utils

class String:

    def Join(array):
        string = ""

        for index, value in enumerate(array):
            if (index == 0):
                string = value
            else:
                string = string + "," + " " + value

        return string

    def JoinWithColor(array, color):
        string = ""

        for index, value in enumerate(array):
            if (index == 0):
                string = Utils.Message(value, color)
            else:
                string = string + "," + " " + Utils.Message(value, color)

        return string