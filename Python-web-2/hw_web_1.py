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


class SerializationJsonTuple(SerializationInterface):
    def serialize(self, data):
        return json.dumps(list(data))

    def deserialize(self, packed_data):
        return tuple(json.loads(packed_data))


class SerializationJsonSet(SerializationInterface):
    def serialize(self, data):
        return json.dumps(list(data))

    def deserialize(self, packed_data):
        x = json.loads(packed_data)
        for i, el in enumerate(x):
            if type(el) == list:
                x[i] = tuple(el)
        return set(x)


class SerializationJsonDict(SerializationInterface):
    def serialize(self, data):
        return json.dumps(data)

    def deserialize(self, packed_data):
        return json.loads(packed_data)


class SerializationBinList(SerializationInterface):
    def serialize(self, data):
        return pickle.dumps(data)

    def deserialize(self, packed_data):
        return pickle.loads(packed_data)


class SerializationBinTuple(SerializationInterface):
    def serialize(self, data):
        return pickle.dumps(data)

    def deserialize(self, packed_data):
        return pickle.loads(packed_data)


class SerializationBinSet(SerializationInterface):
    def serialize(self, data):
        return pickle.dumps(data)

    def deserialize(self, packed_data):
        return pickle.loads(packed_data)


class SerializationBinDict(SerializationInterface):
    def serialize(self, data):
        return pickle.dumps(data)

    def deserialize(self, packed_data):
        return pickle.loads(packed_data)


example_list = ["apple", "banana", "cherry"]
example_tuple = ("apple", "banana", "cherry")
example_set = {"apple", "banana", "cherry"}
example_dict = {"brand": "Ford", "model": "Mustang", "year": 1964}


packed_data = SerializationJsonList().serialize(example_list)
des_data = SerializationJsonList().deserialize(packed_data)
assert example_list == des_data

packed_data = SerializationJsonTuple().serialize(example_tuple)
des_data = SerializationJsonTuple().deserialize(packed_data)
assert example_tuple == des_data

packed_data = SerializationJsonSet().serialize(example_set)
des_data = SerializationJsonSet().deserialize(packed_data)
assert example_set == des_data

packed_data = SerializationJsonDict().serialize(example_dict)
des_data = SerializationJsonDict().deserialize(packed_data)
assert example_dict == des_data

packed_data = SerializationBinList().serialize(example_list)
des_data = SerializationBinList().deserialize(packed_data)
assert example_list == des_data

packed_data = SerializationBinTuple().serialize(example_tuple)
des_data = SerializationBinTuple().deserialize(packed_data)
assert example_tuple == des_data

packed_data = SerializationBinSet().serialize(example_set)
des_data = SerializationBinSet().deserialize(packed_data)
assert example_set == des_data

packed_data = SerializationBinDict().serialize(example_dict)
des_data = SerializationBinDict().deserialize(packed_data)
assert example_dict == des_data