pipeline {
    agent {
      docker { 
        image 'python:3.11'
      }
    }
    parameters {
        string(name: 'SELENOID_URL')
        string(name: 'OPENCART_URL')
        string(name: 'BROWSER')
        string(name: 'BROWSER_VERSION')
        string(name: 'THREADS')
    }
stages {
      stage('Run Tests') {
            steps {
                script {
                    sh 'python3 -m pip config set global.trusted-host "pypi.org files.pythonhosted.org"'
                    sh 'python3 -m pip install -r requirements.txt'
                    sh 'pytest --browser ${params.BROWSER} --ver ${params.BROWSER_VERSION} --threads ${params.THREADS} --base_url ${params.OPENCART_URL} --executor ${params.SELENOID_URL}'
                }
            }
        }
}
      

    
}
