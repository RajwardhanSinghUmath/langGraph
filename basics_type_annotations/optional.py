from typing import Optional

def nice_message(name:Optional[str])->None:
    if name is None:
        print("Hey random person!")
    else:
        print(f"Hey {name}!")

# here name can be string or none 
