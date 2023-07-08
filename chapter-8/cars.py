def make_car(manufecturer, model, **others):
    car_dict = {
        'manufecturer': manufecturer.title(),
        'model': model.title(),
    }
    for options, values in others.items():
        car_dict[options] = values
    return car_dict

my_outback = make_car('subaru', 'outback', color='blue', tow_package=True)
print(my_outback)

my_old_accord = make_car('honda', 'accord', year=1991, color='white',
        headlights='popup')
print(my_old_accord)