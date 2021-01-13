"""
my_calendar_v2.py contains the Class My_Calendar, which creates a dictionary with events.

Calendar Structures:
1) Dict{Date_Format: {Time_Format: {Event: some_type_of_value}}}
2) Dict{Date_Format: {Event: some_type_of_value}}

"some_type_of_value" can be: int, float, double, str, list, dict, etc

Example 1: Let's say we need to add a temperature event, we can do it like this.
Dict{'08/01/2020': {'00:00': {'Athens': {Date: '08/01/2020', Time: '00:00', Temperature: '26.2',
                              'Brest': {Date: '08/01/2020', Time: '00:00', Temperature: '16.6'}}}}

Let's say we need to export it to excel:
1) Give date range for the exporting dates (e.g. start: 08/01/2020, end: 11/30/2020)
2) Give the format of the file (CSV of XLSX)
3) Create First Line ['Date', 'Time', 'Athens_Temperature', 'Brest_Temperature]
4) For each date in range export these value. If value does not exist print -9999.99
"""

import datetime as dt
import warnings

# Create lists that corresponds to date, time strings
# Create list for months
list_str_id_months_m = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
list_str_id_months_mm = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']

# Create list for days
list_str_id_single_days_m = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
                             '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24',
                             '25', '26', '27', '28', '29', '30', '31']
list_str_id_days_mm = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12',
                       '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24',
                       '25', '26', '27', '28', '29', '30', '31']

# Create list for hours
list_str_id_hours = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11',
                     '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']

# Create list for hours
list_str_id_minutes = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09',
                       '10', '11', '12', '13', '14', '15', '16', '17', '18', '19',
                       '20', '21', '22', '23', '24', '25', '26', '27', '28', '29',
                       '30', '31', '32', '33', '34', '35', '36', '37', '38', '39',
                       '40', '41', '42', '43', '44', '45', '46', '47', '48', '49',
                       '50', '51', '52', '53', '54', '55', '56', '57', '58', '59']

# Leap situations
list_int_month_days_not_leap = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
list_int_month_days_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Different systems to create a date
DD_MM_YYYY = 'ddmmyyyy'
DD_YYYY_MM = 'ddyyyymm'
MM_DD_YYYY = 'mmddyyyy'
MM_YYYY_DD = 'mmyyyydd'
YYYY_MM_DD = 'yyyymmdd'
YYYY_DD_MM = 'yyyyddmm'

D_M_YYYY = 'dmyyyy'
D_YYYY_M = 'dyyyym'
M_D_YYYY = 'mdyyyy'
M_YYYY_D = 'myyyyd'
YYYY_M_D = 'yyyymd'
YYYY_D_M = 'yyyydm'

DD_MM_YY = 'ddmmyy'
DD_YY_MM = 'ddyymm'
MM_DD_YY = 'mmddyy'
MM_YY_DD = 'mmyyydd'
YY_MM_DD = 'yymmdd'
YY_DD_MM = 'yyddmm'

D_M_YY = 'dmyy'
D_YY_M = 'dyym'
M_D_YY = 'mdyy'
M_YY_D = 'myyd'
YY_M_D = 'yymd'
YY_D_M = 'yydm'

# Different systems to create the hour
HH_MM = 'hhmm'
HH_MM_SS = 'hhmmss'

# Delimeters
del_comma = ','
del_hashtag = '#'
del_colon = ':'
del_semicolon = ';'
del_space = ' '
del_underscore = '_'
del_dash = '-'
del_slash = '/'

NaN = "nan"


def read_csv(csv_path: str, delimeter=del_comma):
    """
    A Function for reading CSV files.
    :param csv_path: The path for the csv to be imported.
    :param delimeter: The delimeter of values.
    :return: []
    """
    import csv  # import csv library
    list_tmp_csv = []  # create a temporary empty list
    with open(csv_path) as csv_file:  # open the csv path
        csv_reader = csv.reader(csv_file, delimiter=delimeter)
        for row in csv_reader:  # for each row in csv_reader file
            list_tmp_csv.append(row)   # append the row to list
    return list_tmp_csv  # return the list


