import random
import statistics

# Optimistic, most likely, and pessimistic durations in Days of three activities
Optimistic_Activity_A = 8
Most_likely_Activity_A = 10
Pessimistic_Activity_A = 12

Optimistic_Activity_B = 10
Most_likely_Activity_B = 12
Pessimistic_Activity_B = 14

Optimistic_Activity_C = 12
Most_likely_Activity_C = 14
Pessimistic_Activity_C = 16

def run_simulation(Optimistic_Activity_A, Most_likely_Activity_A, Pessimistic_Activity_A, 
                    Optimistic_Activity_B, Most_likely_Activity_B, Pessimistic_Activity_B, 
                    Optimistic_Activity_C, Most_likely_Activity_C, Pessimistic_Activity_C, Number_of_simulations):
  
  Answers = []

  # The simulations
  for i in range(Number_of_simulations):

    # Find/Generate random values for each Activity
    
    Activity_A_duration = random.triangular(Optimistic_Activity_A, Most_likely_Activity_A, Pessimistic_Activity_A)
    Activity_B_duration = random.triangular(Optimistic_Activity_B, Most_likely_Activity_B, Pessimistic_Activity_B)
    Activity_C_duration = random.triangular(Optimistic_Activity_C, Most_likely_Activity_C, Pessimistic_Activity_C)

    # Add those durations for each Activity together to get the total duration for this simulation
    Total_duration = Activity_A_duration + Activity_B_duration + Activity_C_duration
    Answers.append(Total_duration)

    # Print the total duration
    print("Total duration for simulation", i + 1, ":", Total_duration)

  # Calculate the Average of the results(duration)
  Average_Days = sum(Answers) / len(Answers)
  print(" Average duration:", Average_Days)


  # Count the number of durations between 30 and 35
  count_30_35 = 0
  for Total_duration in Answers:
    if 30 <= Total_duration <= 35:
      count_30_35 += 1
  print("Number of durations between 30 and 35:", count_30_35)

  # Count the number of durations between 36 and 38
  count_36_38 = 0
  for Total_duration in Answers:
    if 36 <= Total_duration <= 38:
      count_36_38 += 1
  print("Number of durations between 36 and 38:", count_36_38)

  # Count the number of durations between 39 and 42
  count_39_42 = 0
  for Total_duration in Answers:
    if 39 <= Total_duration <= 42:
      count_39_42 += 1
  print("Number of durations between 39 and 42:", count_39_42)
      
# Run it for 500 times
Number_of_simulations = 500

# Run the simulation
run_simulation(Optimistic_Activity_A, Most_likely_Activity_A, Pessimistic_Activity_A, Optimistic_Activity_B, Most_likely_Activity_B, Pessimistic_Activity_B, Optimistic_Activity_C, Most_likely_Activity_C, Pessimistic_Activity_C, Number_of_simulations)
