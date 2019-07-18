class Bike(object):         # aka Repository class
    def __init__(self, adapter=None):
        self.client = adapter()

    def find_all(self, selector):
        return self.client.find_all(selector)
    
    def find(self, selector):
        return self.client.find(selector)
    
    def create(self, bikeInfo):
        return self.client.create(bikeInfo)
    
    def update(self, selector, bikeInfo):
        return self.client.update(selector, bikeInfo)
    
    def delete(self, selector):
        return self.client.delete(selector)