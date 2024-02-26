import pandas as pd

mydf = pd.read_csv("mostwatchedvideos.csv")
flag = True

def menu():
    while flag:
        print("(1) 5 Most Watched Videos")
        print("(2) 5 Most Liked Videos")
        print("(3) 5 Most Commented on Videos")
        
        userchoice = input("Please select an option: ")
        
        try:
            choice = int(userchoice)
            if choice < 1 or choice > 3:
                print("Invalid choice")
                return menu()
            else:
                return choice
        
            break 
        except ValueError:
            print("Invalid Choice, Please try again.")

if flag:
    choice = menu() 

def mostwatchedvideos():
    newdf1 = mydf.copy(deep = True)
    top5watched = newdf1.nlargest(5, "view_count")
    print(top5watched)

def mostlikedvideos():
    newdf2 = mydf.copy(deep = True)
    top5liked = newdf2.nlargest(5, "like_count")
    print(top5liked)

def mostcommentsvideo():
    newdf3 = mydf.copy(deep = True)
    top5comments = newdf3.nlargest(5, "comment_count")
    print(top5comments)

if choice == 1:
    mostwatchedvideos()
elif choice == 2:
    mostlikedvideos()
elif choice == 3:
    mostcommentsvideo()

