pipeline{
    agent any

    parameters{
        string(name: 'Bucket_Name', defaultValue: 'aops-bucket', description: 'Enter the S3 bucket Name.')
        string(name: 'File_Name', defaultValue: 'sample_customer_data.csv', description: 'Enter the File Name (Must contain file extension type *.csv)')
        choice(
        name: 'REGION',
        choices: [
            ' ',
            'us-east-1',
            'us-east-2'
            ],
        description: 'AWS Account Region'
        )
    }

    stages{
        stage('stack-execution'){
                steps{
                    withAWS(role: 'AopsJenkins', region: 'us-east-1'){
                            sh 'alternatives --set python /usr/bin/python3'
                            //sh 'alias python=python3'
                            sh 'python --version'
                            sh 'pip3 install boto3'
                            sh "chmod +x -R ${env.WORKSPACE}"
                            sh 'scripts/deploy.sh ${Bucket_Name} ${File_Name} ${REGION}'
                        } 
            }
        }
    }
}