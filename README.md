# Laptop Price Prediction App

This is a Streamlit web application that predicts laptop prices based on user inputs. The app is built using Python and machine learning models. It allows users to input various laptop specifications such as brand, type, RAM, weight, touchscreen, screen size, CPU, and more, and provides a price prediction in rupees (₹).

## Features

- **Brand Selection**: Choose from various laptop brands.
- **Type Selection**: Select the type of laptop (e.g., Gaming, Ultrabook).
- **RAM & Storage Options**: Input the amount of RAM and storage options (HDD/SSD).
- **Weight**: Input the laptop's weight.
- **Touchscreen & IPS Display**: Choose whether the laptop has a touchscreen and IPS display.
- **Screen Specifications**: Input screen size and resolution.
- **CPU, GPU, and OS**: Select the CPU, GPU, and operating system of the laptop.
- **Price Prediction**: Get a predicted price in Indian Rupees (₹) based on your inputs.

## Tech Stack

- **Python**
- **Streamlit** (for the web interface)
- **Scikit-learn** (for the machine learning model)
- **Pandas** (for data manipulation)
- **Pickle** (for loading the trained model)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-repo/laptop-price-predictor.git
cd laptop-price-predictor
2. Install the Dependencies
Ensure you have Python installed. Then, install the required packages using:

bash
Copy code
pip install -r requirements.txt
3. Run the Application
To run the application locally, use the following command:

bash
Copy code
streamlit run app.py
Usage
Once the app is running, open the provided URL in your browser. Input the necessary details about the laptop you're looking to price, and click on the Predict Price button. The app will return an estimated price in rupees (₹).

File Structure
plaintext
Copy code
.
├── app.py                 # Main Streamlit app file
├── model.pkl              # Pre-trained machine learning model
├── data.pkl               # Dataset used for training
├── requirements.txt       # Dependencies file
└── README.md              # This file
v