def write_csv(csv_path: str, list_write: [], delimeter=del_comma):
    """
    A Function for writing CSV files.
    :param csv_path: The path for the csv to be exported.
    :param list_write: The list to be written in file
    :param delimeter: The delimeter for values
    :return: Nothing
    """
    import csv  # import csv library
    import os  # import os library
    if not os.path.exists(csv_path):  # Check if path does not exist
        warnings.warn("Path does not exist! Path will be created!")  # Warn in console
        directory = os.path.dirname(csv_path)  # Find the direcrories in the path
        os.mkdir(directory)  # Create the directories

    with open(csv_path, 'w', newline='') as csvfile:  # Open the path to write the file
        csv_writer = csv.writer(csvfile, delimiter=delimeter, quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in list_write:  # For each row
            csv_writer.writerow(row)  # Write row to file


class MyCalendar:
    def __init__(self, list_of_years: [] = None, is_time: bool = False, date_format=DD_MM_YYYY,
                 date_delimeter=del_slash):
        if list_of_years is None:  # if list_of_year is None
            list_of_years = [dt.datetime.now().year]  # create a list with only the current year
        self.list_of_years = list_of_years  # set the self.list_of_years
        self.is_time = is_time  # set the self.is_time
        self.list_of_is_leap = [self.isLeap(year) for year in list_of_years]  # set list_of_is_leap
        self.date_format = date_format  # set the date format
        self.date_delimeter = date_delimeter  # set the date delimeter
        self.list_timespamp = None  # set the list timestamp
        self.int_list_size = 0  # set the list size to 0
        self.dict_calendar = {}  # create the calendar

    @staticmethod
    def isLeap(year=dt.datetime.now().year):
        """
        :param year: The year we need to check
        :return: True/False
        """
        if year % 4 == 0:  # if is integer divisible by 4
            if year % 100 != 0 or year % 400 == 0:  # if is not integer divisible by 100 or is integer divisible by 400
                return True  # is leap
            else:
                return False  # is not leap
        else:
            return False  # is not leap

    @staticmethod
    def set_time(hour_start=0, hour_end=24, hour_step=1, minute_start=0, minute_end=60, minute_step=0):
        """
        :param hour_start: The starting hour. Range (0, 24)
        :param hour_end: The ending hour. Range (0, 24)
        :param hour_step: The step for hours. Range (1, 24). Big step means same hour.
        :param minute_start: The starting minute. Range (0, 60).
        :param minute_end: The ending minute. Range (0, 60)
        :param minute_step: The minute step. Range (0, 60). Big step means the same minute every hour.
        :return:
        """
        if hour_start < 0 or hour_start > 24:
            warnings.warn("Hour start out of range. Set it to default value '0'")
            hour_start = 0
        if hour_end < hour_start or hour_end > 24:
            warnings.warn("Hour end out of range. Set it to default value '24'")
            hour_end = 24
        if minute_start < 0 or minute_start > 60:
            warnings.warn("Minute start out of range. Set it to default value '0'")
            minute_start = 0
        if minute_end < minute_start or minute_end > 60:
            warnings.warn("Minute end out of range. Set it to default value '60'")
            minute_end = 60

        list_timestamp = []
        int_size = 0

        if hour_step <= 0:
            return None
        else:
            for hour in range(hour_start, hour_end, hour_step):
                if minute_step == 0:
                    timestamp_tmp = str_id_hours[hour] + ':'
                    timestamp_tmp += str_id_minutes[0]
                    list_timestamp.append(timestamp_tmp)
                    int_size += 1
                    # print(timestamp_tmp)
                else:
                    for minutes in range(minute_start, minute_end, minute_step):
                        timestamp_tmp = str_id_hours[hour] + ':'
                        timestamp_tmp += str_id_minutes[minutes]
                        list_timestamp.append(timestamp_tmp)
                        int_size += 1
                        # print(timestamp_tmp)
        # print(list_timestamp)
        return list_timestamp, int_size

    @staticmethod
    def change_day_month_to_single_format(day, month):
        day_single = int(day)
        day_single = str_id_single_days[day_single - 1]
        month_single = int(month)
        month_single = str_id_single_months[month_single - 1]
        return day_single, month_single

    @staticmethod
    def change_day_month_to_double_format(day, month):
        day_double = int(day)
        day_double = str_id_days[day_double - 1]
        month_double = int(month)
        month_double = str_id_months[month_double - 1]
        return day_double, month_double

    @staticmethod
    def date_break_to_day_month_year(date: str, date_format: str, date_delimeter=del_slash, century=21):
        """
                Check the format of the day (eg DD/MM/YYYY) and returns a string.
                :param century: The current century
                :param date: The date to be changed
                :param date_format: The date format. Can be: DD_MM_YYYY
                                                             DD_YYYY_MM
                                                             MM_DD_YYYY
                                                             MM_YYYY_DD
                                                             YYYY_MM_DD
                                                             YYYY_DD_MM
                                                             D_M_YYYY
                                                             D_YYYY_M
                                                             M_D_YYYY
                                                             M_YYYY_D
                                                             YYYY_M_D
                                                             YYYY_D_M
                                                             DD_MM_YY
                                                             DD_YY_MM
                                                             MM_DD_YY
                                                             MM_YY_DD
                                                             YY_MM_DD
                                                             YY_DD_MM
                                                             D_M_YY
                                                             D_YY_M
                                                             M_D_YY
                                                             M_YY_D
                                                             YY_M_D
                                                             YY_D_M

                :param date_delimeter: The delimeter of the date.
                :return: day: str, month: str, year: str
                """
        # DD_MM_YYYY or D_M_YYYY or DD_MM_YY or D_M_YY
        if date_format == DD_MM_YYYY or date_format == D_M_YYYY or date_format == DD_MM_YY or date_format == D_M_YY:
            day, month, year = date.split(date_delimeter)
            if date_format == DD_MM_YY or date_format == D_M_YY:
                year = str(int(year) + (century - 1) * 100)
            return day, month, year
        # DD_YYYY_MM or D_YYYY_M or DD_YY_MM or D_YY_M
        elif date_format == DD_YYYY_MM or date_format == D_YYYY_M or date_format == DD_YY_MM or date_format == D_YY_M:
            day, year, month = date.split(date_delimeter)
            if date_format == DD_YY_MM or date_format == D_YY_M:
                year = str(int(year) + (century - 1) * 100)
            return day, month, year
        # MM_DD_YYYY or M_D_YYYY or MM_DD_YY or M_D_YY
        elif date_format == MM_DD_YYYY or date_format == M_D_YYYY or date_format == MM_DD_YY or date_format == M_D_YY:
            month, day, year = date.split(date_delimeter)
            if date_format == MM_DD_YY or date_format == M_D_YY:
                year = str(int(year) + (century - 1) * 100)
            return day, month, year
        # MM_YYYY_DD or M_YYYY_D or MM_YY_DD or M_YY_D
        elif date_format == MM_YYYY_DD or date_format == M_YYYY_D or date_format == MM_YY_DD or date_format == M_YY_D:
            month, year, day = date.split(date_delimeter)
            if date_format == MM_YY_DD or date_format == M_YY_D:
                year = str(int(year) + (century - 1) * 100)
            return day, month, year
        # YYYY_MM_DD or YYYY_M_D or YY_MM_DD or YY_M_D
        elif date_format == YYYY_MM_DD or date_format == YYYY_M_D or date_format == YY_MM_DD or date_format == YY_M_D:
            year, month, day = date.split(date_delimeter)
            if date_format == YY_MM_DD or date_format == YY_M_D:
                year = str(int(year) + (century - 1) * 100)
            return day, month, year
        # YYYY_DD_MM or YYYY_D_M or YY_DD_MM or YY_D_M
        elif date_format == YYYY_DD_MM or date_format == YYYY_D_M or date_format == YY_DD_MM or date_format == YY_D_M:
            year, day, month = date.split(date_delimeter)
            if date_format == YY_DD_MM or date_format == YY_D_M:
                year = str(int(year) + (century - 1) * 100)
            return day, month, year

    @staticmethod
    def change_hour_number_list_to_time(list_hour: [], date_format=HH_MM):
        list_hour_tmp = []
        if date_format == HH_MM:
            for hour in list_hour:
                list_hour_tmp.append('%02i' % int(hour) + ':00')
        elif date_format == HH_MM_SS:
            for hour in list_hour:
                list_hour_tmp.append('%02i' % int(hour) + ':00:00')
        return list_hour_tmp

    @staticmethod
    def change_hour_number_in_a_cal_list_to_time(list_event: [], date_format=HH_MM):
        list_hour_tmp = []
        if date_format == HH_MM:
            for event in list_event:
                event[1] = '%02i' % int(event[1]) + ':00'
                list_hour_tmp.append(event)
        elif date_format == HH_MM_SS:
            for event in list_event:
                event[1] = '%02i' % int(event[1]) + ':00'
                list_hour_tmp.append(event)
        return list_hour_tmp























