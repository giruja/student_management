import json
import os
print("Student Management System")
print("---------------------------")
print("1.Add Student")
print("2.View All Students")
print("3.Search Student")
print("4.Update Student")
print("5.Show Rank")
print("6.Save Records")
print("7.Load Records")
print("8.Exit")

student_list=[]
def add_student(student_id,student_name,eng_mark,tam_mark,math_mark,sci_mark,social_mark):
    student={
    "ID":student_id,
    "Name":student_name,
    "English Mark":eng_mark,
    "Tamil Mark":tam_mark,
    "Maths Mark":math_mark,
    "Science Mark":sci_mark,
    "Social Mark":social_mark
    }
    student_list.append(student)
def view_students():
    if student_list:
        for item in student_list:
            for key,value in item.items():
                print(f"{key}-{value}")
    else:
        print("There are no records")
def search_student(student_id):
    for item in student_list:   
        if item["ID"]==student_id:
            for key,value in item.items():
                print(f"{key}-{value}")
            return
    print("ID not Found!")
def update_student(student_id):
    for item in student_list:
        if item["ID"]==student_id:
            print("1.Update Name")
            print("2.Update Mark")
            ch=int(input("Enter your choice:"))
            if ch==1:
                corrected_name=input("Enter the corrected name:")
                item["Name"]=corrected_name
            elif ch==2:
                print("1.Update English Mark")
                print("2.Update Tamil Mark")
                print("3.Update Maths Mark")
                print("4.Update Science Mark")
                print("5.Update Social Mark")
                choice=int(input("Enter your choice:"))
                if choice==1:
                    corrected_eng=int(input("Enter the corrected English Mark:"))
                    item["English Mark"]=corrected_eng
                elif choice==2:
                    corrected_tam=int(input("Enter the corrected Tamil Mark:"))
                    item["Tamil Mark"]=corrected_tam
                elif choice==3:
                    corrected_math=int(input("Enter the corrected Maths Mark:"))
                    item["Maths Mark"]=corrected_math
                elif choice==4:
                    corrected_sci=int(input("Enter the corrected Science Mark:"))
                    item["Science Mark"]=corrected_sci
                elif choice==5:
                    corrected_social=int(input("Enter the corrected Social Mark:"))
                    item["Social Mark"]=corrected_social
                    
def show_rank():
    for item in student_list:
        total=item["English Mark"]+item["Tamil Mark"]+item["Maths Mark"]+item["Science Mark"]+item["Social Mark"]
        item["Total"]=total
    sorted_list=sorted(student_list, key=lambda x:x["Total"], reverse=True)
    for rank,student in enumerate(sorted_list,start=1):
        print(f"{rank}-{student['Name']}")
        
   
while True:
  try:
    ch=int(input("Enter your choice:"))
    if ch==8:
        print("Thank You")
        break
    elif ch==1:
        student_id=int(input("Enter the student ID:"))
        student_name=input("Enter the student name:")
        eng_mark=int(input("Enter the English mark:"))
        tam_mark=int(input("Enter the Tamil mark:"))
        math_mark=int(input("Enter the Maths mark:"))
        sci_mark=int(input("Enter the Science mark:"))
        social_mark=int(input("Enter the social mark:"))
        add_student(student_id,student_name,eng_mark,tam_mark,math_mark,sci_mark,social_mark)
    elif ch==2:
        view_students()
    elif ch==3:
        student_id=int(input("Enter the student ID whose details are to be shown:"))
        search_student(student_id)
    elif ch==4:
        student_id=int(input("Enter the student ID whose details are to be updated:"))
        update_student(student_id)
    elif ch==5:
        show_rank()
    elif ch==6:
        with open("student.json","w") as f:
            json.dump(student_list,f)
            print("Data Saved")
    elif ch==7:
        if os.path.exists("student.json"):
          with open("student.json","r") as f:
            data=json.load(f)
            student_list.clear()
            student_list.extend(data)
            print("Data Loaded Successfully")
        else:
            print("No saved file found")
       
  except ValueError:
      print("Please enter only numbers")
      
        
        
        
        
       
        
