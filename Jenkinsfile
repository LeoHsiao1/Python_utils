pipeline {
    agent {
        label "cvm1"  // 选择一个主机来部署
    } // 可设置agent any，让Jenkins选择任一主机部署
    environment {   // 定义作用于全局的环境变量
        PORT = "80"
    }
    stages  {
        
        stage("检出") {
            environment { // 定义作用于该阶段的环境变量
                PORT = "8000"
                GIT_BRANCH = "master"
            }
            steps {
                echo "git clone..."
                git(
                    branch: "master",
                    credentialsId: "${git_credentialsid}",  // 使用一个Jenkins的凭证，它包含git要用的ssh公钥
                    url : "git@${script_path}${service}.git"
                )
            }
        }

        stage("build") {
            steps {
                echo "building..."
                sh "who am i"
                sh "pwd"
                echo "build finished."
            }
        }

        stage("测试") {
            steps {
                parallel "单元测试": {  // 并行执行
                    echo "单元测试中..."
                    echo "单元测试完成"
                }, "接口测试": {
                    echo "接口测试中..."
                    echo "接口测试完成"
                }
            }
        }
    }
}