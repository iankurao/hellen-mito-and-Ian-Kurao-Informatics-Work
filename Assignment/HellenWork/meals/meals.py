def main():
    #prompt user for the time
    answer = input("What time is it?")
    #converterfunction
    time = convert(answer)
    #breakfast at 7:00 to 8:00
    if time >= 7 and time <= 8:
        print("breakfast time")
    #lunch at 12:00 to 13:00
    if time >= 12 and time <= 13:
        print("lunch time")
    #dinner at 18:00 to 19:00 
    if time >= 18 and time <= 19:
        print("dinner time")


def convert(time):
    #get hours and minutes
    hours,minutes= time.split(":")
    #time to float
    new_minute = float(minutes)/60
    #return main function result
    return float(hours) + new_minute

if __name__ == "__main__":
    main()


