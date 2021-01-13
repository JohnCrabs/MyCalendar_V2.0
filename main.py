import lib.my_calendar_v2 as cal_v2

start_year = 1990
years = []
for i in range(0, 15):
    years.append(start_year+i)

cal_v2_test = cal_v2.MyCalendar(list_of_years=years,
                                is_time=False,
                                date_format=cal_v2.DD_MM_YYYY,
                                date_delimeter=cal_v2.del_slash,
                                time_format=cal_v2.HH_MM,
                                time_delimeter=cal_v2.del_colon,
                                hour_start=0,
                                hour_end=24,
                                hour_step=1,
                                minute_start=0,
                                minute_end=60,
                                minute_step=0)

cal_v2_test.create()
cal_v2_test.print()