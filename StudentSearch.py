import pickle
def studentsearch():
    try:
        studlist=[]
        with open("student.info","rb") as fp:
            while(True):
                try:
                    record=pickle.load(fp)
                    studlist.append(record)
                except EOFError:
                    break
            found=False
            stno=int(input("Enter student number to search the details:"))
            for indexval in range(0,len(studlist)):
                if(studlist[indexval][0]==stno):
                    found=True
                    recindex=indexval
                    break
            print("-"*50)
            if(found):
                print("Single student information")
                print("-"*50)
                for val in studlist[recindex]:
                    print(val,end="\t")
                print()
            else:
                print("Record doesnot exist")
            print("-"*50)
    except FileNotFoundError:
        print("File doesnot exist")        

