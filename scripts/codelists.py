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
    "user/elsie_horne/ami_snomed/4f19cfce.csv",
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

ckd_snomed = codelist_from_csv(
    "user/elsie_horne/ckd_snomed/25d9dcd5.csv",
    system="snomed",
    column="code",
)

ckd_icd10 = codelist_from_csv(
    "user/elsie_horne/ckd_icd10/0cca69a0.csv",
    system="icd10",
    column="code",
)

copd_snomed = codelist_from_csv(
    "user/elsie_horne/copd_snomed/419c1000.csv",
    system="snomed",
    column="code",
)

copd_icd10 = codelist_from_csv(
    "user/elsie_horne/copd_icd10/5aab8335.csv",
    system="icd10",
    column="code",
)

dementia_snomed = codelist_from_csv(
    "user/elsie_horne/dementia_snomed/7bd3364ccsv",
    system="snomed",
    column="code",
)

dementia_icd10 = codelist_from_csv(
    "user/elsie_horne/dementia_icd10/2df21cb7.csv",
    system="icd10",
    column="code",
)

dic_icd10 = codelist_from_csv(
    "user/elsie_horne/dic_icd10/62c3c317.csv",
    system="icd10",
    column="code",
)

dvt_dvt_icd10 = codelist_from_csv(
    "user/elsie_horne/dvt_dvt_icd10/49b44fe2.csv",
    system="icd10",
    column="code",
)

dvt_icvt_icd10 = codelist_from_csv(
    "user/elsie_horne/dvt_icvt_icd10/30a4dcad.csv",
    system="icd10",
    column="code",
)

dvt_icvt_snomed = codelist_from_csv(
    "user/elsie_horne/dvt_icvt_snomed/7e85f642.csv",
    system="snomed",
    column="code",
)

dvt_pregnancy_icd10 = codelist_from_csv(
    "user/elsie_horne/dvt_pregnancy_icd10/6576830d.csv",
    system="icd10",
    column="code",
)

hf_snomed = codelist_from_csv(
    "user/elsie_horne/hf_snomed/33579ca3.csv",
    system="snomed",
    column="code",
)

hf_icd10 = codelist_from_csv(
    "user/elsie_horne/hf_icd10/4c670fd8.csv",
    system="icd10",
    column="code",
)
