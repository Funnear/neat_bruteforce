# License

This software is distributed under [WTFPL](http://www.wtfpl.net/) license.

If you want to fork and extend the project, please, consider contributing here instead. We are Open Source. 

# About Neat Brute Force

**Neat Brute Force** solution is designed exceptionally for Python study purposes. It has no aim to violate any law restrictions.

The provided algorithms can be used to demonstrate the crack-proof passwords importance and can help to increase the cyber-security awareness. 

Neat Brute Force can also be used to:
 - check if your passwords are crack-proof
 - compare various passwords pick-up algorithms efficiency (number of attempts and time to crack)

Some parts of the solution can be re-used for primitive **penetration testing** and, perhaps, some sort of **load tests** (though it would be bizarre, indeed).

`pickup_credentials` method can also be helpful to fill in your test environment with random users.

# Authors

Neat Brute Force solution was kick-started as a result of @Funnear attending the free boot-camp "Python for Newbies" from [Skillbox](Skillbox.ru). 
- Boot-camp coach - [Nikita Levashov | Никита Левашов](https://habr.com/en/users/nlevashov/), CTO of [Lia platform](https://lia.chat/) and a teacher in Skillbox. 
- Webinars recordings (in Russian):
  - [Day 1](https://live.skillbox.ru/webinars/code/osnovy-python2/)
  - [Day 2](https://live.skillbox.ru/webinars/code/vzlomy-i-brute-force-ataki2/)
  - [Day 3](https://live.skillbox.ru/webinars/code/python-intensiv-podvedenie-itogov2/)

The provided server emulator code initial version is a copy of Nikita's sample.

# Setup

Before the first execution run:
`pip install -r requirements.txt`

In order to use **Neat Brute Force** you need to have a server that accepts authentication requests. You can use a provided server emulator or use any other.

## Use the server from the package

The solution contains a source code of a simple server that uses **Flask** library.

To run the server simply go to */server emulator* directory and start it from the command line:

` ./server.py`

If it doesn't run - change file permissions to executable for the user.

The server will start listening for authentication requests at the endpoint:

`http://127.0.0.1:5000/auth`

You can update the list of login-password pairs for this server anytime you like in `users.json`.

This might be very handy for educational demonstrations.

## Use Neat Brute Force against any other server 

To use the Neat Brute Force against any other server make sure that this line:

`auth_url = "http://127.0.0.1:5000/auth"`

in file `client.config` points to the authentication endpoint of your target server.

Please, note that the solution is not mature enough to guarantee stable work with any server you like.  

# Neat Brute Force execution modes

Neat Brute Force is currently supporting the following use cases:

 user name (login) | personal data | password pick-up algorithm | credentials requirements |  number of credentials to pick-up
 --- | --- | --- | --- |  ---
 is known | unknown | based on alphabet | minimal password = minimal username are known |  1
 is known | unknown | based on the most common credentials | minimal password = minimal username are known |  1
 is known | is known | based on knowledge about user | minimal password = minimal username are known |  1
 unknown | is known | based on knowledge about user | minimal password = minimal username are known |  1

See implementation plans in `TODOs.md`

Personal data used is: name, surname, e-mail, date of birth. All these field values should be present in `resources/user_data.json`.
Known (single) login should be specified in `client.config`:

`login = admin`

Minimal password (and username) length should be specified in `client.config`:

`minimal_password_length = 8`


# Pick-up algorithms

Neat Brute Force solution currently contains the code of 3 approaches to login/password pick-up:
1. Based on the most common credentials
2. Based on alphabet
3. Based on knowledge about user

## Based on alphabet

The elementary brute-force method based on generating all possible combinations of elements of specified alphabet.

## Based on the most common credentials

A lot of cyber-security analysts provide their lists of the most common passwords and login names. Neat Brute Force uses only one of them taken from this repository:
- [https://github.com/danielmiessler/SecLists](https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials)


## Based on knowledge about user

This part is genuinely designed by @Funnear. It uses information about some user stored in `resources/user_data.json`. All this data is completely imaginative, all matches with real people are coincidence. 

The `pickup_credentials` method can be used for user name (login) generation.

Algorithm is based on the following assumptions:
- All user data fields have proper values
- Name and Surname are written with latin letters
- User name doesn't start with a digit (this speeds up the pick-up for the most cases, but can be dropped to use brute force with wider range of possible credentials.)

# Usage

Running with default parameters:

```bash
python3 main.py
```

This will start a pick-up:
 - using algorithm based on the most common credentials
 - with passwords limit defaulted to 10,000
 - for one username defined in `client.config` as `login` value
 - against the server specified in `client.config` as `auth_url` value

All possible keyword arguments:

Keyword | default value | value type | Notes
---- | ---- | ---- | ----
method | 1 | int | See `method.py` with enum object definition for all supported method ids
username | config.get('login') | str | You can skip this argument if you specify your user in `client.config`
passwords_limit | 10000 | int | Current implementation of Neat Bruteforce require specifying `passwords_limit` parameter for execution. It limits the amount of attempts to generate a password using the preferred pick-up algorithm. See TODOs for future plans.
generate_usernames | - | any | It will use the same usernames generator method as for passwords
iterator | - | any | Only used with `Method.COMMON` but runs it with difference in implementation regarding memory and time complexity. It remains for forthcoming performance tests.

Possible running commands with arguments:
```bash
python3 main.py username='cat'
```
```bash
python3 main.py username='Ivan2002' method=3 passwords_limit=1000
```
```bash
python3 main.py generate_usernames=1 iterator=1
```

# Precepts

Precepts are small instructions that `neat_requests` module gives to main module. This approach is used to determine the execution logic depending on multiple conditions. It helps to separate conditions analysis from execution itself.

