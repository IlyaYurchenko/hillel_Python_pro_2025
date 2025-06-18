echo "Enter env name"
read python_env
if [ -f "requirements.txt" ]; then
echo "Installing requirements processing..."
python3 -m venv "$python_env"
source "$python_env/bin/activate"
pip install -r requirements.txt
deactivate
echo "Requirements installed successfully in the virtual environment '$python_env'."
else
echo "requirements.txt file not found. Please ensure it exists in the current directory."
fi