'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    substr = "th"
    if len(word) < len(substr):
        return 0
    
    if word[:2] == substr:
        return count_th(word[1:]) + 1
        
    else:
        return count_th(word[1:])
        
    
    



print(count_th("ththth"))