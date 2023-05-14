# Notes on exploratory analysis of data

## GBD projection

Data split into following (non-codebook) files

```
IHME_POP_2017_2100_DEATH_FASTER_Y2020M05D01.CSV
IHME_POP_2017_2100_DEATH_FASTEST_Y2020M05D01.CSV
IHME_POP_2017_2100_DEATH_PAST_Y2020M05D01.CSV
IHME_POP_2017_2100_DEATH_REFERENCE_Y2020M05D01.CSV
IHME_POP_2017_2100_DEATH_SDG_Y2020M05D01.CSV
IHME_POP_2017_2100_DEATH_SLOWER_Y2020M05D01.CSV
IHME_POP_2017_2100_LIFE_EXPECTANCY_Y2020M05D01.CSV
IHME_POP_2017_2100_LIVE_BIRTHS_Y2020M05D01.CSV
IHME_POP_2017_2100_MIGRATION_Y2020M05D01.CSV
IHME_POP_2017_2100_POP_BOTH_SEX_ALL_AGE_Y2020M05D01.CSV
IHME_POP_2017_2100_POP_FASTER_Y2020M05D01.CSV
IHME_POP_2017_2100_POP_FASTEST_Y2020M05D01.CSV
IHME_POP_2017_2100_POP_PAST_Y2020M05D01.CSV
IHME_POP_2017_2100_POP_REFERENCE_Y2020M05D01.CSV
IHME_POP_2017_2100_POP_SDG_Y2020M05D01.CSV
IHME_POP_2017_2100_POP_SLOWER_Y2020M05D01.CSV
IHME_POP_2017_2100_TFR_Y2020M05D01.CSV
```

handy as this splits everything up into data in a good format for plotting and answering questions

from the live births data:
```
scenario_name
Faster Met Need and Education     7.883581e+09
Fastest Met Need and Education    7.899042e+09
Reference                         9.095052e+09
SDG Met Need and Education        7.553404e+09
Slower Met Need and Education     1.426350e+10
```

so we don't quite reach the next 8Bn in these scenarios. Taking a quick look at pacf to see if we could maybe just throw an arima at it with a sensible order to extrapolate (would be sensible to think a bit about this as an arma process - but probably fine as a quick and dirty extrapolation - as long as we're not going out too far)
