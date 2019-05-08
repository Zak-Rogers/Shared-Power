from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from shutil import copy
from decimal import Decimal
import os
import datetime
import threading
import uuid
import sys


from Classes.Register_user import Register_User
from Classes.Tools import Tools

#---------------toolRegister------------#

#-------------------Search--------------#
def search_Page(currentUser):

    def tool_Register():
        global Font
        nonlocal search_Window
        search_Window.withdraw()

        def rndID():
            nonlocal iD
            iD.set("Tool Id: " + str(uuid.uuid1()))


        #-----Function----#
        def toolOBJ(tool):
            tool = Tools()
            return tool

        def Upload(): #upload image
            nonlocal imgSource
            imgSource = filedialog.askopenfilename(filetypes = [("Gif files","*.gif")])
            destination = os.path.dirname(__file__)
            destination += '\\Data\\Tools\\images\\'
            imageName = imgSource.split("/")[-1]
            Label(toolReg_Window, font = ("Arial",12),text = imageName).grid(row=5, column = 2)
            nonlocal Image
            Image = PhotoImage(file = imgSource)

            imagePreview.create_image((0,0),image = Image)
            
        def writeImage(source):
           
            Destination = os.path.dirname(__file__)
            Destination += '\\Data\\Tools\\images\\'
            copy(source,Destination)
            imageName = source.split("/")[-1]
            os.rename("Data/Tools/images/" + imageName ,"Data/Tools/images/" + iD.get().split(" ")[-1] + ".gif")
            messagebox.showinfo("Success","Tool has been registerd")
    
            

        def addTool():
            imCheck = imageCheck()
            if imCheck:
                rndID()
                nonlocal iD
                Tool = toolOBJ(iD)
                Tool.add_tool_info(toolTypeEntry.get(),toolMakeEntry.get(),\
                toolModelEntry.get(), Description.get("1.0", END),iD.get().split(" ")[-1],\
                fullDayEntry.get(), halfDayEntry.get())
                writeFile(Tool)
                writeImage(imgSource)

        def makeCheck():
            if toolMakeEntry.get() == "":
                messagebox.showerror("Error!","Please enter the tools make")
            else:
                return True
            
        def typeCheck ():
            if toolTypeEntry.get() =="":
                messagebox.showerror("Error!","Please enter the tools type")
            else:
                return True
            
        def modelCheck ():
            if toolModelEntry.get() =="":
                messagebox.showerror("Error!","Please enter the tools Model")
            else:
                return True
            
        def dayCheck ():
            fullday = fullDayEntry.get()
            
            if fullday == "":
                messagebox.showerror("Error!","Please enter the price")
            else:
                try:
                    float(fullday)
                    return True
                except ValueError:
                    messagebox.showerror("Enter!","Please enter the valid price")
                    
        def hdayCheck ():
            halfday = halfDayEntry.get()
            
            if halfday == "":
                messagebox.showerror("Error!","Please enter the valid price")
            else:
                try:
                    float(halfday)
                    return True
                except ValueError:
                    messagebox.showerror("Error!","Please enter the valid price")
            
            
        def imageCheck():
            nonlocal imgSource
            if imgSource == "":
                messagebox.showerror("Error","Please upload a image.")
            else:
                return True
                
            

        def writeFile(Tool):
            #checks:
            maCheck = makeCheck()
            tCheck = typeCheck ()
            moCheck = modelCheck()
            dCheck = dayCheck ()
            hdCheck = hdayCheck()
            
            

            if maCheck:
                if tCheck:
                    if moCheck:
                        if dCheck:
                            if hdCheck:
                               
                                fileName = Tool.tool_Make + "-" + Tool.tool_Model + "__" + str(iD.get().split(" ")[-1])  
                                Directory = os.path.dirname(__file__)
                                Directory += '\\Data\\Tools\\'
                                Directory += Tool.tool_Type + "\\"
                                if not os.path.exists(Directory):
                                    os.makedirs(Directory)
                                filePath = Directory + fileName
                                toolFile = open(filePath, "w")
                                toolFile.write(str(iD.get()) + "\n")
                                toolFile.write("Tool Make: " + Tool.tool_Make + "\n")
                                toolFile.write("Tool Model: " + Tool.tool_Model + "\n")
                                toolFile.write("Tool Info: " + Tool.tool_Info + "\n")
                                toolFile.write("Tool Owner: " + currentUser.user_Name+ "\n") # placeholder
                                toolFile.write("Multiday Price(per day): " + Tool.per_Day + "\n")
                                toolFile.write("Single Day Price: " + Tool.per_Hday + "\n")
                                toolFile.write("\n")
                                toolFile.write("Booked Dates: ")
                                toolFile.close()
                                    
        toolReg_Window = Toplevel()
        toolReg_Window.title("Shared Power - Tool Registry")
        toolReg_Window.geometry("650x350")
        toolReg_Window.maxsize(width=650,height=350)
        toolReg_Window.minsize(width=650,height=350)

        Image = PhotoImage(file = "")
        iD = StringVar()
        imgSource = StringVar()
        #-----labels------#
        blankLabel = Label(toolReg_Window, text = "")
        Label(toolReg_Window, font = Font, text = "Tool Make:").grid(row = 1, column = 0, sticky = E)
        Label(toolReg_Window, font = Font, text = "Tool Model:").grid(row = 2, column = 0, sticky = E)
        Label(toolReg_Window, font = Font, text = "Tool Type:").grid(row = 3, column = 0, sticky = E)
        Label(toolReg_Window, font = Font, textvariable = iD).grid(row = 1, column  = 2, columnspan = 2, sticky = W)
        Label(toolReg_Window, font = Font, text = "Price for multiple days (per day): £").grid(row = 2, column = 2, sticky = E)
        Label(toolReg_Window, font = Font, text = "Price for single day (12 Hours): £").grid(row = 3, column = 2, sticky = E)
        Label(toolReg_Window, font = Font, text = "Description:").grid(row = 4, column = 0, sticky = W)
        #--------Entry boxes----------#
        toolMakeEntry = Entry(toolReg_Window)
        toolModelEntry = Entry(toolReg_Window)
        toolTypeEntry= Entry(toolReg_Window)
        halfDayEntry = Entry(toolReg_Window)
        fullDayEntry = Entry(toolReg_Window)
        Description = Text(toolReg_Window, width = 30, height = 14)
        #------Buttons-----------#
        toolRegister = Button(toolReg_Window,  font = Font, text = "Register Tool" ,command = addTool, height = 4)
        upload = Button(toolReg_Window, font = Font, text = "Upload Photo", command = Upload)
        #--------image box--------#
        imagePreview = Canvas(toolReg_Window, width = 200, height = 200)
        imagePreview.grid(row = 6, column = 2, sticky = N)
        #-------------Layout-----------#
        toolMakeEntry.grid(row = 1, column = 1, sticky = W)
        toolModelEntry.grid(row = 2, column = 1, sticky = W)
        toolTypeEntry.grid(row = 3, column = 1, sticky = W)
        halfDayEntry.grid(row = 2, column = 3)
        fullDayEntry.grid(row = 3, column = 3)
        toolRegister.grid(row = 6, column = 3, sticky = E+S+W)
        upload.grid(row = 5, column = 3, sticky = N)
        Description.grid(row = 5, column = 0, columnspan = 2, rowspan = 3, sticky = N+W)

        def Close():
            toolReg_Window.destroy()
            search_Window.deiconify()

        toolReg_Window.protocol("WM_DELETE_WINDOW", Close)
        toolReg_Window.mainloop()
        
        
    def lateFee(daysLate,dayHire):
        doubleRate = dayHire * 2
        Fee = doubleRate * daysLate.days
        return Fee

    def lastInvoice():
        Directory = os.path.dirname(__file__)
        Directory += "\\Data\\Invoices\\"
        filePath = Directory + currentUser.user_Name + ".txt" 
        invoiceFile = open(filePath,"r")
        Lines = invoiceFile.read()
        lastInvoice = Lines.split("~~~~~\n")[-1]

        invoice_Window = Toplevel()
        textBox = Text(invoice_Window, font = Font, height = 50, width = 40)
        textBox.grid()
        textBox.insert(INSERT,lastInvoice)
        invoice_Window.mainloop()
        
        
    def Invoice(): 
        Date = datetime.datetime.now().strftime("%d/%m/%y")

        Directory = os.path.dirname(__file__)
        Directory += "\\Data\\Users\\"
        filePath = Directory + currentUser.user_Name +".txt" 

        userFile = open(filePath, "r")
        Lines = userFile.read()
        Lines = Lines.split("#")
        userDetails = Lines[0:10]
        
        Lines = Lines[10:]
        userFile.close()
        

        Directory = os.path.dirname(__file__)
        Directory += "\\Data\\Invoices\\"
        filePath = Directory + currentUser.user_Name + ".txt" 

        try:        
            invoiceFile = open(filePath, "r")
            Invoices = invoiceFile.read()
            lastInvoice = Invoices.split("~~~~~\n")[-1]
            
            invoiceNumber = lastInvoice.split("\n")

            invoiceNumber = int(invoiceNumber[0].split(": ")[1]) + 1
            
        except:
            invoiceNumber = 1

        invoiceFile = open(filePath, "a")
        invoiceFile.write("~~~~~\n")
        invoiceFile.write("Invoice Number: "+ str(invoiceNumber)+ "\n")
        invoiceFile.write("\n")
        invoiceFile.write("Shared Power\n")
        invoiceFile.write("2 Luton Way\n")
        invoiceFile.write("Luton\n")
        invoiceFile.write("LU1 3FR\n")
        invoiceFile.write("\n")
        invoiceFile.write("Date: " + Date + "\n")
        invoiceFile.write("\n")
        invoiceFile.write("Customer Details:\n\n")
        userName = userDetails[0].split(": ")[1]
        invoiceFile.write(currentUser.get_name() + "\n")
        Address = userDetails[5].split(": ")[1]
        City = userDetails[6].split(": ")[1]
        Postcode = userDetails[7].split(": ")[1]
        invoiceFile.write(Address + "\n" + City + "\n" + Postcode + "\n")
        Email =userDetails[3].split(": ")[1]
        Phone = userDetails[4].split(": ")[1]
        invoiceFile.write(Email +"\n"+ Phone + "\n\n")
        invoiceFile.write("Username: " + userName + "\n\n")
        
        invoiceFile.write("\n")
        invoiceFile.write("{:<30}{:>20}".format("Tools Hired","Cost\n\n"))
        Total = 0
        for Line in Lines:
            toolInfo = Line.split(" ~ ")
            toolName = toolInfo[0]
            toolStart = toolInfo[2]
            toolEnd = toolInfo[3]
            toolDay = toolInfo[4]
            toolhDay = toolInfo[5]
            toolDelivery = toolInfo[6]
            toolPickup = ""
            toolReturned = ""
            if toolDelivery == "True":
                toolDelivery = 10
            else:
                toolDelivery = 0 
            if len(toolInfo) > 7:
                toolPickup = toolInfo[7]
                toolReturned = toolInfo[8]
                if toolPickup == "True":
                    toolPickup = 10
                else:
                    toolPickup = 0
            
            toolStart = datetime.datetime.strptime(toolStart, "%d/%m/%y")
            toolEnd = datetime.datetime.strptime(toolEnd, "%d/%m/%y")
            Duration = toolEnd - toolStart
            if Duration.days == 0:
                toolCost = int(toolhDay)
            else:
                toolCost = Duration.days * int(toolDay)

            invoiceFile.write("{:<30}{:>20}".format(toolName,"£" + str(toolCost) + "\n"))
            Fee = 0
            if toolReturned != "":
                rDate = datetime.datetime.strptime(toolReturned, "%d/%m/%y")
                Difference = rDate - toolEnd
                if Difference.days >= 1:
                    Fee = lateFee(Difference,int(toolDay))
                    invoiceFile.write("{:<30}{:>20}".format("late fee:", "£" + str(Fee) + "\n"))
            if toolDelivery != 0:
                invoiceFile.write("{:<30}{:>20}".format("delivery charge:","£" + str(toolDelivery) + "\n"))

            if toolPickup != "" and toolReturned != "":
                invoiceFile.write("{:<30}{:>20}".format("Pickup charge:", "£" + str(toolPickup) + "\n"))
            invoiceFile.write("\n")
            Total += toolCost
            Total += toolDelivery
            Total += Fee
            if toolPickup != "":
                Total += toolPickup
            

        Insurance = 5
        invoiceFile.write("{:<30}{:>20}".format("Insurance:", "£" + str(Insurance) + "\n"))
        invoiceFile.write("\n")
        invoiceFile.write("{:<30}{:>20}".format("Sub Total:","£" + str(Total) + "\n"))
        Vat = Total * 0.20 
        Vat = Decimal(Vat)
        Vat = round(Vat,2)
        invoiceFile.write("{:<30}{:>20}".format("Vat:", "£" + str(Vat) + "\n"))
        Total = Total + Vat
        Total += Insurance
        invoiceFile.write("{:<30}{:>20}".format("Total:", "£" + str(Total) + "\n"))       
        
        invoiceFile.close()

        removeTools(currentUser.user_Name)

    def removeTools(username):
        Directory = os.path.dirname(__file__)
        Directory += "\\Data\\Users\\"
        filePath = Directory + username + ".txt"

        userFile = open(filePath, "r")
        Info = userFile.read()
        userInfo = Info.split("#")
        userInfo = userInfo[0:10]
        userFile.close()

        userFile = open(filePath,"w")
        Supplier = userInfo[-1]
        Update = ""
        for Info in userInfo:
            if Info == Supplier:
                Update += Info
            else:
                Update += Info + "#"
        userFile.write(Update)
        
        userFile.close()
        

        

    def pickupRider():
        messagebox.showinfo("Pick up!", "Details have been passed onto the pickup rider.")

    def account_Page():
        nonlocal currentUser        
        def Return():
            if hiredTools.curselection() == ():
                messagebox.showerror("Error!","You haven't selected any tools.")
            else:
                Tool = hiredTools.get(ACTIVE)
                toolInfo = Tool.split(" ~ ")
                nonlocal pickUp
                

                                       
                Directory = os.path.dirname(__file__)
                Directory += '\\Data\\Users\\'
                fileName = currentUser.user_Name + ".txt" 
                filePath = Directory + fileName


                userFile = open(filePath, "r")
                Lines = userFile.read()
                userInfo = Lines.split("#")
                userTools = userInfo[10:]
                userFile.close()

                
                Date = datetime.datetime.now().strftime("%d/%m/%y")

                for userTool in userTools:
                    usertoolInfo = userTool.split(" ~ ")
                    
                    if toolInfo[0] == usertoolInfo[0] and toolInfo[1] == usertoolInfo[3]:
                        Index = userInfo.index(userTool)
                        userInfo[Index] = userTool + " ~ " + str(pickUp.get()) + " ~ " + Date + " ~ " + str(Condition.get())
                        
                        Id = usertoolInfo[1]
                        
                        userFile = open(filePath, "w")
                        Update = ""
                        lastTool = userInfo[-1]
                        for Info in userInfo:
                            if Info == lastTool:
                                Update += Info
                            else:
                                Update += Info + "#"
                        userFile.write(Update)
                        userFile.close()

                nonlocal returnImage
                nonlocal imageSource

                imageSource = filedialog.askopenfilename(filetypes = [ ("Gif files","*.gif")])
                Destination = os.path.dirname(__file__)
                Destination += "\\Data\\Tools\\images\\Returns\\"
                
                imageName = imageSource.split("/")[-1]
                filePath = Destination + Id + ".gif"
                if os.path.exists(filePath):
                    os.remove(filePath)
                copy(imageSource,Destination)
                os.rename("Data/Tools/images/Returns/" + imageName, "Data/Tools/images/Returns/" + Id + ".gif")      
                
                
                if Condition.get() == "Damaged" or Condition.get() == "Faulty":
                    
                    Directory = os.path.dirname(__file__)
                    Directory += "\\Data\\Tools\\"
                    Types = populateType()
                    fileName = toolInfo[0] + "__" + Id

                    for Type in Types:
                        filePath = Directory + Type + "\\" + fileName
                        if os.path.exists(filePath):
                            toolFile = open(filePath, "a")
                            toolFile.write("\n" + Condition.get() + "\n")
                            toolFile.close()
                            messagebox.showinfo("Reported!","The condition of the tool has been updated and the insurance company informed")

                if pickUp.get():
                    pickupRider()
                else:
                    messagebox.showinfo("Success!","Tool has been Returned")            

        nonlocal search_Window
        search_Window.withdraw()
        global Font
        
        account_Window = Toplevel()
        account_Window.title("Shared Power - Account Information")
        account_Window.geometry("650x350")
        account_Window.maxsize(width=650,height=350)        
        account_Window.minsize(width=650,height=350)
        
        returnImage = PhotoImage(file="")
        imageSource = StringVar()
        
        #Tool Lists
        Label(account_Window,text = "Tools Owned ~ ID", font = Font).grid(row = 0, column = 0, columnspan=2)
        ownedTools = Listbox(account_Window)
        ownedTools.grid(row = 1, column = 0, columnspan=2, sticky = W+E)
        
        Label(account_Window,text = "Tools Under Hire ~ Booked Till", font = Font).grid(row = 0, column = 3, columnspan=2)
        hiredTools = Listbox(account_Window)
        hiredTools.grid(row = 1, column = 3, columnspan = 2, sticky = W+E)

        #gets hired tools
        Directory = os.path.dirname(__file__)
        Directory += "\\Data\\Users\\"
        filePath = Directory + currentUser.user_Name + ".txt" 
        userFile = open(filePath, "r")
        Text = userFile.read()
        userInfo = Text.split("#")
        userTools = userInfo[10:]
        
        Date = datetime.datetime.now().strftime("%d/%m/%y")
        for Item in userTools:
            Info = Item.split(" ~ ")
            String = Info[0] + " ~ " + Info[3]
            if Info[-2] != Date:
                hiredTools.insert(END,String)

        #gets owned tools

        Directory = os.path.dirname(__file__)
        Directory += "\\Data\\Tools\\"
        Types = os.listdir(Directory)
        Types.remove("images")

        

        for Type in Types:
            Files = os.listdir(Directory + "\\" + Type)
            for File in Files:
                filePath = Directory + "\\" + Type + "\\" + File
                if os.path.exists(filePath):
                    toolFile = open(filePath)
                    Lines = toolFile.readlines()
                   
                    if len(Lines) >3: 
                        toolOwner = Lines[5]
                        toolOwner = toolOwner.split(": ")[-1]
                        toolOwner = toolOwner[:-1]
                        if toolOwner == currentUser.user_Name: 
                            Make = Lines[1].split(": ")
                            Make = Make[-1]
                            Make = Make[:-1]
                            Model = Lines[2].split(": ")
                            Model = Model[-1]
                            Model = Model[:-1]
                            Id = Lines[0].split(": ")
                            Id = Id[-1]
                            Id = Id[:-1]
                            Tool = Make + " " + Model + " ~ " + Id
                            ownedTools.insert(END,Tool)

        def Back():
            search_Window.deiconify()
            account_Window.destroy()
        
        nonlocal pickUp
        pickUpCbox = Checkbutton(account_Window, font = Font, variable = pickUp, text = "Arrange Pick Up")
        pickUpCbox.grid(row = 1, column = 5, sticky = E+N+S)

        Label(account_Window, font = Font, text = "Tool condition:").grid(row = 1, column = 5, sticky = S)
        Condition = Combobox(account_Window)
        Condition["values"] = ("Good","Worn","Damaged","Faulty")
        Condition.current(0)
        Condition.grid(row = 2, column = 5, sticky= W+S+E)

        returnButton = Button(account_Window, font = Font, text = "Return Tool", command = Return)
        returnButton.grid(row = 3, column =5)

        invoiceButton = Button(account_Window, font = Font, text = "Invoice", command = lastInvoice)
        invoiceButton.grid(row = 4, column = 5)

        Back = Button(account_Window, font = Font, text = "Back", command = Back)
        Back.grid(row = 4, column = 1)
        
        def Close():
            account_Window.destroy()
            search_Window.deiconify()

        account_Window.protocol("WM_DELETE_WINDOW", Close)    
