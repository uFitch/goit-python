from abc import abstractclassmethod, ABCMeta
import pickle
import json


class SerializationInterface(metaclass=ABCMeta):
    @abstractclassmethod
    def serialize(self):
        pass

    @abstractclassmethod
    def deserialize(self):
        pass


class SerializationJsonList(SerializationInterface):
    def serialize(self, data):
        return json.dumps(data)

    def deserialize(self, packed_data):
        return json.loads(packed_data)


class SerializationJsonDict(SerializationInterface):
    def serialize(self, data):
        return json.dumps(data)

    def deserialize(self, packed_data):
        return json.loads(packed_data)


class SerializationJsonSet(SerializationInterface):
    def serialize(self, data):
        return json.dumps(list(data))

    def deserialize(self, packed_data):
        x = json.loads(packed_data)
        for i, el in enumerate(x):
            if type(el) == list:
                x[i] = tuple(el)
        print(set(x), type(x))
        return set(x)


class SerializationJsonTuple(SerializationInterface):
    def serialize(self, data):
        return json.dumps(list(data))

    def deserialize(self, packed_data):
        return tuple(json.loads(packed_data))


class SerializationBinList(SerializationInterface):
    def serialize(self, data):
        return pickle.dumps(data)

    def deserialize(self, packed_data):
        return pickle.loads(packed_data)


class SerializationBinList(SerializationInterface):
    def serialize(self, data):
        return pickle.dumps(data)

    def deserialize(self, packed_data):
        return pickle.loads(packed_data)


class SerializationBinDict(SerializationInterface):
    def serialize(self, data):
        return pickle.dumps(data)

    def deserialize(self, packed_data):
        return pickle.loads(packed_data)


class SerializationBinSet(SerializationInterface):
    def serialize(self, data):
        return pickle.dumps(data)

    def deserialize(self, packed_data):
        return pickle.loads(packed_data)
        

class SerializationBinTuple(SerializationInterface):
    def serialize(self, data):
        return pickle.dumps(data)

    def deserialize(self, packed_data):
        return pickle.loads(packed_data)