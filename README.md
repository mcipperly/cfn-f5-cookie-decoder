# F5 Cookie Decoder

This repository contains code to deploy a Cloud Function on Google Cloud which will decode unencrypted F5 cookies, commonly starts with `BIGipServer`

## Steps for deploying/use

1. Authenticate/set your project using `gcloud`

2. Deploy using `gcloud`:

   `gcloud beta functions deploy f5-decode --region=<REGION> --trigger-http --runtime python37 --entry-point cfn_entry`

3. Use:

   ```
   $ curl https://<REGION>-<PROJECT>.cloudfunctions.net/f5-decode
   {"status": "ok", "nodeinfo": "10.1.1.1:8080"}
   ```

## Credits / Additional Reading

This incorporates some code written by dusty at https://penturalabs.wordpress.com/2011/03/29/how-to-decode-big-ip-f5-persistence-cookie-values/

TODO: Passphrase encrypted cookies, maybe?
