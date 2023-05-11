from django.contrib import admin
from .models.silos import Silos
from .models.logs import Logs
from .models.liquids import Liquids
from .models.sensors_in_silos import SensorsInSilos
from .models.sizes import Sizes
from .models.sensors_types import SensorsTypes
from .models.liquid_properties import LiquidProperties
from .models.property import Properties


admin.site.register(Liquids)
admin.site.register(Logs)
admin.site.register(Silos)
admin.site.register(SensorsInSilos)
admin.site.register(Sizes)
admin.site.register(SensorsTypes)
admin.site.register(LiquidProperties)
admin.site.register(Properties)
