from pyndatic import BaseModel

class User(BaseModel):
    id : int
    name:str
    is_active:bool
    
imput_data ={'id': '101a', 'name': "Chaicode", 'is_active': True}

user = User(**imput_data)
print(user)    