def menu():
    print('--------------------------------------------------------------------------*---------------------------------------------------------------------------------------------------')
    print('                                                     WELCOME TO TECH HUB COMPUTER INSTITUTE         ')
    print('                                                                  VASANT KUNJ ')
    print('                                                                   NEW DELHI ')
    print('--------------------------------------------------------------------------*---------------------------------------------------------------------------------------------------')

    print('\n')
    print('                                                                         MENU')
    print()
    print('PRESS 1 FOR ENTERING A RECORD ')
    print('PRESS 2 FOR SEARCHING A RECORD ')
    print('PRESS 3 FOR DISPLAYING ALL THE RECORDS')
    print('PRESS 4 FOR DELETING A RECORD   ')
    print('PRESS 5 FOR EDITING A RECORD')
    print('PRESS 6 FOR EXIT')
    print('PRESS 7 FOR ABOUT US')
    print()
    print('--------------------------------------------------------------------------*---------------------------------------------------------------------------------------------------')
def course_menu():
    print('***************************************************************************************************************')
    print('*SNO.      *          COURSE NAME          *          COURSE DURATION          *          COURSE FEE          *')
    print('***************************************************************************************************************')
    print('*  1.      *  BASIC COMPUTER COURSE        *          2 MONTHS                 *         RS.5,000             *')
    print('*  2.      *  PYTHON FULL COURSE           *          6 MONTHS                 *         RS.10,000            *')
    print('*  3.      *  JAVA SCRIPT FULL COURSE      *          1 YEAR                   *         RS.30,000            *')
    print('*  4.      *  C++ FULL COURSE              *          1 YEAR                   *         RS.25,000            *')
    print('*  5.      *  WEB DEVELOPMENT              *          6 MONTHS                 *         RS.15,000            *')
    print('*  6.      *  GRAPHIC DESIGNING            *          6 MONTHS                 *         RS.15,000            *')
    print('*  7.      *  HTML FULL COURSE             *          3 MONTHS                 *         RS.6,000             *')
    print('*  8.      *  ETHICAL HACKING(18 ABOVE )   *          1 YEAR                   *         RS.35,000            *')
    print('***************************************************************************************************************')
    print('BOTH OFFLINE AND ONLINE CLASSES ARE AVAILABLE!')
def selectivedisplay():
    f=open('records.dat','rb')
    r=int(input('ENTER YOUR ENROLLMENT NO. FOR DETAILS: '))
    tf=0
    while f:
        try:
            rec=pickle.load(f)
            if rec[0]==r:
                print('*********************************************************')
                print()
                print('ENROLLMENT NO.: ',rec[0])
                print('NAME: ',rec[1])
                print('AGE: ',rec[2])
                print('CONTACT NO. : ',rec[3])
                print('ADRESS: ',rec[4])
                print('COURSE NAME: ',rec[5])
                print('COURSE DURATION: ',rec[6])
                print('COURSE FEES: ',rec[7])
                print('COURSE MODE: ',rec[8])
                print()
                print('*********************************************************')
                tf=1
                break
            
        except EOFError:
            break
    f.close()
    if tf==0:
        print('*************SORRY! RECORD NOT FOUND************************************')

import pickle
import os

