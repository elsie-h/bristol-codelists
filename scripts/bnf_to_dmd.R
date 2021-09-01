library(tidyverse)
library(readr)

setwd(file.path("~", "OneDrive - University of Bristol", "codelists"))

codelists <- list.files(path = file.path("lists"))

codelists_meds <- codelists[str_detect(codelists, "bnf|dmd")]

# "anticoagulant_bnf.csv"  
read_csv("~/OneDrive - University of Bristol/codelists/lists/elsie_horne-anticoagulant-4a7b0371-dmd.csv") %>%
  transmute(dmd_id = as.character(dmd_id)) %>%
  write_csv(file = file.path("lists", "anticoagulant_dmd.csv"))

# "antiplatelet_bnf.csv"       
read_csv("~/OneDrive - University of Bristol/codelists/lists/elsie_horne-antiplatelet-316b903c-dmd.csv") %>%
  transmute(dmd_id = as.character(dmd_id)) %>%
  write_csv(file = file.path("lists", "antiplatelet_dmd.csv"))

# "bp_lowering_bnf.csv"
read_csv("~/OneDrive - University of Bristol/codelists/lists/elsie_horne-bp_lowering-4d2dc367-dmd.csv") %>%
  transmute(dmd_id = as.character(dmd_id)) %>%
  write_csv(file = file.path("lists", "bp_lowering_dmd.csv"))

# "cocp_bnf.csv"
read_csv("~/OneDrive - University of Bristol/codelists/lists/elsie_horne-cocp-185c1d07-dmd.csv") %>%
  transmute(dmd_id = as.character(dmd_id)) %>%
  write_csv(file = file.path("lists", "cocp_dmd.csv"))

# "diabetes_drugs_dmd.csv"
read_csv("~/OneDrive - University of Bristol/codelists/lists/diabetes_drugs_dmd.csv", col_names = FALSE) %>%
  transmute(dmd_id = as.character(X1)) %>%
  write_csv(file = file.path("lists", "diabetes_drugs_dmd.csv"))

# "hrt_bnf.csv"
read_csv("~/OneDrive - University of Bristol/codelists/lists/elsie_horne-hrt-7f4ca9d1-dmd.csv") %>%
  transmute(dmd_id = as.character(dmd_id)) %>%
  write_csv(file = file.path("lists", "hrt_dmd.csv"))

# "hypertension_drugs_dmd.csv" 
read_csv("~/OneDrive - University of Bristol/codelists/lists/hypertension_drugs_dmd.csv", col_names = FALSE) %>%
  transmute(dmd_id = as.character(X1)) %>%
  write_csv(file = file.path("lists", "hypertension_drugs_dmd.csv"))

# "lipid_lowering_bnf.csv"   
read_csv("~/OneDrive - University of Bristol/codelists/lists/elsie_horne-lipid_lowering-341e5032-dmd.csv") %>%
  transmute(dmd_id = as.character(dmd_id)) %>%
  write_csv(file = file.path("lists", "lipid_lowering_dmd.csv"))

# names of opensafely lists to copy and paste
codelists_os <- list.files(path = file.path("lists"))
codelists_os[str_detect(codelists_os, "elsie_horne")]