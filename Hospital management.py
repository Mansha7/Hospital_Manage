#-----------------------------------------------------------------------------

# SECTION-1: MANIPULATING THE DATABASE.

def admin():
    while True:
        print("\t\t.....................................")
        print("\t\t*****Database Management System*****")
        print("\t\t.....................................")
        print("\n\t\t*****HOSPITAL*****")
        print("1: Add Record")
        print("2: Show Table")
        print("3: Search")
        print("4: Delete Records")
        print("5: Update Records")
        print("7: Return")
        print("\t\t.....................................")
        choice=int(input("Enter your choice"))
        if choice==1:
            hospital.admin_details()
        elif choice==2:
            hospital.show_details()
        elif choice==3:
            hospital.search_details()
        elif choice==4:
            hospital.delete_details()
        elif choice==5:
            hospital.edit_name()
        elif choice==6:
            break
        else:
            print("Error: Invalid choice try again....")
            input("Press enter to continue")
            
# SECTION-1.1: ADD RECORD.

    def admin_details():
    
        try:
            #mycon=mysql connecing stuff
            cursor=mycon.cursor()
            number=input("Enter serial number:")
            Hospital=input("Enter name of hospital:")
            Location=input("Enter location of hospital:")
            bedassigned=int(input("Enter number of available beds:"))
            contactinfo=int(input("Enter phone number:"))
            Staffno=int(input("Enter serial number:"))

            query="insert into hospital(number,Hospital,Location,bedassigned,contactinfo,Staffno)values('{}','{}','{}',{},{},{})".format(number,Hospital,Location,bedassigned,contactinfo,Staffno)
            cursor.execute(query)
            mycon.commit()
            mycon.close()
            cursor.close()
            print("Record has been saved in hostpital table")
        except:
            print("error")
            
# SECTION-1.2: SHOW TABLE.

    def show_details():
    
        #mycon=#mysql connecing stuff
        cursor=mycon.cursor()
        cursor.execute("select * from hospital")
        data=cursor.fetchall()
        for row in data:
            print(row)
            
# SECTION-1.3: SEARCH DATA.

    def search_details():

        #mycon=#mysql connecing stuff
        cursor=mycon.cursor()
        ac=input('Enter number:')
        st="select * from hospital where number='%s'"%(ac)
        cursor.exectute(st)
        data=cursor.fetchall()
        print(data)

 # SECTION-1.4: DELETE RECORD.

    def delete_details():
        
        #mycon=#mysql connecing stuff
        cursor=mycon.cursor()
        ac=input('Enter number:')
        st="delete from hospital where number='%s'"%(ac)
        cursor.execute(st)
        mycon.commit()
        print("Data deleted successfully")
        
 # SECTION-1.5: UPDATE RECORD.
 
    def edit_details():
        
        #mycon=#mysql connecing stuff
        cursor=mycon.cursor()

        print("1: Edit hospital name")
        print("2: Edit location")
        print("3: Edit number of beds")
        print("4: Edit contact info")
        print("5: Edit staff number")
        print("6: Return")
        print("\t\t------------------------------")
        choice=int(input("Enter your choice"))
        if choice==1:
            hospital.edit_name()
        elif choice==2:
            hospital.edit_location()
        elif choice==3:
            hospital.edit_beds()
        elif choice==4:
            hospital.edit_contact()
        elif choice==5:
            hospital.edit_staff()
        elif choice==6:
            return
        else:
            print("Error: Invalid Choice. Try again....")
            input("Press enter to continue")
            
    def edit_name():
        
        #mycon=#mysql connecing stuff
        cursor=mycon.cursor()
        ac=input('Enter number:')
        nm=input('Enter correct name:')
        st="update hospital set Hospital='%s' where number='%s'"%(nm,ac)
        cursor.execute(st)
        mycon.commit()
        print('Data updated successfully')
        
    def edit_location():
        
        #mycon=#mysql connecing stuff
        cursor=mycon.cursor()
        ac=input('Enter number:')
        nm=input('Enter correct location:')
        st="update hospital set Location='%s' where number='%s'"%(nm,ac)
        cursor.execute(st)
        mycon.commit()
        print('Data updated successfully')
        
    def edit_beds():
        
        #mycon=#mysql connecing stuff
        cursor=mycon.cursor()
        ac=input('Enter number:')
        nm=input('Enter correct no: of beds:')
        st="update hospital set bedassigned ='%s' where number='%s'"%(nm,ac)
        cursor.execute(st)
        mycon.commit()
        print('Data updated successfully')
        
    def edit_contact():
        
        #mycon=#mysql connecing stuff
        cursor=mycon.cursor()
        ac=input('Enter number:')
        nm=input('Enter correct contact:')
        st="uptade hospital set contactinfo='%s' where number='%s'"%(nm,ac)
        cursor.execute(st)
        mycon.commit()
        print('Data updated successfully')
        
    def edit_staff():
        
        #mycon=#mysql connecing stuff
        cursor=mycon.cursor()
        ac=input('Enter number:')
        nm=input('Enter correct no: of staff:')
        st="uptade hospital set Staffno='%s' where number='%s'"%(nm,ac)
        cursor.execute(st)
        mycon.commit()
        print('Data updated successfully')

