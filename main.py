from pyscript import document
import numpy as np
import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)

import matplotlib.pyplot as plt

def check_attendance(e):
    document.getElementById('output').innerHTML = ""

    # Get absences for each day
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    day_ids = ['mon', 'tue', 'wed', 'thu', 'fri']

    absences_list = []
    for day_id in day_ids:
        value = document.getElementById(day_id).value
        absences_list.append(int(value) if value else 0)
    
    schedule = np.array(absences_list)

    # Show graph
    plt.plot(days, schedule, color='green')
    plt.xlabel('Number of Absences')
    plt.title("10-Emerald's Weekly Attendance")
    plt.tight_layout()
    plt.show()
    
    # Display attendance summary
    output = "<h5>Attendance Summary:</h5><ul>"
    for day, absences in zip(days, absences_list):
        output += f"<li>{day}: {absences} absences</li>"
    output += "</ul>"
    document.getElementById('output').innerHTML = output
