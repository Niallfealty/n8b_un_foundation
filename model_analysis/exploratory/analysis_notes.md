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

with an AR(1) extrapolation out to 2120 we get:

```
scenario_name
Faster Met Need and Education     8.991398e+09
Fastest Met Need and Education    8.697718e+09
Reference                         1.051867e+10
SDG Met Need and Education        8.208836e+09
Slower Met Need and Education     1.920251e+10
Name: val, dtype: float64
```

we'll stick with this for now (though should probably be noted that the lower two models have a non-trivial ts structure, could be worth looking more lags, arma process...)

UNPD forecasts added, all variants (quite a lot of data on plots) 

This is what we get for the total births post 2022

```
Constant fertility                    1.953372e+10
Constant mortality                    9.717888e+09
High                                  1.471278e+10
Instant replacement                   1.009563e+10
Instant replacement zero migration    1.007334e+10
Low                                   6.512962e+09
Lower 80 PI                           8.854529e+09
Lower 95 PI                           8.309479e+09
Median PI                             1.003345e+10
Medium                                1.003345e+10
Momentum                              9.818377e+09
No change                             1.836689e+10
Upper 80 PI                           1.151160e+10
Upper 95 PI                           1.244501e+10
Zero migration                        1.004192e+10
Name: BirthsSingle, dtype: float64
```

So only actually need to extrapolate for the Low scenario.

That said, extrapolating out 100 years
```
Variant
Constant fertility                    3.263214e+11
Constant mortality                    8.171322e+09
High                                  3.842643e+10
Instant replacement                   2.310487e+10
Instant replacement zero migration    2.304269e+10
Low                                   7.356312e+09
Lower 80 PI                           8.524059e+09
Lower 95 PI                           8.846125e+09
Median PI                             1.093259e+10
Medium                                1.093259e+10
Momentum                              2.040578e+10
No change                             2.207480e+11
Upper 80 PI                           2.639345e+10
Upper 95 PI                           3.198641e+10
Zero migration                        1.078206e+10
Name: BirthsSingle, dtype: float64
```

if we extrapolate out past about 2140 the number of live biths goes negative so we can't extrapolate any more...
