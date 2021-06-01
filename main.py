import lib.my_calendar_v2 as cal_v2
import pandas as pd


def test_temperature_dataset():
    # Common To Both Years
    # Create the output CSV information
    final_csv_header = ['Date', 'Time', 'Athens_Temp', 'Brest_Temp', 'Madrid_Temp', 'Vienna_Temp']
    Athens_csv_header = ['Date', 'Time', 'Athens_Temp']
    Brest_csv_header = ['Date', 'Time', 'Brest_Temp']
    Madrid_csv_header = ['Date', 'Time', 'Madrid_Temp']
    Vienna_csv_header = ['Date', 'Time', 'Vienna_Temp']
    dataset_event_names = ['Temperature']

    # Read the temperatures_data
    path_Athens = 'data/temperatures_dataset/Current/Athens2021_from_1_to_4.csv'
    path_Brest = 'data/temperatures_dataset/Current/Brest2021_from_1_to_4.csv'
    path_Madrid = 'data/temperatures_dataset/Current/Madrid2021_from_1_to_4.csv'
    path_Vienna = 'data/temperatures_dataset/Current/Vienna2021_from_1_to_4.csv'

    list_Athens = cal_v2.read_csv(path_Athens)
    list_Brest = cal_v2.read_csv(path_Brest)
    list_Madrid = cal_v2.read_csv(path_Madrid)
    list_Vienna = cal_v2.read_csv(path_Vienna)

    # Calendar Creation for the year of 2020 and add default event values
    temp_cal = cal_v2.MyCalendar(list_of_years=[2020, 2021], is_time=True, date_format=cal_v2.MM_DD_YYYY,
                                 date_delimiter=cal_v2.del_slash, time_format=cal_v2.HH_MM,
                                 time_delimiter=cal_v2.del_colon, hour_start=0, hour_end=24, hour_step=1,
                                 minute_start=0, minute_end=60, minute_step=0)

    # Change the Athens_2020 date format to be the same as calendar's.
    list_Athens = cal_v2.change_date_format_in_list(list_event=list_Athens,
                                                    date_index=0,
                                                    date_format_from=cal_v2.MM_DD_YYYY,
                                                    date_format_to=cal_v2.MM_DD_YYYY,
                                                    date_delimiter_from=cal_v2.del_slash,
                                                    date_delimiter_to=cal_v2.del_slash,
                                                    century=21)

    # Change the Brest_2020 date format to be the same as calendar's.
    list_Brest = cal_v2.change_date_format_in_list(list_event=list_Brest,
                                                   date_index=0,
                                                   date_format_from=cal_v2.MM_DD_YYYY,
                                                   date_format_to=cal_v2.MM_DD_YYYY,
                                                   date_delimiter_from=cal_v2.del_slash,
                                                   date_delimiter_to=cal_v2.del_slash,
                                                   century=21)

    # Change the Madrid_2020 date format to be the same as calendar's.
    list_Madrid = cal_v2.change_date_format_in_list(list_event=list_Madrid,
                                                    date_index=0,
                                                    date_format_from=cal_v2.MM_DD_YYYY,
                                                    date_format_to=cal_v2.MM_DD_YYYY,
                                                    date_delimiter_from=cal_v2.del_slash,
                                                    date_delimiter_to=cal_v2.del_slash,
                                                    century=21)

    # Change the Madrid_2020 date format to be the same as calendar's.
    list_Vienna = cal_v2.change_date_format_in_list(list_event=list_Vienna,
                                                    date_index=0,
                                                    date_format_from=cal_v2.MM_DD_YYYY,
                                                    date_format_to=cal_v2.MM_DD_YYYY,
                                                    date_delimiter_from=cal_v2.del_slash,
                                                    date_delimiter_to=cal_v2.del_slash,
                                                    century=21)

    temp_cal.add_list_key_event_to_calendar(list_key_event=dataset_event_names, list_of_headers=final_csv_header)
    temp_cal.add_events_to_calendar(list_of_events=list_Athens, date_index=0, time_index=1,
                                    first_row_header=False, list_of_headers=Athens_csv_header, event_index=0,
                                    input_event_name=dataset_event_names[0])  # 1
    temp_cal.add_events_to_calendar(list_of_events=list_Brest, date_index=0, time_index=1,
                                    first_row_header=False, list_of_headers=Brest_csv_header, event_index=0,
                                    input_event_name=dataset_event_names[0])  # 2
    temp_cal.add_events_to_calendar(list_of_events=list_Madrid, date_index=0, time_index=1,
                                    first_row_header=False, list_of_headers=Madrid_csv_header, event_index=0,
                                    input_event_name=dataset_event_names[0])  # 3
    temp_cal.add_events_to_calendar(list_of_events=list_Vienna, date_index=0, time_index=1,
                                    first_row_header=False, list_of_headers=Vienna_csv_header, event_index=0,
                                    input_event_name=dataset_event_names[0])  # 4
    # temp_cal_2020.print()
    list_temperatures = temp_cal.dict_to_list(['01/01/2021', '30/04/2021'])
    list_temperatures = pd.DataFrame(list_temperatures)
    # list_temperatures = list_temperatures.T
    list_temperatures.fillna(method='bfill', inplace=True)
    list_temperatures.fillna(method='ffill', inplace=True)
    # list_temperatures = list_temperatures.T
    list_temperatures = list_temperatures.values.tolist()
    # print(list_temperatures)

    cal_v2.write_csv(csv_path="export_folder/temperatures_2021.csv",
                     list_write=list_temperatures, delimiter=cal_v2.del_comma)

