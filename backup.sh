echo 'Enter the filename to backup'
read filename

backup_file="$filename-$(date +%Y%m%d).backup"
if [ -f "$filename" ]; then
   cp "$filename" "$backup_file"
   echo "Backup created succesfully: $backup_file"
else
   echo "File '$filename' does not exist. Cannot create backup."
fi