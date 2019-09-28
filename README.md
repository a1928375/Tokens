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

