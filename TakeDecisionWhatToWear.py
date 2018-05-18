# TakeDecisionWhatToWear.py

rainy = input("How is the weather? Is it raining? (y/n)").lower()
cold = input("Is it cold outside? (y/n)").lower()
if (rainy == 'y' and cold == 'y'):      # Rainy and cold, yuck!
    print("You would better wear a raincoat.")
elif (rainy == 'y' and cold != 'y'):    # Rainy, but warm
    print("Carry an umbrella with you.")
elif (rainy != 'y' and cold == 'y'):    # Dry, but cold
    print("Put on a jacket, it is cold outside.")
elif (rainy != 'y' and cold != 'y'):    # Warm and sunny, yay!
    print("Yay!!Wear whatever you want, it is beautiful outside.")


