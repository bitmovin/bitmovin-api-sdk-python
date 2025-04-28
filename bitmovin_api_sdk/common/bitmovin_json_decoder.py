import re
from enum import EnumMeta
from importlib import import_module
from dateutil.parser import parse


from bitmovin_api_sdk.models import PaginationResponse


class BitmovinJsonDecoder(object):
    model_module = import_module('bitmovin_api_sdk.models')

    @staticmethod
    def map_dict_to_pagination_response(result, model):
        # type: (object, type) -> object

        model_to_return = BitmovinJsonDecoder.map_dict_to_model(result, PaginationResponse)

        pagination_items = list()

        model_instance = model()
        if 'discriminator_value_class_map' in model.__dict__:
            for i in model_to_return.items:
                model_class = type(model_instance)
                discriminator_value = model_instance.discriminator_value_class_map.get(i['type'])
                if discriminator_value is not None:
                    model_class = getattr(BitmovinJsonDecoder.model_module, discriminator_value)
                pagination_items.append(BitmovinJsonDecoder.map_dict_to_model(i, model_class))
        else:
            pagination_items = BitmovinJsonDecoder.map_dict_to_list(model_to_return.items, model)

        model_to_return.items = pagination_items
        return model_to_return

    @staticmethod
    def map_dict_to_list(result, model):
        # type: (iter, type) -> list

        list_to_return = list()
        for i in result:
            list_to_return.append(BitmovinJsonDecoder.map_dict_to_model(i, model))

        return list_to_return

    @staticmethod
    def map_dict_to_model(result, model):
        # type: (dict, type) -> object

        if isinstance(model, EnumMeta):
            return get_enum_value(result, model)

        if issubclass(model, list):
            return result

        if type(result)==list:
            return result

        model_instance = model()

        if 'discriminator_value_class_map' in model.__dict__:
            model_name = model_instance.discriminator_value_class_map.get(result['type'])
            if model_name is not None:
                model = getattr(BitmovinJsonDecoder.model_module, model_name)

        model_instance = model()

        if not hasattr(model_instance, 'attribute_map'):
            model_instance.attribute_map = {}

        all_attributes = model_instance.attribute_map

        for key in all_attributes:
            value = result.get(all_attributes.get(key))
            if value is not None:
                type_ = model_instance.openapi_types.get(key)

                try:
                    if re.match('list', type_, re.I):
                        matches = re.search(r'\[(.*)\]', type_)

                        if matches is not None and len(matches.groups()) is 1:
                            if getattr(BitmovinJsonDecoder.model_module, matches.group(1)):
                                model_class = getattr(BitmovinJsonDecoder.model_module,
                                                      matches.group(1))
                                new_value = list()
                                for k in value:
                                    val = k
                                    if isinstance(value, dict):
                                        val = value[k]

                                    new_value.append(
                                        BitmovinJsonDecoder.map_dict_to_model(val, model_class))
                                model_instance.__setattr__(key, new_value)
                                continue

                    model_class = getattr(BitmovinJsonDecoder.model_module, type_)

                    if isinstance(model_class, EnumMeta):
                        value = get_enum_value(value, model_class)
                        model_instance.__setattr__(key, value)
                        continue

                    new_value = BitmovinJsonDecoder.map_dict_to_model(value, model_class)
                    model_instance.__setattr__(key, new_value)
                except (NameError, AttributeError) as e:  # pylint: disable=unused-variable
                    # No model type that has to be special handled
                    if type_ == 'date':
                        new_value = parse(value).date()
                        model_instance.__setattr__(key, new_value)
                    elif type_ == 'datetime':
                        new_value = parse(value)
                        model_instance.__setattr__(key, new_value)
                    else:
                        new_value = value
                        model_instance.__setattr__(key, new_value)

        return model_instance


def get_enum_value(value, model_class):
    # type: (object, EnumMeta) -> str

    # Search for the attribute in the Enum
    for attr in model_class:
        if attr.value == value:
            return attr
