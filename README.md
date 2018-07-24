# Digital Traces of Gentrification


Team members:  
[Baoling Zhou](https://github.com/baolingz), [Juan Sokoloff](https://github.com/juansokoloff), [Lingyi Zhang](https://github.com/lingyielia), [Srikanth Namuduri](https://github.com/srikanth261)

----------------

Gentrification is one of the most complex topics regarding urban development in modern cities. On one hand, it has beneficial effects such as creating economic dynamism in not very successful neighborhoods, but on the other hand it also leads to an increase in land prices which affects the population negatively who lives in the gentrifying areas. In this paper we create a definition of gentrification that involves the increase in rent and physical transformation in cities, and then identify variables that are correlated to the process, in order to promptly detect gentrifying neighborhoods or even being able to predict which will happen. To do this, we first develop a definition of gentrification that includes consequences, like rent increase, and also generating factors such as the number renewal licenses in an area, followed by the identification of variables that change when gentrification occurs, and finally developing a model that can pinpoint gentrifying neighborhoods or even predict which will gentrify. This will allow to identify the gentrification process before one can detect it from census and other more static/non-frequently updated data, even further this project could be beneficial for both city agencies and developers in order to mitigate the negative impacts that the process brings or to maximize their investment returns, respectively.

## Project Scope
__Baseline Goals__:
An exploration of the various indicators of Gentrification and a resulting definition in terms of a measure for displacement of population and renewal of the region
Identification of digital traces in openly available data such as 311 data, historical rental prices, business license data etc
Create an urban-activity based model that can identify areas in NYC that are getting gentrified

__Challenge__:
Predict what areas in NYC may be gentrified next

## Repo directory structure
```shell
.
├── DataProcessing_EDA
│   ├── 311complaints
│   │   ├── complaint_change_2010_2015.ipynb
│   │   └── data_process_311complaint.py
│   ├── clustering
│   │   ├── clustering.ipynb
│   │   └── timeSeriesCluster.ipynb
│   ├── commercial_activity_growth_index
│   │   ├── DataScrape.py
│   │   └── commercial_activity_growth_index.ipynb
│   ├── crime
│   │   └── Crime.ipynb
│   ├── target_variables
│   │   ├── MapofGentrification.ipynb
│   │   └── Target_variables_and_index_validation.ipynb
│   └── transportation
│       ├── GreenTaxi_monthly.ipynb
│       ├── Subway_EDA.ipynb
│       ├── Subway_monthly_update.ipynb
│       ├── Taxi_EDA.ipynb
│       ├── YellowTaxi_monthly.ipynb
│       └── annual_data_EDA.ipynb
├── DataSource.md
├── Modeling
│   ├── OLS_LSVC
│   │   └── Preliminary_OLS_and_LSVC.ipynb
│   ├── RandomForest_GradientBoosting
│   │   ├── RandomForest_GradientBoosting_part1.ipynb
│   │   └── RandomForest_GradientBoosting_part2.ipynb
│   └── correlation_analysis
│       └── Correlation_and_statistical_significance_of_selected_features.ipynb
└── README.md
```
