import  subprocess
import os

print('********** WELCOME TO SMS **********')
print ('1-Facebook',
       '2-Insta','3-LIN','4- All')

def facebook():
    user_id_facebook =input("Enter facebook user ID : ")
    url="https://www.facebook.com/"+user_id_facebook
    
    s= open("input.txt",'w')
    s.write(url)
    s.close()
    subprocess.Popen(["python", "facebook.py"])
    
def insta():
    user =input('Enter Instagram user name ')
    os.chdir("instagram/")
    os.system("instagram-scraper "+user)
    print(2)

def link():
    subprocess.Popen(["python", "linkedin.py"])
    
ch= int(input('Enter Your Choice: '))


if ch == 1  :
    facebook()
    
elif ch == 2 :
    print(2)
    insta()
    
    print(2)
elif ch == 3 :
    print(3)
    query = input("Enter Linkedin user id ")
    loca=input("Enter Linkedin user loca ")
    link()
    
elif ch == 4 :
    print(4)
    facebook()
    insta()
    query = input("Enter Linkedin user id ")
    loca=input("Enter Linkedin user loca ")
    link()
