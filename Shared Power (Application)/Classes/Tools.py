
#variables = per_Day
#funtions = set_p
import uuid


class Tools:


    per_Day =""
    per_Hday =""
    tool_Type =""
    tool_ID ="" #uuid
    tool_Info =""
    tool_Make =""
    tool_Model = ""
    tool_Owner = ""
    
    
        
    def add_tool_info (self, Type, Make, Model, Info, ID,Day,Hday):
        self.tool_Type = Type
        self.tool_Make = Make
        self.tool_Model = Model
        self.tool_Info = Info
        self.tool_ID = ID
        self.per_Day= Day
        self.per_Hday = Hday
        
       
    


    
