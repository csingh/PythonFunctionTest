# http://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python

class ColourNotDefined(Exception):
    pass

class PurrdyPrinter:

    COLOURS = dict()
    COLOURS["pink"] = '\033[95m'
    COLOURS["blue"] = '\033[94m'
    COLOURS["green"] = '\033[92m'
    COLOURS["yellow"] = '\033[93m'
    COLOURS["red"] = '\033[91m'
    COLOURS["white"] = '\033[1m'
    COLOURS["underline"] = '\033[4m'

    COLOUR_END_CODE = '\033[0m'

    @staticmethod
    def put(colour, thing):
        if colour not in PurrdyPrinter.COLOURS:
            raise ColourNotDefined("Colour '{}' is not supported.".format(str(colour)))
        else:
            colour_code = PurrdyPrinter.COLOURS[colour]
            end_code = PurrdyPrinter.COLOUR_END_CODE
            print(colour_code + str(thing) + end_code)

if __name__ == '__main__':
    PurrdyPrinter.put("pink", "Hello!")
    PurrdyPrinter.put("blue", "Hello!")
    PurrdyPrinter.put("green", "Hello!")
    PurrdyPrinter.put("yellow", "Hello!")
    PurrdyPrinter.put("red", "Hello!")
    PurrdyPrinter.put("white", "Hello!")
    PurrdyPrinter.put("underline", "Hello!")



