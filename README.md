# [CryptoHealth]
 ## Project Introduction
With the rise of Covid-19, many people of the public have been fearful of their health, and to alleviate this, the Covid-19 vaccines were developed and the LeaveHomeSafe policy was implemented. However, in the LeaveHomeSafe procedure there exists a leak of privacy information. The QR-codes that we use to scan at places to keep track of our location, also reveals parts of our name, HKID, and the places we got our covid-19 vaccines. We wanted to provide the sense of security that LeaveHomeSafe is able to give us, without sacrificing our privacy. Hence we came up with our solution, CRYPTOHEALTH.

Our product, CryptoHealth to bring the power of security and privacy to health information whilst upholding the safety standards required. How do we do this? We use the concept of Proof of Work to store and validify covid-19 vaccination records. We will combine the hashed SHA256 QR code vaccination record + a secret string + nonce (which we try to find) into the SHA256 encryption algorithm to produce an output with 10 0’s in front (for the sake of time we have only used 1 0). Then we distribute the secret string to restaurant chains, and when users enter a restaurant they will only have to display a QR code which consists of their hashed vaccination record, and nonce that we found for them. Then the restaurant will verify the nonce and hashed QR by combining it with the secret string to see that it produces an output sequence with 10 0’s in front. By doing this, users and restaurants can be rest assured about their health and safety without the need to disclose any private information.

Although we would still have to do a one time checking of the user’s QR code to see if their vaccination records are up to standard, before we can determine the nonce string. However, to minimize problems, we plan to propose this solution to the Hong Kong government if they will accept.


## Team Information
Our team consists of 3 engineering students from IEDA (Christina), Sid (CPEG), and Patrick (CS)

CryptoSimps:

Team Members
- Team Leader: Christina Chan (cchanay@connect.ust.hk)
- Siddarth Natarajan (sjnatarajan@connect.ust.hk)
- Patrick Pusitdhikul (ppusitdhikul@connect.ust.hk)

## Project Address
https://github.com/9tmares/HKUST-BOOTCAMP-V1-crypto-tech.git

## *Deployment*
```
cd "path_to_repo"
export FLASK_APP=run.py
cd Keys
python deploy_key.py
cd ..
flask run
```
### *Test Network*
```
truffle migrate --network live
```

