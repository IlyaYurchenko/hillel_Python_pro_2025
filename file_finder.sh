echo 'enter the filename'
read filename
if [ -f "$filename" ]; then
    echo "File '$filename' exists."
else
    echo "File '$filename' does not exist."
    echp "Creating file '$filename'."
    touch "$filename"
    echo "File '$filename' created successfully."
fi

