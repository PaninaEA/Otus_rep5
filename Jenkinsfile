pipeline {
     agent any

    parameters {
        string(name: 'SELENOID_URL', defaultValue: '192.168.0.108')
        string(name: 'OPENCART_URL', defaultValue: 'http://192.168.0.108:8081')
        string(name: 'BROWSER', defaultValue: 'chrome')
        string(name: 'BROWSER_VERSION', defaultValue: '128.0')
        string(name: 'THREADS', defaultValue: '3')
    }

stages {
     stage('Build image') {
            steps {
                script {
                    sh 'docker build -t opencart-tests .'
                }
            }
        }
      stage('Run Tests') {
            steps {
                script {
                    sh 'git config --global --add safe.directory "/var/jenkins_home/workspace/Test_opencart"'
                    sh "docker run opencart-tests -n ${params.THREADS} --browser ${params.BROWSER} --ver ${params.BROWSER_VERSION} --base_url ${params.OPENCART_URL} --executor ${params.SELENOID_URL}"
                }
            }
        }

        stage('Allure Report') {
            steps {
                allure([
                    includeProperties: false,
                    jdk: '',
                    results: [[path: 'Test_opencart/allure-results']]
                ])
            }
        }
    }

}
