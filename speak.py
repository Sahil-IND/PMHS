import pyttsx3
import datetime
import pickle
stu={} # 1
st={}  # 2
su={}  # 3
tu={}  # 4
found=False

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1])
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

print("Hello my name is zid")
print("I am your PMHS")
print("PMHS:--- PROJECT MANGEMENT HELPING SYSTEM")
print("I was created by Sahil from class-12th ")
print("Please let me know how can i help you")
print("you can select from the following:---")
    
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")
        speak("Hello my name is zid")
        speak("I am your PMHS")
        speak("PMHS stands for PROJECT MANGEMENT HELPING SYSTEM")
        speak("I was created by Sahil from class-12th ")
        speak("Please let me know how can i help you")
        speak("you can select from the following")


    elif hour>=12 and hour<18:
        speak("Good afternoon Sir")
        speak("Hello my name is zid") # guru,captain,Zid,chatterbox,astronaut
        speak("I am your PMHS")
        speak("PMHS stands for PROJECT MANGEMENT HELPING SYSTEM")
        speak("I was created by Sahil from class-12th ")
        speak("Please let me know how can i help you")
        speak("you can select from the following")


    else:
        speak("Good evening Sir ")   
        speak("Hello my name is zid")
        speak("I am your PMHS")
        speak("PMHS stands for PROJECT MANGEMENT HELPING SYSTEM")
        speak("I was created by Sahil from class-12th ")
        speak("Please let me know how can i help you")
        speak("you can select from the following")



if __name__ == "__main__":
    wishMe()





# adding

def adddata():
    speak("you selected add data")
    f1=open("cs.dat","wb")
    ans='y'
    while ans=='y':
        speak("enter the roll number")
        rno=int(input("enter the roll number:--- "))
        speak("enter the name")
        name=input("enter the name:--- ")
        speak("enter the project name")
        pro=input("enter the project name:--- ")
        stu['rollno']=rno
        stu['name']=name
        stu['project']=pro
        pickle.dump(stu,f1)
        speak("Please let me know you want to add more record or not")
        ans=input("want to add more data y/n:--- ")
    f1.close()

#  -------------------------------------------------------------------------------------------------------------------
# showing

def showdata():
    speak("you selected show data")
    f2=open("cs.dat","rb")
    try:
        print("the file contains:---")
        speak("the file contains")
        while True:
            st=pickle.load(f2)
            print(st)
            speak(st)
    except EOFError:
        f2.close()
# --------------------------------------------------------------------
# searching

def searchdata():
    speak("you selected search for data")
    f3=open("cs.dat","rb")
    speak("enter the roll number to be searched")
    a=int(input("enter the roll number to be searched:--- "))
    sc=[a]
    try:
        print("data:-------------------------------------")
        while True:
            su=pickle.load(f3)
            if su['rollno']in sc:
                print(su)
                speak(su)
                found=True
    except EOFError:
        if found==False:
            print("no such data in present in the record")
            speak("no such data in present in the record")
        else:
            print("search sucessful....")
            speak("search sucessful....")

# ----------------------------------------------------------------
# modifying

def modifydata():
    speak("you selected modify data")
    f4=open("cs.dat","rb+")
    speak("enter the project name you want to update")
    pr=input("enter the project name:--- ")
    speak("enter new project name")
    pr1=input("enter new project name:--- ") 
    try:
        while True:       
            cp=f4.tell()
            tu=pickle.load(f4)
            if tu['project']==pr:
                tu['project']=pr1
                f4.seek(cp)
                pickle.dump(tu,f4)
                print(tu)
                speak(tu)
                found=True
    except EOFError:
        if found==False:
            print("no such data in present in the record")
            speak("no such data in present in the record")            
            


        else :
            print("updated sucessfully")
            speak("updated sucessfully")


# -------------------------------------------------------------------------------------
# processing

def mainmenu():
    

    speak("Add new data in the record")
    speak("show the data")
    speak("Search for a data")
    speak("Modify Existing data")
    speak("Exit")
    choice=0
    while choice!=5:
        print("\n")
        print("1. Add new data in the record")
        print("2. show the  data")
        print("3. Search for a data")
        print("4. Modify Existing data")
        print("5. Exit")


        speak("Please tell me what you want to do now ")
        
        choice=int(input('Enter your choice:---'))
        if choice==1:
            adddata()
        elif choice==2:
            showdata()
        elif choice==3:
            searchdata()
        elif choice==4:
            modifydata()
        elif choice==5:
            print("all the work has been done")
            print("and saved")
            print("have a nice day...")
            speak("all the work has been done")
            speak("and saved")
            speak("have a nice day...")
            break
mainmenu()
