# 💪 Workout Tracker

A simple web application to track your gym workouts. Built with Python Flask and modern CSS.

![Workout Tracker Screenshot](/assets/workout-tracker.png)

##  Features

- **Add Workouts**: Log exercise name, sets, reps, weight, and date
- **View History**: See all your workouts in an organized table
- **Persistent Storage**: All workouts are saved to a local file
- **Modern UI**: Clean, gradient-based design with responsive layout

##  Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3
- **Data Storage**: Text file (workouts.txt)
- **Version Control**: Git & GitHub

##  Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

##  Installation & Setup

1. **Clone the repository**
```bash
   git clone https://github.com/YOUR-USERNAME/workout-tracker.git
   cd workout-tracker
```

2. **Create a virtual environment**
```bash
   python -m venv venv
```

3. **Activate the virtual environment**
   - Windows:
```bash
     venv\Scripts\activate
```
   - Mac/Linux:
```bash
     source venv/bin/activate
```

4. **Install dependencies**
```bash
   pip install flask
```

5. **Run the application**
```bash
   python app.py
```

6. **Open your browser**
   - Navigate to: `http://localhost:5000`

## 📁 Project Structure
```
workout-tracker/
├── app.py              # Main Flask application
├── workouts.txt        # Data storage file
├── templates/
│   └── index.html      # Main HTML template
├── static/
│   └── style.css       # CSS styling
├── venv/               # Virtual environment (not tracked)
└── README.md           # Project documentation
```

## 🎨 Screenshots

### Main Interface
Clean form for adding workouts with all necessary fields.

### Workout History
Table view showing all logged workouts with date, exercise, sets, reps, and weight.

## 🔮 Future Enhancements

- [ ] Delete/Edit workout functionality
- [ ] Filter workouts by exercise type
- [ ] Progress tracking and analytics
- [ ] Data visualization with charts
- [ ] Export to CSV functionality
- [ ] User authentication
- [ ] Database integration (SQLite/PostgreSQL)

## 📝 What I Learned

This project helped me understand:
- Flask routing and request handling
- Form data processing
- File I/O operations in Python
- HTML templating with Jinja2
- CSS styling and responsive design
- Git version control workflow

## 👨‍💻 Author

**Derron**
- GitHub: [DCloudOps](https://github.com/dcloudops)
- YouTube: [Derronintech](https://youtube.com/@derronintech-io?si=PKGaXiCCtGI70Ea9)

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

Built as part of my journey to improve my Python and web development skills. Open to feedback and suggestions!

---

⭐ If you found this project helpful, please give it a star!