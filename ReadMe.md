# Defistream
It process logs of all listening streams made on that date. FInd out top50 streams of last 7days for each country given
- It runs the python script using systemd at 11:55 PM every night automatically
- It doesn't consider any stream log file lines that are broken
- It uses generators for optimal memory usage
- It is tested on an ubuntu system
- It uses systemd configuration to start on every night 11.55PM automatically


### Configuration to start script automatically
- Give write permissoin to the 'init.sh'

```sh
chmod +x init.sh
```

- Execute following command to create stream logs folder, results folder, and to copy all systemd files and start a service to run the script

```sh
sudo ./init.sh
```

- Stream log files must be downloaded to "/find_top_songs/stream_logs"
- Result files will be written to "/find_top_songs/top50_results_daily"
- Voila! The script will automatically run every night at 11:55PM 


### Launch manually

#### Prequisities
- I assume, "stream_logs" directory do exists on the root of this repo. All stream logs are downloaded to this folder
- The directory "top50_results" exist at the root of this repo 
- To execute the scirpt, go to the root of this repo, and run

```sh
    python3 find_top_songs/main.py stream_logs top50_results
```
- Result file will be generated on the "top50_results" folder