#####
        account_Window.mainloop()

            
    def populateType():
        Directory =os.path.dirname(__file__)
        Directory += "\\Data\\Tools\\"
        types_of_Tools = os.listdir(Directory)
        types_of_Tools.remove("images")
        return types_of_Tools

    def populateList():
        dValidate = dateValidation()
        toolLBox.delete(0,END)
        if dValidate:

            Directory = os.path.dirname(__file__)
            Directory += '\\Data\\Tools\\'
            if Type.get() != "All Types":
                Directory += Type.get()
                list_of_Tools = os.listdir(Directory)
                dateCheck(list_of_Tools,Directory)
            else:
                toolTypes = os.listdir(Directory)
                toolTypes.remove("images")
                list_of_Tools = []
                for Item in toolTypes:
                    list_of_Tools.extend(os.listdir(Directory + Item))

                dateCheck(list_of_Tools,Directory + Item)
                
                        
            for Tool in list_of_Tools:
                
                toolLBox.insert(END, Tool)

    def addToBasket():
        if toolLBox.curselection() == (): 
            messagebox.showerror("Error!","You haven't selected any tools.")
            
        else:
            Items = toolLBox.get(ACTIVE)
            basketLBox.insert(END, Items)
            itemIndexs = toolLBox.curselection()
            toolLBox.delete(itemIndexs)

    def removeFromBasket():
        if basketLBox.curselection() == (): #empty selection
            messagebox.showerror("Error!","You haven't selected any tools.") 
        else:
            Items = basketLBox.get(ACTIVE)
            toolLBox.insert(END, Items)
            itemIndexs = basketLBox.curselection()
            basketLBox.delete(itemIndexs)

    def dateCheck(toolList,Directory):
        sDate = startDate.get()
        eDate = endDate.get()
        
        for Tool in toolList:
            filePath = Directory + "\\" + Tool 
            if os.path.exists(filePath):
                toolFile = open(filePath, "r")
                Lines = toolFile.readlines()
                Lines = Lines[10:]
                for Line in Lines:
                    Date = Line.split(": ")
                    Date = Date[-1]
                    
                    Date = Date[:-1]
                    
                    
                    if Date == sDate or Date == eDate or Date == "Damaged" or Date == "Faulty":
                        
                        if Tool in toolList:
                            toolList.remove(Tool)

    def dispatchRider():
        messagebox.showinfo("Delivery!", "Details have been passed onto the delivery rider")


    def checkOut(): 

        if basketLBox.get(0,END) == ():
            messagebox.showerror("Error!","Your basket is empty.")
        else:        
            nonlocal Delivery
            if Delivery.get():
                dispatchRider()
            else:
                messagebox.showinfo("Success","The tools will be ready for colection at 8am on your start day")

            Costs = {}
            
            Tools = basketLBox.get(0,END)
            Directory = os.path.dirname(__file__)
            Directory += '\\Data\\Tools\\'
            toolTypes = os.listdir(Directory)
            toolTypes.remove("images")
            for types in toolTypes:
                for tool in Tools:
                    fileName = tool

                    
                    filePath = Directory + types + "\\" + fileName
                    if os.path.exists(filePath):
                    
                        toolFile = open(filePath, "r")
                        Lines = toolFile.readlines()
                        pDay = Lines[6]
                        pDay = pDay.split(": ")
                        pDay = pDay[1]
                        pDay = pDay[:-1]
                        hDay = Lines[7]
                        hDay = hDay.split(": ")
                        hDay = hDay[1]
                        hDay = hDay[:-1]
                        Costs= {tool + "Day":pDay,tool + "hDay":hDay}
                        toolFile.close()
                        
                        toolFile = open(filePath, "a")
                        Dates =getDate()
                        toolFile.write("\n" + Dates + currentUser.user_Name)
                        toolFile.close()

            
            sDate = startDate.get()
            eDate = endDate.get()
            for Tool in Tools:
                Directory = os.path.dirname(__file__)
                Directory += "\\Data\\Users\\"
                filePath = Directory + currentUser.user_Name + ".txt"
                userFile = open(filePath, "a")
                Tool = Tool.split("__")
                Id = Tool[1]
                Tool = Tool[0]            
                Day = Costs[tool + "Day"]
                hDay = Costs[tool + "hDay"]
                userFile.write("#" + Tool + " ~ " + Id + " ~ " + sDate + " ~ " + eDate  + " ~ " + Day + " ~ " + hDay + " ~ " + str(Delivery.get()))
                userFile.close()

    def on_sDateClick(event):
        if startDate.get() == "DD/MM/YY":
            startDate.delete(0,END)
            
    def on_eDateClick(event):
        if endDate.get() =="DD/MM/YY":
            endDate.delete(0,END)

    def off_sDateClick(event):
        if startDate.get() == "":
            startDate.insert(0,"DD/MM/YY")
        
    def off_eDateClick(event):
        if endDate.get() == "":
            endDate.insert(0,"DD/MM/YY")

    def toolInfo():
        Make = StringVar()
        Model = StringVar()
        toolType = StringVar()
        Info = StringVar()
        
        fDay = StringVar()
        hDay = StringVar()
        

        if toolLBox.curselection() == ():
            messagebox.showerror("Error!","You have not selected a tool")
        else:
            Tool = toolLBox.get(ACTIVE)
            toolType = Type.get()
            if toolType != "All Types":
                Directory = os.path.dirname(__file__)
                Directory += '\\Data\\Tools\\'
                Directory += toolType + '\\'
                filePath = Directory + Tool

                toolFile = open(filePath,"r")
                Lines = toolFile.readlines()

                iD = Lines[0]
                iD = iD.split(": ")[-1]
                iD = iD[:-1]
                Make =Lines[1]
                Model = Lines[2]
                Info = Lines[3]
                fDay = Lines[6]
                hDay = Lines[7]


                toolFile.close()

            else:
                Directory = os.path.dirname(__file__)
                Directory += '\\Data\\Tools\\'
                Types = os.listdir(Directory)
                Types.remove("images")

                for each in Types:
                    if os.path.exists(Directory + each + "\\" + Tool):
                        filePath = Directory + each + "\\" + Tool
                        toolFile = open(filePath, "r")
                        Lines = toolFile.readlines()

                        iD = Lines[0]
                        iD = iD.split(": ")[-1]
                        iD = iD[:-1]
                        Make = Lines[1]
                        Model = Lines[2]
                        Info = Lines[3]
                        fDay = Lines[6]
                        hDay = Lines[7]

                        toolFile.close()

            imgSource = os.path.dirname(__file__)
            imgSource += '\\Data\\Tools\\images\\'
            imgSource += iD + ".gif"

            global Image
            Image = PhotoImage(file = imgSource)
            
            infoPage = Toplevel()
            Label(infoPage, text = Make).grid()
            Label(infoPage, text = Model).grid()
            Label(infoPage, text = Info).grid()
            Label(infoPage, text = fDay).grid()
            Label(infoPage, text = hDay).grid()

            imagePreview = Canvas(infoPage, width = 200, height = 200)
            imagePreview.grid()
            imagePreview.create_image((50,50), image = Image)
        
        
        

    def getDate(): 
        dateFormat = "%d/%m/%y"
        dateNow = datetime.datetime.now().strftime(dateFormat)
        sDate = datetime.datetime.strptime(startDate.get(),dateFormat)
        eDate = datetime.datetime.strptime(endDate.get(),dateFormat)
        Difference = eDate - sDate
        Dates = []
        for day in range(Difference.days +1):
            Date = sDate + datetime.timedelta(day)
            Dates.append(Date.strftime(dateFormat))

        if len(Dates) ==3:
            strDates = "Book from: " + Dates[0] + "\nIncluding: " + Dates[1] + "\nTill: " + Dates[2] + "\n"
        elif len(Dates) == 1:
            strDates = "Book from: " + Dates[0] + "\nTill: " + Dates[0] + "\n" #for x hours
        else:
            strDates = "Book from: " + Dates[0] + "\nTill: " + Dates[1] + "\n"
            
        return strDates
        
    def dateValidation():
        dateFormat = "%d/%m/%y"
        dateNow = datetime.datetime.now().strftime(dateFormat)
        dateNow = datetime.datetime.strptime(dateNow, dateFormat)

        try:
            sDate = datetime.datetime.strptime(startDate.get(),dateFormat)
            eDate = datetime.datetime.strptime(endDate.get(),dateFormat)
        
            
            dayDifference = eDate - sDate
            weekDifference = sDate- dateNow

            

            if weekDifference.days/7 <= 6:
                if dayDifference.days <= 3:
                    return True
                else:
                    messagebox.showerror("Error!","You can't hire a tool for more than 3 days")
            else:
                messagebox.showerror("Error!","You can't hire a tool more than 6 weeks in advance")
         
        except ValueError:
            messagebox.showerror("Error!","Dates don't match example format, DD/MM/YY.")     



    global Font
    search_Window = Tk()
    search_Window.title("Shared Power - Tool Search")
    search_Window.geometry("650x350")    
    search_Window.maxsize(width=650,height=350)        
    search_Window.minsize(width=650,height=350)

    # Labels
    Label(search_Window, font = ("Arial", 12), text = "Tool Type").grid(row = 0, column = 0)
    Label(search_Window, font = ("Arial", 12), text = "Start Date").grid(row = 1, column = 0)
    Label(search_Window, font = ("Arial", 12), text = "End Date").grid(row = 2, column = 0)
    Label(search_Window, text = "").grid(row = 3)
    Label(search_Window, font = ("Arial", 12), text = "Tools").grid(row = 4, column = 1)
    Label(search_Window, font = ("Arial", 12), text = "Basket").grid(row = 4, column = 3)
    Label(search_Window,font = Font, text = "Working Hours 8am-8pm").grid(row = 2,column = 3, sticky = W)

    # Drop downs

    Type = Combobox(search_Window)
    Types = populateType()
    Type["values"] = ("All Types",*Types)
    Type.current(0)
    Type.grid(row = 0, column = 1, sticky= W+S+E+N)

    # Entry
    startDate = Entry(search_Window)
    startDate.insert(0, "DD/MM/YY")
    startDate.bind("<FocusIn>", on_sDateClick)
    startDate.bind("<FocusOut>", off_sDateClick)

    endDate = Entry(search_Window)
    endDate.insert(0, "DD/MM/YY")
    endDate.bind("<FocusIn>", on_eDateClick)
    endDate.bind("<FocusOut>", off_eDateClick)

    startDate.grid(row = 1, column = 1, sticky= W+S+E)
    endDate.grid(row = 2, column = 1, sticky= W+S+E)
    #Checkbox
    pickUp = BooleanVar()
    Delivery = BooleanVar()
    deliveryCbox = Checkbutton(search_Window, font = Font, variable = Delivery, text = "Delivery")
    deliveryCbox.grid(row = 5, column = 5, sticky = E+N)
    #Buttons
    Button(search_Window, font = ("Arial", 12), text="Search Tool", command = populateList).grid(row = 0, column = 3, sticky = W)
    
    if currentUser.supplier == "True":
        Button(search_Window, font = Font, text="Add New Tool", command = tool_Register).grid(row = 1, column = 3, sticky = W)
    Button(search_Window, font = ("Arial", 12), text="My Account", command = account_Page).grid(row = 0, column = 5, sticky = E)
    Button(search_Window, font = ("Arial", 12), text="Checkout", command = checkOut).grid(row = 5, column = 5, sticky = E)
    Button(search_Window, font = ("Arial", 12), text=">", command = addToBasket).grid(row = 5, column = 2, sticky = N+W+E)
    Button(search_Window, font = ("Arial", 12), text="Info", command = toolInfo).grid(row = 5, column = 2, sticky = W+E)
    Button(search_Window, font = ("Arial", 12), text="<", command = removeFromBasket).grid(row = 5, column = 2, sticky= W+S+E)

    Image = PhotoImage(file="")

    # Listboxs
    toolLBox = Listbox(search_Window)
    toolLBox.grid(row = 5, column = 1, sticky = W+E)

    basketLBox =Listbox(search_Window)
    basketLBox.grid(row = 5, column = 3, sticky = W+E)

