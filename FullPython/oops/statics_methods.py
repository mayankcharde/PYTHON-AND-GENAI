class chauUtils:
    # A static method is a method that belongs to a class but does not depend on instance or class data.
    @staticmethod
    def clean_ingri(text):
        return [item.strip() for item in text.split(",")]
    
    #  JAISE YE CLASS KE DATA PE DEPEND NHI HAI HUMNE BAHAR DATA DIYA HAI LIKE THAT 
raw = " water , milk , ginger , honey "

cleaned = chauUtils.clean_ingri(raw)
print(cleaned)