# Using python to manipulate str
''''
Python can be used to manipulate strings, wich can
be expressed in sevral ways

They can be enclosed in single quotes ('...')
or double quotes ('...')

\' can be used to escape quotes

Python strings cannot be changed - They are immutable

We will also look ate the built in function called len()
This functions returns the length of a string:

Strings have a bunch of methods available:
    capitalized() -> Converts the first character to upper case
    casefold() -> Converts string into lower case
    center() -> Returns a centered string
    count(pattern: string) -> Returns the number of times a specified pattern occurs in a string
    encode() -> Returns an encoded version of the string
    endswitch(pattern: strin) -> Returns true if the string ends with the specified value
    expandtabs() ->  Sets the tab size of the string
    find() ->  Searches the string for a specified value and returns the position of where it was found
    format() ->  Formats specified values in a string
    format_map() ->  Formats specified values in a string
    index() ->  Searches the string for a specified value and returns the position of where it was found
    isalnum() ->  Returns True if all characters in the string are alphanumeric
    isalpha() ->  Returns True if all characters in the string are in the alphabet
    isascii() ->  Returns True if all characters in the string are ascii characters
    isdecimal() ->  Returns True if all characters in the string are decimals
    isdigit() ->  Returns True if all characters in the string are digits
    isidentifier() ->  Returns True if the string is an identifier
    islower() ->  Returns True if all characters in the string are lower case
    isnumeric() ->  Returns True if all characters in the string are numeric
    isprintable() ->  Returns True if all characters in the string are printable
    isspace() ->  Returns True if all characters in the string are whitespaces
    istitle() ->  Returns True if the string follows the rules of a title
    isupper() ->  Returns True if all characters in the string are upper case
    join() ->  Converts the elements of an iterable into a string
    ljust() ->  Returns a left justified version of the string
    lower() ->  Converts a string into lower case
    lstrip() ->  Returns a left trim version of the string
    maketrans() ->  Returns a translation table to be used in translations
    partition() ->  Returns a tuple where the string is parted into three parts
    replace() ->  Returns a string where a specified value is replaced with a specified value
    rfind() -> 	 Searches the string for a specified value and returns the last position of where it was found
    rindex() ->  Searches the string for a specified value and returns the last position of where it was found
    rjust() ->  Returns a right justified version of the string
    rpartition() ->  Returns a tuple where the string is parted into three parts
    rsplit() ->  Splits the string at the specified separator, and returns a list
    rstrip() ->  Returns a right trim version of the string
    split() ->  Splits the string at the specified separator, and returns a list
    splitlines() ->  Splits the string at line breaks and returns a list
    startswith() ->  Returns true if the string starts with the specified value
    strip() ->  Returns a trimmed version of the string
    swapcase() ->  Swaps cases, lower case becomes upper case and vice versa
    title() ->  Converts the first character of each word to upper case
    translate() ->  Returns a translated string
    upper() ->  Converts a string into upper case
    zfill() ->  Fills the string with a specified number of 0 values at the beginning
'''

# The basics
print('spam eggs') # A single quote string
print('Mcdonald\'s') # Used the scape-bit
print('"Yes", they said. And so I used double quotes inside of simple quote')

# New Line
my_str = 'First line.\nSecond line.' # We can use the ascii char like in C
print(my_str)

# Basically, if using the '' and need to use a simple quote inside the string you can either use the scape bit
# or use "" on the external quotes and will be understood that ' is from the string

# Raw String
print('C:some\name') # here \n means a new line
print(r'C:some\name') # here \n it's only a part of string, thanks to the 'r' being a regular expression

# String literals
# this following print will be like an comment on the display, so it can be used for doc maybe
print("""\
        Usage: thingy [OPTIONS]
        -h                          Display this usage message
        -H hostname                 Hostname to connect to
""")

# Concatenated

3 * 'un' + 'ium' # -> 'unununium'

'Did' 'Coding' # -> DidCoding

text = ('Put several strings within parentheses '
        'to have them joined together.')

print(text)

# this only works with two literals though
# not wth variables or expressions

prefix = 'Did'
prefix 'Coding' #-> Throwns an error!
prefix + 'Coding' #-> Correect



# Indexing
'''
 +---+---+---+---+---+---+---+---+---+
 | D | i | d | C | o | d | i | n | g |
 +---+---+---+---+---+---+---+---+---+
   0   1   2   3   4   5   6   7   8
  -9  -8  -7  -6  -5  -4  -3  -2  -1
'''

word = 'Didcoding'
word[0]  # character in position 0
word[5]  # character in position 5
word[0:2]  # characters from position 0 (included) to 2 (excluded)
word[2:5]  # characters from position 2 (included) to 5 (excluded)
word[:2]   # character from the beginning to position 2 (excluded)
word[4:]   # characters from position 4 (included) to the end
word[-2:]  # characters from the second-last (included) to the end
word[:2] + word[2:]
word[:4] + word[4:]

word[0] = 'p' #-> throwns a error, cuz literals are imutable and cannot be changed or assigned
# The correct way
new_world = 'P' + word[1:]
print(word[:2] + 'di')

# String length
s = 'bobby-didcoding'
len(s)

# Handy built-in functions
'''
When you don’t need fancy output but just want a quick display 
of some variables for debugging purposes, you can convert any 
value to a string with the repr() or str() functions.

The str() function is meant to return representations of values 
which are fairly human-readable, while repr() is meant to generate 
representations which can be read by the interpreter
You also have format().

The format() method formats the specified value(s) and insert them 
inside the string's placeholder '{}'.
'''

x=20
y=400 
print(repr((x,y, ('spam', 'eggs')))) #-> (20, 400, ('spam', 'eggs'))
print(str((x,y, ('spam', 'eggs')))) #-> (20, 400, ('spam', 'eggs'))

print('{0} and {1}'.format('spam', 'eggs')) #-> spam and eggs
print('{1} and {0}'.format('spam', 'eggs')) #-> eggs and spam