######
    Running = True
    def dateLoop():
        nonlocal Running

        Directory = os.path.dirname(__file__)
        Directory += "\\Data\\Invoices\\"
        filePath = Directory + currentUser.user_Name + ".txt"# placeholder for current user
        if os.path.exists(filePath): 
            invoiceFile = open(filePath,"r")
            Invoices = invoiceFile.read()
            try:
                lastInvoice = Invoices.split("~~~~~\n")[-1]
                invoiceInfo = lastInvoice.split("\n")
                lastDate = invoiceInfo[7].split(": ")[-1]
                invoiceFile.close()
                lastDate = datetime.datetime.strptime(lastDate,"%d/%m/%y")
            except: IndexError

            try:    
                while Running:
                    Date = datetime.datetime.now()
                    if Date.strftime("%d") == "01" and lastDate.strftime("%m") != Date.strftime("%m"):
                        Invoice()
                        break# but have too open my accounts page on the 1st
            except: #UnboundLocalError
                Invoice()
            
        else:
             invoiceFile = open(filePath,"w")
             invoiceFile.close()
             
    dateLoop = threading.Thread(target = dateLoop)
    dateLoop.start()

    def endLoop():
        nonlocal Running
        Running = False
        nonlocal search_Window
        search_Window.destroy()
        sys.exit()

        
