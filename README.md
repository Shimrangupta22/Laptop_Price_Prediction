# Laptop Price Prediction App

This is a Streamlit web application designed to predict laptop prices based on user inputs. Built using Python and machine learning models, the app allows users to enter various laptop specifications and provides a price prediction in Indian Rupees (₹).

## Features

- **Brand Selection**: Choose from a list of laptop brands.
- **Type Selection**: Select the laptop type (e.g., Gaming, Ultrabook).
- **RAM & Storage**: Enter the amount of RAM and select storage options (HDD/SSD).
- **Weight**: Input the laptop's weight.
- **Touchscreen & IPS Display**: Indicate if the laptop has a touchscreen and/or an IPS display.
- **Screen Specifications**: Provide screen size and resolution.
- **CPU, GPU, and OS**: Choose the CPU, GPU, and operating system.
- **Price Prediction**: Receive a price estimate in Indian Rupees (₹) based on your inputs.

## Tech Stack

- **Python**
- **Streamlit**: For the web interface
- **Scikit-learn**: For the machine learning model
- **Pandas**: For data manipulation
- **Pickle**: For loading the trained model

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/laptop-price-predictor.git
   cd laptop-price-predictor
   
2. **Install Dependencies**:
     Ensure Python is installed. Then, run:

   ```bash
   pip install -r requirements.txt

3. **Run the Application**:

   ```bash
   streamlit run app.py
