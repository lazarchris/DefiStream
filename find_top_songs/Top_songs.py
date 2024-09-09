import os
from datetime import datetime, timedelta
import calendar
from collections import Counter

def get_last_no_days(last_number_of_days):
    """
    Calculates and return 7 or required last number of days
    """
    current_date = datetime.now()
    return [current_date - timedelta(days=i) for i in range(last_number_of_days)]


def validate_line_format(line):
    """
    This function takes a line of text and checks whether it conforms to a specific format, 
    specifically "songid|user_id(numbers)|countrycode(two chars)".
    """
    line_parts = line.split('|')
    if len(line_parts) == 3:
        song_id = line_parts[0].strip()
        user_id = line_parts[1].strip()
        country_code = line_parts[2].strip()
        if song_id and user_id and len(country_code) == 2:
            return True
    return False

def process_file(file_path):
    """
    This generator function takes a file_path as input and yields each line 
    of the file after stripping leading and trailing whitespace.
    
    Use generators for memory usage optimization
    """
    try:
        with open(file_path, 'r') as file:
            for line in file:
                stripped_line = line.strip()
                if validate_line_format(stripped_line):
                    yield stripped_line
    except IOError:
        raise Exception(f"Error: Failed to process file '{file_path}'.")



def load_files(folder_path, last_number_of_days):
    """
    This function retrieves a list of files in the given folder path and filters them based on the file name format.
    It considers the last number of days(7here)' files and takes into account the total days in a month, including leap years.
    """
    try:
        file_paths = []

        for day in get_last_no_days(last_number_of_days):
            year = day.year
            month = day.month
            day_str = day.strftime("%d")

            total_days = calendar.monthrange(year, month)[1]

            # Loop through the days of the month
            for d in range(1, total_days + 1):
                file_name = f"listen-{year}-{month:02d}-{day_str}.log"

            file_path = os.path.join(folder_path, file_name)

            if os.path.isfile(file_path):
                file_paths.append(file_path)
        
        return file_paths
    
    except Exception as e:
        raise Exception(f"Error: Failed to load files from folder '{folder_path}' due to {e}.")

    
def count_top_song_by_country(files, top_total_number):
    """
    This function takes a list of file paths and an optional top_total_number parameter, 
    and returns the top N songs per country as a dictionary with the format {country: {song id: rank}}.
    """
    top_songs_by_country = {}

    for file in files:
        song_id_counts_by_country = {}

        for line in process_file(file):
            line_parts = line.split('|')
            if len(line_parts) >= 3:
                song_id = line_parts[0].strip()
                country = line_parts[2].strip()

                if country not in song_id_counts_by_country:
                    song_id_counts_by_country[country] = Counter()

                song_id_counts_by_country[country][song_id] += 1


        for country, id_counts in song_id_counts_by_country.items():
            top_songs = id_counts.most_common(top_total_number)
            top_songs_str = {song_id: rank+1 for rank, (song_id, _) in enumerate(top_songs)}
            if country not in top_songs_by_country:
                top_songs_by_country[country] = top_songs_str
            else :
                top_songs_by_country[country].update(top_songs_str)

    return top_songs_by_country

def get_result_file_name():
    """
    Returns the result file name in the format country_top50_yyyymmdd.log
    """
    today = datetime.now()
    today_str = today.strftime('%Y%m%d')
    file_name = f"country_top50_{today_str}.log"
    return file_name

def write_to_file(result, resul_file_path):
    """
    Write ID rankings by country to a file.

    This function takes a dictionary of ID rankings by country and writes it to a file in the specified file path.
    Each line in the file will be in the format 'country|song_id:n(rank),song_id:n(rank),...'.
    """

    try:
        with open(resul_file_path, 'w') as file:
            for country, id_rank_dict in result.items():
                line_parts = [country + '|']
                line_parts.extend([f"{id}:n{rank}," for id, rank in id_rank_dict.items()])
                line = "".join(line_parts).rstrip(",")
                file.write(line + '\n')
        print("Data successfully written to the file.")
    except IOError:
        print(f"Error: Failed to write data to the file '{resul_file_path}'.")
        raise Exception("Error occurred unable to write file")
