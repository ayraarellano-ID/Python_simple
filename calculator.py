import math
import sys


def calc(term):
	term = term.replace('rad', 'radians')
	term = term.replace('%', '/100')
    term = term.replace(' ', '')
    term = term.replace('^', '**')
    term = term.replace('=', '')
    term = term.replace('?', '')
    
    
    term = term.replace('mod', '%')

    functions = ['sin', 'cos', 'tan', 'cosh', 'sinh', 'tanh', 'sqrt', 'pi', 'radians', 'e'] 
    term = term.lower()
    
    for function in functions:            
        if function in term:
            withmath = 'math.' + function
            term = term.replace(function, withmath)

    try:
        term = eval(term)

    except ZeroDivisionError:

        print("Undefined")

    except NameError:

        print('Invalid')

    except AttributeError:

        print('Invalid')
        
    return term


def result(term):
    print("\n" + str(calc(term)))


def main():
    print("\nScientific Calculator\n\nFor Example: sin(rad(90)) + 50% * (sqrt(16)) + round(1.42^2)"+\
          "- 12mod3\n\nEnter quit to exit")

    if sys.version_info.major >= 3:
        while True:
            k = input("\nINPUT: ")
            if k == 'quit':
                break
            result(k)

    else:
        while True:
            k = raw_input("\nINPUT: ")
            if k == 'quit':
                break
            result(k)


if __name__ == '__main__':
    main()