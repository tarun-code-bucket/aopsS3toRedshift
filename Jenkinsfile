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

    environment {
        PATH = "/usr/local/bin:${env.PATH}"
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
                            //sh "sudo su -l ec2-user"
                            //sh 'pip3 install virtualenv && virtualenv --version && virtualenv venv && virtualenv -p /usr/bin/python3 venv '
                            //sh "source venv/bin/activate"
                            //sh "export PATH=\"/var/lib/jenkins/.local/bin/dbt/bin:${env.PATH}\""
                            //sh "echo ${env.PATH}"
                            //sh "cd ${env.WORKSPACE}"
                            sh "pwd" && "echo ${env.WORKSPACE}"
                            sh "sudo pip3 uninstall dbt-core dbt-redshift -y"
                            sh "sudo pip3 install dbt-core dbt-redshift"
                            sh "export PATH=\"/usr/local/bin/:${PATH}\""
                            sh "echo $PATH"
                            sh "dbt --version"
                            dir("s3DBTRedshift"){
                                //sh "mkdir /var/lib/jenkins/.dbt"
                                sh "sudo mkdir /var/lib/jenkins/workspace/aops_pipeline/s3DBTRedshift/seeds"
                                sh "sudo mv /var/lib/jenkins/workspace/aops_pipeline/sample_customer_data.csv seeds/sample_customer_data.csv"
                                sh "sudo mv profiles.yml /var/lib/jenkins/.dbt/profiles.yml"
                                sh "dbt debug"
                                sh "dbt seed"
                                sh "dbt run"
                            }
                        } 
                }
        }
    }
}