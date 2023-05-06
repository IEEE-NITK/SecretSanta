# Secret Santa

## About

- This is a simple Python script to send emails to all secret santa participants!
- The script assumes the pairings are already made. Check the Google Form responses from [this Google Form](https://docs.google.com/forms/d/e/1FAIpQLSfHeqRPS-wCnGX2uxIaOSoPbvrmkwP13i8M5ez68KoMjvvo3A/viewform?usp=sf_link).

## Usage Instructions

- Install the dependencies using `pip`.
```bash
pip install -r requirements.txt
```
- Update the password field in the config block of the script (line 18).
- Update the other config fields if required, and update the email body if required as well.
- Run the following command (will not work on NITK-NET since SMTP ports are blocked)
```bash
python secretsanta.py
```

## License

The software is registered under the [MIT License](./LICENSE).
