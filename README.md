# uk-covid-cases-la

Plot of UK COVID cases by local authority

- `data/ons_local_authority_median_age.csv` Columns C,D,E,G from row 16 onwards in the sheet
  "Median age and pop. density" in
  [source](https://www.ons.gov.uk/visualisations/dvc1071/profiles/datadownload.xlsx)
  retrieved via
  [ONS website](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/articles/populationprofilesforlocalauthoritiesinengland/2020-12-14)
  on 20th December 2021
- `data/ukhsa_local_authority_covid_case_rates.csv` came from
  [source](https://api.coronavirus.data.gov.uk/v2/data?areaType=ltla&metric=newCasesBySpecimenDateRollingRate&format=csv)
  via [VictimOfMaths](https://github.com/VictimOfMaths/COVID-19/blob/master/Heatmaps/COVIDCasesLTLAPhasePlot.R)
  originally via [Twitter](https://twitter.com/VictimOfMaths/status/1472968769353965568) on 20th
  December 2021
