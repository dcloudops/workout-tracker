from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

# File to store workouts
WORKOUT_FILE = 'workouts.txt'

def read_workouts():
    """Read all workouts from the file and return as a list"""
    workouts = []
    
    # Check if file exists
    if os.path.exists(WORKOUT_FILE):
        with open(WORKOUT_FILE, 'r') as file:
            for line in file:
                # Split the line by | to get individual values
                parts = line.strip().split('|')
                if len(parts) == 5:
                    workout = {
                        'date': parts[0],
                        'exercise': parts[1],
                        'sets': parts[2],
                        'reps': parts[3],
                        'weight': parts[4]
                    }
                    workouts.append(workout)
    
    return workouts

@app.route('/')
def home():
    # Get all workouts and send them to the page
    workouts = read_workouts()
    return render_template('index.html', workouts=workouts)

@app.route('/add_workout', methods=['POST'])
def add_workout():
    # Get the form data
    exercise = request.form.get('exercise')
    sets = request.form.get('sets')
    reps = request.form.get('reps')
    weight = request.form.get('weight')
    date = request.form.get('date')
    
    # Create a workout entry (one line with all the data)
    workout_entry = f"{date}|{exercise}|{sets}|{reps}|{weight}\n"
    
    # Save to file (append mode so we don't overwrite)
    with open(WORKOUT_FILE, 'a') as file:
        file.write(workout_entry)
    
    print(f" Saved: {exercise} - {sets} sets x {reps} reps @ {weight} lbs on {date}")
    
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)