# Tokens

(1) Specifying Tokens:  Write code for the LANGLESLASH token to match </ in our HTML.

(2) Quoted Strings:  Suppose a string starts with " and ends with " and contains any number of characters except ". Write a definition for t_STRING. Match Exactly:
    
    "cuneiform"
    "sumerian writing"
    
Do Not Match Exactly:
    "esc \" ape"
    League of Nations Treaty Series
    
(3) Whitespace:  Suppose a WORD is any number of characters EXCEPT < > or space. A WORD token should leave its value unchanged. Submit a definition for t_WORD.

(4) Crafting Input:  Define a variable called webpage that holds a string that causes our lexical analyzer to produce the exact output below: 

    LexToken(WORD,'This',1,0)
    LexToken(WORD,'is',1,5)
    LexToken(LANGLE,'<',2,11)
    LexToken(WORD,'b',2,12)
    LexToken(RANGLE,'>',2,13)
    LexToken(WORD,'webpage!',2,14)
    
(5) Identifier:  Identifiers are textual string descriptions that refer to program elements, such as variables and functions. Write a indentifier token rule for Javascript identifiers. The token rule should match:

    factorial
    underscore_separated
    mystery
    ABC

The token rule should not match:

    _starts_wrong
    123

(6) Numbers:  Write a indentifier token rule for Javascript numbers that converts the value of the token to a float.

The token rule should match:

    12
    5.6
    -1.
    3.14159
    -8.1
    867.5309

The token rule should not match:

    1.2.3.4
    five
    jenny

(7) Hexadecimal Numbers:  In this exercise you will write a lexical analyzer that breaks strings up into whitespace-separated identifiers and numbers. An identifier is a sequence of one or more upper- or lower-case letters. In this exercise, however, there are two types of numbers: decimal numbers, and _hexadecimal_ numbers. Humans usually write numbers using "decimal" or "base 10" notation. The number# 234 means 2*10^2 + 3*10 + 4*1. It is also possible to write numbers using other "bases", like "base 16" or "hexadecimal". Computers often use base 16 because 16 is a convenient power of two (i.e., it is a closer fit to the "binary" system that computers use internally). A hexadecimal number always starts with the two-character prefix "0x" so that you know not to mistake it for a binary number. The number 0x234 means

        2 * 16^2
        + 3 * 16^1
        + 4 * 16^0 
        = 564 decimal. 

Because base 16 is larger than base 10, the letters 'a' through 'f' are used to represent the numbers '10' through '15'. So the hexadecimal number 0xb is the same as the decimal number 11. When read out loud, the "0x" is often pronounced like "hex". "0x" must always be followed by at least one hexadecimal digit to count as a hexadecimal number. Modern programming languages like Python can understand hexadecimal numbers natively! Try it: 

    print 0x234  # uncomment me to see 564 printed
    print 0xb    # uncomment me to see 11 printed 

This provides an easy way to test your knowledge of hexadecimal. For this assignment you must write token definition rules (e.g., t_ID,  t_NUM_hex) that will break up a string of whitespace-separated identifiers and numbers (either decimal or hexadecimal) into ID and NUM  tokens. If the token is an ID, you should store its text in the token.value field. If the token is a NUM, you must store its numerical
value (NOT a string) in the token.value field. This means that if a hexadecimal string is found, you must convert it to a decimal value. 

Hint 1: When presented with a hexadecimal string like "0x2b4", you can convert it to a decimal number in stages, reading it from left to right:
        
        number = 0              # '0x' 
        number = number * 16 
        number = number + 2     # '2'
        number = number * 16 
        number = number + 11    # 'b'
        number = number * 16
        number = number + 4     # '4'
        
Of course, since you don't know the number of digits in advance, you'll probably want some sort of loop. There are other ways to convert a hexadecimal string to a number. You may use any way that works. Hint 2: The Python function ord() will convert a single letter into an ordered internal numerical representation. This allows you to perform simple arithmetic on numbers:  
       
       print ord('c') - ord('a') == 2 

(8) Expanding Exp
