from app.bikeRepository import Bike
from app.bikeRepository.mongo import MongoBike
from .schema import BikeSchema


class Service(object):
    def __init__(self, user_id, bike_client=Bike(adapter=MongoBike)):
        self.bike_client = bike_client
        self.user_id = user_id

        if not user_id:
            raise Exception("user id not provided")

    def find_all_bikes(self):
        bikes = self.bike_client.find_all({'user_id': self.user_id})
        return [self.dump(bike) for bike in bikes]

    def find_kudo(self, bike_id):
        bike = self.bike_client.find({'user_id': self.user_id, 'bike_id': bike_id})
        return self.dump(bike)

    def create_bike_for(self, bikeInfoFromClient):
        self.bike_client.create(self.prepare_bike(bikeInfoFromClient))
        return self.dump(bikeInfoFromClient.data)

    def update_bike_with(self, bike_id, bikeInfoFromClient):
        records_affected = self.bike_client.update({'user_id': self.user_id, 'bike_id': bike_id}, self.prepare_bike(bikeInfoFromClient))
        return records_affected > 0

    def delete_bike_for(self, bike_id):
        records_affected = self.bike_client.delete({'user_id': self.user_id, 'bike_id': bike_id})
        return records_affected > 0

    def dump(self, data):
        return BikeSchema(exclude=['_id']).dump(data).data

    def prepare_bike(self, bikeInfoFromClient):
        data = bikeInfoFromClient.data
        data['user_id'] = self.user_id
        return data

        