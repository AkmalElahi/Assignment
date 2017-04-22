def build_profile(name, last,**info):
    profile={}
    profile['first name']=name
    profile['last name'] =last
    for key,value in info.items():
        profile[key]=value
    return profile

my_profile=build_profile('Akmal','Elahi',Email='akmalelahi@gmail.com',contact='090078601')
print(my_profile)