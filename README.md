# Digital Traces of Gentrification


Team members:  
[Baoling Zhou](https://github.com/baolingz), [Juan Sokoloff](https://github.com/juansokoloff), [Lingyi Zhang](https://github.com/lingyielia), [Srikanth Namuduri](https://github.com/srikanth261)

----------------

Gentrification is an urban process in which neighborhoods undergo fast renewal, it can lead to a to a rent increase and the displacement of low-income population. This process is usually measured by the demographic changes such as income and race change which is collected infrequently and expensively. As a result, the government is unable to timely detect the phenomenon and notify the residents for early preparation. In this paper, we aim to find human behavior features that can help trace gentrifying neighborhoods in New York City. In order to do so, we defined a set of target variables, inherent to the gentrification process and identified a set of human behavior variables (digital traces) that might be correlated with the process. Then we applied three statistical models (Linear Support Vector Classification, Random Forest, and Gradient Boosting) to all the variables and found some common features that present significant correlation with gentrification and also the expected relationship when contrasted with previous studies. These findings can lead to future work in which through the use of this features, gentrification can be predicted, allowing policymakers to amplify the positive impacts and minimize the negative ones that these changes bring to neighborhoods.

## - [Full Report](https://www.authorea.com/users/152594/articles/298517-digital-traces-of-gentrification) - [Website]()

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
