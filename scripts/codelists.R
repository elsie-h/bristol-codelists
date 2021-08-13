library(tidyverse)
library(googlesheets4)

codelists <- read_sheet("https://docs.google.com/spreadsheets/d/1-ZZk_UnFnnrgWVg_n1GV1orWPyX_zwgFtskioDWUQ-w/edit#gid=57957362",
                        sheet = "codelist")

# code column as list because of different cell types in googlesheet
# unlist to convert all to character
# do not specify character in "col_types" arg of "read_sheet" due to handling of scientific notation
codelists$code <- unlist(codelists$code)


codelists <- codelists %>%
  mutate_at('name', 'terminology', tolower)



codelist %>% filter(name %in% 'cancer', terminology %in% 'SNOMED') %>% View()

codelist %>% filter(str_detect(code, '\\.')) %>% distinct(terminology)
