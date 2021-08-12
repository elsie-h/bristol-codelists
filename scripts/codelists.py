from os import system
from cohortextractor import codelist, codelist_from_csv

opensafely_ethnicity_codes_16 = codelist_from_csv(
    "codelists/opensafely-ethnicity.csv",
    system="ctv3",
    column="Code",
    category_column="Grouping_16",
)

primis_covid19_vacc_update_ethnicity = codelist_from_csv(
    "codelists/primis-covid19-vacc-uptake-eth2001.csv",
    system="snomed",
    column="code",
    category_column="grouping_16_id",
)

smoking_clear = codelist_from_csv(
    "codelists/opensafely-smoking-clear.csv",
    system="ctv3",
    column="CTV3Code",
    category_column="Category",
)

smoking_unclear = codelist_from_csv(
    "codelists/opensafely-smoking-unclear.csv",
    system="ctv3",
    column="CTV3Code",
    category_column="Category",
)

ami_snomed = codelist_from_csv(
    "user/elsie_horne/ami_snomed/36d11028.csv",
    system="snomed",
    column="code",
)

ami_icd10 = codelist_from_csv(
    "user/elsie_horne/ami_snomed/36d11028.csv",
    system="icd10",
    column="code",
)

artery_dissect_icd10 = codelist_from_csv(
    "user/elsie_horne/artery_dissect_icd10/20745ce9.csv",
    system="icd10",
    column="code",
)

bmi_obesity_snomed = codelist_from_csv(
    "user/elsie_horne/bmi_obesity_snomed/0764e9b4.csv",
    system="snomed",
    column="code",
)

bmi_obesity_icd10 = codelist_from_csv(
    "user/elsie_horne/bmi_obesity_icd10/6e55767e.csv",
    system="icd10",
    column="code",
)

cancer_snomed = codelist_from_csv(
    "user/elsie_horne/cancer_snomed/23271cdf.csv",
    system="snomed",
    column="code",
)

cancer_icd10 = codelist_from_csv(
    "user/elsie_horne/cancer_icd10/55460349.csv",
    system="icd10",
    column="code",
)
cardiomyopathy_snomed = codelist_from_csv(
    "user/elsie_horne/cardiomyopathy_snomed/0a17a9aa.csv",
    system="snomed",
    column="code",
)

cardiomyopathy_icd10 = codelist_from_csv(
    "user/elsie_horne/cardiomyopathy_icd10/71083674.csv",
    system="icd10",
    column="code",
)