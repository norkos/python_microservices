# learning_python_microservices
For Linux please execute "export DOCKERHOST=$(ifconfig | awk '/docker0/{getline; print}' | awk '{ print $2 }')"