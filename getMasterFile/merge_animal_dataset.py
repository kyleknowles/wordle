

import pandas as pd

df = pd.read_csv("animalDataset.csv")

df["Genus"] = df["Animal"].str.split(" ").str[-1].str.capitalize()

cols = df.columns.to_list()

for column in cols:
    if (("(" in column) | (column == "Offspring per Birth")):

        df[column] = df[column].str.replace("Up to ", "")
        df[column] = df[column].str.replace("Varies", "")
        df[column] = df[column].str.replace("Not Applicable", "")

        df[column] = (df[column].str.split("-"))
    else:
        df[column] = df[column].fillna("").str.split(", ")



df["Genus"] = df["Genus"].str[0]


#df = df.groupby("Genus").agg(lambda x: ", ".join(x.astype(str))).reset_index()

merged = df.groupby("Genus", as_index=False).agg(
    lambda x: sum(x, [])
)



for column in cols:
    if (column != "Genus"):
        merged[column] = merged[column].apply(lambda x: [i for i in x if i != ""])
        merged[column] = merged[column].apply(lambda x: list(set(x)))

        if (("(" in column) | (column == "Offspring per Birth")):
            merged[column] = merged[column].apply(lambda x: "?" if len(x) == 0 else str(x[0]) if len(x) == 1 else str(min(x) + "-" + max(x)))

        else:
            merged[column] = merged[column].apply(lambda x: ", ".join(x))

print(merged)

df.to_csv("genusDataset.csv")