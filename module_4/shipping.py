
class ShippingContainer:

    HEIGHT_FT = 8.5
    WIDTH_FT = 8.0

    next_serial = 1337

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return str(owner_code) + str(serial).zfill(6)

    @classmethod
    def _get_next_serial(cls):
        result = cls.next_serial
        cls.next_serial += 1
        return result

    @classmethod
    def create_empty(cls, owner_code, length_ft, *args, **kwargs):
        return cls(owner_code, length_ft, contents=None, *args, **kwargs)

    @classmethod
    def create_with_items(cls, owner_code, length_ft, items, *args, **kwargs):
        return cls(owner_code, length_ft, list(items), *args, **kwargs)

    def __init__(self, owner_code, length_ft, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.length_ft = length_ft
        self.bic = self._make_bic_code(
            owner_code,
            ShippingContainer._get_next_serial())

    @property
    def volume_ft3(self):
        return ShippingContainer.HEIGHT_FT * ShippingContainer.WIDTH_FT * self.length_ft


class RefrigeratedShippingContainer(ShippingContainer):

    MAX_CELSIUS = 4.0
    FRIDGE_VOLUME_FT3 = 100

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return str(owner_code) + "R" + str(serial).zfill(6)

    def __init__(self, owner_code, length_ft, contents, celsius):
        super().__init__(owner_code, length_ft, contents)
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        self._set_celsius(value)

    def _set_celsius(self, value):
        if value > RefrigeratedShippingContainer.MAX_CELSIUS:
            raise ValueError("Temprature to hot!")
        self._celsius = value

    @property
    def volume_ft3(self):
        return super().volume_ft3 - RefrigeratedShippingContainer.FRIDGE_VOLUME_FT3


class HeatedRefrigeratedShippingContainer(RefrigeratedShippingContainer):

    MIN_CELSIUS = -20.0

    # Setter with property overriding
    # @RefrigeratedShippingContainer.celsius.setter
    # def celsius(self, value):
    #     if value < HeatedRefrigeratedShippingContainer.MIN_CELSIUS:
    #         raise ValueError("Temprature to cold")
    #     RefrigeratedShippingContainer.celsius.fset(self, value)

    def _set_celsius(self, value):
        """ Solution using template method"""
        if value < HeatedRefrigeratedShippingContainer.MIN_CELSIUS:
             raise ValueError("Temprature to cold")
        super()._set_celsius(value)