def record_entry():
    try:
         e_no=int(input('ENTER ENROLLMENT NUMBER: '))
         name=input('ENTER NAME OF THE STUDENT: ')
         age=int(input('ENTER AGE OF THE STUDENT:'))
         mode=input('ENTER MODE OF CLASSES(offline/online): ')
         if age<16:
             print("SORRY! THE COURSES AVAILABLE ARE ONLY FOR 16 YEARS AND ABOVE STUDENTS")
         else:
             p_no=int(input('ENTER CONTACT NUMBER OF THE STUDENT:'))
             adress=input('ENTER THE ADRESS OF THE STUDENT: ')
             course_menu()
             c_no=input('CHOOSE A COURSE FROM THE ABOVE MENU AND ENTER ITS S.NO.: ')
         if c_no=='1':
             c_name="BASIC COMPUTER COURSE"
             c_duration='2 MONTHS'
             c_fee='RS.5,000'
         elif c_no=='2':
             c_name="PYTHON FULL COURSE"
             c_duration='6 MONTHS'
             c_fee='RS.10,000'
         elif c_no=='3':
             c_name="JAVA SCRIPT FULL COURSE"
             c_duration='1 YEAR '
             c_fee=' RS.30,000 '
         elif c_no=='4':
              c_name="C++ FULL COURSE"
              c_duration='1 YEAR '
              c_fee='RS.25,000'
         elif c_no=='5':
             c_name="WEB DEVELOPMENT"
             c_duration='6 MONTHS '
             c_fee='RS.15,000'
         elif c_no=='6':
             c_name="GRAPHIC DESIGNING"
             c_duration='6 MONTHS '
             c_fee='RS.15,000'
             
         elif c_no=='7':
             c_name="HTML FULL COURSE"
             c_duration='3 MONTHS '
             c_fee='RS.6,000'
         elif c_no=='8':
             if age<18:
                 print('SORRY! YOU ARE NOT ELIGIBLE FOR THIS COURSE')
             else:
                 c_name="ETHICAL HACKING"
                 c_duration='1 YEAR '
                 c_fee='RS.35,000'
                 
         else:
             print('PLEASE ENTER THE COURSE NO AVAILABLE IN COURSE LIST!')
         f=open("records.dat",'ab')
         r=[e_no,name,age,p_no,adress,c_name,c_duration,c_fee,mode]
         pickle.dump(r,f)
         print('HURRAY! ',name, 'YOU HAVE BEEN SUCESSFULLY REGISTERED FOR ',c_name)
         print('THANK YOU! FOR CHOOSING TECH HUB COMPUTER INSTITUTE ')
         f.close()
    except :
        print('PLEASE ENTER VALID DATA! ')
def COMPLETE_DISPLAY():
    f=open('records.dat','rb')
    while f:
        try:
            rec=pickle.load(f)
            print('*********************************************************')
            print()
            print('ENROLLMENT NO.: ',rec[0])
            print('NAME: ',rec[1])
            print('AGE: ',rec[2])
            print('CONTACT NO. : ',rec[3])
            print('ADRESS: ',rec[4])
            print('COURSE NAME: ',rec[5])
            print('COURSE DURATION: ',rec[6])
            print('COURSE FEES: ',rec[7])
            print('COURSE MODE: ',rec[8])
            print()
            print('*********************************************************')
            print()
        except EOFError:
            break
    f.close()
        
def modify():
    f = open("records.dat","rb")
    f1=open("temp.dat","wb")
    r= int(input("ENTER YOUR ENROLLMENT NO. TO UPDATE RECORDS:"))
    try:
        while f:
            l=pickle.load(f)
            print(l)
            if l[0]==r:
                print('CHOOSE THE FIELD YOU WANT TO EDIT ')
                print('1. NAME')
                print('2. AGE')
                print('3. CONTACT NUMBER')
                print('4. ADRESS')
                print('5. COURSE NAME')
                print('6. COURSE MODE')
                field=int(input('ENTER THE FIELD NO. YOU WANT TO EDIT: '))
                if field==1:
                    l[1]=input('ENTER NEW NAME: ')
                elif field==2:
                    l[2]=input('ENTER NEW AGE: ')
                elif field==3:
                    l[3]=input('ENTER NEW CONTACT NUMBER: ')
                elif field==4:
                    l[4]=input('ENTER NEW ADRESS: ')
                elif field==5:
                    course_menu()
                    c_no=input('CHOOSE A COURSE FROM THE ABOVE MENU AND ENTER ITS S.NO.: ')
                    if c_no=='1':
                        l[5]="BASIC COMPUTER COURSE"
                        l[6]='2 MONTHS'
                        l[7]='RS.5,000'
                    elif c_no=='2':
                        l[5]="PYTHON FULL COURSE"
                        l[6]='6 MONTHS'
                        l[7]='RS.10,000'
                    elif c_no=='3':
                        l[5]="JAVA SCRIPT FULL COURSE"
                        l[6]='1 YEAR '
                        l[7]=' RS.30,000 '
                    elif c_no=='4':
                        l[5]="C++ FULL COURSE"
                        l[6]='1 YEAR '
                        l[7]='RS.25,000'
                    elif c_no=='5':
                        l[5]="WEB DEVELOPMENT"
                        l[6]='6 MONTHS '
                        l[7]='RS.15,000'
                    elif c_no=='6':
                        l[5]="GRAPHIC DESIGNING"
                        l[6]='6 MONTHS '
                        l[7]='RS.15,000'
                    elif c_no=='7':
                        l[5]="HTML FULL COURSE"
                        l[6]='3 MONTHS '
                        l[7]='RS.6,000'
                    elif c_no=='8':
                        if l[2]<18:
                            print('SORRY! YOU ARE NOT ELIGIBLE FOR THIS COURSE')
                        else:
                            l[5]="ETHICAL HACKING"
                            l[6]='1 YEAR '
                            l[7]='RS.35,000'
                 
                    else:
                        print('PLEASE ENTER THE COURSE NO AVAILABLE IN COURSE LIST!')
                elif field==6:
                          l[8]=input('ENTER THE NEW COURSE MODE(ONLINE/OFFLINE): ')
                else:
                          print("PLEASE ENTER VALID CHOICE!")
                pickle.dump(l,f1)
            else:
                pickle.dump(l,f1)
    except EOFError:
        print('RECORD UPDATED! ')
    f.close()
    f1.close()
    os.remove('records.dat')
    os.rename('temp.dat','records.dat')
