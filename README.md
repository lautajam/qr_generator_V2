# QR Code Generator

This is a simple Python-based QR code generator that creates QR codes from URLs in a text file. The application features a graphical interface to easily select files and folders for saving the generated QR codes.

## Requirements

To run this project, you need to have Python and some additional libraries installed. Follow these steps to set it up:

1. **Install Python**:

   - Download and install Python from the [official Python website](https://www.python.org/downloads/).
   - Ensure you check the "Add Python to PATH" option during installation.

2. **Install pip**:

   Pip is generally installed with Python. You can check its installation with the following command in the terminal or command prompt:
   ```sh
   pip --version

3. **Install dependencies**:

    Once you have Python and pip installed, install the necessary dependencies. Create a requirements.txt file in the root of your project with the following content:

    qrcode[pil]

    Then, install the dependencies using:

    ```sh
    pip install -r requirements.txt

4. **Install PyInstaller**:

    PyInstaller is a tool that converts Python scripts into standalone executables. Install it with:

    ```sh
    pip install pyinstaller


## Usage

**Run the application**:

Execute the Python script directly from the terminal or command prompt with:
    ```sh
    python script_name.py

Replace script_name.py with the name of the file where you saved the code.

**Generate QR codes**:

Select a text file with URLs. The file should contain one URL per line. If a line includes a name separated by ;, that name will be used for the QR code image file. Otherwise, the URL (with some characters replaced) will be used as the file name.
Choose a folder where the QR code images will be saved.
The application will generate the QR codes and save them in the selected folder.
Help:

For more information on the URL file format, click the "Help" button in the application interface.

## Create an Executable

To create a standalone executable of the project using PyInstaller, use the following command in the terminal or command prompt from the directory where the script is located:
    ```sh
    pyinstaller --onefile --noconsole script_name.py

Replace script_name.py with the name of the file where you saved the code.
This will generate an executable in the dist folder.

## Troubleshooting and Support

If you encounter any issues or need additional help, please check the common issues section or contact [the project author](https://github.com/lautajam).