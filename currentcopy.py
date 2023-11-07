# currentcopy

import os
import shutil
import argparse
import logging.config

def create_output_directory(output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

def copy_file(src_path, dest_path, overwrite):
    if not os.path.exists(dest_path) or (os.path.getmtime(src_path) > os.path.getmtime(dest_path) and overwrite):
        shutil.copy2(src_path, dest_path)

def copy_recent_files(input_dir, output_dir, overwrite=False):
    create_output_directory(output_dir)

    for root, _, files in os.walk(input_dir):
        for file in files:
            src_path = os.path.join(root, file)
            relative_path = os.path.relpath(src_path, input_dir)
            dest_path = os.path.join(output_dir, relative_path)
            output_dir_structure = os.path.dirname(dest_path)
            create_output_directory(output_dir_structure)

            copy_file(src_path, dest_path, overwrite)

def main():
    parser = argparse.ArgumentParser(description="Copy the most recent files from an input directory to an output directory recursively.")
    parser.add_argument('--input', required=True, help="Path to the input directory")
    parser.add_argument('--output', required=True, help="Path to the output directory")
    parser.add_argument('--overwrite', action='store_true', help="Overwrite existing files in the output directory")
    args = parser.parse_args()

    if not os.path.exists(args.input) or not os.path.exists(args.output):
        logging.error("Input or output directory does not exist. Please check your paths.")
        return

    log_config = {
        'version': 1,
        'formatters': {
            'verbose': {'format': '%(asctime)s - %(levelname)s: %(message)s'}
        },
        'handlers': {
            'file': {
                'level': 'INFO',
                'class': 'logging.FileHandler',
                'filename': 'copy_recent_files.log',
                'formatter': 'verbose'
            }
        },
        'root': {
            'handlers': ['file'],
            'level': 'INFO'
        }
    }
    logging.config.dictConfig(log_config)

    logging.info("Copying recent files from {} to {}. Overwrite: {}".format(args.input, args.output, args.overwrite))

    try:
        copy_recent_files(args.input, args.output, args.overwrite)
        logging.info("Copy operation completed successfully.")
    except FileNotFoundError as e:
        logging.error(f"File not found: {e.filename}")
    except (PermissionError, OSError) as e:
        logging.error(f"Error copying file: {e}")
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
