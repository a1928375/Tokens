grammar = [ 
    ("exp", ["exp", "+", "exp"]),
    ("exp", ["exp", "-", "exp"]),
    ("exp", ["(", "exp", ")"]),
    ("exp", ["num"]),
    ]

def expand(tokens, grammar):
    
    for pos in range(len(tokens)):   # this tokens means sentence => sentence is element of utterances => Ex: ["exp"]
                                     # len(tokens) => len(sentence) => len("exp") (because sentence will be longer 
                                     # in different depth, Ex: len(['exp', '+', 'exp'])) => so every "exp" should be 
                                     # replaced
        for rule in grammar:         # Ex: rule = ("exp", ["exp", "+", "exp"])
            
            if tokens[pos] == rule[0]:
                
                yield tokens[0:pos]+rule[1]+tokens[pos+1:]
                
depth = 1

utterances = [["exp"]]

for x in range(depth):
    
    for sentence in utterances:
        
        utterances = utterances + [ i for i in expand(sentence, grammar)]

for sentence in utterances:
    
    print (sentence)
