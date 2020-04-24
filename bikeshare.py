import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    days=['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    months= ['all','january', 'february', 'march', 'april', 'may', 'june']
    cities=['chicago', 'new york city', 'washington']
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:

        try:
            city=input('Enter the name of the city(chicago, new york city, washington) : ').lower()
            if city not in cities:
                print("Please try again")
            else:
                break;
        except:
            print('input not valid,please try again')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month=input('Enter the month (all, january, february,march,april,may, june) for filter: ').lower()
            if month not in months:
                print("Please try again.")
            else:
                break;
        except:
             print('input not valid,please try again')


    # TO DO: get user input for day of week (all, monday, tuesday,wednesday ... sunday)
    while True:
        try:
            day=input('Enter the day of  week (all, monday, tuesday, ... sunday) for filter: ').lower()
            if day not in days:
                print("Please try again.")
            else:
                break;
        except:
             print('input not valid,please try again')

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
     # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])


    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1

        # filter by month to create the new dataframe
        df = df[df['month']==month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        day=days.index(day)+1
        df = df[df['day_of_week']==day]




    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    months = ['january', 'february', 'march', 'april', 'may', 'june']

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common montha
    print('The most common month chosen')
    print(months[df['month'].mode()[0]-1])

    # TO DO: display the most common day of week
    print('The most common day of week chosen')
    print(days[df['day_of_week'].mode()[0]-1])

    # TO DO: display the most common start hour
    print('The most common start hour')
    print(df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most commonly used start station')
    print(df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('Most commonly used end station')
    print(df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip

    df['start end']=df['Start Station'] + "-" + df['End Station']
    print('Most frequent combination of start station and end station trip')
    print(df['start end'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['total time']=df['End Time']-df['Start Time']
    print('Total travel time')
    print(df['total time'].sum())

    # TO DO: display mean travel time
    print('Mean travel time')
    print(df['total time'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of user types')
    print(df['User Type'].value_counts())

    try:
    # TO DO: Display counts of gender

        gender_count=df['Gender'].value_counts()
        print('Counts of gender')
        print(gender_count)

    # TO DO: Display earliest, most recent, and most common year of birth
        print('Earliest, most recent, and most common year of birth')
        try:
            print(df['Birth Year'].value_counts().idxmin())
        except:
            print(df['Birth Year'].value_counts())
    except:
        print("Gender & Birth Year are not present in the data")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        x=0
        while True:
            display=input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n')
            if display.lower()=='yes':
                print(df[x:x+5])
                x+=5
            else:
                break

        restart = input('\nWould you like to restart? Enter yes or no.\n')

        if restart.lower() = 'no':
            break


if __name__ == "__main__":
	main()
