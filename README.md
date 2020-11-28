# InfVis Module Task

*Timeo Wullschleger*

*02.12.2020*

*MSE - module InfVis*

*Module supervisor: Prof. Dr. Susanne Bleisch*

## Summary

**U5MR** stands for Under 5 Mortality Rate. Typically, an U5MR value describes the number of children who died before the age of Fife years. Children, especially at a young age, are the most vulnerable part of a society. Using the mortality rate at an age under five years, the wealth of a country or a continent can be described. In the past 20 years, the worldwide U5MR was halved. Most people think, that the world is getting worse but it is not. The goal is to show the global increase of wealth.

Tools & libraries used

* Python
* Plotly
* PowerPoint

## Dataset


UNdata provides multiple datasets with U5MR data.
[This](http://data.un.org/Data.aspx?q=under+five+mortality&d=PopDiv&f=variableID%3a80) dataset contains five-year averaged data from 1950 to 2020 and projected data from 2020 to 2100. It is the biggest dataset and contains data of every country with more than 90'000 inhabitants (in 2019). Next to the countries, it also contains the worldwide average and averages of continents and regions.

Where UNdata got each values can be seen [here](https://population.un.org/wpp/DataSources/). The dataset was downloaded as `.csv`.

Because we do not know what will happen in the future, i have limited the used values to the historical values.



The first dataset has the following structure:
```csv
      Country or Area Code Country or Area    Year(s) Variant    Value
0                        4     Afghanistan  2095-2100  Medium   12.133
1                        4     Afghanistan  2090-2095  Medium   13.109
2                        4     Afghanistan  2085-2090  Medium   14.154
3                        4     Afghanistan  2080-2085  Medium   15.389
4                        4     Afghanistan  2075-2080  Medium   16.669
...                    ...             ...        ...     ...      ...
8665                   716        Zimbabwe  1970-1975  Medium  111.207
8666                   716        Zimbabwe  1965-1970  Medium  119.019
8667                   716        Zimbabwe  1960-1965  Medium  138.869                                                  8668                   716        Zimbabwe  1955-1960  Medium  160.934                                                  8669                   716        Zimbabwe  1950-1955  Medium  181.452 
```
I was able to download the same dataset as an excel sheet `UnderFiveMortality5q0SustDevGroups.xlsx` grouped by regions from [here](https://population.un.org/PEPxplorer/api/queryweb/exportexcel). 
>Unfortunately, their website has changed and the data selector tool does not work anymore.

The second dataset has following structure:
```
     ISO 3166-1 numeric code                                    Location  ... 2010 - 2015 2015 - 2020                   0                        900                                       World  ...         NaN         NaN                   1                       1828  Sustainable Development Goal (SDG) regions  ...         NaN         NaN                   2                        947                          Sub-Saharan Africa  ...        93.0        78.0                   3                        910                              Eastern Africa  ...        73.0        60.0                   4                        108                                     Burundi  ...        78.0        63.0                   ..                       ...                                         ...  ...         ...         ...                   228                      528                                 Netherlands  ...         4.0         3.0                   229                      756                                 Switzerland  ...         4.0         4.0                   230                      918                            Northern America  ...         7.0         7.0                   231                      124                                      Canada  ...         5.0         5.0                   232                      840                    United States of America  ...         7.0         7.0                    
```

### Getting to know the data


## Plot 1 - Change over the last 50y



### Anotations

* Rwanda 1994
* Cambodia 1975-1979



## Geographig distribution and change over time