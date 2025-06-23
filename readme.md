# HFGWplotter_Sh: Plotter of noise equivalent strain for gravitational wave detectors

### Created by Francesco Muia, Andreas Ringwald and Carlos Tamarit. Code maintained by C.T.

HFGWplotter_Sh is an interactive web application designed for visualizing and analyzing sensitivitiy curves for gravitational wave experiments. It offers a user-friendly interface for plotting  detector sensitivity curves, allowing researchers and enthusiasts to explore and interpret gravitational wave data effectively.

# Online version

The app is running online at 

https://incandenza-01.zdv.uni-mainz.de/Shplot/

# Dependencies

Requires python3 with the following additional dependencies:

numpy
scipy
bokeh
flask
matplotlib


# How to run

Execute the following command in the main folder:

python3 app_local.py 

The plot can be accessed in a browser by entering the following local address:

http://127.0.0.1:5003/Shplot




## Project Structure

The application is organized as follows:

```
HFGWplotter_Sh/                     # Project directory
│
├── Curves                          # Repository containing all the curves to be plotted
│   └── DetectorCurves              # Repository containing all detector curves
│ 
│
├── aux                             # Repository containing auxiliary files
│   ├── aux_functions.py            # File containing auxiliary functions
│   ├── data_files.py               # File containing information about the curves to be plotted
│   ├── imports.py                  # File containing all the imports
|   └── signal_functions.py         # File containing definitions for functions for some signal spectra (e.g. 1st order phase transitions)
|
│   
├── Shplot 
│   ├──static/                      # Static files
│   │   ├── css/                    # CSS files
│   │   │   └── styles.css          # Main stylesheet
│   │   └── js/                     # JavaScript files
│   │         └── scripts.js        # JavaScript logic
│   │ 
│   └── templates/                  # HTML templates
│         └── index.html            # Main HTML template
│
├── app_local.py                    # Main Flask application
└── README.md                       # README file
```

## Features

### Current Features

- Interactive plotting of gravitational wave sensitivitiy curves
- Toggle visibility of different gravitational wave detector sensitivity curves.
- Annotations on the plot that provide additional information.
- Customizable plot ranges and dimensions through interactive sliders.
- Users can upload their own curves from a csv file


## Contributing

Contributions to HFGWplotter are welcome, whether they be in the form of feature requests, bug reports, or pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License
MIT License. 