def delete():
    f = open("records.dat","rb")
    f1=open("temp.dat","wb")
    r= int(input("ENTER YOUR ENROLLMENT NO. TO DELETE RECORD:"))
    try:
        while f:
            data= pickle.load(f)
            if data[0]==r:
                    continue
            else:
                pickle.dump(data,f1)
    except EOFError:
        print('YOUR RECORD HAS BEEN SUCCESFULLY DELETED!')
    f.close()
    f1.close()
    os.remove('records.dat')
    os.rename('temp.dat','records.dat')
            
ch=1
pswd='tech hub1234'
while ch>0:
    menu()
    num=int(input('ENTER YOUR CHOICE FROM THE MENU: '))
    if num==1:
        x=int(input('ENTER NO. OF RECORDS YOU WANT TO ENTER: '))
        for i in range(0,x):
            record_entry()
    elif num==2:
        selectivedisplay()
    elif num==3:
        print('**ONLY ADMIN CAN SEE THE FULL RECORD**')
        p=input('ENTER THE ADMIN PASSWORD: ')
        if p==pswd:
            COMPLETE_DISPLAY()
        else:
            print('*******WARNING!*******')
            print('ENTER VALID PASSWORD!')
            continue
    elif num==4:
        print('**ONLY ADMIN CAN DELETE RECORD**')
        p=input('ENTER THE ADMIN PASSWORD: ')
        if p==pswd:
            delete()
        else:
            print('*******WARNING!*******')
            print('ENTER VALID PASSWORD!')
            continue
    elif num==5:
        modify()
    elif num==6:
        print()
        print('THANK YOU FOR BEING WITH US! ')
        break
    elif num==7:
        print('****************************************************************************************************************************************************************************')
        print('                                                                       ABOUT US                                         ')
        print('****************************************************************************************************************************************************************************')
        print()
        print('Our institute was started in the year 2010. At its earliest stage our institute provided the students with basic computer training, but now it is a government approved')
        print('computer coaching institute which provide with all types of computer courses from basic training to learning advanced level of programming languages. We have well  ')
        print('trained teachers which have been passed out from top universities. Our institute is one of the top computer training institute in Delhi and it provides both offline ')
        print('online classes. Our coaching center provides with smart classes and computer labs, it has been constructed on an area of 1.5 acers. Currently! 5k students are studying ')
        print('in our institute both offline and online.')
        print()
        print('ADRESS:- ')
        print()
        print('Plot no- 12, Vasant kunj, New Delhi-110070 ')
        print()
        print()
        print('HELP & SUPPORT')
        print()
        print('For help and support please reach us at our gmail id- tech_hub_care@gmail.com  or contact at our toll free no. 110-xxxxxxxxx ')
    else:
        print('PLEASE ENTER VALID CHOICE! ')
             
    


    
    
