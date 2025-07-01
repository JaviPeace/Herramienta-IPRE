from enum import Enum
from abc import ABC, abstractmethod

# Define los tipos de filtro
class FilterType(Enum):
    NEGATIVE = "Negative"
    NO_GREEN = "NoGreen"
    BLACK_AND_WHITE = "BlackAndWhite"

# Interfaz base
class IFilter(ABC):
    @abstractmethod
    def apply(self, image):
        pass

# Filtro base sin modificación
class NoFilter(IFilter):
    def apply(self, image):
        return image  # No modifica nada

# Filtros decoradores
class FilterDecorator(IFilter):
    def __init__(self, base_filter: IFilter):
        self.base_filter = base_filter

class NegativeFilter(FilterDecorator):
    def apply(self, image):
        image = self.base_filter.apply(image)
        # aplicar filtro negativo (ejemplo)
        return f"Negative({image})"

class NoGreenFilter(FilterDecorator):
    def apply(self, image):
        image = self.base_filter.apply(image)
        # eliminar canal verde (ejemplo)
        return f"NoGreen({image})"

class BlackAndWhiteFilter(FilterDecorator):
    def apply(self, image):
        image = self.base_filter.apply(image)
        # convertir a blanco y negro (ejemplo)
        return f"BlackAndWhite({image})"

class BlueFilter(FilterDecorator):
    def apply(self, image):
        image = self.base_filter.apply(image)
        # efecto azul (ejemplo)
        return f"Blue({image})"

# Controlador principal
class Controller:
    @staticmethod
    def build_filter(filters: list[FilterType]) -> IFilter:
        final_filter: IFilter = NoFilter()

        for filter_type in filters:
            if filter_type == FilterType.NEGATIVE:
                final_filter = NegativeFilter(final_filter)
            if filter_type == FilterType.NO_GREEN:
                final_filter = NoGreenFilter(final_filter)
            if filter_type == FilterType.BLACK_AND_WHITE:
                final_filter = BlackAndWhiteFilter(final_filter)

        return final_filter

    @staticmethod
    def build_my_filter() -> IFilter:
        return BlueFilter(NoFilter())