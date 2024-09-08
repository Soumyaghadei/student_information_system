import pickle 
class InvalidNameError(Exception):pass

def validatename(name):
    words=name.split()
    if(len(words)==0):
        raise ZeroDivisionError
    else:
        res=False
        for word in words:
            if(not word.isalpha()):
                res=True
                break
        if(res):
            raise InvalidNameError
        else:
            return name
def insertrecords():
    with open("student.info","ab") as fp:
        try:
            print("-"*50)
            sno=int(input("Enter student Number::"))
            sname=validatename(input("Enter Student Name:"))
            marks=float(input("Enter student marks:"))
            print("-"*50)
            lst=list()
            lst.append(sno)
            lst.append(sname)
            lst.append(marks)
            pickle.dump(lst,fp)
            print("Student data saved successfully in a file")
        except ValueError:
            print("Dont entter strs,symbols,and alnum for sno and marks---try again")
        except InvalidNameError:
            print("Dont enter the name with digits,special symbol--try again")