def test_covid_dataset():
    str_changes_visitors_path = 'data/covid_dataset/changes-visitors-covid.csv'
    str_covid_19_testing_policy_path = 'data/covid_dataset/covid-19-testing-policy.csv'
    str_covid_contact_tracing_path = 'data/covid_dataset/covid-contact-tracing.csv'
    str_covid_containment_and_health_index_path = 'data/covid_dataset/covid-containment-and-health-index.csv'
    str_covid_stringency_index_path = 'data/covid_dataset/covid-stringency-index.csv'
    str_covid_vaccination_policy_path = 'data/covid_dataset/covid-vaccination-policy.csv'
    str_dept_relief_path = 'data/covid_dataset/debt-relief-covid.csv'
    str_face_covering_policies_path = 'data/covid_dataset/face-covering-policies-covid.csv'
    str_income_support_path = 'data/covid_dataset/income-support-covid.csv'
    str_internal_movement_path = 'data/covid_dataset/internal-movement-covid.csv'
    str_international_travel_path = 'data/covid_dataset/international-travel-covid.csv'
    str_owed_covid_data_path = 'data/covid_dataset/owid-covid-data.csv'
    str_public_campaigns_path = 'data/covid_dataset/public-campaigns-covid.csv'
    str_public_events_path = 'data/covid_dataset/public-events-covid.csv'
    str_public_gathering_rules_path = 'data/covid_dataset/public-gathering-rules-covid.csv'
    str_public_transport_path = 'data/covid_dataset/public-transport-covid.csv'
    str_school_closure_path = 'data/covid_dataset/school-closures-covid.csv'
    str_stay_at_home_path = 'data/covid_dataset/stay-at-home-covid.csv'
    str_workplace_closures_path = 'data/covid_dataset/workplace-closures-covid.csv'

    list_changes_visitors_csv = cal_v2.read_csv(csv_path=str_changes_visitors_path, delimiter=cal_v2.del_comma)
    list_covid_19_testing_policy_csv = cal_v2.read_csv(csv_path=str_covid_19_testing_policy_path,
                                                       delimiter=cal_v2.del_comma)
    list_covid_contact_tracing_csv = cal_v2.read_csv(csv_path=str_covid_contact_tracing_path,
                                                     delimiter=cal_v2.del_comma)
    list_covid_containment_and_health_index_csv = cal_v2.read_csv(csv_path=str_covid_containment_and_health_index_path,
                                                                  delimiter=cal_v2.del_comma)
    list_covid_stringency_index_csv = cal_v2.read_csv(csv_path=str_covid_stringency_index_path,
                                                      delimiter=cal_v2.del_comma)
    list_covid_vaccination_policy_csv = cal_v2.read_csv(csv_path=str_covid_vaccination_policy_path,
                                                        delimiter=cal_v2.del_comma)
    list_dept_relief_csv = cal_v2.read_csv(csv_path=str_dept_relief_path, delimiter=cal_v2.del_comma)
    list_face_covering_policies_csv = cal_v2.read_csv(csv_path=str_face_covering_policies_path,
                                                      delimiter=cal_v2.del_comma)
    list_income_support_csv = cal_v2.read_csv(csv_path=str_income_support_path, delimiter=cal_v2.del_comma)
    list_internal_movement_csv = cal_v2.read_csv(csv_path=str_internal_movement_path, delimiter=cal_v2.del_comma)
    list_international_travel_csv = cal_v2.read_csv(csv_path=str_international_travel_path, delimiter=cal_v2.del_comma)
    list_owed_covid_data_csv = cal_v2.read_csv(csv_path=str_owed_covid_data_path, delimiter=cal_v2.del_comma)
    list_public_campaigns_csv = cal_v2.read_csv(csv_path=str_public_campaigns_path, delimiter=cal_v2.del_comma)
    list_public_events_csv = cal_v2.read_csv(csv_path=str_public_events_path, delimiter=cal_v2.del_comma)
    list_public_gathering_rules_csv = cal_v2.read_csv(csv_path=str_public_gathering_rules_path,
                                                      delimiter=cal_v2.del_comma)
    list_public_transport_csv = cal_v2.read_csv(csv_path=str_public_transport_path, delimiter=cal_v2.del_comma)
    list_school_closure_csv = cal_v2.read_csv(csv_path=str_school_closure_path, delimiter=cal_v2.del_comma)
    list_stay_at_home_csv = cal_v2.read_csv(csv_path=str_stay_at_home_path, delimiter=cal_v2.del_comma)
    list_workplace_closures_csv = cal_v2.read_csv(csv_path=str_workplace_closures_path, delimiter=cal_v2.del_comma)

    list_countries = []
    dict_of_event_type = []

    def set_list_countries(list_input, country_index):
        for event_name in list_input[0]:
            if event_name not in dict_of_event_type:
                dict_of_event_type.append(event_name)
        for i in range(1, len(list_input)):
            if list_input[i][country_index] not in list_countries:
                list_countries.append(list_input[i][country_index])
                # print(list_input[i][country_index])

    set_list_countries(list_changes_visitors_csv, 0)  # 1
    set_list_countries(list_covid_19_testing_policy_csv, 0)  # 2
    set_list_countries(list_covid_contact_tracing_csv, 0)  # 3
    set_list_countries(list_covid_containment_and_health_index_csv, 0)  # 4
    set_list_countries(list_covid_stringency_index_csv, 0)  # 5
    set_list_countries(list_covid_vaccination_policy_csv, 0)  # 6
    set_list_countries(list_dept_relief_csv, 0)  # 7
    set_list_countries(list_face_covering_policies_csv, 0)  # 8
    set_list_countries(list_income_support_csv, 0)  # 9
    set_list_countries(list_internal_movement_csv, 0)  # 10
    set_list_countries(list_international_travel_csv, 0)  # 11
    set_list_countries(list_owed_covid_data_csv, 2)  # 12
    set_list_countries(list_public_campaigns_csv, 0)  # 13
    set_list_countries(list_public_events_csv, 0)  # 14
    set_list_countries(list_public_gathering_rules_csv, 0)  # 15
    set_list_countries(list_public_transport_csv, 0)  # 16
    set_list_countries(list_school_closure_csv, 0)  # 17
    set_list_countries(list_stay_at_home_csv, 0)  # 18
    set_list_countries(list_workplace_closures_csv, 0)  # 19
    list_countries.sort()

    # print(dict_of_event_type)

    covid_calendar = cal_v2.MyCalendar(list_of_years=[2020, 2021], is_time=False, date_format=cal_v2.YYYY_MM_DD,
                                       date_delimiter=cal_v2.del_dash, time_format=cal_v2.HH_MM,
                                       time_delimiter=cal_v2.del_colon, hour_start=0, hour_end=24, hour_step=1,
                                       minute_start=0, minute_end=60, minute_step=0)
    covid_calendar.add_list_key_event_to_calendar(list_key_event=list_countries)

    covid_calendar.add_list_key_event_to_calendar(list_key_event=list_countries, list_of_headers=dict_of_event_type)

    covid_calendar.add_events_to_calendar(list_of_events=list_changes_visitors_csv, date_index=2, time_index=None,
                                          first_row_header=True, list_of_headers=None, event_index=0)  # 1
    covid_calendar.add_events_to_calendar(list_of_events=list_covid_19_testing_policy_csv, date_index=2,
                                          time_index=None,
                                          first_row_header=True, list_of_headers=None, event_index=0)  # 2
    covid_calendar.add_events_to_calendar(list_of_events=list_covid_contact_tracing_csv, date_index=2, time_index=None,
                                          first_row_header=True, list_of_headers=None, event_index=0)  # 3
    covid_calendar.add_events_to_calendar(list_of_events=list_covid_containment_and_health_index_csv, date_index=2,
                                          time_index=None, first_row_header=True, list_of_headers=None,
                                          event_index=0)  # 4
    covid_calendar.add_events_to_calendar(list_of_events=list_covid_stringency_index_csv, date_index=2,
                                          time_index=None, first_row_header=True, list_of_headers=None,
                                          event_index=0)  # 5
    covid_calendar.add_events_to_calendar(list_of_events=list_covid_vaccination_policy_csv, date_index=2,
                                          time_index=None, first_row_header=True, list_of_headers=None,
                                          event_index=0)  # 6
    covid_calendar.add_events_to_calendar(list_of_events=list_dept_relief_csv, date_index=2,
                                          time_index=None, first_row_header=True, list_of_headers=None,
                                          event_index=0)  # 7
    covid_calendar.add_events_to_calendar(list_of_events=list_face_covering_policies_csv, date_index=2,
                                          time_index=None, first_row_header=True, list_of_headers=None,
                                          event_index=0)  # 8
    covid_calendar.add_events_to_calendar(list_of_events=list_income_support_csv, date_index=2,
                                          time_index=None, first_row_header=True, list_of_headers=None,
                                          event_index=0)  # 9
    covid_calendar.add_events_to_calendar(list_of_events=list_internal_movement_csv, date_index=2,
                                          time_index=None, first_row_header=True, list_of_headers=None,
                                          event_index=0)  # 10
    covid_calendar.add_events_to_calendar(list_of_events=list_international_travel_csv, date_index=2,
                                          time_index=None, first_row_header=True, list_of_headers=None,
                                          event_index=0)  # 11
    covid_calendar.add_events_to_calendar(list_of_events=list_owed_covid_data_csv, date_index=3,
                                          time_index=None, first_row_header=True, list_of_headers=None,
                                          event_index=2)  # 12
    covid_calendar.add_events_to_calendar(list_of_events=list_public_campaigns_csv, date_index=2,
                                          time_index=None, first_row_header=True, list_of_headers=None,
                                          event_index=0)  # 13
    covid_calendar.add_events_to_calendar(list_of_events=list_public_events_csv, date_index=2,
                                          time_index=None, first_row_header=True, list_of_headers=None,
                                          event_index=0)  # 14
    covid_calendar.add_events_to_calendar(list_of_events=list_public_gathering_rules_csv, date_index=2,
                                          time_index=None, first_row_header=True, list_of_headers=None,
                                          event_index=0)  # 15
    covid_calendar.add_events_to_calendar(list_of_events=list_public_transport_csv, date_index=2,
                                          time_index=None, first_row_header=True, list_of_headers=None,
                                          event_index=0)  # 16
    covid_calendar.add_events_to_calendar(list_of_events=list_school_closure_csv, date_index=2,
                                          time_index=None, first_row_header=True, list_of_headers=None,
                                          event_index=0)  # 17
    covid_calendar.add_events_to_calendar(list_of_events=list_stay_at_home_csv, date_index=2,
                                          time_index=None, first_row_header=True, list_of_headers=None,
                                          event_index=0)  # 18
    covid_calendar.add_events_to_calendar(list_of_events=list_workplace_closures_csv, date_index=2,
                                          time_index=None, first_row_header=True, list_of_headers=None,
                                          event_index=0)  # 19
    list_calendar = covid_calendar.dict_to_list(date_range=['2020-01-01', '2021-01-08'])
    cal_v2.write_csv(csv_path="export_folder/covid_measures.csv", list_write=list_calendar, delimiter=cal_v2.del_comma)


