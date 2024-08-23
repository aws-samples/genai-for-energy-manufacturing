---
title : "Lab setup"
weight : 8
---
# Lab setup

# Download and configure the assets for the labs

1. In the AWS Cloud9 IDE, select the bash terminal
  
![Sign in](/static/cloud9/cloud9-terminal.png)

2. Paste and run the following into the terminal to download and unzip the code.

```
cd ~/environment/

git clone https://github.com/aws-samples/genai-for-energy-manufacturing.git

cd genai-for-energy-manufacturing

```

Once completed, you should see the unzip results in the terminal:

3. Install the dependencies for the labs.

```
pip3 install pip==24.0 && pip3 install -r ./requirements.txt -U
```

If everything worked properly, you should see a success message (you can disregard a warning like below):

![Sign in](/static/cloud9/reqs.png)

1. Verify configuration by pasting and running the following into the AWS Cloud9 terminal:

```
python ./api/bedrock_api.py
```

If everything is working properly, you should see a response about Manchester, New Hampshire:

![Sign in](/static/cloud9/test.png)

## Configure streamlit
1. In the AWS Cloud9 IDE, select the bash terminal
  
2. Paste and run the following into the terminal to create config.toml file.
```
mkdir -p /home/ubuntu/.streamlit
cat >/home/ubuntu/.streamlit/config.toml <<EOL
[server]
enableXsrfProtection = false
enableCORS = false
```

1. Type ``` EOL ```.
   
---
