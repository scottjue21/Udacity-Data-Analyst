def display_data():
    print('test')
    start_data_display = 0
    display_input = input('\nDo you want to see the raw data? Please type: "yes" or "no"\n').lower()
    while True:
        if display_input.lower() == 'no':
            break
        if display_input.lower() == 'yes':
            print(df.iloc[start_data_display : start_data_display + 5])
        display_more_input = input('\nWould you like to view more data? Please type: "yes" or "no"\n').lower()
        while True:
            if display_more_input.lower() == 'no':
                break
            if display_more_input.lower() == 'yes':
                start__data_display += 5
                print(df.iloc[start_data_display : start_data_display + 5])     
        else:
           print('Sorry, I do not understand your input. Please type: "yes" or "no".')
        
        
        
        
        
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
                display_more_Data = input('\nWould you like to view more data? Please type "yes" or "no"\n')
                valid_input_2 = is_valid(display_more_data)
                if valid_input_2 == True:
                    break
                else:
                    print('Sorry, I do not understand your input. Please type "yes" or "no"')
            if display_more_data.lower() == 'yes':
                start += 5
                end += 5
                print(df.iloc[start:end])
            elif display_more_data.lower() == 'no':
                break