class KaggleMember(): #line1
    #class member
    kaggle_member_count=0  #line2
        
    def __init__(self, name, surname, level=None): #line3
        
        #object members
        self.name=name.capitalize() #line4
        self.surname=surname.upper() #line5
        self._set_level(level) #6
        
        KaggleMember.kaggle_member_count+=1 #line7
        self.kaggle_id=KaggleMember.kaggle_member_count #line8
        
        
    
    def display_number_of_member(self): #line11
        print("There are {} members in Kaggle community".format(KaggleMember.kaggle_member_count)) #line12
    
    def display_member_info(self): #line13
        print("Kaggle Member Full Name:{} {}".format(self.name, self.surname)) #line14
        print("Level:{:15}".format(self.level)) #line15
        print("Kaggle ID:",self.kaggle_id)
    
    def _set_level(self, level):
        if level is None: #line6
            self.level='Novice' #line7
        else: #line8
            self.level=level.title() #line9
        
    
    myclass_name='Kaggle Member' #line16