def test_covid_dataset_2021():
    str_covid_dt_2021_00_covid_stringency_index_path = 'data/covid_dataset_2021/00_covid-stringency-index.csv'
    str_covid_dt_2021_01_school_closures_path = 'data/covid_dataset_2021/01_school-closures-covid.csv'
    str_covid_dt_2021_02_workplace_closures_path = 'data/covid_dataset_2021/02_workplace-closures-covid.csv'
    str_covid_dt_2021_03_public_events_path = 'data/covid_dataset_2021/03_public-events-covid.csv'
    str_covid_dt_2021_04_public_gathering_rules_path = 'data/covid_dataset_2021/04_public-gathering-rules-covid.csv'
    str_covid_dt_2021_05_stay_at_home_path = 'data/covid_dataset_2021/05_stay-at-home-covid.csv'
    str_covid_dt_2021_06_international_travel_path = 'data/covid_dataset_2021/06_international-travel-covid.csv'
    str_covid_dt_2021_07_internal_movement_path = 'data/covid_dataset_2021/07_internal-movement-covid.csv'
    str_covid_dt_2021_08_public_transport_path = 'data/covid_dataset_2021/08_public-transport-covid.csv'
    str_covid_dt_2021_09_international_travel_path = 'data/covid_dataset_2021/09_international-travel-covid.csv'
    str_covid_dt_2021_10_owid_covid_path = 'data/covid_dataset_2021/10_owid-covid-data.csv'

    list_covid_dt_2021_00 = cal_v2.read_csv(csv_path=str_covid_dt_2021_00_covid_stringency_index_path,
                                            delimiter=cal_v2.del_comma)
    list_covid_dt_2021_01 = cal_v2.read_csv(csv_path=str_covid_dt_2021_01_school_closures_path,
                                            delimiter=cal_v2.del_comma)
    list_covid_dt_2021_02 = cal_v2.read_csv(csv_path=str_covid_dt_2021_02_workplace_closures_path,
                                            delimiter=cal_v2.del_comma)
    list_covid_dt_2021_03 = cal_v2.read_csv(csv_path=str_covid_dt_2021_03_public_events_path,
                                            delimiter=cal_v2.del_comma)
    list_covid_dt_2021_04 = cal_v2.read_csv(csv_path=str_covid_dt_2021_04_public_gathering_rules_path,
                                            delimiter=cal_v2.del_comma)
    list_covid_dt_2021_05 = cal_v2.read_csv(csv_path=str_covid_dt_2021_05_stay_at_home_path,
                                            delimiter=cal_v2.del_comma)
    list_covid_dt_2021_06 = cal_v2.read_csv(csv_path=str_covid_dt_2021_06_international_travel_path,
                                            delimiter=cal_v2.del_comma)
    list_covid_dt_2021_07 = cal_v2.read_csv(csv_path=str_covid_dt_2021_07_internal_movement_path,
                                            delimiter=cal_v2.del_comma)
    list_covid_dt_2021_08 = cal_v2.read_csv(csv_path=str_covid_dt_2021_08_public_transport_path,
                                            delimiter=cal_v2.del_comma)
    list_covid_dt_2021_09 = cal_v2.read_csv(csv_path=str_covid_dt_2021_09_international_travel_path,
                                            delimiter=cal_v2.del_comma)
    list_covid_dt_2021_10 = cal_v2.read_csv(csv_path=str_covid_dt_2021_10_owid_covid_path,
                                            delimiter=cal_v2.del_comma)

    # print(list_covid_dt_2021_10)

    list_countries = []
    dict_of_event_type = []

    def set_list_countries(list_input, country_index=0):
        for event_name in list_input[0]:
            if event_name not in dict_of_event_type:
                dict_of_event_type.append(event_name)
        for i in range(1, len(list_input)):
            if list_input[i][country_index] not in list_countries:
                list_countries.append(list_input[i][country_index])
                # print(list_input[i][country_index])

    set_list_countries(list_covid_dt_2021_00)
    set_list_countries(list_covid_dt_2021_01)
    set_list_countries(list_covid_dt_2021_02)
    set_list_countries(list_covid_dt_2021_03)
    set_list_countries(list_covid_dt_2021_04)
    set_list_countries(list_covid_dt_2021_05)
    set_list_countries(list_covid_dt_2021_06)
    set_list_countries(list_covid_dt_2021_07)
    set_list_countries(list_covid_dt_2021_08)
    set_list_countries(list_covid_dt_2021_09)
    set_list_countries(list_covid_dt_2021_10)
    list_countries.sort()

    # print(list_countries.__len__())
    # print(dict_of_event_type)

    covid_calendar = cal_v2.MyCalendar(list_of_years=[2020, 2021], is_time=False, date_format=cal_v2.YYYY_MM_DD,
                                       date_delimiter=cal_v2.del_dash, time_format=cal_v2.HH_MM,
                                       time_delimiter=cal_v2.del_colon, hour_start=0, hour_end=0, hour_step=1,
                                       minute_start=0, minute_end=0, minute_step=0)
    covid_calendar.add_list_key_event_to_calendar(list_key_event=list_countries)
    covid_calendar.add_list_key_event_to_calendar(list_key_event=list_countries, list_of_headers=dict_of_event_type)

    covid_calendar.add_events_to_calendar(list_of_events=list_covid_dt_2021_00, date_index=2,
                                          time_index=None,
                                          first_row_header=True, list_of_headers=None, event_index=0)
    covid_calendar.add_events_to_calendar(list_of_events=list_covid_dt_2021_01, date_index=2,
                                          time_index=None,
                                          first_row_header=True, list_of_headers=None, event_index=0)
    covid_calendar.add_events_to_calendar(list_of_events=list_covid_dt_2021_02, date_index=2,
                                          time_index=None,
                                          first_row_header=True, list_of_headers=None, event_index=0)
    covid_calendar.add_events_to_calendar(list_of_events=list_covid_dt_2021_03, date_index=2,
                                          time_index=None,
                                          first_row_header=True, list_of_headers=None, event_index=0)
    covid_calendar.add_events_to_calendar(list_of_events=list_covid_dt_2021_04, date_index=2,
                                          time_index=None,
                                          first_row_header=True, list_of_headers=None, event_index=0)
    covid_calendar.add_events_to_calendar(list_of_events=list_covid_dt_2021_05, date_index=2,
                                          time_index=None,
                                          first_row_header=True, list_of_headers=None, event_index=0)
    covid_calendar.add_events_to_calendar(list_of_events=list_covid_dt_2021_06, date_index=2,
                                          time_index=None,
                                          first_row_header=True, list_of_headers=None, event_index=0)
    covid_calendar.add_events_to_calendar(list_of_events=list_covid_dt_2021_07, date_index=2,
                                          time_index=None,
                                          first_row_header=True, list_of_headers=None, event_index=0)
    covid_calendar.add_events_to_calendar(list_of_events=list_covid_dt_2021_08, date_index=2,
                                          time_index=None,
                                          first_row_header=True, list_of_headers=None, event_index=0)
    covid_calendar.add_events_to_calendar(list_of_events=list_covid_dt_2021_09, date_index=2,
                                          time_index=None,
                                          first_row_header=True, list_of_headers=None, event_index=0)
    covid_calendar.add_events_to_calendar(list_of_events=list_covid_dt_2021_10, date_index=2,
                                          time_index=None,
                                          first_row_header=True, list_of_headers=None, event_index=0)

    list_calendar = covid_calendar.dict_to_list(date_range=['2020-04-01', '2020-11-30'])
    cal_v2.write_csv(csv_path="export_folder/covid_measures_2020_April_to_November.csv",
                     list_write=list_calendar, delimiter=cal_v2.del_comma)

    list_calendar = covid_calendar.dict_to_list(date_range=['2020-01-01', '2020-05-23'])
    cal_v2.write_csv(csv_path="export_folder/covid_measures_2021.csv",
                     list_write=list_calendar, delimiter=cal_v2.del_comma)

    # covid_calendar.print()


# test_temperature_dataset()
# test_covid_dataset()
test_covid_dataset_2021()
