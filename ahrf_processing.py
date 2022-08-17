import ahrf
class_data = ahrf.Dataset('AHRF_2020-2021_SAS/AHRF2021.sas7bdat')
class_data.dataset()

class_data.apply_dtype_organizer()
class_data.apply_string_cleaner()
class_data.rename_geo()

# # Uncomment for non-code column names
# class_data.load_all_names()

class_data.export('ahrf_cleaned.csv')