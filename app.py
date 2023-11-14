from remote_llama2 import llama2_run

prompt = input("How can I help you?: ")

answer = llama2_run(prompt)

print("The answer is: " + str(answer))