from LinkedList import *
import time
from datetime import date, timedelta
import datetime


class PropBooks:
    def __init__(self, booknum, name, isBooked, amount):
        self.booknum = booknum
        self.name = name
        self.isBooked = isBooked
        self.amount = amount
        
    def Add(self):
        MySinglyLinkedList = SinglyLinkedList()
        MySinglyLinkedList.add(self.amount)
        MySinglyLinkedList.add(self.isBooked)
        MySinglyLinkedList.add(self.name)
        MySinglyLinkedList.add(self.booknum)
        MySinglyLinkedList.AddTxtBOOK()
        
class Member:
    def __init__(self, level,idNumber, name, lastname):
        self.level = level
        self.idNumber = idNumber
        self.name = name
        self.lastname = lastname
    def Add(self):
        MySinglyLinkedList = SinglyLinkedList()
        MySinglyLinkedList.add(self.lastname)
        MySinglyLinkedList.add(self.name)
        MySinglyLinkedList.add(self.idNumber)
        MySinglyLinkedList.add(self.level)
        MySinglyLinkedList.AddTxtMEM()





class System:
    @staticmethod
    def borrowBook(IDmember, IDbook):
        
        MyLinkedList = SinglyLinkedList()
        today = date.today()
        diff = datetime.timedelta(days=5)
        returnDay = today + diff
        # Index is value of index to Select the file
        index = 0
        index1 = 2
        index2 = 1
        # index = 0 "MemberDetail.txt"
        # index = 1 "MemberBorrowDetail.txt"
        # index = 2 "BooksDetail.txt"
        
        memberIsInTheSystem = System.helperCheckMemberinDatabase(IDmember, index)
        if  memberIsInTheSystem == False:
            return
        
        bookisBooked = System.helperCheckBookisBooked(IDbook, index1)
        bookinStrock = System.helperCheckBookinStrock(IDbook, index1)
        if (memberIsInTheSystem == True) and (bookisBooked == False and bookinStrock == True):
            print("################################################")
            print("********************Correct*********************")
            print("################################################\n")
            # if Member never borrow a book before
            # We can Add new
            EvenBorrowed = System.helperCheckEvenBorrowed(IDmember, index2)
            
            if EvenBorrowed == False:
                MyLinkedList.add(str(IDbook) + "," + str(today)+ "," + str(returnDay))
                MyLinkedList.add(str(IDmember))
                MyLinkedList.AddTxt(IDmember)
                return
            if EvenBorrowed == True:
                aList = System.helperBorrow()
                for i in range (0, len(aList)):
                    if str(IDmember) == str(aList[i][0]):
                        editList = aList[i]
                        del aList[i] 
                        break
                #---------------------------------------------------------------------
                #Add new BOOK
                MyLinkedList.add(str(IDbook) + "," + str(today)+ "," + str(returnDay))
                for i in range(1, len(editList)):
                    MyLinkedList.add(editList[i])
                MyLinkedList.add(editList[0])
                #---------------------------------------------------------------------
                #Add Old BOOK
                #newCheckList = [num for elem in aList for num in elem]
                for j in range(0, len(aList)):
                    for k in range(1 ,len(aList[j])):
                        MyLinkedList.add(aList[j][k])
                    
                    MyLinkedList.add(aList[j][0])

                MyLinkedList.AddTxt(IDmember)
                #---------------------------------------------------------------------

                
    @staticmethod
    def returnBook(IDmember, IDaBook):
        
        MyLinkedList = SinglyLinkedList()
        today = date.today()
        diff = datetime.timedelta(days=5)
        returnDay = today + diff
        
        # Index is value of index to Select the file
        index = 0
        index1 = 1
        index2 = 2
        # index = 0 "MemberDetail.txt"
        # index = 1 "MemberBorrowDetail.txt"
        # index = 2 "BooksDetail.txt"
        
        memberIsInTheSystem = System.helperCheckMemberinDatabase(IDmember, index)
        if  memberIsInTheSystem == False:
            return

        EvenBorrowed = System.helperCheckEvenBorrowed(IDmember, index1)
        print(EvenBorrowed)
        if (EvenBorrowed == True):
            print("\n################################################")
            print("********************Correct*********************")
            print("################################################")
            aList = System.helperBorrow()
            for i in range (0, len(aList)):
                if str(IDmember) == str(aList[i][0]):
                    editList = aList[i]
                    del aList[i] 
                    break
            print(editList)    
            #Add new BOOK 
            for j in range(1, len(editList)):
                MyLinkedList.add(editList[j])
            MyLinkedList.add(editList[0]) 
            #-----------Delete-----------------------------
            for k in range (1, len(editList)):
                forcheck = editList[k].split(",")
                if str(forcheck[0]) == str(IDaBook):
                    #check over deadline
                    CheckerOver = System.penaltyFee(today, forcheck[2])
                    if (CheckerOver > 0):
                        print("\n>>>>>>>>>>>>>>   OVER DEADLINE   >>>>>>>>>>>>>>>>")
                        print((">>>>>>>>>>>>>>   PLEASE PAY :  %r   <<<<<<<<<<<<<<")%CheckerOver)
                        print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
                        MyLinkedList.delete(editList[k])
                        break
                    else:
                        MyLinkedList.delete(editList[k])
                        break
            for l in range(0, len(aList)):
                for m in range(1 ,len(aList[l])):
                    MyLinkedList.add(aList[l][m])
                    
                MyLinkedList.add(aList[l][0])
            MyLinkedList.AddTxt(IDmember)

        
    @staticmethod    
    def renewBook(IDmember, IDaBook):
        currentDate = date.today()
        checkContinue = True
        aList = System.helperBorrow()
        #check time is not over
        #bookisBooked = System.helperCheckBookisBooked(IDaBook, index1)
        for i in range (0, len(aList)):
            if str(IDmember) == str(aList[i][0]):
                editList = aList[i]
                del aList[i] 
                break
        for k in range (1, len(editList)):
                forcheck = editList[k].split(",")
                
                if str(forcheck[0]) == str(IDaBook):
                    check = forcheck[2].split("-")
                    
                    over = currentDate - datetime.date(int(check[0]), int(check[1]), int(check[2]))
                    overDate = datetime.timedelta(days = 0)
                    if over > overDate:
                        return False
                    
        if(checkContinue):
            System.returnBook(IDmember, IDaBook)
            System.borrowBook(IDmember, IDaBook)
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            print(">>>>>>>>>>The Renewing was successful.<<<<<<<<<<")
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
            return
            
        else:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("!!!!!!!!The Renewing wasn't successful.!!!!!!!!!")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            return
        
    @staticmethod    
    def detailMember(idMember):
        aList = System.helperDetailMember()
        for i in range (0, len(aList)):
            if str(idMember) == str(aList[i][1]):
                editList = aList[i]
                del aList[i] 
                break
        print(editList)


        
    @staticmethod
    def penaltyFee(currentDate, returnDate):
        check = returnDate.split("-")
        over = currentDate - datetime.date(int(check[0]), int(check[1]), int(check[2]))
        overDate = datetime.timedelta(days = 0)
        if over >= overDate:
            penaltyFee = (over.days)*5
        else:
            return 0
        
        return penaltyFee
    @staticmethod 
    def helperBorrow(): 
        filename = "MemberBorrowDetail.txt"
        with open(filename, 'r') as data:
            templist = [line.strip() for line in data]
        ListforHelp = [i.split(" ")for i in templist]
        #Change txt to array or list
        return ListforHelp

    @staticmethod 
    def helperDetailMember(): 
        filename = "MemberDetail.txt"
        with open(filename, 'r') as data:
            templist = [line.strip() for line in data]
        ListforHelp = [i.split(" ")for i in templist]
        #Change txt to array or list
        return ListforHelp
    
    @staticmethod    
    def helperChangeDataToArray(index):
        Structurefilename = ["MemberDetail.txt", "MemberBorrowDetail.txt", "BooksDetail.txt"]
        with open(Structurefilename[index], 'r') as data:
            templist = [line.strip() for line in data]
        ListforCheck = [i.split(" ")for i in templist]
        #Change txt to array or list
        return ListforCheck

    
