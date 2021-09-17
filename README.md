<h1 align=center>Github Repo Cloner (In Bulk)</h1>

#### Basically clones all the public repo for the the `username` provided.

## Where did the idea came from?
So basically, I lost my [2FA](https://docs.github.com/en/github/authenticating-to-github/securing-your-account-with-two-factor-authentication-2fa/about-two-factor-authentication) device and the recovery codes my Github Account :(, contacted the github support, then after
7-8 days of email exchanges, The conclusion was that we'll (the github guys) unlink the email and username, then remove
the account then I can again create your new account with the same email and unsername, which cause the all
repo/commit/PR to be gone forever,

So to get the all public repos, I created this [script](main.py).

### NOTE: Never forget your recovery codes to backup somewhere you can get thenat the time of need.


## How it works?

- Run the script via `python3 ./main.py`
<img src="https://i.imgur.com/B4Hkpny.png">

- Enter the github username
<img src="https://i.imgur.com/IcTdW0K.png">

- Enter the path where you want to save the repos (In my case I choose default, so I simply press `Enter Key` )

### Then the cloning will be started, just wait till the cloning get completed, It may take several minutes according to the number of repos are cloning and the size of the repos

## Have any issue, while using the script?

- Create an issue [here](https://github.com/pvcodes/github-repo-cloner/issues).
- Explain your problem, and copy paste the error message you get.