#--------------------------------------------------------------------------------------------
    

# SECTION-2: LOGIN



users = {}
status = " "


def displayMenu():
    status = input("Are you registered user? y/n? Press q to quit: ")
    if status == "y":
        oldUser()
    elif status == "n":
        newUser()
    elif status == "q":
        print("\t\t---------------------------------------------")
        print("\t\t\t***Have a nice day.***")
        print("\t\t---------------------------------------------")
        displayMenu()
    else:
        print("\n\tINVALID CHOICE....TRY AGAIN!!\n")
        displayMenu()


    
def newUser():
    
    print("\t\t---------------------------------------------")
    print("\t\t\t\t SIGN UP")
    print("\t\t---------------------------------------------")
    print("\n(Press enter to go back)\n")
    
    createLogin = input("Create login name: ")
 
    if createLogin in users or createLogin=='Admin':
        print("\n\t ***Login name already exist!***\n")
        newUser()
    elif createLogin=="":
        displayMenu()
    else:
     #  createPassw = input("Create password:/n(Password must contain minimum 4 characters.)")
        #while createPassw==" " or len(createPassw)<4:
            #print("Valid password required!")
            #createPassw = input("Create password:/n(Password must contain minimum 4 characters.)")
            
        users[createLogin] = createPassw
        print("\n\t***User created!***\n")
        print("\nLogin successful!\n")
        
    
        
    
        
def oldUser():

    print("\t\t---------------------------------------------")
    print("\t\t\t\t LOGIN")
    print("\t\t---------------------------------------------")
    print("\n(Press enter to go back)\n")
    
    login = input("Enter login name: ")
    if login=="":
        displayMenu()
        return
    #while login not in 'a b c d e f g h i j k l m n o p q r s t u v w x y z' or login not in 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z':
   
       # print("Please enter a valid name!")
        #login = input("Enter login name: ")
        
    
    passw = input("Enter password:/n (Password should contain minimum 4 characters.)")
    if len(passw)<4:
            print("Valid password required!")
            
            
    if login in users and users[login] == passw:
        print("\nLogin successful!\n")
        
    elif login=='Admin' and passw=='project':
        print("You are logged in as admin.")
        admin()
    elif passw=="":
        displayMenu()
        
    else:
        print("\nUser doesn't exist or wrong password!\n")
        displayMenu()    

 

displayMenu()    


    
age=int(input("Enter age:"))

#while age not in "1 2 3 4 5 6 7 8 9 0" and age>100 or age<=0:
    print("Please enter valid age!")
    age=int(input("Enter age:"))
    
    
    