##    @staticmethod
##    def helperCheckMemberinDatabase(ID, index):
##        # Index is value of index to Select the file
##        # 0."MemberDetail.txt"
##        # 1."MemberBorrowDetail.txt"
##        # 2."BooksDetail.txt"
##        checkMember = False
##        database = System().helperChangeDataToArray(index)
##        #print(database)
##        for i in range(0, len(database)):
##            if str(ID) == str(database[i][1]):
##                checkMember = True
##            
##        return checkMember

    @staticmethod
    def helperCheckMemberinDatabase(ID, index):
        MyLinkedList = SinglyLinkedList()
        # Index is value of index to Select the file
        # 0."MemberDetail.txt"
        # 1."MemberBorrowDetail.txt"
        # 2."BooksDetail.txt"
        checkMember = False
        database = System().helperChangeDataToArray(index)
        #print(database)
        for i in range(0, len(database)):
            MyLinkedList.add(database[i][1])
        checkMember = MyLinkedList.search(str(ID))
        
        
        return checkMember
##############################################################################    
    @staticmethod
    def helperCheckLevelMember(ID, index):
        MyLinkedList = SinglyLinkedList()
        # Index is value of index to Select the file
        # 0."MemberDetail.txt"
        # 1."MemberBorrowDetail.txt"
        # 2."BooksDetail.txt"
        checkLevelMember = 0
        database = System().helperChangeDataToArray(index)
        #print(database)
        for i in range(0, len(database)):
            
            if str(ID) == str(database[i][1]):
                if int(database[i][0]) == 1:
                    checkLevelMember = 1
                    return checkLevelMember

