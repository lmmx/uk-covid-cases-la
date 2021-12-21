import pandas as pd
import matplotlib.pyplot as plt

ons_demog_tsv = "data/ons_local_authority_median_age.tsv"
ukhsa_la_case_tsv = "data/ukhsa_local_authority_covid_case_rates.csv"

age_df = pd.read_csv(ons_demog_tsv, sep="\t")
new_age_df_cols = ["areaCode", "areaName", "medianAge", "popDensity"]
age_df = age_df.rename(dict(zip(age_df.columns, new_age_df_cols)), axis="columns")
case_df = pd.read_csv(ukhsa_la_case_tsv)

case_x_lab = "newCasesBySpecimenDateRollingRate"
case_y_lab = "changeSevenDays"
case_c_lab = "medianAge"

most_recent_cases = case_df.groupby(["areaName"]).agg("first").reset_index().merge(age_df[["areaCode", "medianAge"]], how="left")
week_old_cases = (
    case_df.groupby(["areaName"])
    .shift(-7)
    .groupby(["areaCode"], sort=False, as_index=False)
    .agg("first")[case_x_lab]
)
most_recent_cases["changeSevenDays"] = most_recent_cases[case_x_lab] - week_old_cases

most_recent_cases.plot.scatter(x=case_x_lab, y=case_y_lab, c=case_c_lab, s=100, colormap="viridis", figsize=(20,14))
plt.tight_layout(pad=2)
#plt.show()
plt.savefig("scatter.png")
