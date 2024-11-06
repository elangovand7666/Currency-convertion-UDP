Currency Converter with API Integration

A Django-based currency converter application that allows users to convert between different currencies using real-time exchange rates fetched from an external API.

Features:

    User Input: Users can enter an amount, select the source and target currencies.
    API Integration: Fetches live exchange rates from ExchangeRate-API (or any other preferred currency exchange API).
    Real-Time Conversion: Automatically converts the entered amount based on the selected currencies and displays the result.
    Responsive UI: Designed with HTML, CSS, and flexible layout to work seamlessly on different screen sizes.

Technologies Used:

    Django (Backend)
    Requests (API calls)
    HTML/CSS (Frontend)

How to Run:

    Clone this repository to your local machine:

git clone https://github.com/yourusername/currency-converter.git

Install the required dependencies:

pip install -r requirements.txt

Set up your API key (replace the placeholder in the views.py file with your actual API key).
Run the Django development server:

    python manage.py runserver

    Access the app at http://127.0.0.1:8000/.

Contributions: Feel free to open an issue or submit a pull request for any enhancements or bug fixes.