#####

    def Exit():
        search_Window.destroy()
        sys.exit()
        
    search_Window.protocol("WM_DELETE_WINDOW",endLoop)

    search_Window.mainloop()
    
#------------------Register-------------#
def register_Page():
    
    def passwordVerify(): #checks passwords match
        if passWord.get() == passWordConfirm.get():
            return True
        else:
            messagebox.showerror("Error!","Passwords did not match.")

    def entryCheck(): #checks if all fields are complete except supplier Cbox
        if userName.get() == "" or passWord.get() == "" \
           or passWordConfirm.get() == "" or Email.get() == "" \
           or firstName.get() == "" or lastName.get() == "" \
           or Phone.get() == "" or address_Line1.get() == "" \
           or City.get() == "" or postCode.get() == "":
            messagebox.showerror("Error!","You have not completed all the fields.")
        else:
            return True 

    def usernameCheck(filePath): #checks if username already exists
        if os.path.exists(filePath):
            messagebox.showerror("Error!","Username already exists.")
        else:
            return True

    def emailCheck():
                if re.match(r"[^@]+@[^@]+\.[^@]+",Email.get()):
                    return True
                else:
                    messagebox.showerror("Error!","Oops you enterd invalid email.")

    def phoneCheck():
        if len(Phone.get()) == 11:
            return True
        else:
            messagebox.showerror("Error!","Not a valid phone number.")

    def userOBJ(user):
        user = Register_User()
        return user
        

        
    def writeFile(): #writes info to file 
        User = userOBJ(userName.get())
        User.add_user_info(firstName.get(),lastName.get(),userName.get(),Email.get(),\
                           Phone.get(),address_Line1.get(),City.get(),postCode.get(),Supplier.get())
        pCheck = passwordVerify()
        eCheck = entryCheck()
        phCheck = phoneCheck()
        mCheck = emailCheck()
        fileName = userName.get() + ".txt"
        directory = os.path.dirname(__file__)
        directory += '\\Data\\Users\\'
        filePath = directory  + fileName

        uCheck = usernameCheck(filePath)
        if uCheck:
            if eCheck:
                if phCheck:
                    if mCheck:
                        if pCheck:
                            encode_Password = passWord.get()          
                            encoded_Password = encode_Password.encode("UTF-16")
                            encoded_Password = str(encoded_Password)

                            userInfo = open(filePath, "wb")
                            userInfo.write(bytes("Username: " + User.user_Name+ "#","UTF-8"))
                            userInfo.write(bytes("First Name: " + User.first_Name + "#","UTF-8"))
                            userInfo.write(bytes("Last Name: " + User.last_Name+ "#","UTF-8"))
                            userInfo.write(bytes("Email: " + User.email+ "#","UTF-8"))
                            userInfo.write(bytes("Phone Number: " + User.phone_Number+ "#","UTF-8"))
                            userInfo.write(bytes("Address Line 1: " + User.address_Line+ "#","UTF-8"))
                            userInfo.write(bytes("City: " + User.city+ "#","UTF-8"))
                            userInfo.write(bytes("Postcode: " + User.postcode+ "#","UTF-8"))
                            userInfo.write(bytes("Supplier: " + str(User.supplier) + "#","UTF-8"))
                            userInfo.write(bytes("Password: " + encoded_Password, "UTF-8"))
                            userInfo.close()
                            messagebox.showinfo("Success!", "You have been Registered")
                            reg_Window.destroy()
                            search_Page(User)
    def Back():
        login_Window.deiconify()
        reg_Window.destroy()

                        
    login_Window.withdraw()
    
    global Font
    reg_Window = Toplevel()
    reg_Window.title("Shared Power - Register")
    # Heading
    Label(reg_Window, text ="Please fill in the details \n to register your account:").grid(row=0, sticky=W)
    # CheckBox
    Supplier = BooleanVar()
    Supplier_CBox = Checkbutton(reg_Window, font =Font, variable = Supplier,)
    Supplier_CBox.grid(row=1, column = 4, sticky = W)
    Label(reg_Window, font =Font, text = "Are you a Supplier?").grid(row = 1, column = 2, sticky=E)
    # Labels
    Blank = Label(reg_Window, text = "")
    Label(reg_Window, font =Font, text = "First Name:").grid(row=1, sticky=E)
    Label(reg_Window, font = Font, text = "Last Name:").grid(row=2, sticky=E)
    Label(reg_Window, font = Font, text = "Username:").grid(row=3, column = 2, sticky=E)
    Blank.grid(row = 4, column = 3)
    Label(reg_Window, font = Font, text = "Password:").grid(row=5, column = 2, sticky=E)
    Label(reg_Window, font = Font, text = "Verify Password:").grid(row=6, column = 2, sticky=E)
    Label(reg_Window, font = Font, text = "Email:").grid(row=3, sticky=E)
    Blank.grid(row =4)
    Label(reg_Window, font = Font, text = "Phone Number:").grid(row=5, sticky=E)
    Label(reg_Window, font = Font, text = "Address Line 1:").grid(row=6, sticky=E)
    Label(reg_Window, font = Font, text = "City:").grid(row=7, sticky=E)
    Label(reg_Window, font = Font, text = "Postcode:").grid(row=8, sticky=E)
    # Entry Boxes
    firstName = Entry(reg_Window)
    lastName = Entry(reg_Window)
    userName = Entry(reg_Window, width=16)
    passWord = Entry(reg_Window, show="*", width=16)
    passWordConfirm = Entry(reg_Window, show="*", width=16)
    Email = Entry(reg_Window)
    Phone = Entry(reg_Window)
    address_Line1 = Entry(reg_Window)
    City = Entry(reg_Window)
    postCode = Entry(reg_Window)
    # Layout
    firstName.grid(row = 1, column = 1)
    lastName.grid(row =2, column = 1)
    userName.grid(row=3,column=4)
    Email.grid(row = 3, column = 1)
    Phone.grid(row = 5,column = 1)
    address_Line1.grid(row = 6, column = 1)
    City.grid(row = 7, column = 1)
    postCode.grid(row =8, column=1)
    passWord.grid(row=5,column=4) 
    passWordConfirm.grid(row=6,column=4)
    #Button
    Register = Button(reg_Window, font = Font, text = "Register", command = writeFile)
    Register.grid(row=9, column = 4)
    Back = Button(reg_Window, font = Font, text = "Back",command = Back)
    Back.grid(row = 9, column = 2)

    reg_Window.mainloop()