gender=input("Enter gender (M-Male/F-Female):")
#while gender != 'M' and gender != 'F':
    print("Please enter M for Male and F for Female")
    gender=input("Enter gender (M-Male/F-Female):")
    
name=input("Enter your name:")

#while name not in 'a b c d e f g h i j k l m n o p q r s t u v w x y z' or name not in 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z':
    print("Please enter a valid name!")
    name=input("Enter your name:")
    
        
print("---------------------------------------------")

#------------------------------------------------------------------------

#SECTION-3: HOSPITAL

#------------------------------------------------------------------------

# SECTION-4: DIAGNOSIS.

def diagonise():
    Fev=[1,13,17,18,44,19,20,21,22,23,24]
    Nausmig=[4,5,30,9,10,41,29]
    Bronchasthma=[6,7,29,31,15,28,21,32,3,9,16]
    Pneumonia=[10,3,1,46,41,9,29,39,42,4,30,21]
    Anaemia=[11,16,45,44,19,22]
    
    print("Common illnesses and symptoms:\n")
    print("ILLNESS:/n")
    print("1)  fever")
    print("2)  common cold")
    print("3)  cough")
    print("4)  nausea")
    print("5)  migraine")
    print("6)  bronchitis")
    print("7)  asthma")
    print("8)  diarrhoea")
    print("9)  headache")
    print("10) pneumonia")
    print("11) anaemia")
    print("12) any kind of pain\n")      

          
    print("SYMPTOMS:\n")
    print("13) chills")
    print("14) itching")
    print("15) sore throat")
    print("16) tiredness")
    print("17) high temperature")
    print("18) sickness")
    print("19) lethargy")
    print("20) depression")
    print("21) loss of appetite")
    print("22) sleepiness")
    print("23) hyperalgesia")
    print("24) inability to concentrate")
    print("25) urge-to-vomit")
    print("26) severe-headache")
    print("27) sore-throat")
    print("28) blocked-nose")
    print("29) wheezing")
    print("30) vomiting")
    print("31) shortness-of-breath")
    print("32) tight-chest")
    print("33) stomach-cramps")
    print("34) diarrhoea")
    print("35) headache")
    print("36) pneumonia")
    print("37) anaemia")
    print("38) any kind of pain")
    print("39) fatigue")
    print("40) rapid-heartbeat")
    print("41) chest-pain")
    print("42) coughing-up-blood")
    print("43) weakness")
    print("44) dizziness")
    print("45) fainting")
    print("46) sweating")

    lst1=[]     
    while True:
        print("type 0 to to exit")
        sym=int(input("Please enter the symptoms/illness from the list printed above:"))
        lst1.append(sym)
        if sym==0:
            break
         
    
    
    
    cf=cn=cb=ca=cp=0
    for i in lst1:
        if i in Fev:
            cf+=1
        elif i in Nausmig:
            cn+=1
        elif i in Bronchasthma:
            cb+=1
        elif i in Anaemia:
            ca+=1
        elif i in Pneumonia:
            cp+=1
    countlist=[cf,cn,cb,ca,cp]
    maxi=max(countlist)
    if maxi==cf:
        print("RESULT: FEVER!")
        input("press enter to coninue:")
    elif maxi==cn:
        print("RESULT: NAUSEA OR MIGRAINE!")
        input("press enter to coninue:")
    elif maxi==cb:
        print("RESULT: BRONCHITIS OR ASTHMA!")
        input("press enter to coninue:")
    elif maxi==ca:
        print("RESULT: ANAEMIA!")
        input("press enter to coninue:")
    elif maxi==cp:
        print("RESULT: PNEUMONIA!")
        input("press enter to coninue:")

#------------------------------------------------------------

# SECTION-5: INJURY.

