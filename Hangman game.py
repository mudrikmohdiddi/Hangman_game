def secret_word():
    from time import strftime
    list_word=["mmanga","muntathir","zaynab","chwaka","suza","sob","program","python","bita","print"]
    return list_word[int(strftime("%S")[1])]
def main():
    list_letter=list(secret_word())
    copy=list_letter.copy()
    correct=[]
    for i in range(len(list_letter)):
        correct.append("-")
    n=0
    for a in range(1,len(list_letter)+1):
        #print(list_letter)
        guessed=input("Enter only one guesses letter in word:")
        while((guessed not in list_letter) or len(guessed)!=1):
            if(guessed in correct):
                print("This letter has been entered,try other letter")
            else:
                print("You enter letter that not found in word")
            n+=1
            print(f"You have mistake {n} times")
            if(n>=6):
                print("Game is over")
                break
            guessed=input("Enter only one guesses letter in word:")
        if(n>=6):
            break
        q=0
        p=list_letter.index(guessed)
        if(list_letter.count(guessed)>1):
            list_letter.pop(p)
            list_letter.insert(p,"-")
            q=list_letter.index(guessed)
            list_letter.pop(q)
            list_letter.insert(q,"-")
            correct.pop(p)
            correct.insert(p,guessed)
            correct.pop(q)
            correct.insert(q,guessed)
        else:
            list_letter.pop(p)
            list_letter.insert(p,"-")
            correct.pop(p)
            correct.insert(p,guessed)
        #print(correct)
        str_correct=""
        for b in correct:
            str_correct+=b
        print(str_correct)
        if(correct==copy):
            break
    if(list(str_correct)==copy):
        print(f"congratulation you win at {((6-n)/6)*100}%")
        print(f"To complete word {str_correct}")
    else:
        print("You losse")
        print(f"To complete word {str_correct}")
main()    
            
        
                

