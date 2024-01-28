# # Модуль 5. Объектно-Ориентированное Программирование
# ## Наследование

# ### Супер-класс и класс наследник

# class СуперКласс(object):
    # pass


# class КлассНаследник(СуперКласс):
    # pass


# объект_супер = СуперКласс()
# объект = КлассНаследник()

# isinstance(объект, КлассНаследник) # True
# isinstance(объект, СуперКласс) # True
# issubclass(КлассНаследник, СуперКласс) # True


# ### Расширение класса методами

# ### Добавление метода


# class СуперКласс:
    # def метод1(self):
        # pass
    # def метод2(self):
        # pass
    

# class КлассНаследник(СуперКласс):
    # def метод(self):
        # pass


# объект = КлассНаследник()

# объект.метод()
# объект.метод1()
# объект.метод2()


# ### Переопределение метода


# class СуперКласс:
    # def метод1(self):
        # pass
    # def метод2(self):
        # pass
    


# class КлассНаследник(СуперКласс):
    # def метод2(self, параметр):
        # pass


# объект = КлассНаследник()

# объект.метод1()
# объект.метод2('значение')


# ### Обращение к методу супер-класса


# class СуперКласс:
    # def метод(self, параметр):
        # pass
    


# class КлассНаследник(СуперКласс):
    # def метод(self, параметр1, параметр2):
        # СуперКласс.метод2(self, параметр1)
        

# объект = КлассНаследник()

# объект.метод('значение1', 'значение2')


# class КлассНаследник(СуперКласс):
    # def метод(self, параметр1, параметр2):
        # super().метод(параметр1) # Ого! никакого self!


# ### Перегрузка операторов

# class Человек:
    # def __init__(self, возраст):
        # self.возраст = возраст
    
    # def __eq__(self, другой_объект):
        # return self.возраст == другой_объект.возраст
    
    # def __lt__(self, другой_объект):
        # return self.возраст < другой_объект.возраст
    
    # def __gt__(self, другой_объект):
        # return self.возраст > другой_объект.возраст
        


# вася = Человек(25)
# петя = Человек(33)
# федя = Человек(25)

# print(вася == федя)
# print(вася > федя)
# print(вася > петя)
