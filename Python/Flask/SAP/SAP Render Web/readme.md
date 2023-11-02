# SAP Render Web - Flask Interface for SAP RFCs

## Description

This Flask application serves as an intermediary web interface, enabling users to execute SAP Remote Function Calls (RFCs) via a simple web form. The application is designed to be used by developers and other users who need to interact with SAP systems without directly using SAP client tools.

## Features

- **Web Form Submission**: Users can input parameters such as `P_MATNR` to be passed to SAP RFCs.
- **SAP RFC Execution**: The backend, written in Python, utilizes the `pyrfc` library to execute RFCs against configured SAP systems.
- **Dynamic Response Display**: Responses from SAP RFCs are dynamically displayed on the web page, allowing for immediate feedback.

## Project Structure

- `flaskapp.py`: This is the main Flask application file. It sets up the web server and routes.
- `sap.py`: Contains the `bapicall` function which handles the communication with the SAP system using RFC.
- `Templates`: Holds the HTML templates required by Flask.
  - `index.html`: The main template that renders the input form and displays the response.

## Getting Started

To get the application running, follow these steps:

1. Ensure you have Python and Flask installed.
2. Clone this repository to your local machine.
3. Fill in the necessary SAP system connection details in `sap.py`.
4. Run the Flask application:

```bash
python flaskapp.py
```

5. Navigate to `http://localhost:5000` in your web browser to access the application.

## Usage

1. Enter the `P_MATNR` (change for your parameters in your transaction) value in the web form.
2. Click "Submit" to send the request to the Flask application.
3. The SAP RFC response will be displayed below the form on the same page.
