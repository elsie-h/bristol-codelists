library(tidyverse)
library(googlesheets4)

codelists <- read_sheet("https://docs.google.com/spreadsheets/d/1-ZZk_UnFnnrgWVg_n1GV1orWPyX_zwgFtskioDWUQ-w/edit#gid=57957362",
                        sheet = "codelist")

# code column as list because of different cell types in googlesheet
# unlist to convert all to character
# do not specify character in "col_types" arg of "read_sheet" due to handling of scientific notation
codelists$code <- unlist(codelists$code)

# name and terminology columns in lowercase
codelists <- codelists %>%
  mutate(across(c(name, terminology), tolower))

# sort by name, terminology, code
codelists <- codelists %>%
  arrange(name, terminology, code)

# view distinct names
codelists %>%
  distinct(name) %>%
  unlist() %>% unname()

# cleaning
codelists <- codelists %>%
  # sort out covariate_only names and add terminology as suffix
  mutate(across(name,
                # ami_covariate only seems to refer to prior ami
                ~ case_when(. %in% "ami_covariate_only" 
                            ~ "ami_prior",
                            # all the rest seem to just differ by terminology, which will be added as a suffix anyway
                            . %in% c("dvt_icvt_covariate_only", 
                                     "pe_covariate_only",
                                     "stroke_sah_hs_covariate_only",
                                     "tcp_covariate_only",
                                     "vt_covariate_only") 
                            ~ str_remove(., "_covariate_only"),
                            TRUE ~ .))) %>%
  mutate(across(terminology, 
                ~ case_when(. %in% "ctv3_snomedmapped" ~ "snomed",
                            TRUE ~ .))) %>%
  # add terminology as suffix
  mutate(across(name,
                ~ str_c(., terminology, sep = '_'))) %>%
  # remove "." from codes for upload to OpenSAFELY
  mutate(across(code, 
                ~ str_remove(., "\\.")))

# write all codes for each distinct name to a csv file for upload to OpendSAFELY
for (i in distinct(codelists, name)$name) {
  codelists %>%
    filter(name %in% i) %>%
    select(code) %>%
    write_csv(file = file.path("~", "OneDrive - University of Bristol", "codelists", "lists", str_c(i, ".csv")),
              append = FALSE,
              col_names = FALSE)
}
