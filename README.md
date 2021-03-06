# uk-covid-cases-la

Plot of UK COVID cases by local authority (confirming a hunch that median age correlated with surges)

![](https://raw.githubusercontent.com/lmmx/uk-covid-cases-la/master/scatter.png)

- `data/ons_local_authority_median_age.tsv` came from columns C,D,E,G (row 16 onwards) in the sheet
  "Median age and pop. density" in
  [source spreadsheet](https://www.ons.gov.uk/visualisations/dvc1071/profiles/datadownload.xlsx)
  retrieved via
  [ONS website](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/articles/populationprofilesforlocalauthoritiesinengland/2020-12-14)
  on 20th December 2021

- `data/ukhsa_local_authority_covid_case_rates.csv` came from
  [source CSV](https://api.coronavirus.data.gov.uk/v2/data?areaType=ltla&metric=newCasesBySpecimenDateRollingRate&format=csv)
  via [VictimOfMaths](https://github.com/VictimOfMaths/COVID-19/blob/master/Heatmaps/COVIDCasesLTLAPhasePlot.R)
  originally via [Twitter](https://twitter.com/VictimOfMaths/status/1472968769353965568) on 20th
  December 2021
