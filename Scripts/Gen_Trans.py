import os
import subprocess
import sys
import pandas as pd

# Function for processing transcriptions using filenames
def create_spaced_text_files(input_folder, include_underscore, include_tr_dr, include_consonant_clusters):
    no_space_combinations = ["ch", "sh", "ts", "dh", "th", "vf", "hh", "jh", "ng"]
    if include_tr_dr:
        no_space_combinations.extend(["tr", "dr"])

    if include_underscore:
        no_space_combinations.extend(["aa", "ah", "ao", "ax", "ae", "ay", "aw", "eh", "er", "ey", "ih", "iy", "ow", "oy", "uh", "uw"])

    if include_consonant_clusters:
        no_space_combinations.extend(["ky", "py", "by", "ny", "my", "fy", "hy", "gy", "dy", "ty", "vy", "zy", "ry"])

    for subdir, dirs, files in os.walk(input_folder):
        for filename in files:
            file_path = os.path.join(subdir, filename)

            filename_no_ext = os.path.splitext(filename)[0]
            filename_no_ext_no_dash = filename_no_ext.replace("-", "")
            if not include_underscore:
                filename_no_ext_no_dash = filename_no_ext_no_dash.replace("_", "")

            txt_filename = filename_no_ext + ".txt"
            txt_file_path = os.path.join(subdir, txt_filename)

            with open(txt_file_path, "w", encoding="utf-8") as txt_file:
                spaced_filename = ""
                i = 0
                while i < len(filename_no_ext_no_dash):
                    if i < len(filename_no_ext_no_dash) - 1 and filename_no_ext_no_dash[i:i+2] in no_space_combinations:
                        spaced_filename += filename_no_ext_no_dash[i:i+2] + " "
                        i += 2
                    else:
                        spaced_filename += filename_no_ext_no_dash[i] + " "
                        i += 1

                if include_underscore:
                    spaced_filename = spaced_filename.replace("_", " ")
                    spaced_filename = spaced_filename.replace("   ", " ")

                # Add SP to the beginning and end
                spaced_filename = f"SP {spaced_filename.strip()} SP"

                txt_file.write(spaced_filename)

# Function for processing transcriptions using index.csv
def process_index_csv(csv_path):
    df = pd.read_csv(csv_path, encoding='utf-8')
    # Assuming the CSV has columns 'file' and 'transcription'
    for index, row in df.iterrows():
        wav_filename = row['file']
        transcription = row['transcription']

        # Extract directory and base filename
        directory = os.path.dirname(wav_filename)
        base_filename = os.path.splitext(os.path.basename(wav_filename))[0]

        # Construct .txt filename
        txt_filename = base_filename + ".txt"
        txt_file_path = os.path.join(directory, txt_filename)

        # Write transcription to .txt file
        with open(txt_file_path, "w", encoding="utf-8") as txt_file:
            txt_file.write(transcription)

# Main script logic
if __name__ == "__main__":
    print("Choose the transcription method:")
    print("0: Use filenames in folders")
    print("1: Use index.csv file")

    while True:
        try:
            method_choice = int(input("Enter your choice (0 or 1): "))
            if method_choice in [0, 1]:
                break
            else:
                print("Invalid choice. Please enter 0 or 1.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    if method_choice == 0:
        input_folder = input("Enter the input folder path: ")

        underscore_choice = input("What format is your voicebank? (0 for Japanese, 1 for Arpasing): ")
        include_underscore = underscore_choice == "1"

        include_tr_dr = False
        if include_underscore:
            tr_dr_choice = input("Include 'tr' and 'dr' in output? (0 for no, 1 for yes): ")
            include_tr_dr = tr_dr_choice == "1"

        include_consonant_clusters = False
        if underscore_choice == "0":
            consonant_cluster_choice = input("Split consonant clusters like 'ky', 'py'? (0 for no, 1 for yes): ")
            include_consonant_clusters = consonant_cluster_choice == "0"

        create_spaced_text_files(input_folder, include_underscore, include_tr_dr, include_consonant_clusters)
    else:
        csv_path = input("Enter the path to the CSV file: ")
        process_index_csv(csv_path)