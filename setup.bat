@echo off

REM Check if a virtual environment directory exists, if not, create it
if not exist "venv" (
    echo Creating virtual environment...
    py -3 -m venv venv
)

REM Activate the virtual environment
echo Activating virtual environment...
call venv\Scripts\activate

REM Install packages from requirements.txt
echo Installing packages from requirements.txt...
pip install -r requirements.txt

REM Update requirements.txt with current environment packages
echo Updating requirements.txt with current packages...
pip freeze > requirements.txt

echo Setup complete!
