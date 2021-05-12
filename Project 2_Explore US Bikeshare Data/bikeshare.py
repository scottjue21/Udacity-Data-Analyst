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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while city.lower() not in ['chicago', 'new york', 'washington']:
        city = input('\nWhich city you would like to explore?please typye in full name (SELECT: Chicago, New York City, or Washington)\n').lower()
        if city in ['chicago', 'new york city', 'washington']:
            print (city)
            break
        else:
           print('Oops, try again. Please select: Chicago, Washington, or New York City')

    # TO DO: get user input for month (all, january, february, ... , june)
    month = ''
    while month.lower() not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
        month = input('\nWhich month you would like to filter on? Please type the full month name (SELECT: all, January, February, March, April, May, or June)\n').lower()
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            print (month)
            break
        else:
           print('Oops, try again. Please select: all, January, February, March, April, May, or June')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ''
    while day.lower() not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        day = input('\nWhich day you would like to filter on? Please type the full name (SELECT: all, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday)\n').lower()
        if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            print (day)
            break
        else:
           print('Oops, try again. Please select: all, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday')

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
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most popular month:\n', popular_month) 
    
    # TO DO: display the most common day of week
    popular_day = df['day'].mode()[0]
    print('Most popular day:\n', popular_day)
    
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most popular start hour:\n', popular_hour)
         
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most popular start station:\n', popular_start_station)
    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most popular end station:\n', popular_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    popular_start_end_station= df[['Start Station', 'End Station']].mode().loc[0]
    print("Most popular start station and end station:\n{} to {}".format(popular_start_end_station[0], popular_start_end_station[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('\nTotal Travel Time:\n', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time =df['Trip Duration'].mean()
    print('\nMean Travel Time:\n', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('\nCounts of user types:\n', user_types)
    
    # TO DO: Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print('\nCounts of gender:\n', gender_count)
        
    except:
        print('There is no gender data in the source.')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year = int(np.min(df['Birth Year']))
        print ('\nEarliest year of birth:\n', earliest_birth_year)
        most_recent_birth_year = int(np.max(df['Birth Year']))
        print ('\nMost recent year of birth:\n', most_recent_birth_year)
        most_common_birth_year= int(df['Birth Year'].mode()[0])
        print ('\nMost common year of birth is:\n', most_common_birth_year)
       
    except:
        print('There is no birth date data in the source.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    
    def is_valid(display_data):
        if display_data.lower() in ['yes', 'no']:
            return True
        else:
            return False
    start = 0
    end = 5
    valid_input = False
    while valid_input == False:
        display_data = input('\nWould you like to view individual trip data? Please type "yes" or "no"\n')
        valid_input = is_valid(display_data)
        if valid_input == True:
            break
        else:
            print('Sorry, I do not understand your input. Please type "yes" or "no"')
    if display_data.lower() == 'yes':
        print(df.iloc[start:end])
        display_more_data = ''
        while display_more_data.lower() != 'no':
            valid_input_2 = False
            while valid_input_2 == False:
                display_more_data = input('\nWould you like to view more data? Please type "yes" or "no"\n')
                valid_input_2 = is_valid(display_more_data)
                if display_more_data.lower() == 'yes':
                    start += 5
                    end += 5
                    print(df.iloc[start:end])
                    
                if valid_input_2 == True:
                    break
                    
                elif display_more_data.lower() == 'no':
                    break
                else:
                    print('Sorry, I do not understand your input. Please type "yes" or "no"')
                                      
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
