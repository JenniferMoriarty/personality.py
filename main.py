

#PRODUCT-------------------------------------------------------------------
class Personality:
    
    def __init__(self):
        self.__extroversion = None #the double underscore prevents name conflicts with subclasses, makes private
        self.__sensing = None
        self.__thinking = None
        self.__judging = None
        
    def set_extroversion(self, extroversion):
        self.__extroversion = extroversion
        
    def set_sensing(self, sensing):
        self.__sensing = sensing
        
    def set_thinking(self, thinking):
        self.__thinking = thinking
    
    def set_judging(self, judging):
        self.__judging = judging
        
    def product_properties(self):
        print(f"extroversion: {self.__extroversion.num}, sensing: {self.__sensing.num}, thinking: {self.__thinking.num}, judging: {self.__judging.num}")

#COMPONENTS OF THE PRODUCT----------------------------------------------------
class Extroversion:
    num = None
    
class Sensing:
    num = None
    
class Thinking:
    num = None

class Judging:
    num = None

#BUILDER INTERFACE------------------------------------------------------------
class IBuilder():
    
    def get_extroversion(self):
        "assembly extroversion"
        
    def get_sensing(self):
        "assembly sensing"
        
    def get_thinking(self):
        "assembly thinking"
        
    def get_judging(self):
        "assembly judging"
        
#CONCRETE BUILDERS--------------------------------------------------------------
class ISFJ(IBuilder):
    
    def get_extroversion(self):
        extroversion = Extroversion()
        extroversion.num = -1
        return extroversion
    
    def get_sensing(self):
        sensing = Sensing()
        sensing.num = 1
        return sensing
    
    def get_thinking(self):
        thinking = Thinking()
        thinking.num = -1
        return thinking

    def get_judging(self):
        judging = Judging()
        judging.num = 1
        return judging
    
class ESFJ(IBuilder):
    
    
    def get_extroversion(self):
        extroversion = Extroversion()
        extroversion.num = 1
        return extroversion
    
    def get_sensing(self):
        sensing = Sensing()
        sensing.num = 1
        return sensing
    
    def get_thinking(self):
        thinking = Thinking()
        thinking.num = -1
        return thinking

    def get_judging(self):
        judging = Judging()
        judging.num = 1
        return judging
    
class ISTJ(IBuilder):
    
    def get_extroversion(self):
        extroversion = Extroversion()
        extroversion.num = -1
        return extroversion
    
    def get_sensing(self):
        sensing = Sensing()
        sensing.num = 1
        return sensing
    
    def get_thinking(self):
        thinking = Thinking()
        thinking.num = 1
        return thinking

    def get_judging(self):
        judging = Judging()
        judging.num = 1
        return judging
    
#DIRECTOR------------------------------------------------------------------------------
class Director:
    
    __builder = None
    
    def set_builder(self, builder):
        self.__builder = builder
        
    def get_personality(self):
        personality = Personality()
        
        extroversion = self.__builder.get_extroversion()
        personality.set_extroversion(extroversion)
        
        sensing = self.__builder.get_sensing()
        personality.set_sensing(sensing)
        
        thinking = self.__builder.get_thinking()
        personality.set_thinking(thinking)
        
        judging = self.__builder.get_judging()
        personality.set_judging(judging)
        
        return personality
    
#-driver code------------------------------------------------------------

isfj_personality = ISFJ()
esfj_personality = ESFJ()
istj_personality = ISTJ()
director = Director()

#personality 1: ISFJ
director.set_builder(isfj_personality)
isfj_engineer = director.get_personality()
isfj_engineer.product_properties()

#personality 2: ESFJ
director.set_builder(esfj_personality)
esfj_engineer = director.get_personality()
esfj_engineer.product_properties()

#personality 3: ISTJ
director.set_builder(istj_personality)
istj_engineer = director.get_personality()
istj_engineer.product_properties()


