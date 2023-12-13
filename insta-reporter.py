import requests

def login(username, password):
    # Same as before...

def report_user(session, user_id):
    # Same as before...

if __name__ == "__main__":
    # Replace 'your_username' and 'your_password' with your actual Instagram credentials
    your_username = 'your_username'
    your_password = 'your_password'
    
    user_id_to_report = 'user_you_want_report'  # Replace 'user_you_want_report' with the user ID of the profile you want to report
    num_reports = 100

    session = login(your_username, your_password)

    for i in range(num_reports):
        report_user(session, user_id_to_report)
        print(f"Report {i + 1} completed.")

    print("All reports completed.")
