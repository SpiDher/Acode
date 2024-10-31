
```markdown
# Twitter API Interaction Script "xrequest.py"

This Python script interacts with the Twitter API for various operations, including user lookups, posting tweets, and deleting tweets. It utilizes the Twitter API v2 endpoints to perform these tasks.

## Features

- **User Lookup:** Retrieve user information by username.
- **Post Tweet:** Post a new tweet.
- **Delete Tweet:** Delete a tweet by its ID.

## Prerequisites

- Python 3.x
- `requests` library
- `requests_oauthlib` library

Setup

1. Install Dependencies:

   Ensure you have the required libraries installed. You can install them using pip:
   ```bash
   pip install requests requests_oauthlib
   ```

2. Create `keys.csv`:

   Create a `keys.csv` file in the same directory as the script. This file should contain your Twitter API keys and tokens. The format should be:
   ```
   name,token
   Api_key,<your_api_key>
   Api_secret_key,<your_api_secret_key>
   Access_token,<your_access_token>
   Access_token_secret,<your_access_token_secret>
   bearer_token,<your_bearer_token>
   ```

 Usage

Run the script with the desired action and parameters. The script supports the following actions:

- **User Lookup (`ul`):** Retrieve user information by username.
  ```bash
  python xrequests.py ul <username>
  ```

- **Post Tweet (`p`):** Post a new tweet with the specified text.
  ```bash
  python xrequests.py p "<tweet_text>"
  ```

- **Delete Tweet (`d`):** Delete a tweet by its ID.
  ```bash
  python xrequests.py d <tweet_id>
  ```

### Example

- To look up a user with username `jack`:
  ```bash
  python xrequests.py ul jack
  ```

- To post a tweet with text "Hello Twitter!":
  ```bash
  python xrequests.py p "Hello Twitter!"
  ```

- To delete a tweet with ID `1234567890`:
  ```bash
  python xrequests.py d 1234567890
  ```

 Files Created

- **`ul_response.csv`**: Contains the response from the user lookup operation.
- **`post_response.csv`**: Contains the response from the post tweet operation.

Notes

- Ensure that your API keys and tokens are kept secure and not shared publicly.
- The script assumes that the `keys.csv` file is correctly formatted and located in the same directory.

Contributing

Feel free to submit issues or pull requests if you have improvements or suggestions.

 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

OTP Email Sender
It is a simple OTP System built for educational purpose.

This Python script generates a One-Time Password (OTP), sends it via email to a list of recipients, and provides a prompt for the user to confirm the OTP. The script uses the smtplib library to send emails and a CSV file to store login credentials and recipient email addresses.

Features

Generates a 4-digit OTP.

Sends the OTP to a list of emails provided in email_list.csv.

Prompts the user to confirm the OTP.

Validates the OTP entered by the user.


Requirements

Python 3.x

An email account that supports SMTP (e.g., Gmail).

The following Python libraries:

smtplib

csv

email

threading

random



Setup

1. Login Credentials: Create a login.csv file in the same directory with the following format:

email,password
your_email@gmail.com,your_password

Replace your_email@gmail.com and your_password with the credentials of the email account you want to use to send the OTP.


2. Email List: Create an email_list.csv file with a list of recipient email addresses (one per line):

recipient1@example.com
recipient2@example.com


3. Allow Less Secure Apps (if using Gmail): If you're using Gmail, you may need to allow less secure apps to send emails. Follow this link to enable it.



How to Use

1. Run the Script: Run the script in your terminal:

python otp.py


2. Check Email for OTP: The OTP will be sent to all emails listed in email_list.csv with the subject "Test OTP".


3. Enter OTP: When prompted, enter the OTP sent to your email to confirm. If the OTP matches, you'll see "OTP confirmed"; otherwise, you'll see "Invalid OTP".



Code Explanation

generator: A lambda function that generates a random 4-digit OTP.

OTP_counter: Generates an OTP and sets a timer. (You can extend it to handle OTP expiration by modifying the Timer logic.)

smtp_login: Reads the email credentials from login.csv.

get_emails: Reads the recipient emails from email_list.csv.

send_email: Configures and sends an email with the generated OTP.

confirm_otp: Prompts the user to enter the OTP and checks if it matches.

main: The main function that orchestrates OTP generation, email sending, and OTP confirmation.


Example

OTP sent to emails provided at email_list.csv
Enter OTP sent to your email: 1234
OTP confirmed

If the OTP doesn't match, it will print "Invalid OTP."

Notes

Email Settings: Ensure that the email service provider supports SMTP and that the SMTP server settings are correct. For Gmail, use smtp.gmail.com on port 587.

Security: Avoid hardcoding sensitive information like passwords in the code. Use environment variables or secure credential storage for production.


License

This project is licensed under the MIT License.