#--------------------Login--------------#
Font = ("Arial",12)
login_Window = Tk()
login_Window.title("Shared Power - Login")
login_Window.resizable(0,0)

Label(login_Window,font = Font,text = "Shared Power - Login")\
                        .grid(columnspan = 2, stick = E+W)
Label(login_Window, font = Font, text="Username:").\
                    grid(row=1, sticky=E)
Label(login_Window, font = ("Arial", 12), text="Password:").\
                    grid(row=2, sticky=E)

userNameEntry = Entry(login_Window, width=16)
passWordEntry = Entry(login_Window, show="*", width=16)
userNameEntry.grid(row=1, column=1)
passWordEntry.grid(row=2, column=1)

def passwordCheck():
    Directory = os.path.dirname(__file__)
    Directory += '\\Data\\Users\\'
    list_of_Users = os.listdir(Directory)
    userName = userNameEntry.get()  
    for User in list_of_Users:      
        File = open(Directory + User, "r")
        Lines = File.read().split("#")
        Check = passWordEntry.get()
        Check = bytes(Check,"UTF-16")

        passLine = Lines[9]
        Pass = passLine.split(": ")
        correctPass = Pass[1]

        firstName = Lines[1]
        fName = firstName.split(": ")
        firstName = fName[-1]

        lastName = Lines[2]
        lName = lastName.split(": ")
        lastName = lName[-1]

        Email = Lines[3]
        eMail = Email.split(": ")
        Email = eMail[-1]

        Phone = Lines[4]
        phoneNumb = Phone.split(": ")
        Phone = phoneNumb[-1]

        addressLine = Lines[5]
        address = addressLine.split(": ")
        addressLine = address[-1]

        City = Lines[6]
        Place = City.split(": ")
        City = Place[-1]

        Postcode = Lines[7]
        code = Postcode.split(": ")
        Postcode =code[-1]

        Supplier = Lines[8]
        Owner = Supplier.split(": ")
        Supplier = Owner[-1]
        
        
        if userName == User[:-4]:         
            if str(Check) == str(correctPass):
                currentUser = userOBJ(userName)
                currentUser.add_user_info(firstName,lastName,userName,Email,Phone,addressLine,City,Postcode,Supplier)
                login_Window.destroy()
                search_Page(currentUser)
                
                
            else:
                messagebox.showerror("Error!","Password was incorrect")
        
    if userName + ".txt" not in list_of_Users:
        messagebox.showerror("Error!","User not recognised")
            
            
        File.close()

def userOBJ(user):
    user = Register_User()
    return user
    

loginButton = Button(login_Window, font = Font, text="Log In", command = passwordCheck)
registerButton = Button(login_Window, font = Font, text="Register", command = register_Page)

loginButton.grid(row=4, column=0)
registerButton.grid(row=4, column=1)

login_Window.mainloop()
