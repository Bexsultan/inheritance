# #problems1


# data = {

# "markers": [{"name": "Rixos The Palm Dubai","location": [25.1212, 55.1535],},
# {"name": "Shangri-La Hotel","location": [25.2084, 55.2719]},
# {"name": "Grand Hyatt","location": [25.2285, 55.3273]}]}

# class Hotel:
    
#     def __init__(self, data):
#         self.data = data

#     def get_names(self):
#         hotel_names = []
#         for hotel in self.data['markers']:
#             hotel_names.append(hotel['name'])
#         return hotel_names

#     def get_dict(self):
#         names = []
#         for i in self.data['markers']:
#             names.append(i['name'])
            
#         location = []
#         for i in self.data['markers']:
#             location.append(i['location'])
        
#         tuple1 = tuple(names)
#         tuple2 = tuple(location)

#         datas = {
#             'name':tuple1,
#             'location':tuple2
#         }
#         return datas

#     def add_id_status(self):
#         for i in self.data['markers']:
#             i['status_id'] = 1
#         return 'Добавлен'


# hotel = Hotel(data)
# hotel_names = hotel.get_names()
# hotel_dict = hotel.get_dict()
# hotel_id = hotel.add_id_status()
# print(hotel_dict, hotel_id)
        

# #problems2
# class Factory:
#     def engine(self):
#         return 'Двигатель создан'
    
#     def bridge(self):
#         return 'Ходовая часть создана'

# class Toyota(Factory):
    
#     def wheels(self):
#         return 'Колёса готовы'
    
#     def windows(self):
#         return 'Стёкла готовы'


# avto = Toyota()
# print([avto.engine(), avto.bridge(), avto.wheels(), avto.windows()])