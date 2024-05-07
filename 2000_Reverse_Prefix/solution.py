def reversePrefix(word: str, ch: str):
    i = word.find(ch)
    
    if i != -1:
        new_word = word[:i+1]
        print(new_word)
        new_word = new_word[::-1]
        print(new_word)
        word = new_word + word[i+1:]
        print(word)
        return word
    
    return word
    
    

    
    
    
def main():
    word = 'abcd'
    ch = 'z'
    print(reversePrefix(word, ch))
    
    
if __name__ == '__main__':
    main()