def injury():
    injury=1


    while injury!=0:
        print("select injury:",'\n\t')
        print("1. Cut/Scrape",'\t')
        print("2. Burn",'\t')
        print("3. Insect Bite/Sting",'\t')
        print("4. Splinter",'\t')
        print("5. Sunburn",'\t')
        print("6. Nosebleed",'\t')   
        print("7. Sprains, Strains, and Tears",'\t')
        print("8. Fractures",'\t')
        print("(Press 0 to exit)")
        print("\t")
        injury=int(input("Enter the number corresponding to injury: "))
        print("\t")

        if injury==1:
            print("-------------------------------------------------------------------------------")
            
            print("* If there is bleeding, press firmly over the site with a clean cloth")
            print("  until it stops, anywhere from three to 15 minutes.",'\n')
            
            print("* Clean with lukewarm running water and gently pat dry.",'\n')
            
            print("* If the skin is broken, apply a thin layer of antibiotic ointment,")
            print("  then cover with a bandage or gauze and adhesive tape.","\n")
            
            print("* If you can't control the bleeding after several attempts with direct pressure,")
            print("  call your pediatrician or head to an Emergency Room.","\n")
            
            print("* Continue utilize antibiotic ointment and apply a new bandage daily")
            print("  (or more often if necessary) until the cut heals.","\n")
            
            print("* If the wound appears to be forming or draining pus or becomes swollen,")
            print("  tender, or red, see a doctor right away to treat the infection.","\n")
            
            print("-------------------------------------------------------------------------------")
            
            input("Press enter to coninue:")
            print("...............................................................................")

        elif injury==2:
            print("-------------------------------------------------------------------------------")
             
            print("* Immediately hold injury under cold running water or apply a cold,")
            print("  wet towel until the pain subsides.","\n")

            print("* Cover any small blisters with a loose bandage or gauze and tape.","\n")
                  
            print("* Call a doctor as soon as possible if burns are on the face, hands, or genitals,")
            print("  or if they're larger than 1/4 inch anywhere on the body.","\n")

            print("* If the injury looks rooted, go to the Emergency Room.","\n")
                  
            print("* For a burn covering a tenth of the body or more, don't use cold compresses;")
            print("* CALL 112 and cover up with a clean sheet or a blanket to prevent hypothermia until help arrives.","\n")
                  
            print("* DO NOT pop any blisters yourself.","\n")
                  
            print("* If the skin breaks, apply antibiotic cream and cover the area with a bandage or gauze until it's healed.","\n")
                  
            print("* Watch for any redness, swelling, tenderness, or discharge for these are all signs of infection.")

            print("-------------------------------------------------------------------------------")

            input("Press enter to coninue:")
            print("...............................................................................")

        elif injury==3:
            print("-------------------------------------------------------------------------------")
            
            print("* If the insect left a stinger, gently scrape the skin with your fingernail to remove it without breaking it.","\n")
            
            print("* Refrain from using tweezers because that can squeeze more venom out of the stinger, causing further injury.","\n")
            
            print("* Call 911 if you have trouble breathing, coughing, or develop a hoarse voice, hives, or swollen lips or tongue.","\n")
            
            print("* To combat itching, apply 1% hydrocortisone cream or a topical antihistamine if the skin isn't broken or scabbed.","\n")
            
            print("* Contact your doctor if you suspect a tick bite. They may want to test for Lyme disease and other tick-borne diseases.","\n")

            print("-------------------------------------------------------------------------------")

            input("Press enter to coninue:")
            print("...............................................................................")

        elif injury==4:
            print("-------------------------------------------------------------------------------")

            print("* Use soap and water to wash around the splinter.","\n")
            
            print("* Clean a pair of tweezers with rubbing alcohol and slowly pull the splinter out.","\n")
            
            print("* Rewash the skin.","\n")
            
            print("* If you come across a fragment that is hard to remove, leave it for a day or so to see if it will come out on its own.","\n")

            print("-------------------------------------------------------------------------------")

            input("Press enter to coninue:")
            print("...............................................................................")

        elif injury==5:
            print("-------------------------------------------------------------------------------")

            print("* If you feel dizzy, weak, sick to your stomach, or are spiking a high fever—or if the")
            print("  burn is severe (oozing blisters form within 48 hours) and covering a significant portion of your body—go to the Emergency Room.","\n")

            print("* If your only symptoms are discomfort and redness, apply cold compresses and aloe vera lotion and take some ibuprofen.","\n")

            print("* Avoid creams with petroleum, which can cause infection, or anything ending in -Caine.")
            print("  When not administered by a professional, these drugs may be dangerous.","\n")

            print("-------------------------------------------------------------------------------")

            input("Press enter to coninue:")
            print("...............................................................................")

        elif injury==6:
            print("-------------------------------------------------------------------------------")


            print("* Sit upright and don't tilt your head back.","\n")
            print("* Loosen any tight clothing around your neck.","\n")
            
            print("* Pinch the lower end of the nose close to the nostrils and lean forward while you apply constant pressure for five to ten minutes.","\n")
            
            print("* Don't release and check the nose; it could prolong the bleeding.","\n")
            
            print("* If the nosebleed is the result of trauma, you can reduce swelling by holding an ice pack against the bridge of the nose after the bleeding slows down.","\n")
            
            print("* If it persists for more than ten minutes or returns later, call your doctor or go to the Emergency Room to check for breakage.","\n")

            print("-------------------------------------------------------------------------------")

            input("Press enter to coninue:")
            print("...............................................................................")

        elif injury==7:
            print("-------------------------------------------------------------------------------")
            
            print("* When a sprain, strain, or tear takes place, the first thing to do is immobilize the affected area, elevate it, and apply ice and compression to reduce swelling.","\n")
            
            print("* Strains accompanied by severe pain, swelling, or discoloration may require a trip to the hospital.","\n")
            
            print("* In milder cases, rest, ice, and anti-inflammatory medication will help the area heal.","\n")

            print("-------------------------------------------------------------------------------")

            input("Press enter to coninue:") 
            print("...............................................................................")

        elif injury==8:
            print("-------------------------------------------------------------------------------")

            print("(Fractures are broken bones, and they can occur as a result of falls or other harsh impacts.")
            print("When this happens, the affected part should be immobilized, and additional manipulation of the affected area should be avoided.")
            print("Remember that a fracture could sever a blood vessel or a nerve if it is not immobilized, resulting in a much more severe injury.)","\n")
            
            print("* Immobilize the injured part, and transport the patient to the nearest hospital or medical clinic as soon as possible.")

            print("-------------------------------------------------------------------------------")

            input("Press enter to coninue:")
            print("...............................................................................")


        elif injury==0:
            menu()
        else:
            print("INVALID SELECTION!!!","\n")
            
            input("Press enter to coninue:")
            print("...............................................................................")
            


            
    print("exit")

#--------------------------------------------------------
def menu():
    
    print("\nWhat are you here for today?",'\n',"1)To know the nearby hospitals(type 'H')",'\n',"2)To get first aid information for accidental minor injury(type 'A')",'\n',"3)To get information/diagnosis for common ailments/illnesses(type 'D')")
    print("\nType 'H' for 1), 'A' for 2), 'D' for 3) and 'E' to exit")        
    prob=input("Select a choice:")
    
    if prob=='H':
        print(" not yet")
        menu()
    elif prob=='A':
        injury()
        print("For any emergencies, dial the emergency number 112.................")
    elif prob=='D':
        diagonise()
    elif prob=='E':
        print("THANK YOU FOR YOUR COOPERATION.",'\n\n',"LOGGING OUT.............")
        displayMenu()  
    else:
        print("INVALID CHOICE....TRY AGAIN!")
        menu()
          
prob="H"   
while prob in 'HAD':
    print("\n")
    print("Hello",name,"\nHow can we help you today?")
    menu()
    

    

