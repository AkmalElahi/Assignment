def describe_car(manufacturer,model_name,**other_specification):
    car_info={}
    car_info['manufacturer']=manufacturer
    car_info['model_name']=model_name
    for key,values in other_specification.items():
        car_info[key]=values
    return car_info

my_car=describe_car('Honda','Civic',doors='4',trammission='Auto',cylinders='4')
print(my_car)
