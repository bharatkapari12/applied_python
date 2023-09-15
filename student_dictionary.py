# DICT of Student Information 
def Student_Input_Information():
    Student_information={}
    StdNo=int(input("Enter the no of Students:"))
    for i in range (StdNo):
        StudentNo="Student "+str(i)
        Student_information[StudentNo]={}
        name=input("Enter the Student name:")
        address=input("Enter the address of the Student:")
        phoneNo=input("Enter the phone number of the Student:")
        email=input("Enter the email of the Student:")
        SubjectAp=float(input("Enter the Marks for AP: "))
        SubjectCG=float(input("Enter the Marks for CG: "))
        SubjectCA=float(input("Enter the Marks for CA: "))
        Student_information[StudentNo]["name"]=name
        Student_information[StudentNo]["address"]=address
        Student_information[StudentNo]["phoneNo"]=phoneNo
        Student_information[StudentNo]["email"]=email
        Student_information[StudentNo]["SubjectAp"]=SubjectAp
        Student_information[StudentNo]["SubjectCG"]=SubjectCG
        Student_information[StudentNo]["SubjectCA"]=SubjectCA
       
    return Student_information

def Calculate_Grade(Student_information):
    print(Student_information)
    for key,value in Student_information.items():
        for key in value:
            print(key+":",value[key])
           
           

Student_information=Student_Input_Information()
Calculate_Grade(Student_information)