################################################################################       
        
        return 0

    
    @staticmethod
    def helperCheckBookisBooked(numbook, index):
        
        # Index is value of index to Select the file
        # 0."MemberDetail.txt"
        # 1."MemberBorrowDetail.txt"
        # 2."BooksDetail.txt"
        isBooked = False
        database = System().helperChangeDataToArray(index)
        #print(database)
        for i in range(0, len(database)):
            
            if str(numbook) == str(database[i][0]):
                if int(database[i][2]) == 1:
                    isBooked = True
            
        return isBooked

    @staticmethod
    def helperCheckBookinStrock(numbook, index):
        # Index is value of index to Select the file
        # 0."MemberDetail.txt"
        # 1."MemberBorrowDetail.txt"
        # 2."BooksDetail.txt"
        inStrock = False
        database = System().helperChangeDataToArray(index)
        #print(database)
        for i in range(0, len(database)):
            if str(numbook) == str(database[i][0]):
                if int(database[i][3]) > 0:
                    inStrock = True
            
        return inStrock


    
    @staticmethod
    def helperCheckEvenBorrowed(Id, index):
        # Index is value of index to Select the file
        # 0."MemberDetail.txt"
        # 1."MemberBorrowDetail.txt"
        # 2."BooksDetail.txt"
        isEvenBorrowed = False
        database = System().helperChangeDataToArray(index)
        #print(database)
        for i in range(0, len(database)):
            if str(Id) == str(database[i][0]):
                isEvenBorrowed = True
        return isEvenBorrowed
    
##    @staticmethod
##    def Search_Item(ID):
##        CheckList = System().helperMemberCheckinDatabase()
##        for i in range (0, len(CheckList)):
##            checker = CheckList[i][0]
##
##            #Check the same of product
##            if str(checker) == str(ID):
##                return CheckList
##        return

    @staticmethod
    def checkWhoOverDeadLine():
        
        currentDate = date.today()
        MyLinkedList = SinglyLinkedList()
        Structures = System.helperBorrow()
        for i in range(0, len(Structures)):
            checkover = False
            for j in range(1, len(Structures[i])):
            #splittext = Structures[i].split(",")
                
                splittext = Structures[i][j].split(",")
                splittext = splittext[2].split("-")
                
                
                over = currentDate - datetime.date(int(splittext[0]), int(splittext[1]), int(splittext[2]))
                
                overDate = datetime.timedelta(days = 0)
                if over > overDate:
                    checkover = True
##                    print(str(Structures[i][0]))
##                    print(splittext)
##                    
                    MyLinkedList.add(str(Structures[i][j]))
                else:
                    continue
            if (checkover == True):
                MyLinkedList.add(str(Structures[i][0]))
                MyLinkedList.AddTxtWhoOverDeadLine(str(Structures[i][0]))
##                MyLinkedList.show()

    @staticmethod        
    def show(ID):
        Mybooks = []
        namebook = []
        printer = ""
        aList = System.helperBorrow()
        for i in range(0, len(aList)):
            
            if str(aList[i][0]) == str(ID):
                Mybooks = aList[i]
        for j in range(1, len(Mybooks)):
            if str(Mybooks[j].split(",")[0]) not in namebook:
                namebook.append(Mybooks[j].split(",")[0])

        database = System().helperChangeDataToArray(2)
        for l in range(0, len(namebook)):
            for k in range(0, len(database)):
                if str(namebook[l]) == str(database[k][0]):
                    printer += str(namebook[l])+ "," + str(database[k][1]) + " | "
            
        print(printer)
            
        

    
    
    
