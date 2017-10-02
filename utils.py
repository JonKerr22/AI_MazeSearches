class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def redText(text):
    return '\033[91m'+str(text)+bcolors.ENDC
def greenText(text):
    return '\033[92m'+str(text)+bcolors.ENDC
def yellowText(text):
    return '\033[93m'+str(text)+bcolors.ENDC
def blueText(text):
    return '\033[34m'+str(text)+bcolors.ENDC
def magentaText(text):
    return '\033[95m'+str(text)+bcolors.ENDC
def cyanText(text):
    return '\033[96m'+str(text)+bcolors.ENDC

def redBG(text):
    return '\033[41m'+str(text)+bcolors.ENDC
def greenBG(text):
    return '\033[42m'+str(text)+bcolors.ENDC
def yellowBG(text):
    return '\033[43m'+str(text)+bcolors.ENDC
def blueBG(text):
    return '\033[44m'+str(text)+bcolors.ENDC
def magentaBG(text):
    return '\033[45m'+str(text)+bcolors.ENDC
def cyanBG(text):
    return '\033[46m'+str(text)+bcolors.ENDC
def lightGrayBG(text):
    return '\033[47m'+str(text)+bcolors.ENDC
def darkGrayBG(text):
    return '\033[100m'+str(text)+bcolors.ENDC
def whiteBG(text):
    return '\033[107m'+str(text)+bcolors.ENDC

def accepts_tuple_arg(func):
    def wrapper(*args, **kwargs):
        #args = map(lambda arg: (arg[0],arg[1] if isinstance(arg,tuple) else arg), args)
        #placeholder while I work on this
        temp = []
        for arg in args:
            if isinstance(arg,tuple):
                temp += [coord for coord in arg]
            else:
                temp.append(arg)
        return func(*temp, **kwargs)
    return wrapper
def add_tuples(a,b):
    return tuple([sum(x) for x in zip(a,b)])


if __name__ == "__main__":
    print(redBG("Hello"))







