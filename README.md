# 🚗 Car Price Prediction App

This is a **Streamlit-based web application** that predicts the price of a used car based on various input features such as brand, year, fuel type, mileage, engine capacity, and more. It uses a **pre-trained machine learning model** to generate the prediction.

## 📌 Features

- Interactive UI with sliders and dropdowns
- Predicts car prices based on historical data
- Fast predictions using a cached ML model
- Clean and minimal Streamlit layout

## 🧰 Tech Stack

- **Python**
- **Streamlit** – for the web interface
- **Pandas** – for data processing
- **NumPy** – for numerical operations
- **Pickle** – for loading the trained model
- (Optional) **scikit-learn** – used during model training (not shown in this repo)

## 📂 Project Structure

Install dependencies:
We recommend using a virtual environment.

bash
Copy
Edit
pip install -r requirements.txt
Run the app:

bash
Copy
Edit
streamlit run app.py
Open in your browser at http://localhost:8501.

🧪 Example Inputs
Brand: Maruti

Year: 2015

KM Driven: 30,000

Fuel: Petrol

Seller Type: Individual

Transmission: Manual

Owner: First Owner

Mileage: 18 kmpl

Engine: 1200 CC

Max Power: 85 bhp

Seats: 5

➡️ Estimated Price Output: ₹ X,XX,XXX.XX (based on model)

📝 Notes
The model (model.pkl) must be present in the root directory.

The dataset (Cardetails.csv) should match the structure expected in the code.

You can retrain the model using your own data and replace model.pkl.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

📬 Contact
For questions or suggestions, feel free to open an issue or reach out at [shrikant31thakare@gmail.com].


