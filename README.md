## Server Monitoring and Email Script

### Description
This Python script monitors server health by gathering free disk space and active process count. It logs this data to a file and then sends a summary email with the collected information.

### Prerequisites
* Python 3.x
* Required libraries: `psutil`, `shutil`, `smtplib`
* Email configuration details (sender email, recipient email, SMTP server, port, username, password)

### Configuration
* **Email Settings:** Replace the placeholder values in the script with your actual email configuration details.
* **Log File Path:** Specify the desired path for the log file.

### Usage
1. **Install dependencies:**
   ```bash
   $py -m pip install psutil shutil smtplib
   ```
2. **Configure email settings:** Edit the script with your email credentials.
3. **Run the script:** Execute the Python script.

### How it Works
* Collects free disk space and active process count using `psutil`.
* Appends the collected data to a log file.
* Creates an email body summarizing the collected data.
* Sends the email using `smtplib`.

### Log File
The script creates a log file named `server_monitor.log` in the same directory. Each line in the log file contains a timestamp, free disk space, and active process count.

### Email Content
The email includes a summary of the latest log entry, providing a quick overview of server health.

### Additional Notes
* For production environments, consider using a more robust logging library and implementing error handling.
* Explore using a dedicated email library for enhanced features and security.
* Implement scheduling using tools like `cron` or task schedulers to automate the monitoring process.
* Consider using encryption for sensitive email credentials.

### Security
* Protect your email credentials and sensitive information.
* Be cautious about sharing the script with others.

**Disclaimer:** This script is a basic example and might require adjustments for specific environments. Always test thoroughly before deploying in production.
 
