# Вареная картошка картофель 200 гр, масло 20 гр, лук 10 гр, соль 2 гр
# Салат помидоры 100 гр, огурцы 100гр, петрушка 20 гр, масло 30 мл, редиска 50 гр, лук 10 гр
# Компот сухофрукты 50гр, сахар 10 гр, специи 10 гр

cook_book = {
  'вареная картошка': [
    {'ingridient_name': 'картофель', 'quantity': 200, 'measure': 'гр'},
    {'ingridient_name': 'масло сливочное', 'quantity': 20, 'measure': 'гр'},
    {'ingridient_name': 'лук', 'quantity': 10, 'measure': 'гр'},
    {'ingridient_name': 'соль', 'quantity': 2, 'measure': 'гр'}
    ],
  'салат': [ 
    {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр'},
    {'ingridient_name': 'огурцы', 'quantity': 100, 'measure': 'гр'},
    {'ingridient_name': 'петрушка', 'quantity': 20, 'measure': 'гр'},
    {'ingridient_name': 'масло подсолнечное', 'quantity': 30, 'measure': 'мл'},   
    {'ingridient_name': 'редиска', 'quantity': 50, 'measure': 'гр'},
    {'ingridient_name': 'лук', 'quantity': 10, 'measure': 'гр'}    
    ],
  'компот': [ 
    {'ingridient_name': 'сухофрукты', 'quantity': 50, 'measure': 'гр'},
    {'ingridient_name': 'сахар', 'quantity': 10, 'measure': 'гр'},
    {'ingridient_name': 'специи', 'quantity': 10, 'measure': 'гр'}
    ]
}

def get_shop_list_by_dishes(dishes, person_count):
  shop_list = {}
  for dish in dishes:
    for ingridient in cook_book[dish]:
      new_shop_list_item = dict(ingridient)
      new_shop_list_item['quantity'] *= person_count
      if new_shop_list_item['ingridient_name'] not in shop_list:
        shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
      else:
        shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
  return shop_list
    
def print_shop_list(shop_list):
  for shop_list_item in shop_list.values():
    print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'], shop_list_item['measure']))
  
def create_shop_list():
  person_count = int(input('Введите количество человек'))
  dishes = input('Введите блюда в расчете на одного человека через запятую').lower().split(',')
  shop_list = get_shop_list_by_dishes(dishes, person_count)
  print_shop_list(shop_list)
  
create_shop_list()
  

  