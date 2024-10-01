# import platform
# import random
 
    
# print(platform.processor())
# print(random.randint(10000 ,99999))

# lister = [
#     'ali' ,'amir' , 'mamad' , "mamadiyan"
# ]
# print(random.choice(lister))
#################################################
from datetime import *

start = datetime(2020 , 5 , 23)
end = start + timedelta(days=30)
print(start - end)