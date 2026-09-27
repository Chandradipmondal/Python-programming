#palindromes means some words or numbers which read first to last and last to first giving same number , one single words or number is cal
def palin(text):
    if len(text) <=1 :
        print("Palindrome")
    else:
        if text[0]==text[-1]:
            return palin(text[1:-1])
        else:
            print("not palindrome")
palin('madam')
palin('madam')
palin('malalam')
palin('lala')