import psutil
import smtplib
from email.mime.text import MIMEText
import datetime


def check_system_status():
    """Checks disk space, process count, and writes to a log file."""
    log_file = "system_status.log"

    try:
        # Get disk usage
        disk_usage = psutil.disk_usage('/')
        free_space = disk_usage.free / (1024 * 1024 * 1024)  # Convert to GB

        # Get process count
        process_count = len(psutil.pids())

        # Get current timestamp
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Write to a log file
        with open(log_file, "a") as f:
            f.write(f"{current_time}\n")
            f.write(f"Free disk space: {free_space:.2f} GB\n")
            f.write(f"Number of active processes: {process_count}\n")

        return log_file

    except Exception as e:
        print(f"Error occurred: {e}")
        return None


def send_email(log_file):
    """Sends the log file as an email."""
    sender_email = "211111230@stu.manit.ac.in"
    receiver_email = "harshgarg1921@gmail.com"
    password = "lxhw qhfr ftss jebc"

    try:
        with open(log_file, "r") as f:
            log_content = f.read()

        msg = MIMEText(log_content)
        msg['Subject'] = "System Status Report"
        msg['From'] = sender_email
        msg['To'] = receiver_email

        with smtplib.SMTP('smtp.gmail.com', 587) as s:
            s.starttls()
            s.login(sender_email, password)
            s.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent successfully!")

    except Exception as e:
        print(f"Error sending email: {e}")


if __name__ == "__main__":
    log_file = check_system_status()
    if log_file:
        send_email(log_file)
