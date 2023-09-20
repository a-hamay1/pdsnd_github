# Project name: Bike Share Data Analysis with Python
# Porject Craeter: Ala Hamayel
# Creation Date: 16/09/2023
# Data File : Chicago.csv ,new_york_city.csv, washington.csv
#sources used: Udemy and code camp

import time
import pandas as pd
import numpy as np

CITY_DATA = {
    'chicago': 'C:/Users/Ala/Documents/BikesProject/all-project-files/chicago.csv',
    'new york city': 'C:/Users/Ala/Documents/BikesProject/all-project-files/new_york_city.csv',
    'washington': 'C:/Users/Ala/Documents/BikesProject/all-project-files/washington.csv'
}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    while True:
        city = input('Enter city name (Chicago, New York City, Washington): ').lower()
        if city in CITY_DATA:
            break
        else:
            print('Invalid city name. Please choose from the provided options.')

    month = input('Enter month (all, january, february, ... , june): ').lower()
    day = input('Enter day of the week (all, monday, tuesday, ... sunday): ').lower()

    print('-' * 40)
    return city, month, day

def load_data(city, month, day):
    """Loads data for the specified city and filters by month and day if applicable."""
    try:
        filename = CITY_DATA[city]
        df = pd.read_csv(filename)

        df['Start Time'] = pd.to_datetime(df['Start Time'])

        if month != 'all':
            df = df[df['Start Time'].dt.month == pd.to_datetime(month, format='%B').month]

        if day != 'all':
            df = df[df['Start Time'].dt.day_name().str.lower() == day]

        return df
    except KeyError:
        print("Invalid city name. Please choose from 'chicago', 'new york city', or 'washington'.")
        return None

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Convert 'Start Time' column to datetime if not already
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Calculate and display the most common month
    df['Month'] = df['Start Time'].dt.month
    common_month = df['Month'].mode()[0]
    print(f"Most common month: {common_month}")

    # Calculate and display the most common day of the week
    df['Day of Week'] = df['Start Time'].dt.day_name()
    common_day = df['Day of Week'].mode()[0]
    print(f"Most common day of the week: {common_day}")

    # Calculate and display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    common_hour = df['Hour'].mode()[0]
    print(f"Most common start hour: {common_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Calculate and display the most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print(f"Most commonly used start station: {common_start_station}")

    # Calculate and display the most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print(f"Most commonly used end station: {common_end_station}")

    # Calculate and display the most frequent combination of start and end stations
    common_trip = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print(f"Most frequent combination of start and end stations: {common_trip[0]} to {common_trip[1]}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Calculate and display the total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(f"Total travel time: {total_travel_time} seconds")

    # Calculate and display the average travel time
    average_travel_time = df['Trip Duration'].mean()
    print(f"Average travel time: {average_travel_time} seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    while True:
        print("Choose an option for analysis:")
        print("1. Counts of user types")
        print("2. Counts of gender (if available)")
        print("3. Earliest, most recent, and most common birth year (if available)")
        print("4. Back to main menu")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            # Display counts of user types
            user_type_counts = df['User Type'].value_counts()
            print("\nCounts of user types:")
            print(user_type_counts)
        elif choice == '2':
            # Display counts of gender (if available)
            if 'Gender' in df:
                gender_counts = df['Gender'].value_counts()
                print("\nCounts of gender:")
                print(gender_counts)
            else:
                print("\nGender information not available for this city.")
        elif choice == '3':
            # Display earliest, most recent, and most common birth year (if available)
            if 'Birth Year' in df:
                earliest_birth_year = int(df['Birth Year'].min())
                most_recent_birth_year = int(df['Birth Year'].max())
                most_common_birth_year = int(df['Birth Year'].mode()[0])
                print(f"\nEarliest birth year: {earliest_birth_year}")
                print(f"Most recent birth year: {most_recent_birth_year}")
                print(f"Most common birth year: {most_common_birth_year}")
            else:
                print("\nBirth year information not available for this city.")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        if df is not None:
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
