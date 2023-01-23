from elements.elements import *

class MapElement(Element):
    """
    Base class for all the map elements.
    :param name: the element name
    :param extension: the element extension
    """
    def __init__(self, name: str):
        super().__init__(name)
    
    @property
    def data(self):
        return self.__dict__


class Nation(MapElement):
    def __init__(self, name: str, population: int, extension: int, traits: list=[], *args, **kwargs):
        super().__init__(name)
        self.traitsvar = traits
        self.extensionvar = extension
        self.populationvar = population

        for i in kwargs:
            self.add_data(i, kwargs[i])


    def add_data(self, data: str, value: int):
        data_name= data+'var'
        def gett(self):
            return self.__dict__[data_name]
        def sett(self, x):
            self.__dict__[data_name]= x

        self.__dict__[data_name]= value
        setattr(self.__class__, data, property(fget= gett, fset= sett))


    def population_get(self):
        return self.populationvar

    def population_set(self, value: int):
        self.populationvar= value
    
    population= property(population_get, population_set)


    def extension_get(self):
        return self.extensionvar
    
    def extension_set(self, value: int):
        self.extensionvar= value
    
    extension= property(extension_get, extension_set)

    
    def traits_get(self):
        return self.traitsvar
    
    def traits_set(self, value):
        self.traitsvar.append(value)
    
    def traits_del(self, value):
        self.traitsvar.remove(value)
    
    traits= property(traits_get, traits_set, traits_del)

    #fix
    def get_nation_data(self, data_name: str):
        return self.data[data_name]

    def get_nation_all_data(self):
        """returns a dictionary with all the data(resources) of the nation"""
        return self.data
    
    # def get_nation_data(self, data_name: str):
    #     data= 0
    #     for prov in self.contains.values():
    #         if prov.data.get(data_name):
    #             data+= prov.data[data_name]
    #     return data

    # def get_nation_all_data(self):
    #     """returns a dictionary with all the data(resources) of the nation"""
    #     all_data = {}
    #     for prov in self.contains.values():
    #         for data_name in prov.data.keys():
    #             if all_data.get(data_name):
    #                 all_data[data_name]+= prov.data[data_name]
    #             else:
    #                 all_data[data_name]= prov.data[data_name]
    #     return all_data

    # def change_data(self, data_name: str, value: int):
    #     """distributes a change in the country's data(resources) equally among all its provinces"""
    #     total_data=self.get_nation_data(data_name)
    #     for prov in self.contains.values():
    #         if prov.data.get(data_name):
    #             prov.data[data_name]+= prov.data[data_name]*value/total_data
        
    def __str__(self):
        return f'{self.name}'

    def compare(self, new):
        if self.name != new.name:
            raise Exception(f'Error: "{self.name}" and "{new.name}" are not the same nation')
        if type(self) != type(new):
            raise Exception(f'Error: "{self.name}" and "{new.name}" are not of the same type')

        changes= dict()
        for key in self.data.keys():
            if self.data[key] != new.data[key]:
                changes[key]= (self.data[key], new.data[key])
        if changes:
            return changes
        return None
         

class Sea(MapElement):
    def __init__(self, name: str, extension:float):
        super().__init__(name)
        self.extension = extension



class Trait(Element):
    def __init__(self, name: str):
        super().__init__(name)