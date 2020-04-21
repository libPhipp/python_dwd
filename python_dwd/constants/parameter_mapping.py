""" time resolution to parameter mapping """
from python_dwd.enumerations.parameter_enumeration import Parameter
from python_dwd.enumerations.period_type_enumeration import PeriodType
from python_dwd.enumerations.time_resolution_enumeration import TimeResolution

TIME_RESOLUTION_PARAMETER_MAPPING = {
    TimeResolution.MINUTE_1: [[Parameter.PRECIPITATION],
                              [PeriodType.HISTORICAL,
                               PeriodType.RECENT,
                               PeriodType.NOW]],
    TimeResolution.MINUTE_10: [[Parameter.TEMPERATURE_AIR,
                                Parameter.TEMPERATURE_EXTREME,
                                Parameter.WIND_EXTREME,
                                Parameter.PRECIPITATION,
                                Parameter.SOLAR,
                                Parameter.WIND],
                               [PeriodType.HISTORICAL,
                                PeriodType.RECENT,
                                PeriodType.NOW]],
    TimeResolution.HOURLY: [[Parameter.TEMPERATURE_AIR,
                             Parameter.CLOUD_TYPE,
                             Parameter.CLOUDINESS,
                             Parameter.PRECIPITATION,
                             Parameter.PRESSURE,
                             Parameter.TEMPERATURE_SOIL,
                             Parameter.SOLAR,
                             Parameter.SUNSHINE_DURATION,
                             Parameter.VISBILITY,
                             Parameter.WIND],
                            [PeriodType.HISTORICAL,
                             PeriodType.RECENT,
                             ]],
    TimeResolution.DAILY: [[Parameter.CLIMATE_SUMMARY,
                            Parameter.PRECIPITATION_MORE,
                            Parameter.TEMPERATURE_SOIL,
                            Parameter.SOLAR,
                            Parameter.WATER_EQUIVALENT],
                           [PeriodType.HISTORICAL,
                            PeriodType.RECENT,
                            ]],
    TimeResolution.MONTHLY: [[Parameter.CLIMATE_SUMMARY,
                              Parameter.PRECIPITATION_MORE],
                             [PeriodType.HISTORICAL,
                              PeriodType.RECENT,
                              ]],
    TimeResolution.ANNUAL: [[Parameter.CLIMATE_SUMMARY,
                             Parameter.PRECIPITATION_MORE],
                            [PeriodType.HISTORICAL,
                             PeriodType.RECENT,
                             ]]
}