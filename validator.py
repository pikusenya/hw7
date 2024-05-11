from my_exceptions import InvalidAction, InvalidKey, InvalidType


class Validator:
    def validate_type(self, data, type_data):
        if not isinstance(data, type_data):
            raise InvalidType

    def validate_action(self, action, action_list):
        if action not in action_list:
            raise InvalidAction

    def validate_keys(self, data, keys):
        for key in data.keys():
            if key not in keys:
                raise InvalidKey

    def val_calculate(self, data):
        try:
            validator.validate_type(data, dict)
            validator.validate_type(data["a"], (int, float))
            validator.validate_type(data["b"], (int, float))
            validator.validate_action(data["action"], ('+', '-', '/', '*'))
            validator.validate_keys(data, ["a", "b", "action"])
        except InvalidType as error:
            return error.TEXT_EXCEPTION
        except InvalidAction as error:
            return error.TEXT_EXCEPTION
        except InvalidKey as error:
            return error.TEXT_EXCEPTION

    def val_text_editor(self, data):
        try:
            validator.validate_type(data, dict)
            validator.validate_action(data["action"], ("upper", "lower", "trim", "alter"))
            validator.validate_keys(data, ["text", "action"])
        except InvalidType as error:
            return error.TEXT_EXCEPTION
        except InvalidAction as error:
            return error.TEXT_EXCEPTION
        except InvalidKey as error:
            return error.TEXT_EXCEPTION

    def val_parser(self, data):
        try:
            validator.validate_type(data, dict)
            validator.validate_action(data["action"], ("email", "number"))
            validator.validate_keys(data, ["text", "action"])
        except InvalidType as error:
            return error.TEXT_EXCEPTION
        except InvalidAction as error:
            return error.TEXT_EXCEPTION
        except InvalidKey as error:
            return error.TEXT_EXCEPTION


validator = Validator()