def Logo():
##        print("\n")
##        print("########################################################################################")
##        print("########  OOO      OOO  OOOOOOOOO  OOOOOOOO        OOO       OOOOOOOO  OOO     OOO  ####")
##        print("########  OOO      OOO  OOO    OO  OOO   OO      OO   OO     OOO   OO   OOO   OOO  #####")
##        print("########  OOO      OOO  OOOOOOOO   OOOOOOO      OOOOOOOOO    OOOOOOO     OOOOOOO  ######")
##        print("########  OOOOOOO  OOO  OOO    OO  OOO   OO    OOO     OOO   OOO   OO      OOO  ########")
##        print("########  OOOOOOO  OOO  OOOOOOOOO  OOO   OOO  OOOO     OOOO  OOO   OOO     OOO  ########")
##        print("########################################################################################")
    print("################################################")
    print("############                     ###############")
    print("############   LIBRARY SYSTEM    ###############")
    print("############                     ###############")
    print("################################################")
        
def main():
    while True:
        index = 0
        Logo()

        IDuser = int(input("Enter Your ID: "))
        check = System.helperCheckMemberinDatabase(IDuser, index)
        if check == True:
            checklevelUser = System.helperCheckLevelMember(IDuser, 0)
            if checklevelUser == 0:
                print("You are user")


                while True:
                    Logo()
                    print("\n \n1. My Profile | 2. Show My Borrowing Book ")
                    print("3. Renew Books")
                    userSelect = int(input("Select: "))
                    if userSelect == 1:
                        Logo()
                        print("\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
                        System.detailMember(IDuser)
                        print("\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
                    if userSelect == 2:
                        print("\n")
                        System.show(IDuser)
                        
                    if userSelect == 3:
                        Logo()
                        #Show borrow Books
                        System.show(IDuser)
                        print("#######Select your book to RENEW#######")
                        IDaBook = input(": ")
                        System.renewBook(IDuser, IDaBook)
            elif checklevelUser == 1:
                while True:

                    Logo()
                    print("\n \n1. My Profile | 2. Add member | 3. Add a book ")
                    print("4. Return | 5. Renew | 6. Borrowing")
                    print("7. Show who over Deadline ")

                    selector =int(input("Enter number:"))
                    if selector == 1:
                        Logo()
                        print("\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
                        System.detailMember(IDuser)
                        print("\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
                    if selector == 2:
                        level = input("Enter level(0: User | 1: Admin): ")
                        codeID = input("Enter ID member: ")
                        aName = input("Enter ID Name: ")
                        Lastname = input("Enter ID Lastname: ")
                        A = Member(level, codeID, aName, Lastname)
                        A.Add()
                    if selector == 3:
                        booknum = input("Enter book ID: ")
                        name = input("Enter Name's book: ")
                        isBooked = '0'
                        amount = input("Enter amount: ")
                        B = PropBooks(booknum, name, isBooked, amount)
                        B.Add()

                    if selector == 4:
                        print("############        RETURN       ###############")
                        print("################################################")
                        
                        IDmember = int(input("Please fill ID MEMBER:"))
                        System.show(IDmember)
                        aaa= input("Please fill ID BOOK:")
                        System.returnBook(IDmember, aaa)
                        System.show(IDmember)
                        
                    if selector == 5:
                        print("############         RENEW       ###############")
                        print("################################################")
                        IDmember = int(input("Please fill ID MEMBER:"))
                        System.show(IDmember)
                        bbb= input("Please fill ID BOOK:")
                        System.renewBook(IDmember, bbb)
                        System.show(IDmember)
                        
                    if selector == 6:
                        print("############       BORROWING     ###############")
                        print("################################################")
                        IDmember = int(input("Please fill ID MEMBER:"))
                        System.show(IDmember)
                        ccc= input("Please fill ID BOOK:")
                        System.borrowBook(IDmember, ccc)
                        System.show(IDmember)
                    if selector == 7:
                        Logo()
                        System.checkWhoOverDeadLine()
                        filename = "WhoOverDeadLine.txt"
                        with open(filename, 'r') as data:
                            templist = [line.strip() for line in data]
                        ListforHelp = [i.split(" ")for i in templist]
                        for i in ListforHelp:
                            print(i)
            else:
                print("Try again")
        else:
            print("Try again")





        
main()
AAA = '59361430'
BBB = '12345'
CCC = 'K'
##A = System()
##A.helperCheckLevelMember(AAA, 0)
##A.borrowBook(int(AAA), BBB)
##A.detailMember(AAA)
##A.checkWhoOverDeadLine()
##A.borrowBook(int(AAA), '88888', CCC)
##A.borrowBook(int(AAA), '00000')
##A.returnBook(int(AAA), '101001')
##A.renewBook(int(AAA), '00000')

