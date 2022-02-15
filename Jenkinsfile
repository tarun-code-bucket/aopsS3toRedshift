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
                            sh "pip3 install boto3"
                            sh "chmod +x -R ${env.WORKSPACE}"
                            sh 'scripts/deploy.sh ${Bucket_Name} ${File_Name}'
                        } 
                }
        }
        stage('dbt-execution'){
                steps{
                    withAWS(role: 'AopsJenkins', region: 'us-east-1'){
                            //sh "python3.7 -m pip uninstall dbt-core dbt-redshift"
                            //sh "python3 install --upgrade pip3"
                            //sh "pip3 install dbt-core dbt-redshift"
                            //sh "pip3 show dbt"
                            sh "sudo su ec2-user"
                            sh "sudo su -c pip3 install dbt-core dbt-redshift ec2-user"
                            sh "whoami"
                            sh "dbt --version"
                            sh "cd s3DBTRedshift"
                            sh "dbt debug"
                            sh "dbt seed"
                        } 
                }
        }
    }
}