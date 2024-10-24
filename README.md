"newCICD" repository is created in Github
Added index.html file to the repository
Open PowerShell in admin mode and type wsl
Installed Nginx in local linux instance using sudo apt update sudo apt install nginx
Staredt the Nginx using sudo systemctl start nginx
Opened the browser and navigate to http://localhost to see the Nginx welcome page running
Installed Python sudo apt install python3-pip -y pip3 install requests
Installed git sudo apt install git -y
Created a folder named "newCICD" to store your scripts and clone github repo mkdir newproject cd newproject
Created a python script "autocode.py" and write the script to fetch and check the latest commits from Github repository using GithubAPI. Once fetched, the script should store the last commit and verify the new commits coming in.
Make the Bash Script Executable
Set the correct permissions on the bash script:
chmod +x script.sh
Set Up a Cron Job to Run the Python Script
Edit Crontab
Open the cron job scheduler by running:
crontab -e
Add the Python Script to Crontab
Add the following line to the crontab to run the Python script every 2 minutes:
*/2 * * * * /newproject/script.sh > /newproject/log.txt 2>&1
This will run the Python script every 2 minutes.
To test the script, updated the index.html in the repository and navigated to http://localhost to verify the changes are reflecting
