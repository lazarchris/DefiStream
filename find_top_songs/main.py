import Top_songs
import time
import datetime
import sys

def start(logs_folder, result_folder):

    print("Find top songs: Started ...")

    try: 

        # load logs files of last 7 days if they exist
        no_of_days = 7
        files = Top_songs.load_files(logs_folder,no_of_days)

        # retrieve top 50 songs 
        top_total_number_of_songs = 50
        top_songs_by_country = Top_songs.count_top_song_by_country(files,top_total_number_of_songs)

        # write results to a file
        todays_result_file = f"{result_folder}/{Top_songs.get_result_file_name()}"
        
        Top_songs.write_to_file(top_songs_by_country, todays_result_file)
        
        print("Find top songs: Completed ...")
        print(f"Result are written to {todays_result_file}")

    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    """
    This script takes two arguments 
    logs folder: where log files are located
    results fodler: to where result files are written
    """
    if len(sys.argv) != 3:
        print("Invalid number of arguments")
        print("Usage: main.py log_folder result_folder")
    else:
        logs_folder = sys.argv[1]
        results_folder = sys.argv[2]
    
    # Replace start with start_in_loop if you want to run the python script without the help of systemd
    start(logs_folder, results_folder)