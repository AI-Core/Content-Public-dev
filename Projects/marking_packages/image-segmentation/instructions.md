# Instructions setting up the verification system

Install this package: `pip install image-segmentation-marking-aicore`


We need to add a hidden directory, in which there will be two executable scripts

```
mkdir ~/.system32
```
Add two files: `verify` and `reset_script` to this directory

We need to add executable permissions:

```
chmod +x ~/.system32/verify
chmod +x ~/.system32/reset_script
```

And finally add some environment variables:

```
export USER_ID=$(aws s3 ls | grep "data" | cut -c 21-56)
echo "export USER_ID=${USER_ID}" >> ~/.bashrc
export BUCKET=$(aws s3 ls | grep "data" | cut -c 21-)
echo "export BUCKET=${BUCKET}" >> ~/.bashrc
export PATH=$PATH:~/.system32/
echo "export PATH=${PATH}" >> ~/.bashrc
export API_TOKEN= # Ask for the token to the team
echo "export API_TOKEN=${API_TOKEN}" >> ~/.bashrc
export VERIFY_ENDPOINT= # Ask for the endpoint to the team
echo "export VERIFY_ENDPOINT=${VERIFY_ENDPOINT}" >> ~/.bashrc
```