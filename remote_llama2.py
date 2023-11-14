from gradio_client import Client

def llama2_run(prompt):
    client = Client("https://huggingface-projects-llama-2-13b-chat.hf.space/--replicas/5c42d8wx6/")


    # prompt = input("How can I help you?:")
    result = client.predict(
            prompt,	# str  in 'parameter_7' Textbox component
            "",	# str  in 'Optional system prompt' Textbox component
            256,	# int | float (numeric value between 1 and 2048) in 'Max new tokens' Slider component
            0.9,	# int | float (numeric value between 0.1 and 4.0) in 'Temperature' Slider component
            0.6,	# int | float (numeric value between 0.05 and 1.0) in 'Top-p (nucleus sampling)' Slider component
            1,	# int | float (numeric value between 1 and 1000) in 'Top-k' Slider component
            1.2,	# int | float (numeric value between 1.0 and 2.0) in 'Repetition penalty' Slider component
            api_name="/chat"
    )
    return result


if __name__ == "__main__":
    llama2_run("hello")