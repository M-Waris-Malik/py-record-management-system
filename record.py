def add_std():
    print()
    print("--------------------------")
    rollNo=input("Enter RollNo: ")
    name = input("Enter Name: ")
    sub = input("Enter Subject: ")
    grade= input("Enter Grade: ")
    rec= {"RollNo":rollNo, "Name":name, "Subject":sub, "Grade":grade}
    student.append(rec)
    print("--------------------------")
    print()
    
def dis_std():
    print()
    print("--------------------------")
    for i in student:
        print("RollNo:",i["RollNo"])
        print("Name: ",i["Name"])
        print("Subject: ",i["Subject"])
        print("Grade: ",i["Grade"])
        print("--------------------------")
        print()
def search():
    found=False
    print()
    print("--------------------------")
    urn=input("Enter Specific RollNo: ")
    for j in student:
        if urn==j["RollNo"]:
         found=True
         print("RollNo:",j["RollNo"])
         print("Name: ",j["Name"])
         print("Subject: ",j["Subject"])
         print("Grade: ",j["Grade"]) 
         print("--------------------------")
         print() 
         break          
    if found==False:
        print() 
        print("--------------------------")
        print("Student Not Found")
        print("--------------------------")
        print()
        
student=[]
while True:
    print("1.Add Student")
    print("2.Display Students")
    print("3.Search Student")
    print("0.Exit")
    val=int(input("Enter Your Choice: "))
    print("--------------------------")
    print()
    
    if val==1:
        add_std()
    elif val==2:
        dis_std()
    elif val==3:
        search()
    elif val==0:
        break
    else:
        print()
        print("--------------------------")
        print("Invalid input!")
        print("--------------------------")
        print()
        