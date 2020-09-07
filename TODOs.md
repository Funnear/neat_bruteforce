# ToDo's for Neat Brute Force project:

## Improve the implemented algorithms
- [ ] Write Unit Tests before any refactoring
- [ ] In `main`: add support for list of usernames
- [ ] In `main`: make possible to pass arguments like `generate_usernames` without a value
- [ ] Use several pick-up algorithms one-by-one 
- [ ] Pass minimal password length from client.config to all pickup algorithms
- [ ] Partial letter replace
- [ ] Limit password length for a known user (assuming you know credentials requirements) in user_data.json
- [ ] Reduce computational complexity for alphabet_replace (cases when no letter to replace)
- [ ] Reduce memory complexity for common passwords file reader by using custom buffer size
- [ ] Add camel case - 2 options (wOrD and WoRd)
- [ ] Introduce shuffle case (tOtALlyCHAotIc) - 2^len(string) options per word
- [ ] Add '-' and '_' between words from known user data
- [ ] s as 5, A as 4 as alternative symbol replacers
- [ ] *eight as 8 (with regexp replace?) 
- [ ] Convert seconds to minutes in successful attempt record
- [ ] Reverse all strings with not identical letters and longer than 2 -  `[::-1] # as an option`
- [ ] Add automatically most common passwords upload with a switch for amount of them:
  - https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials
- [ ] Implement credentials generation sorting logic based on probability (when user data is given) 
- [ ] Calculate passwords limit based on pick-up logic 
- [ ] Support for Name and Surname in non-latin alphabets.

## Implement credentials requirements knowledge support

- [ ] Pass server's login and password restrictions 

[Sample of requirements, RUS](https://support.google.com/mail/answer/9211434?hl=ru)

## Lacking execution modes

 user name (login) | personal data | password pick-up algorithm | credentials requirements |  number of credentials to pick-up
 --- | --- | --- | --- |  ---
TBD | ~ | is known for multiple users | ~  | ~ |  ~
TBD | ~ | ~ | all possible | ~ |  ~
TBD | ~ | ~ | ~ | are specified | ~ 
TBD | ~ | ~ | ~ | ~ |  all possible

### Based on knowledge about user
- [ ] support for multiple users
- [ ] support for Name and Surname in non-latin alphabets.

## Add other pick-up algorithms

### Based on keyboard layouts

- [ ] TBD


## Password pick-up insights
- [ ] Take default user-password pairs from official setup instructions for popular EDMS and ERP solutions
