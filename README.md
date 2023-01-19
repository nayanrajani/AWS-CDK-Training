# AWS-CDK-Training
- https://cdkworkshop.com
- [AWS CDK User Guide](https://docs.aws.amazon.com/CDK/latest/userguide)
- [AWS CDK Reference](https://docs.aws.amazon.com/cdk/api/latest/docs/aws-construct-library.html)
- [Update-nodejs](https://phoenixnap.com/kb/update-node-js-version)

- Commands Executed
    - Choose profile first
    - mkdir cdk-training
    - cd cdk-training
    - npm install -g aws-cdk
    1. Initiate CDK
        - cdk init sample-app --language=python

    2. Create Virtual Enviornament
        - .venv\Scripts\activate.bat

    3. Install Requirements
        - python -m pip install -r requirements.txt [OR] pip install -r requirements.txt

    - After Changes in code
    4. cdk ls 
    5. cdk synth --profile <profile-name>
    6. cdk bootstrap --profile <profile-name>
    7. cdk deploy --profile <profile-name>

- Delete bootstrap
    - go to console and delete resources manually and then
    - cdk destroy --profile <profile-name>
