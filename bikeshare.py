import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ('january', 'february', 'march', 'april', 'may', 'june')

weekdays = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')

city = ('chicago', 'new york', 'washington')

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Please insert the city you're interested in:\n Chicago, New York City, or Washington\n")
        city = city.lower()
        if city not in ('new york city', 'chicago', 'washington'):
            print("Sorry, your input is incorrect. Please insert a valid city.")
            continue
        else:
            break
    
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Which month would you like to analyze the data for:\n January, February, March, April, May, June, or All\n")
        month = month.lower()
        if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print("Sorry, your input is incorrect. Please insert a valid month.")
            continue
        else:
            break
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True: 
        day = input("Which day of the week would you like to analyze the data for:\nMonday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, or All\n")
        day = day.lower()
        if day not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
            print("Sorry, your input is incorrect. Please insert a valid day.")
            continue
        else:
            break
            
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
  
    if day != 'all':
        months = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = weekdays.index(day)
        df = df[df['day_of_week'] == day]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_often_month = df['month'].mode()[0]
    print('The most common month to travel is:', most_often_month)

    # TO DO: display the most common day of week
    most_often_day_of_week = df['day_of_week'].mode()[0]
    print('The most common day of the week to travel is:', most_often_day_of_week)
    
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_often_start_hour = df['hour'].mode()[0]
    print('The most common start hour for travel is:', most_often_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_often_start_station = df['Start Station'].mode()[0]
    print('The most common start station is:\n {}'.format(  most_often_start_station))

    # TO DO: display most commonly used end station
    most_often_end_station = df['End Station'].mode()[0]
    print('The most common end station is:\n {}'.format( most_often_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    combination_station = df['Start Station'] + " - " +  df['End Station']
    most_often_combination_station = combination_station.mode()[0]
    print('The most common trip from start to end is:\n {}'.format(most_often_combination_station))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    total_travel_time = round(total_travel_time / 60 / 60 ,0)
    print('The total travel time is:', total_travel_time, 'hours')

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    mean_travel_time = round(mean_travel_time / 60 ,0)
    print('The mean travel time is:', mean_travel_time, 'minutes')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The counts of each user type:\n', user_types)
    # TO DO: Display counts of gender
    try:
        gender_counts = df['Gender'].value_counts().to_string()
        print('The respective gender counts are:')
        print(gender_counts)
    except KeyError:
        print('Sorry, there is no gender data available')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year = df['Birth Year'].min()
        print('The earliest birth year of users is:\n',earliest_year)

        latest_year = df['Birth Year'].max()
        print('The most recent birth year of users is:\n',latest_year)

        common_year = df['Birth Year'].mode()[0]
        print('The most common birth year of users is:\n',common_year)
    except:
        print('Sorry, there is no birth data available')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def raw_data(df):
    """Displays 5 lines of raw data when selecting yes."""
    i = 1
    while True:
        rawdata = input('Would you like to see 5 lines of raw data? Enter Yes or No.\n')
        if rawdata.lower() == 'yes':
            print(df[i:i+5])
            i = i+5   
        else: 
            break
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()

#Sources Used

#https://pandas.pydata.org/pandas-docs/stable/user_guide/index.html#user-guide

#https://docs.scipy.org/doc/numpy-1.13.0/contents.html

#https://docs.python.org/3/tutorial/index.html

