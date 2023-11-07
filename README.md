# CurrentCopy

Copy recent files to an output directory

![currentcopy logo](/assets/currentcopy_logo.png)

## Overview
The "CurrentCopy" Python script is a tool that allows you to copy the most recent files from one directory to another. This script is particularly useful when you need to keep your target directory up to date with the latest files from a source directory.

## Features
- Recursively copies the most recent files from the source directory to the destination directory.
- Supports overwriting existing files in the destination directory, controlled by the `--overwrite` flag.
- Provides logging for tracking the copy process and any errors that occur.
- Automatically creates the necessary directory structure in the destination directory.

## Usage
To use the script, follow these simple steps:

1. Make sure you have Python installed on your system.

2. Open your command prompt or terminal.

3. Navigate to the directory where the "currentcopy.py" script is located.

4. Run the script with the following command:

   ```python
   python currentcopy.py --input source_directory --output destination_directory
   ```

   - `source_directory`: The path to the source directory you want to copy files from.
   - `destination_directory`: The path to the destination directory where files will be copied.

Optional Flags:
- `--overwrite`: Use this flag to enable overwriting existing files in the destination directory.

## Examples
### Basic Usage:
```python
python currentcopy.py --input /path/to/source --output /path/to/destination
```

### Overwrite Existing Files:
```python
python currentcopy.py --input /path/to/source --output /path/to/destination --overwrite
```

## Logging
The script generates a log file named "copy_recent_files.log" in the same directory where the script is located. This log file provides information about the copying process, including the source, destination, and any encountered errors.

## Error Handling
The script includes error handling to capture and log various types of exceptions, such as "FileNotFoundError," "PermissionError," and general "OSError." This ensures a smooth and reliable copying process even in the presence of issues.

## Note
Please make sure to specify valid paths for the source and destination directories. If the directories do not exist, the script will display an error message and exit.

**Disclaimer:** This script is provided as-is, without any warranty. Please use it responsibly and ensure that you have appropriate permissions for the source and destination directories.
