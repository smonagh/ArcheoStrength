import numpy as np 
import matplotlib.pyplot as plt 

def generate_image(exercise, exercise_data):
    date_array, volume_array = get_numpy_arrays(exercise_data)
    get_pyplot(date_array, volume_array, exercise)

def get_numpy_arrays(exercise_data):
    volume_list = []
    date_list = []

    for index, date in enumerate(exercise_data['date']):

        volume = (exercise_data['rep_one'][index] + exercise_data['rep_two'][index] + exercise_data['rep_three'][index]) * exercise_data['weight'][index]
        volume_list.append(volume)
        date_list.append(date)

    date_array = np.array(date_list)
    volume_array = np.array(volume_list)
    print(volume_array)

    return date_array, volume_array

def get_pyplot(date_array, volume_array, exercise):

    plt.plot_date(date_array, volume_array)
    plt.title('Volume Over Time')
    plt.xlabel('Date')
    plt.ylabel('Volume')
    plt.xticks(rotation = 90)

    plt.savefig('starting_strength/static/images/{}'.format(exercise))

    #Clear existing plot
    plt.clf()


