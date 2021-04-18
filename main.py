import lib.my_calendar_v2 as cal_v2


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
    path_Athens_2020 = 'data/temperatures_dataset/Athens2020_from_8_to_11.csv'
    path_Brest_2020 = 'data/temperatures_dataset/Brest2020_from_8_to_11.csv'
    path_Madrid_2020 = 'data/temperatures_dataset/Madrid2020_from_8_to_11.csv'
    path_Vienna_2020 = 'data/temperatures_dataset/Vienna2020_from_8_to_11.csv'

    list_Athens_2020 = cal_v2.read_csv(path_Athens_2020)
    list_Brest_2020 = cal_v2.read_csv(path_Brest_2020)
    list_Madrid_2020 = cal_v2.read_csv(path_Madrid_2020)
    list_Vienna_2020 = cal_v2.read_csv(path_Vienna_2020)

    # Calendar Creation for the year of 2020 and add default event values
    temp_cal_2020 = cal_v2.MyCalendar(list_of_years=[2020], is_time=True, date_format=cal_v2.MM_DD_YYYY,
                                      date_delimiter=cal_v2.del_slash, time_format=cal_v2.HH_MM,
                                      time_delimiter=cal_v2.del_colon, hour_start=0, hour_end=24, hour_step=1,
                                      minute_start=0, minute_end=60, minute_step=0)

    # Change the Brest_2020 date format to be the same as calendar's.
    list_Brest_2020 = cal_v2.change_date_format_in_list(list_event=list_Brest_2020,
                                                        date_index=0,
                                                        date_format_from=cal_v2.MM_DD_YY,
                                                        date_format_to=cal_v2.MM_DD_YYYY,
                                                        date_delimiter_from=cal_v2.del_slash,
                                                        date_delimiter_to=cal_v2.del_slash,
                                                        century=21)

    temp_cal_2020.add_list_key_event_to_calendar(list_key_event=dataset_event_names, list_of_headers=final_csv_header)
    temp_cal_2020.add_events_to_calendar(list_of_events=list_Athens_2020, date_index=0, time_index=1,
                                         first_row_header=False, list_of_headers=Athens_csv_header, event_index=0,
                                         input_event_name=dataset_event_names[0])  # 1
    temp_cal_2020.add_events_to_calendar(list_of_events=list_Brest_2020, date_index=0, time_index=1,
                                         first_row_header=False, list_of_headers=Brest_csv_header, event_index=0,
                                         input_event_name=dataset_event_names[0])  # 2
    temp_cal_2020.add_events_to_calendar(list_of_events=list_Madrid_2020, date_index=0, time_index=1,
                                         first_row_header=False, list_of_headers=Madrid_csv_header, event_index=0,
                                         input_event_name=dataset_event_names[0])  # 3
    temp_cal_2020.add_events_to_calendar(list_of_events=list_Vienna_2020, date_index=0, time_index=1,
                                         first_row_header=False, list_of_headers=Vienna_csv_header, event_index=0,
                                         input_event_name=dataset_event_names[0])  # 4
    # temp_cal_2020.print()
    list_temperatures = temp_cal_2020.dict_to_list(['07/31/2020', '11/30/2020'])
    cal_v2.write_csv(csv_path="export_folder/temperatures_2020.csv",
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

    # covid_calendar.print(1)


test_temperature_dataset()
# test_covid_dataset()
